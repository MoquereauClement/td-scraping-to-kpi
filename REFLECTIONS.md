**Reflect:** `rp.read()` (the "obvious" one-liner version of this check) silently
returns "disallow everything" on a network with a proxy in front of it — with no
error, no warning, nothing that looks broken. `rp.parse()` (used above) doesn't have
this problem. In your own words: why is a pipeline stage that fails *silently* worse
than one that crashes loudly, for something whose whole job is "respect the rules
before acting"? Tie your answer to CM3's provenance argument.

A silent failure hides how an access decision was produced, breaking CM3's provenance
chain (slides 18–20), while a crash exposes the problem before later stages inherit it.

**Reflect:** France Travail's API (used in TP1's main pipeline) is official
government open data, explicitly licensed for reuse. This jobspy-derived sample is
not. In your own words, what's the actual difference in risk between the two? Would
your answer change if this repo were private instead of public — and if so, why does
public/private matter here at all?

If you use the government open data to create your own website, you will be fined. 
However if it's used in a private context and don't create a website, you can't be fined. 

**Reflect, before you run anything:** CM5 argues agentic AI belongs at specific
pipeline stages, not everywhere. This TD extracts skills with an LLM, but nothing in
this course ever uses an LLM to decide, say, which application you actually sent or
what your real skill level is. Using CM5's own distinction (not just "because it's
convenient"), explain in your own words *why* free-text-to-structured-list is a good
fit for an LLM and a plain record of your own actions is not.

**Reflect, before you read the code below:** the script is about to define
`TARGET_SKILL = "python"` — a choice someone (this manual) already made for you. If
you were building this dashboard for ENSIM's own curriculum committee, what single
skill would *you* choose to track first, and why? Write your answer down now, before
you see what number the default choice actually produces.

**Reflect:** now change `TARGET_SKILL` to the skill you named above and re-run.
Compare the two `kpi_value` numbers. Which version would you actually trust to tell
a curriculum committee "students should learn X next" — the default, your own
choice, or neither? Say why in two or three sentences.

**Reflect:** if a classmate looked only at your published `kpi.json` (never your
local files), could they reconstruct which specific postings you scraped, or which
company any of them came from? If they genuinely couldn't — what exactly did you
have to leave out of the KPI's fields to guarantee that, and was that a deliberate
design choice in `compute_kpi()` or just luck?

**Reflect:** who is the actual audience for this dashboard as it stands right now —
you personally, checking your own work, or someone else entirely (e.g. a curriculum
committee, per Stage 4's framing)? Does the page's current title and one-line
description actually match that audience? If not, what one sentence would you
change?

**Reflect:** write two sentences comparing your two KPIs — the one from Stage 4 and
this new one. Which would you actually trust to drive a real decision, and why?
