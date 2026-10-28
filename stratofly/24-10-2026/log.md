# 2026-10-24 (Saturday) - H-2 hackathon

## Decided
- Meja 1 (Memory): HASH ON-CHAIN, BLOB OFF-CHAIN, always. Local mode is the
  default and is FREE FOREVER (even inside the paid app); chain mode is an
  optional switch and must NEVER be a demo dependency. Failure of the fancy
  layer must never look like failure of the product.
- Meja 2 (taxonomy fix): DIVISION (where an agent works) and ROLE (what the
  brain is good at) are TWO PERPENDICULAR axes. Social media is a division
  concern, not a role. Seven roles locked: Solver, Architect, Crafter, Analyst,
  Communicator, Sentinel, Operator. Solver is the ONLY role with SUPERVISION
  rights, and it is an ad-hoc orchestrator a user creates on demand; the
  default maintainer crew ships WITHOUT a Solver (keeps the routine crew lean
  and showcases the Create-Agent wizard). Role is METADATA wrapping machinery
  we already shipped green (model_kind detection + fallback chain + persona),
  not a new engine.
- Meja 3 (journal): lives in its OWN repo with two worlds (the public-safe
  stratofly world, and the private-ecosystem world). Because the second world
  exists, the whole journal repo is PRIVATE. Privacy does not block AI: own
  agents read it via a token; the chat assistant reads pasted entries.
- Spec-leads-code applied again: SETTINGS-SPEC v1.2 TARGETS schema 3, but the
  SCHEMA constant STAYS 2 until role and memory are implemented (S5). No
  premature version promise.

## Built / Fixed
- install_specs.py wrote docs/MEMORY-SPEC-v1.md and docs/SETTINGS-SPEC-v1.2.md
  (engine repo) plus journal draft files. Smoke test green: engine still schema
  2, 10 agents, nvidia 11th-agent refusal = True. Committed and pushed the specs.
- fix_wizard_ux.py repaired the wizard: every invalid input now explains itself
  and always offers a back option; per-chain entry numbers de-ambiguated with a
  (#n = entries WITHIN that chain) header; digit aliases added for brain
  actions (4 = view). Self-test green. Committed and pushed.
- install_web2.py built the localhost dashboard, ARCHITECTURALLY corrected: the
  page lives in lib/dashboard.html and lib/web.py READS it (kills the nested
  triple-quote class of bug). Self-recon on disk revealed the real dispatcher:
  variable cmd with 12 commands (setup, brains, settings, model, serve, mock,
  schedule, all, telegram, preflight, patrol, web). ast-guarded splice added a
  web branch. Committed and pushed.
- install_s4.py gave the wizard v2 the 7-role dropdown in Create Agent; the
  dashboard gained a patrol button + recent-reports panel + role badge;
  settings.py gained the roles block + a default role per template agent.
  Committed and pushed.
- install_ask.py built the HONEST door: a free-form ask command that forwards
  ANY prompt to an agent via provider_hub.think(brain, system, user, agent_id).
  Verified live: python main.py ask What is 2+2 -> scout answered 2 + 2 = 4.
  This is the antithesis of a scripted demo: the engine accepts arbitrary
  instructions, proving the platform is genuinely commandable.
- recon_server.py mapped the EXISTING server (lib/api_server.py: JSON-only,
  single-threaded, no do_POST, no HTML) and found onboard.py still ships the
  private-ecosystem repos as its default REPOS value (line 35) - flagged as
  tech-debt, deliberately NOT touched tonight (CLI scope, green code, deadline).
- install_full.py BUILT THE FULL APP BY UNIFYING INTO api_server.py (never a
  third server): switched HTTPServer to ThreadingHTTPServer so LLM calls no
  longer freeze the UI; added do_POST (onboard, settings, agent add and remove,
  ask, patrol, mock); served lib/app.html at /; rebuilt /api/state from settings
  (config truth) MERGED with memory (live state) so all 10 agents always show
  with real lights. app.html uses EVENT-DELEGATION (zero inline onclick).
  Runtime smoke test (server actually started on a random port) = ALL GREEN:
  /health ok, /api/state 10 agents + per_provider nvidia 10, /api/settings
  7 roles + 3 brains, /api/env-status reachable, / about 15k chars with crewGrid
  and NO onclick. The control room now renders: LIVE CREW, ONBOARD, ADD AGENT,
  COMMAND THE CREW. Committed and pushed.

## Bugs found (the honest section - this is where the value is)
1. Wizard silent-swallow: typing 4 at pick brain just looped with no message.
   Found by HANDS-ON testing, not by reading. Root cause: invalid input was
   dropped silently in several prompts. Fix: validate and explain everywhere.
   Lesson for the hackathon: a jury types random keys; every input must answer.
2. install_web.py v1 threw SyntaxError invalid decimal literal at line 144. Root
   cause: an HTML string delimited by triple-quote was embedded INSIDE a web.py
   string also delimited by triple-quote, so the inner triple-quote closed the
   outer one early, leaking CSS font 14px/1.5 as raw code. Disk stayed INTACT
   (error at compile time, before any write). Fix was architectural, not a
   patch: separate the page into its own file and use two different delimiters.
3. The big one: every panel empty + button dead. I MISDIAGNOSED it THREE times,
   blaming the patrol subprocess. The truth (from the captain F12 console): a
   single SyntaxError unexpected token parenthesis at line 93 killed the ENTIRE
   inline script, so load never ran (all panels blank) AND patrol was never
   registered (ReferenceError patrol is not defined, eight times, one per
   click). The fragile nested-onclick escaping was the culprit. Diagnostic rule
   now encoded: if ALL panels are blank, the FRONTEND is dead - do not blame the
   backend. Fix: event-delegation (no onclick) + raw strings + a smoke test that
   RUNS the server and asserts the page has no onclick.
4. Patrol button did nothing was a SYMPTOM of item 3 (and of an earlier choice
   to discard subprocess output to DEVNULL with no feedback), not a patrol bug;
   terminal patrol was green the whole time (exit 0, full output).
5. Latent gitignore leak: the malformed-JSON backup resolves to settings.bak.ts
   (not settings.json.bak.ts), which the exact pattern settings.json missed.
   Patched with settings.bak*. The ugly backup FILENAME itself is logged as
   calm-phase tech-debt (do not refactor a green loader under pressure).
6. Two servers existed briefly (my lib/web.py vs the existing lib/api_server.py),
   violating one source of truth. Resolved by unifying into api_server.py;
   lib/web.py is now redundant and marked for post-demo removal.

## Process lesson (captain over architect)
- I proposed a 7-beat memorized demo script. The captain rejected it as FRAUD:
  stitching a command sequence proves we memorized commands, not that the app
  can be commanded. That rejection redirected the whole evening toward the
  honest frame: the ask command + the web control room, where anyone (jury
  included) can type ANY instruction. The captain was right; the architect had
  drifted into theater. Recorded so the reflex is: demonstrate CAPABILITY, not
  a script.

## Open questions
- Post-demo: trim lib/web.py so api_server.py is the single server (complete
  the one-server doctrine).
- Calm phase: generic-ize onboard.py default REPOS (currently the private
  ecosystem, aliased here).
- S5 (post-hackathon): implement lib/memory.py M1 (local) + bump SCHEMA 2 to 3 +
  wire roles preferred_kinds into provider_hub catalog filtering.
- Live telemetry is currently settings + memory merged; mock mode is the
  offline stage guarantee. Real per-agent heartbeats arrive with the scheduler.

## Tomorrow (Plan)
- S4 real: polish the Telegram gateway + the autonomy switch ON THE ALREADY-GREEN
  surfaces (terminal, wizard, web) - NOT a new front. Then rehearse the HONEST
  demo (open localhost, type a random command, watch the crew answer), FREEZE.

## Aliases used today
- the main protocol repo = the private ecosystem protocol repo
- the product app = the private example-product repo
- the private-ecosystem world = the second folder of this journal repo
