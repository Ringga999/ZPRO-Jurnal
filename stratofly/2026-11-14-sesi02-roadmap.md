\# Roadmap Eksekusi — Sesi 02, 14 November 2026



\*\*Penulis:\*\* Ringga

\*\*Proyek:\*\* local-stratofly (Stratofly Engine)

\*\*Sifat dokumen:\*\* PANDUAN EKSEKUSI AKTIF. Berlaku besok dan beberapa hari ke depan hingga selesai.

\*\*Sumber:\*\* Konsolidasi 6 diskusi hari ini + backlog yang menumpuk + 100 role catalog.



\---



\## 🎯 Tujuan Besar



1\. \*\*Sistem tim berdiri\*\* (ruleset, collaborators, batch workflow).

2\. \*\*100 role ter-author\*\* (US #1-50, TEAM #51-100).

3\. \*\*Kapabilitas core\*\* (clock, browsing, persona unification).

4\. \*\*Demo hackathon siap\*\* (UI polish, build-share, submission pack).

5\. \*\*Bukti nilai kustom\*\* (georesearch pack, simulation studio, asset-mgmt design).



\---



\## 📊 Master Backlog (ID, Owner, Effort, Dependency, Status)



\### Phase 0 — Gerbang \& Housekeeping (segera)

| ID | Item | Owner | Effort | Dep | Status |

|---|---|---|---|---|---|

| M01 | Create ruleset protect-main (Active, bypass Ringga999, target default branch, PR required, approvals=1, code owners, dismiss stale, block force push) | ADMIN | S | - | \*\*pending\*\* |

| M02 | Add collaborators (Write) via Settings → Collaborators → Add people; tim accept undangan | ADMIN+TEAM | S | M01 | pending |

| M03 | Kirim WA onboarding (link repo, katalog, workflow, batch, loop, guardrail) | ADMIN | S | M02 | pending |

| M04 | Unescape raw: jurnal 2026-11-14 + ROLE-CATALOG-100 (powershell regex) | US | S | - | pending |

| M05 | Publish release v0.1.0 dari tag (draft → publish) | ADMIN | S | - | pending |

| M06 | chain\_relay ABI getAnchor → 3 outputs (accuracy fix, tidak menggigit tapi tidak akurat) | US | S | - | pending |

| M07 | role-dropdown-rewire: wizard.py + UI baca /api/roles (hapus hardcoded 7) | US | M | - | pending |

| M08 | Konsolidasi dashboard.html legacy ke app.html | US | M | M07 | pending |



\### Phase 1 — Kapabilitas Core

| ID | Item | Owner | Effort | Dep | Status |

|---|---|---|---|---|---|

| M09 | Clock injection: suntik CURRENT TIME (ISO + timezone) ke system prompt via role\_registry | US | S | - | \*\*design-ready\*\* (anchor di tangan) |

| M10 | Browsing tool: /api/browse + SSRF guard (blokir localhost/IP privat) + timeout + rate-limit + privilege gate per-agen | US | M | M09 | design |

| M11 | Persona fallback + role-consolidation: unifikasi 3 rumah persona (agents/personas/\*.md, lib/persona.py, roles/\*.json) + fallback anggun | US | M | - | design |

| M12 | telegram\_listener inbound: handler /start, draft approval (polling atau webhook) | US | M | - | design (catatan: jaringan lokal blokir Bot API) |



\### Phase 2 — Authoring 100 Role (Paralel)

| ID | Item | Owner | Effort | Dep | Status |

|---|---|---|---|---|---|

| M13 | US author roles #1-50 (batch U1-U10; 10 seed diperluas modulnya + 40 baru) | US | L | M07 | pending |

| M14 | TEAM author roles #51-100 (batch B1-B10; admin review per batch) | TEAM | L | M01,M02,M03 | pending |

| M15 | Role JSON schema validator (fail fast; CI nanti) | US | S | M13,M14 | pending |



\### Phase 3 — Demo / Hackathon

| ID | Item | Owner | Effort | Dep | Status |

|---|---|---|---|---|---|

| M16 | UI polish: design tokens (warna/tipografi/spacing), dark mode, empty/loading states, responsif (tetap single-file app.html) | US | M | - | pending |

| M17 | Build-share: export/import JSON tersanitasi (agents, roles, modules, plugins, brains, limits; tanpa secret/path) | US | M | M13 | pending |

| M18 | README + demo script polish | US | S | M16 | pending |

| M19 | Hackathon submission pack | ADMIN | M | M16,M17,M18 | pending |



\### Phase 4 — Pack \& Simulasi (Custom Proof)

| ID | Item | Owner | Effort | Dep | Status |

|---|---|---|---|---|---|

| M20 | Georesearch pack: contoh komposisi user (GeoResearcher + ClimateAnalyst + ... + EnvironmentalReporter) | US/TEAM | M | M10,M14 | pending |

| M21 | Simulation Studio: 1-skenario proof (mis. tambak lobster) berparameter → HTML+JS+Three.js → label "ilustratif, bukan tersertifikasi" + review manusia | US | L | M13 | design |

| M22 | Asset-mgmt trust-tier design: read-only dulu, approval per write, never raw credentials, OAuth scopes ketat | US | M | M11 | deferred-design |



\### Phase 5 — Trust / Team Platform

| ID | Item | Owner | Effort | Dep | Status |

|---|---|---|---|---|---|

| M23 | Member model + directive board (v1: owner-authored, tanpa auth) | US | M | M14 | design |

| M24 | Multi-user auth (akun/login/permission sungguhan) | US | L | M23 | later |

| M25 | Rotasi NVIDIA key (hanya bila kuota anomali) | ADMIN | S | - | optional |



\### Recurring

\- Jurnal harian di ZPRO-jurnal (runbook style).

\- Admin PR review SLA ≤ 24 jam.



\---



\## 🔗 Dependency Graph



```

M01 → M02 → M03 → M14 (team mulai)

M07 → M13, M14 (dropdown bersih)

M09 → M10 → M20 (browsing gates georesearch)

M13 → M17, M21 (role siap → build-share, sim)

M16 → M18 → M19 (UI → README → submission)

M11 → M22 (persona unified → asset-mgmt trust)

M23 → M24 (directive board → auth)

```



\---



\## 📋 Eksekusi 50 Role US (#1-50) — Batch U1-U10



\*\*Prinsip:\*\* 10 seed (#1-7, 21, 41, 42) sudah ada → \*\*perluas modulnya\*\* (tambah modul planned → done). 40 sisanya = buat baru (roles/<nama>.json + persona + sel blueprint).



\### U1: #1-5 (seed: 1-5)

| # | Role | Status | Aksi |

|---|---|---|---|

| 1 | Solver | seed | Perluas modul: upload, simulation, draft\_queue (planned → done) |

| 2 | Architect | seed | Tambah modul: audit\_viewer, dependency\_graph, redesign\_editor |

| 3 | Crafter | seed | Tambah modul: spec\_input, code\_diff, test\_runner, pr\_creator |

| 4 | Analyst | seed | ✅ report\_gen done; tambah research\_input, source\_list, trend\_chart |

| 5 | Communicator | seed | Tambah modul: platform\_selector, tone\_selector, draft\_composer, approval\_queue, mention\_monitor |



\### U2: #6-10 (seed: 6-7)

| # | Role | Status | Aksi |

|---|---|---|---|

| 6 | Sentinel | seed | Tambah modul: scope\_selector, cve\_dashboard, breaking\_flags, compliance\_checklist |

| 7 | Operator | seed | Tambah modul: routine\_list, handoff\_timeline, pipeline\_health, ops\_summary, alert\_log |

| 8 | Dispatcher | baru | Buat: routing tugas, load balancing |

| 9 | Evaluator | baru | Buat: QA, rubric scoring |

| 10 | Reflector | baru | Buat: post-mortem, lesson extraction |



\### U3: #11-15 (semua baru)

| # | Role | Aksi |

|---|---|---|

| 11 | BackendEngineer | API, services, data layer |

| 12 | FrontendEngineer | UI, state, accessibility |

| 13 | MobileEngineer | Mobile apps, offline sync |

| 14 | DevOpsEngineer | CI/CD, infra, containers |

| 15 | DatabaseEngineer | Schema, queries, migrations |



\### U4: #16-20 (semua baru)

| # | Role | Aksi |

|---|---|---|

| 16 | APIDesigner | Contracts, versioning, docs |

| 17 | CodeReviewer | Static review, style, security |

| 18 | TestEngineer | Unit/integration/e2e tests |

| 19 | RefactorSpecialist | Safe restructuring, debt reduction |

| 20 | BuildReleaseEngineer | Packaging, versioning, changelog |



\### U5: #21-25 (seed: 21)

| # | Role | Status | Aksi |

|---|---|---|---|

| 21 | DataScientist | seed | ✅ report\_gen done; tambah dataset\_input, notebook\_runner, chart\_gallery, model\_card |

| 22 | DataEngineer | baru | Pipelines, ETL, quality |

| 23 | MLEngineer | baru | Train/eval/deploy models |

| 24 | PromptEngineer | baru | Prompt design, eval |

| 25 | DataAnnotator | baru | Labeling, schema, QA |



\### U6: #26-30 (semua baru)

| # | Role | Aksi |

|---|---|---|

| 26 | Statistician | Inference, tests, uncertainty |

| 27 | VisualizationDesigner | Charts, dashboards |

| 28 | NLPSpecialist | Extraction, NER, summarization |

| 29 | ComputerVisionSpecialist | Detection, segmentation |

| 30 | MLOpsEngineer | Registry, monitoring, drift |



\### U7: #31-35 (semua baru)

| # | Role | Aksi |

|---|---|---|

| 31 | Researcher | Source gathering, synthesis |

| 32 | LiteratureReviewer | Survey, gap analysis |

| 33 | FactChecker | Verification, cross-source |

| 34 | Summarizer | Condense, preserve meaning |

| 35 | Translator | Multilingual, locale |



\### U8: #36-40 (semua baru)

| # | Role | Aksi |

|---|---|---|

| 36 | Ontologist | Taxonomy, knowledge graphs |

| 37 | CitationManager | Reference formatting, dedupe |

| 38 | TrendAnalyst | Signal detection, time series |

| 39 | CompetitiveAnalyst | Competitor mapping, positioning |

| 40 | KnowledgeCurator | Organize, tag, maintain KB |



\### U9: #41-45 (seed: 41-42)

| # | Role | Status | Aksi |

|---|---|---|---|

| 41 | VideoEditor | seed | Tambah modul: script\_editor, shot\_list, render\_queue, asset\_library, publish\_approval |

| 42 | SocialMedia | seed | Tambah modul: platform\_selector, tone\_selector, draft\_composer, approval\_queue, schedule\_calendar |

| 43 | Copywriter | baru | Persuasive copy, brand voice |

| 44 | TechnicalWriter | baru | Docs, manuals, clarity |

| 45 | Scriptwriter | baru | Narrative, dialogue, structure |



\### U10: #46-50 (semua baru)

| # | Role | Aksi |

|---|---|---|

| 46 | PodcastProducer | Outline, show notes, audio plan |

| 47 | GraphicDesigner | Layout, visual identity |

| 48 | UXWriter | Microcopy, flows |

| 49 | SEOStrategist | Keywords, structure, metrics |

| 50 | CommunityManager | Engagement, moderation, sentiment |



\---



\## 📋 Eksekusi 50 Role TEAM (#51-100) — Batch B1-B10



\*\*Prinsip:\*\* Tim garap 10 batch @5 role. Admin review per batch. Guardrail wajib untuk B1-B4 (security/finance) \& B7-B8 (simulation): field read\_only, requires\_approval, illustrative + sign-off admin.



\### B1: #51-55 (Security — guardrail)

51\. SecurityAuditor · 52. PenTester · 53. CryptographyAdvisor · 54. PrivacyOfficer · 55. ComplianceAnalyst



\### B2: #56-60 (Security — guardrail)

56\. LicenseAuditor · 57. IncidentResponder · 58. ThreatModeler · 59. AccessController · 60. AuditLogger



\### B3: #61-65 (Finance — guardrail)

61\. Bookkeeper · 62. BudgetAnalyst · 63. ExpenseTracker · 64. InvoiceClerk · 65. PayrollAssistant



\### B4: #66-70 (Finance — guardrail)

66\. TaxPreparer · 67. AssetRegistrar · 68. PortfolioAnalyst · 69. RiskAssessor · 70. FinanceReporter



\### B5: #71-75 (Geo)

71\. GeoResearcher · 72. ClimateAnalyst · 73. WeatherForecaster · 74. GISMapper · 75. HydrologyAnalyst



\### B6: #76-80 (Geo)

76\. SeismologyAnalyst · 77. EcologyAnalyst · 78. AgricultureAdvisor · 79. DisasterModeler · 80. EnvironmentalReporter



\### B7: #81-85 (Simulation — guardrail)

81\. PhysicsSimulator · 82. ChemistrySimulator · 83. MechanicalSimulator · 84. AerospaceSimulator · 85. CivilStructuralSimulator



\### B8: #86-90 (Simulation — guardrail)

86\. BiologicalSimulator · 87. EpidemiologyModeler · 88. EconomicsModeler · 89. TrafficSimulator · 90. EnergySystemsModeler



\### B9: #91-95 (Ops)

91\. ProjectManager · 92. ProductManager · 93. ScrumMaster · 94. HRCoordinator · 95. Recruiter



\### B10: #96-100 (Ops)

96\. CustomerSupport · 97. SalesStrategist · 98. MarketingAnalyst · 99. SupplyChainAnalyst · 100. ExecutiveBriefer



\---



\## 🚦 Next 3 Actions (Segera)



1\. \*\*Phase 0:\*\* M01 Create ruleset → M02 collaborators → M03 WA onboarding.

2\. \*\*Housekeeping:\*\* M04 unescape → M05 release v0.1.0 → M06 ABI fix.

3\. \*\*Core:\*\* M09 clock (anchor siap) → M10 browsing design.



\---



\## ✅ Checklist Harian



\- \[ ] Phase 0 selesai (M01-M08)

\- \[ ] 1 batch US selesai (5 role)

\- \[ ] 1 batch TEAM selesai (5 role, review admin)

\- \[ ] Jurnal harian di ZPRO-jurnal

\- \[ ] SLA review ≤ 24 jam



\---



\## 📝 Catatan Penting



\- \*\*Katalog = menu, devisi = komposisi user.\*\* Tidak ada preset terkunci.

\- \*\*Limit agen (max\_per\_provider/max\_total) ≠ lebar katalog.\*\* Katalog 100 = kapabilitas; agen aktif tetap dibatasi free-tier.

\- \*\*Guardrail wajib\*\* untuk role sensitif (security/finance/simulation).

\- \*\*Copy dari raw, bukan render.\*\* Escape bersembunyi di lapisan mentah.

\- \*\*Nama penulis = Ringga\*\* (bukan Ringga Putra). Sapaan chat = Mr Visioner.



\---



\*\*Dibuat:\*\* 14 November 2026, \~malam

\*\*Status:\*\* AKTIF — berlaku besok dan beberapa hari ke depan.

\*\*Mood:\*\* Terstruktur, siap eksekusi.

