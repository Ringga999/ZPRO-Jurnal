# 2026-10-23 (Friday) - H-3 hackathon

## Decided
- Security audit of the public engine repo = CLEAN. config.py reads every
  credential via os.getenv(); .env and the instance settings.json are both
  git-ignored, so no key or token is reachable from GitHub. The .env.example
  holds only obvious placeholder values (no real keys anywhere).
- Held the line on two minor findings instead of fixing them on the spot:
  (a) the example file still shows the private-ecosystem repos as its REPOS
  sample, and (b) it carries a dead client-id field that config.py never reads.
  Both are public-facing cosmetics, NOT leaks. Deferred to a captain decision
  rather than edited unilaterally under deadline. Lesson recorded: do not move
  data across the private/public boundary without an explicit order.
- S2 part-1 architecture: config.py DELEGATES brains, agents, repos to the
  instance settings.json, with a .env fallback for backward compatibility.
  This protects the private world: the watched-repo list now lives in a
  git-ignored file, so the public repo never has to carry it.
- Doctrine reaffirmed: spec-leads-code. A spec may promise a future schema,
  but the code constant is NOT bumped until the fields it promises exist.

## Built / Fixed
- Rewrote config.py: try-load lib.settings then read REPOS, BRAINS, AGENT_BRAIN
  from settings.json; on any exception fall back to legacy .env parsing. Added
  a tolerant chain parser (provider/model CSV) and a settings-driven agent to
  brain map with a hardcoded default only as a last resort.
- Verified green from the terminal: REPOS resolved from settings (shown here as
  the main protocol repo via alias), 3 brains = WORKHORSE, SPECIALIST, LIFELINE,
  10 agents. Committed and pushed.

## Bugs found
- No code bug today. One PROCESS miss caught by the captain: I nearly offered a
  blanket example-file sanitizer without respecting the standing boundary
  do not touch the private ecosystem. Stopped before writing. Recorded so the
  reflex becomes: ask before crossing the private/public line.

## Open questions
- Should the example file be generic-ized for hackathon consistency, or left
  as-is? (Captain call; not urgent, not a leak.)

## Tomorrow (Plan)
- S2 part-2: the 7-step settings wizard CLI, wiring model-kind badges and the
  hard/soft limits into the user-facing doors.

## Aliases used today
- the main protocol repo = the private ecosystem protocol repo (dogfood target)
- the product app = the private example-product repo
