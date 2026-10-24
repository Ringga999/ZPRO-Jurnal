# make_readme.py - one-shot: writes 3 READMEs into ZPRO-Jurnal (root + 2 worlds).
# Save as make_readme.py inside the ZPRO-Jurnal folder, run once. ASCII-only,
# no triple-backticks inside (so this block never fragments when copied).
from pathlib import Path
B = Path(__file__).resolve().parent

ROOT = r"""# ZPRO Journal

Daily activity log. One file per day, recording what actually got done. This is
the human mirror of the agents' Memory feature (MEMORY-SPEC lives in the engine
repo, not here): the crew remembers its work; you remember yours here. Specs and
contracts do NOT live in this repo - only the diary.

Visibility: PRIVATE. This journal mixes two worlds, one of which (zcp2o-ecosystem)
is private ecosystem work. Keeping the whole thing private protects that work and
keeps the hackathon story (Stratofly) clean and un-blurred. Privacy does NOT stop
AI from reading it: your own agents read it via a GitHub token (PAT) in .env, and
the chat assistant reads whatever entries you paste. Both paths work on private.

Two worlds (folders):
- stratofly/         notes about the Stratofly world: open engine (local-stratofly),
                     commercial app (stratofly), and the hackathon build. Public-safe.
- zcp2o-ecosystem/   notes about the private ZCP2O ecosystem work. STRICTEST rules.

Global rules (apply everywhere):
1. No secrets. Never write an API key, token, password, or wallet private key,
   even partially. If a secret was involved, write [redacted].
2. Alias private repos. Never write the literal name of a private ecosystem repo.
   Use "the main protocol repo", "the product app", etc. Defense in depth: even
   though this repo is private, aliases keep the ecosystem separable if visibility
   ever changes, and keep the hackathon narrative clean.
3. One file per day. Path pattern: <world>/YYYY/YYYY-MM-DD.md
   (example: stratofly/2026/2026-10-24.md).
4. Each entry answers: what did I decide, what did I build or fix, what broke,
   what is open, what is tomorrow. Be honest, not polished.
5. Language: these rule docs are English (project English spine). Daily entries may
   be in any language you think in; English is recommended so future AI-insights
   parse them effortlessly.

Why two folders instead of one flat diary? The two worlds have different audience
and different leak-risk. Splitting them now means you can later separate this repo
into two (a public stratofly-journal + a private zcp2o-journal) without rewriting a
single entry. The structure is already split-proof.
"""

STRATOFLY = r"""# Stratofly World - Journal

Notes about the Stratofly world only: the open-source engine (local-stratofly),
the commercial app blueprint (stratofly), and the hackathon build leading to the
launch gate. This is a diary of what got done each day, not a spec document.

Typical daily entries here:
- architecture decisions and the one-line reason behind them
- commits made and the verification that went green (e.g. "wizard self-test exit 0")
- bugs found while testing, especially ones you caused - record them honestly
- drawing-table conclusions (Memory, Roles, dashboard plans)
- wizard / dashboard / Telegram-gateway progress

Leak-risk: LOW. The engine repo is public, so naming its files (config.py,
lib/wizard.py, docs/*.md) is fine. Still obey the global rules: no secrets, and do
not drag private-ecosystem names into entries here - that belongs in
zcp2o-ecosystem/.

File pattern: stratofly/2026/2026-10-24.md
"""

ECOSYSTEM = r"""# ZCP2O Ecosystem - Journal (PRIVATE WORK)

Notes about the private ZCP2O ecosystem work: the protocol repo, the product app,
and anything that runs on top of the protocol. This folder describes work that is
NOT public, so the rules here are the strictest in the journal.

Strict rules:
1. NEVER write the literal name of any private repo. Always alias: "the main
   protocol repo", "the product app", "the wallet module", etc.
2. NEVER write tokens, keys, or internal endpoints. Use [redacted] if unavoidable.
3. Describe OUTCOMES and DECISIONS, not sensitive internals. "Patrol found 3 stale
   issues, triaged to X" is fine; pasting an internal document is not.
4. If you ever split the stratofly/ side into its own public repo, this folder must
   remain the part that never leaves private. Keeping entries alias-clean makes
   that split trivial and safe.

Typical daily entries here:
- patrol / triage results across the ecosystem repos (aliased)
- release preparation and changelog drafting
- dependency / security observations
- protocol-vs-app compatibility notes (drift, breaking changes)

File pattern: zcp2o-ecosystem/2026/2026-10-24.md
"""

for rel, txt in [("README.md", ROOT),
                 ("stratofly/README.md", STRATOFLY),
                 ("zcp2o-ecosystem/README.md", ECOSYSTEM)]:
    p = B / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(txt, encoding="utf-8")
    print("  OK", rel)

print("\nDONE. 3 READMEs written. Next: publish this folder as a PRIVATE repo.")