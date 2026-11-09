import json, time
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# One deliberately simple, deliberately editable KPI definition -- change
# TARGET_SKILL, or write a different KPI function entirely. Per this course's
# standing principle: a KPI is a construct you chose, not a neutral fact.
TARGET_SKILL = "sql"

def load_extracted(path="data/extracted.json"):
    with open(ROOT / path, encoding="utf-8") as f:
        return json.load(f)["postings"]

def compute_kpi(postings, target_skill=TARGET_SKILL):
    n = len(postings)
    matching = [
        p for p in postings
        if any(target_skill.lower() in s.lower() for s in p.get("required_skills", []))
    ]
    all_skills = Counter()
    for p in postings:
        # One vote per posting; independent LLM calls vary in casing/spacing.
        for s in {" ".join(s.split()).casefold() for s in p.get("required_skills", []) if s.strip()}:
            all_skills[s] += 1

    return {
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "kpi_label": f"% of postings mentioning '{target_skill}'",
        "kpi_value": round(len(matching) / n, 3) if n else 0.0,
        "n_postings_analyzed": n,
        "n_matching": len(matching),
        "top_skills": [{"skill": s, "count": c} for s, c in all_skills.most_common(10)],
        "avg_skills_per_posting": round(sum(all_skills.values()) / n, 2) if n else 0.0,
    }

def compute_cloud_kpi(postings):
    """Share of postings mentioning at least one named cloud provider."""
    providers = {"aws", "amazon web services", "azure", "microsoft azure",
                 "gcp", "google cloud", "google cloud platform"}
    n_matching = sum(
        any(" ".join(s.split()).casefold() in providers
            for s in p.get("required_skills", []))
        for p in postings
    )
    return {
        "kpi_label": "% of postings mentioning AWS, Azure or Google Cloud",
        "kpi_value": round(n_matching / len(postings), 3) if postings else 0.0,
        "n_matching": n_matching,
    }


def main():
    postings = load_extracted()
    kpi = compute_kpi(postings)
    kpi["cloud_kpi"] = compute_cloud_kpi(postings)
    print(json.dumps(kpi, indent=2))
    output = ROOT / "docs/data/kpi.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8") as f:
        json.dump(kpi, f, indent=2)
    print("\nWrote docs/data/kpi.json")

if __name__ == "__main__":
    main()
