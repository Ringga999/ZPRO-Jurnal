# ZPRO Journal (PRIVATE)

Daily activity log. This repo records WHAT GOT DONE each day, in detail. It is
a diary, not a documentation vault. Product specifications (memory, settings,
roles, web3) live in the engine repo under docs/, NEVER here. Keeping that line
sharp is the whole point of this repo.

Visibility: PRIVATE. It mixes two worlds, one of which is private ecosystem
work, so the entire repo stays private. Privacy does not stop AI: your own
agents read it via a token; the chat assistant reads whatever you paste.

Two worlds (top-level folders):
- stratofly/         the public-safe world: engine, app blueprint, hackathon.
- the private-ecosystem world (the second top-level folder): strictest rules.

Structure (the tidy rule): one FOLDER per day, named DD-MM-YYYY, holding that
day detail. Pattern: <world>/DD-MM-YYYY/log.md  (example: stratofly/26-10-2026/
log.md). A day may hold more than one file if the work spans several topics; the
default is a single log.md per day folder.

Global rules (apply everywhere):
1. No secrets. Never write an API key, token, password, or wallet private key,
   even partially. If a secret was involved, write [redacted].
2. Alias private repos. Never write the literal name of a private ecosystem
   repo. Use the main protocol repo, the product app, etc. The engine public
   file names (config.py, lib/wizard.py, docs/*.md) are fine to name literally.
3. Honesty over polish. Record bugs you caused and fixes you regret. The value
   of a diary is truth, not presentation.
4. This repo holds NO product specs. If you find a spec file here, it is in the
   wrong place; move it to engine docs/.

Why a diary at all: the agents get a Memory feature to remember their work;
this journal is the human mirror. Eventually the AI-insights layer reads BOTH
the agent memory and this diary to produce weekly what-we-achieved and
what-is-stuck reports. For now, it is simply so we remember.
