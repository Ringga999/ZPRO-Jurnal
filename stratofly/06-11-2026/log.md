# 2026-11-06 (Friday) - Phase 2 Completion + Architecture Lock

## Decided
- **Taxonomy locked**: 7 core roles (Solver, Architect, Crafter, Analyst, 
  Communicator, Sentinel, Operator) are the permanent framework. All future 
  features will be mapped as modules within these roles, not new roles.
- **Demo scope defined**: The "4-Link Collaboration Chain" (Solver -> Analyst 
  -> Crafter -> Communicator) is our showcase strategy. This proves agent-to-
  agent handoff with shared context, without over-engineering.
- **Social media connectors**: Abstraction-first approach. Mode B (manual token)
  for demos; Mode A (OAuth) is post-launch roadmap. Human-in-the-loop approval
  (draft-first) is non-negotiable for all social actions.
- **Developer UX**: Keep venv (non-negotiable for reproducibility), but will
  add run.bat wrapper to hide activation complexity.
- **Scalability vision**: 100-200+ roles achievable because "Roles are METADATA,
  not separate engines." Requires Role Registry + Role Generator/Composer.

## Built / Fixed

### Bug Fixes (Launch-Blockers Closed)
1. **Agent resurrection bug** (settings.py _merge function):
   - Root cause: _merge(base=defaults(), incoming=file) started from 10-agent
     template, so deleted agents were resurrected on EVERY load().
   - Fix: Made "agents" collection FILE-OWNED (FILE_OWNED_KEYS = {"agents"}).
     Now deletions stick permanently; only missing top-level sections are filled
     from defaults (preserving schema migration).
   - Test: delete agent -> reload -> agent stays deleted. PASS.

2. **Missing import re** (api_server.py):
   - Root cause: _solve_plan used re.findall() but 'import re' was missing.
   - Fix: Added 'import re' to imports.
   - Test: /api/solve works without NameError. PASS.

3. **Delegation Board pollution**:
   - Root cause: Parser captured placeholder rows (<task> -> <id>) and duplicates.
   - Fix: Extracted _parse_delegations() with filters:
     * Drop rows with < or > in task/id
     * Drop unknown agent IDs
     * Deduplicate by (agent, task) tuple
     * Cap at 4 delegations (matches persona rule)
   - Test: Board shows max 4 clean rows, no placeholders. PASS.

### Feature Completion (Phase 2: Solver Orchestration)
1. **SOLVER_PERSONA strengthened**:
   - Added concrete delegation format examples: [DELEGATE: scout | task]
   - Added negative examples (what NOT to do)
   - Appended delegation examples to user prompt in _solve_plan
   - Result: LLM now consistently outputs bracket format

2. **Delegation Board UI**:
   - Shows up to 4 clean delegation rows
   - Each row has "Run via <agent>" button
   - Clicking button executes /api/delegate -> agent answers in its own persona
   - Board only appears for Solver role (hidden for others)

3. **End-to-end flow verified**:
   - Create solver1 agent (role=Solver) -> SUCCESS at 9/10 (after deleting diplomat)
   - Click card -> modal shows "Solve Problem" button
   - Fill 3 textareas (Overview, Goal, Timeline) -> Run Solver
   - Output: Structured 5-phase plan + Delegation Board with 2-4 tasks
   - Click "Run via scout" -> scout responds with its own persona
   - Control negative: scout (Operator) has NO Solve Problem button

### Documentation Updates
1. **ZPRO-Jurnal**:
   - stratofly/06-11-2026/log.md: Architecture review & roadmap alignment
     (5 pillars: taxonomy lock, demo scope, connectors, venv UX, scalability)

2. **local-stratofly/docs/**:
   - ROLE-BLUEPRINT-SPEC-v1.md: Appended "MODULE CATALOG PER ROLE"
     * 70+ modules documented across 7 roles
     * Honest [LIVE] vs [PLANNED] markers
     * Cross-role capabilities documented

## Bugs Found
1. **Installer anchor mismatch**:
   - fix_board_and_cleanup.py looked for multi-group regex that didn't exist
   - Lesson: Always verify anchor against ACTUAL file content, not assumed content
   - Fix: Created fix_parser_final.py with correct anchor (single-group regex)

2. **Premature backup purge**:
   - Purged .bak files BEFORE verifying patch success
   - Lesson: "Hijau dulu, sapu kemudian" (green first, clean after)
   - Fix: New doctrine - only purge backups AFTER commit & push verified

## Process Lessons
1. **Opsi B wins**: Taking time to fix bugs properly (instead of quick workaround)
   pays off in demo confidence. The clean Delegation Board is worth the extra hour.

2. **Documentation as product**: Module Catalog in docs/ is not just notes - it's
   the public contract. [LIVE] vs [PLANNED] markers maintain trust with jury/users.

3. **Installer discipline**: Every installer must:
   - Backup first
   - Ast-guard Python code
   - Runtime smoke test
   - Self-delete after commit
   - Add itself to .gitignore

## Open Questions
- Should we build run.bat now or post-hackathon? (Low priority, nice-to-have)
- Should we add more delegation format examples to improve LLM compliance?
  (Current 3 examples seem sufficient, but could add edge cases)

## Tomorrow (Plan) - 07-11-2026
Priority: **Web3 Anchoring (Phase 3)** - but only if energy permits. Otherwise,
use day for rest and demo rehearsal.

If proceeding with Web3:
1. Deploy StratoflyAnchor contract to Sepolia via Remix (1-2 hours)
   - Contract: anchor(hash) + verify(hash) -> (ok, timestamp)
   - Gas: ~45k per anchor
2. Write lib/chain_relay.py with web3.py (2 hours)
   - Connect to Sepolia via Infura/Alchemy
   - Sign tx with wallet from .env (STRATOFLY_CHAIN_KEY)
   - Send tx, wait for receipt, store tx_hash in memory
3. Hook _anchor_to_chain_async into /api/agent/add (1 hour)
   - Non-blocking background thread
   - Fallback: if RPC down, agent save still succeeds (anchor is bonus)
4. Update UI: Show [ON-CHAIN ✓] badge + Etherscan link (1.5 hours)
   - Badge appears after tx confirmation
   - Link: https://sepolia.etherscan.io/tx/<tx_hash>
5. Test full flow: Add agent -> wait 15s -> verify on Etherscan (1 hour)

If resting:
- Rehearse demo 2-3 times (5-beat flow: Live Crew -> Command -> Add Agent -> 
  Mock Mode -> Solver Orchestration)
- Prepare backup screenshots/video in case live demo fails
- Rest and mental preparation

## Ecosystem ZCP2O Activity
Private-world tasks pending (to be documented in private folder):
- Protocol repo: [captain to fill]
- Product app: [captain to fill]

## Aliases Used
- the main protocol repo = the private ecosystem protocol repo
- the product app = the private example-product repo
- the private-ecosystem world = the second folder of this journal repo
