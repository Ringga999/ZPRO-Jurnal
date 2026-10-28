# 2026-10-25 (Sunday) - H-1 hackathon

NOTE ON DATE: today is Sunday 2026-10-25 (H-1). This folder is dated 25-10-2026
because the captain asked the diary to follow the demo-day folder pattern; the
actual work below happened on the 25th. (See the structure lesson further down.)

## Decided
- Web3 = Opsi A (the honest path). The captain chose NOT to put data on-chain
  for the demo. Decision locked: HASH ON-CHAIN, BLOB OFF-CHAIN, hybrid
  architecture, executed Tuesday-Wednesday AFTER the demo. Reason: storing
  blobs on-chain is expensive and slow; making the demo depend on a faucet is
  a single point of failure; and Web3-for-show would be theater, which the
  captain already rejected once today. The free serverless API tier (the NVIDIA
  build portal) is what makes the $0-modality promise real on stage; the chain
  anchor is a trust bonus layered on top later, never a dependency.
- Product specs belong in the engine repo docs/, NOT in this journal. The
  journal is a daily activity diary only. ROLE-BLUEPRINT and WEB3-INTEGRATION
  were moved to local-stratofly/docs/ so a jury who clones the engine sees the
  full planning depth (now 4 specs in docs/: MEMORY, SETTINGS, ROLE-BLUEPRINT,
  WEB3-INTEGRATION).
- Journal structure corrected to FOLDER-PER-DAY: stratofly/<DD-MM-YYYY>/log.md,
  matching the captain example path stratofly/26-10-2026/. Not file-per-day,
  not a year subfolder. Tidy means one folder per day holding that day detail.
- Role UI blueprint added to the spec: one page per agent, but MODULAR by role
  (Solver sees upload + delegation board; Communicator sees tone + approval
  queue; Sentinel sees the CVE dashboard; no role sees another role toolkit).
  This is "rapi" (tidy) that the captain asked for, and it is now in the spec
  as Section UI/NAVIGATION.

## Built / Fixed
- fix_journal_structure.py (this very script): wrote ROLE + WEB3 specs to the
  engine docs/; rebuilt the diary as folder-per-day (23, 24, 25 Oct); removed
  every spec file from the journal; refreshed both READMEs to declare the new
  structure and the rule that product specs never live here; cleaned leftover
  installer scripts from the journal root; ran a smoke test proving the engine
  .py files were NOT touched (Monday stays frozen and green).

## Bugs found (honest, including my own process errors today)
1. I had placed product SPECS inside the journal. Wrong home. The journal is a
   diary; specs are product documentation and belong in engine docs/. Caught by
   the captain. Fixed by relocation + deletion from the journal.
2. I had used a file-per-day structure (2026/2026-10-24.md). The captain wants
   folder-per-day (24-10-2026/). Fixed by rebuilding the diary layout.
3. A guard FALSE-POSITIVE had silently blocked the Friday and Saturday diary
   entries from ever being written: the old guard flagged the obvious
   placeholder text (the NVIDIA and GitHub key FORMAT prefixes) as a leak and
   aborted the whole write. So the journal had NO diary at all until today.
   Fixed two ways: the guard is now PRECISE (it only catches real-length keys
   and literal private repo names, not placeholders or folder names), AND the
   diary text avoids writing those prefixes literally so even an external
   secret scanner stays quiet. Lesson: a guard that is too dumb is worse than
   no guard, because it fails silently and you trust the empty result.
4. The captain also caught that I had NOT yet instructed the per-role UI /
   navigation (different page per agent, tailored to role). That gap is now
   closed in the ROLE spec Section UI/NAVIGATION.

## Open questions
- After the demo: do we split the public-safe stratofly diary into its own
  public repo, keeping the private-ecosystem world private? The folder-per-day
  structure already makes that split trivial.
- Tuesday: confirm the Sepolia faucet is reachable before building the chain
  relay, so the Web3 milestone does not stall on a dead faucet.

## Tomorrow (Plan)
- MONDAY: REHEARSE the honest demo twice (open localhost, type a random command
  in Command the Crew, watch the crew answer; trigger the HARD-limit refusal;
  flip Mock on). Then FREEZE. No code changes before the stage.

## Aliases used today
- the main protocol repo = the private ecosystem protocol repo
- the product app = the private example-product repo
- the private-ecosystem world = the second folder of this journal repo
