# 2026-10-28 (Tuesday) - Phase 1 Completion

## Decided
- Phase 1 focus: fix UI bugs + add agent detail modal + Free APIs menu.
  Rationale: before building heavy features (Solver, Web3), the foundation
  must be tidy. Juri will see 10 agents with real states, not "not implemented"
  placeholders.
- Opsi A locked for Phase 2: Solver Orchestration. Reason: this is the
  "power demo" that differentiates Stratofly from simple chatbot aggregators.
  Solver can delegate to other agents, run simulations, and present drafts
  for approval. This proves the platform is genuinely commandable, not just
  a script runner.
- Phase 2 timeline: 30 Okt - 1 Nov (3 days). Day 1: Solver core + /solve
  command. Day 2: Multi-agent delegation + draft approval. Day 3: Testing
  + polish. Buffer: 2 Nov for unexpected issues.

## Built / Fixed
- fix_bubble.py: patched api_server.py to filter useless bubbles ("not
  implemented yet", "waiting...") and replace with "ready - waiting for task"
  for idle agents. Smoke test: bubbles_clean = True. All 10 agents now show
  meaningful state (scout = "Patrol complete" from real patrol, 9 others =
  "ready - waiting for task").
- install_phase1.py: rewrote lib/api_server.py v2 + lib/app.html with:
  (a) /api/agent/<id> endpoint returning agent detail + role-specific modules
  (b) Agent detail modal in UI (click card -> modal with brain chain, current
  state, role modules placeholder, recent events, action buttons)
  (c) Free APIs menu in header (6 links: NVIDIA NIM, Groq, OpenRouter,
  DeepSeek, Mistral, GitHub tokenless) - proves "$0 modality" promise
  (d) Smoke test: ALL GREEN (modal: True, menu: True, no-onclick: True)
- Cleanup: deleted fix_bubble.py, install_phase1.py after commit.

## Bugs found
- Installer threading bug: install_phase1.py smoke test failed with
  "NameError: name 'threading' is not defined" because threading was not
  imported in the installer script (not in api_server.py itself). Fixed by
  adding "import threading" to fix_bubble.py smoke test section.
- Bubble logic edge case: old logic only replaced bubble if None, but
  memory.sqlite3 had stale bubbles from previous mock/patrol runs
  ("not implemented yet", "waiting..."). Fixed by filtering useless bubbles
  and replacing with "ready - waiting for task" for idle agents.

## Open questions
- Solver implementation detail: should /solve command accept file uploads
  (PDF/img) via web UI, or only text prompts for now? Web uploads require
  multipart form handling + file storage. Text-only is faster to build
  (1 day vs 2 days). Recommendation: text-only for hackathon demo, file
  uploads as post-demo enhancement.
- Multi-agent delegation: should Solver call other agents via subprocess
  (like patrol) or in-process via provider_hub.think()? Subprocess is safer
  (isolation) but slower. In-process is faster but risks blocking the UI.
  Recommendation: in-process with threading for hackathon speed.

## Tomorrow (Plan) - 29-10-2026
- Start Phase 2 Opsi A: Solver Orchestration
- Day 1 tasks:
  (a) Add /solve endpoint to api_server.py (accepts prompt + optional
      agent_id, returns response from provider_hub.think with Solver persona)
  (b) Add "Solve" button to agent detail modal for Solver-role agents
  (c) Implement Solver persona in lib/persona.py (orchestrator mindset,
      asks-before-acting, thinks in systems)
  (d) Test: create Solver agent -> click Solve -> type complex prompt ->
      get structured response
- Estimated time: 4-6 hours
- Risk: low (reuses existing provider_hub.think infrastructure)

## Ecosystem ZCP2O Activity
NOTE: This journal is PUBLIC. Activity in the private-ecosystem world
(protocol repo, product app) must be documented in the PRIVATE folder of
this repo (not yet created) or a separate private journal. Do NOT write
literal repo names, keys, or sensitive details here.

Planned activity for 29-10-2026 in the private-ecosystem world:
- Protocol repo: pending tasks (to be filled by captain in private folder)
- Product app: pending tasks (to be filled by captain in private folder)

Action required: create the private-ecosystem folder in this repo and
document private-world activity there with strict alias rules.

## Aliases used today
- the main protocol repo = the private ecosystem protocol repo
- the product app = the private example-product repo
- the private-ecosystem world = the second folder of this journal repo
