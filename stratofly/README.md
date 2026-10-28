# Stratofly World - Diary

Daily activity notes about the Stratofly world only: the open-source engine
(local-stratofly), the commercial app blueprint (stratofly), and the hackathon
build. This is a diary of what got done each day. It is NOT a spec document.

Structure: one folder per day, named DD-MM-YYYY, containing log.md (and extra
files only if a single day spans multiple topics). Example: 24-10-2026/log.md.

Typical daily entries: architecture decisions and the one-line reason; commits
made and the verification that went green; bugs found while testing, especially
ones you caused; drawing-table conclusions; wizard / dashboard / Telegram
progress.

Leak-risk: LOW. The engine repo is public, so naming its files (config.py,
lib/wizard.py, docs/*.md) is fine. Still obey the global rules: no secrets, and
do not drag private-ecosystem names into entries here (that belongs in the
other world folder).

Reminder: product specs (MEMORY, SETTINGS, ROLE-BLUEPRINT, WEB3-INTEGRATION)
live in engine docs/, not here. If a spec file appears in this folder, move it.
The free serverless API tier behind the engine is what makes the $0-modality
promise real; the diary tracks building on top of it, day by day.
