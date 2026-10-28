# ZPRO Journal (Public Build Diary)

Daily activity log. This repo publicly records WHAT GOT DONE each day, in detail. 
It is a transparent diary of the build process, NOT a documentation vault. 
Product specifications (memory, settings, roles, web3) live in the engine repo 
under `local-stratofly/docs/`, NEVER here. Keeping that line sharp is the whole 
point of this repo.

Visibility: PUBLIC. This transparency demonstrates our development process, 
architecture decisions, and honest bug reporting. However, strict rules apply 
to protect sensitive infrastructure.

Structure (the tidy rule): one FOLDER per day, named DD-MM-YYYY, holding that 
day's detail. Pattern: `stratofly/DD-MM-YYYY/log.md` (example: `stratofly/24-10-2026/log.md`).

## Global Rules (Strictly Enforced)
1. **No Secrets.** Never write an API key, token, password, or wallet private key, 
   even partially. If a secret was involved, write `[redacted]` or describe the action.
2. **Alias Private Repos.** Never write the literal name of a private ecosystem 
   repo. Use aliases like `the main protocol repo` or `the product app`. Public 
   engine file names (`config.py`, `lib/wizard.py`, `docs/*.md`) are fine to name.
3. **Honesty Over Polish.** Record bugs you caused and fixes you regret. The value 
   of a public diary is truth and learning, not perfect presentation.
4. **No Product Specs Here.** If you find a spec file here, it is in the wrong 
   place; move it to `engine docs/`.

## Why a Diary at All?
The agents get a Memory feature to remember their work; this journal is the human 
mirror. Eventually, the AI-insights layer will read BOTH the agent memory and this 
diary to produce weekly "what-we-achieved" and "what-is-stuck" reports. For now, 
it simply ensures we remember our journey, and allows the community to learn from 
our real-world build process.
