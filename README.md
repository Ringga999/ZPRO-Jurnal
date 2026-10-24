# ZPRO Journal

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
