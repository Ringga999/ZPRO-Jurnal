\# Roadmaping Ulang — 18 November 2026



\*\*Penulis:\*\* Ringga

\*\*Proyek:\*\* local-stratofly (Stratofly Engine)

\*\*Sifat dokumen:\*\* PETA ULANG ROADMAP + DUA SPRINT TERPISAH. Sumber kebenaran terbaru (supersedes status di `2026-11-14-sesi02-roadmap.md` dan penugasan sprint di `2026-11-15.md`).

\*\*Prinsip:\*\* Sprint-1 Concordium (→9 Des) dan Sprint-2 Cosmo (19 Des→18 Jan) BERURUTAN, tidak tumpang tindih, tidak dicampur.



\---



\## 0. Kenapa Dipetakan Ulang



1\. Banyak item selesai sejak roadmap sesi02 ditulis, tapi status file itu masih `pending` (stale).

2\. Fitur wallet user-owned (di luar daftar M awal) selesai 17–18 Nov → mengubah kelayakan Concordium.

3\. Timeline Concordium (→9 Des) dan Cosmo (19 Des→) berurutan → bisa dua tembakan, bukan pilih satu.

4\. Koreksi: "Cosmo buka besok" (15/18 Nov) SALAH; 19 Des ≈ 1 bulan lagi. Deadline dekat = Concordium.



\---



\## 1. Rekonsiliasi Status (semua item)



\### ✅ SELESAI

| ID | Item | Bukti |

|---|---|---|

| M01 | ruleset protect-main | Active, bypass Ringga999 |

| M04 | unescape raw | 3 file bersih; .bak.unescape dibersihkan 18 Nov |

| M16 | UI polish | ops-dark teal #39C6C0 + telemetry atas + Settings/Plugins/Tutorial + accent picker + ikon SVG |

| M06 | getAnchor ABI 3 + read\_anchor + GET /api/memory/anchor | JSON ok:true, owner=wallet user |

| M09 | clock injection | smoke ALL GREEN; UI jawab waktu WIB nyata |

| — | QuietServer | WinError 10053 diredam; terminal tenang |

| — | Wallet user-owned (Step1-3) | connect→prepare→MetaMask sign→persist; tx 0x1aafc946 (uji), 0x10c59a61 (ask nyata) |

| — | Kontrak redeploy+verify | 0x2c4F4712…70E2B5a65, Read Contract hidup |

| — | Katalog100 + TEAM-WORKFLOW + CODEOWNERS + CONTRIBUTING ext | ter-push |

| — | Concordium Checkpoint 1 | project + idea + challenge tertaut (deadline 22 Nov sudah aman) |



\### 🟡 PENDING (backlog / housekeeping / shared)

| ID | Item | Penempatan |

|---|---|---|

| M05 | publish release v0.1.0 | gap antar-sprint |

| M07 | dropdown-rewire (wizard.py + dashboard.html) | gap antar-sprint |

| M08 | konsolidasi dashboard.html | gap antar-sprint |

| M15 | validator JSON role | gap antar-sprint |

| M17 | build-share export/import | Sprint-2 |

| M18 | README + script demo | shared (aset kedua sprint) |

| M19 | submission pack | Sprint-2 |

| M13 | US roles subset (5-10 hero) | Sprint-2 (opsional) |

| M10 | browsing + SSRF | backlog (enabler georesearch Sprint-2) |

| M11 | persona-consolidation | backlog |

| M12 | telegram\_listener | backlog |

| M20 | georesearch pack | backlog / opsi vertical Sprint-2 |

| M21 | simulation studio | backlog / opsi vertical Sprint-2 |

| M22 | asset-mgmt trust design | backlog |

| M25 | rotasi NVIDIA | opsional |



\### 🔵 FREEZE (tim absen sampai \~15 Des) → unfreeze di H3

M02 collaborators · M03 WA onboarding · M14 TEAM #51-100 · M23 directive board · M24 auth.



\---



\## 2. SPRINT-1 — CONCORDIUM (now → 9 Des 2026)



\*\*Target:\*\* submit 9 Des 23:59 UTC. Judging 10–11 Des. Hadiah 1M CCD ×3 + eligibility Grants 75M CCD.

\*\*Syarat wajib:\*\* jalan di \*\*Concordium testnet\*\* + ≥1 komponen Concordium signifikan.

\*\*Judging:\*\* depth of integration + path-to-production + it-works (demo end-to-end) + usefulness. BUKAN jumlah transaksi.

\*\*Aset submit:\*\* deskripsi + repo publik + video demo ≤3 menit + link CCDExplorer + dokumen path-to-production.



\### Komponen integrasi (ID C)

| ID | Komponen | Isi | Prioritas |

|---|---|---|---|

| C1 | Agent Registry + badge | daftarkan agen di Agent Registry Concordium testnet (ERC-8004 Agent Card) + Verified-by-Concordium badge; tautkan alamat Ethereum existing | INTI |

| C2 | Accountability anchor | mirror chain\_relay: anchor hash memori ke Concordium testnet (jejak EU AI Act Art.12) | INTI |

| C3 | MCP / A2A lookup | endpoint MCP/A2A menyajikan Agent Card + badge agar agen lain memverifikasi sebelum berurusan | INTI |

| C4 | Concordium ID / Verify\&Access | gate atribut (mis. usia) tanpa simpan data pribadi (ZK) | stretch |

| C5 | x402 payments | agen bayar/dibayar agen lain + sponsored tx | stretch |



\*\*Gap jujur:\*\* anchor kita kini Ethereum Sepolia; C1/C2 memindahkan/menambah jalur ke Concordium testnet = pemenuhan syarat wajib. Workshop 6 (18 Nov 22:00 WIB) = resep C1/C3 (Agent Registry MCP + A2A).



\### Timeline Sprint-1

| Tanggal | Aksi |

|---|---|

| 18 Nov (hari ini) | Workshop 6 22:00 WIB; verifikasi Checkpoint 1 di platform; commit trio M06/M09/QuietServer |

| 19–22 Nov | tonton rekaman W1–W4; baca developer hub + Agent Registry reference; putuskan path SDK (Python-gRPC vs Node-sidecar vs MCP-only); Checkpoint 1 deadline 22 Nov (sudah aman) |

| 23–29 Nov | build C1+C2+C3 di Concordium testnet; office hours Sel/Jum 15:00 UTC |

| 30 Nov–5 Des | demo end-to-end + UI badge + rekam video ≤3 menit (A1) + dokumen path-to-prod + CCDExplorer (A2) |

| 6–8 Des | polish + buffer |

| 9 Des | SUBMIT (A3) 23:59 UTC |

| 10–11 Des | judging |



\### Aset submit Sprint-1 (ID A)

A1 video demo ≤3 menit · A2 path-to-production doc + link CCDExplorer · A3 submit final 9 Des.

(M18 README/demo script = aset shared yang menopang A1/A2.)



\### Risiko + mitigasi

| Risiko | Mitigasi |

|---|---|

| Kurva belajar SDK Concordium | Workshop 6 + office hours Sel/Jum + jalur minimal MCP-only bila perlu |

| Hadiah non-cash (CCD) | nilai = Grants 75M CCD + portfolio + kredibilitas; bukan cash |

| Bandwidth solo | inti C1+C3 dulu; C2 menyusul; C4/C5 hanya bila waktu |

| Testnet perlu CCD | faucet test CCD gratis |



\---



\## 3. GAP ANTAR-SPRINT (10–18 Des)



\- Housekeeping: M05 release, M07 dropdown-rewire, M08 dashboard, M15 validator.

\- \~15 Des: tim kembali → H3 onboarding (unfreeze M02/M03/M14).

\- Persiapan Cosmo: pilih vertical, setup repo/demo.

\- Istirahat terukur setelah submit Concordium.



\---



\## 4. SPRINT-2 — COSMO HACKS (19 Des 2026 → 18 Jan 2027)



\*\*Target:\*\* submit 18 Jan. Prize $146,700. Online, open-ended, Devpost standard (GitHub + demo), minimal platform-lock.

\*\*Tim:\*\* kembali \~15 Des → ikut sprint ini (H3).



\### Item Sprint-2 (ID H)

| ID | Item | Tanggal |

|---|---|---|

| H1 | registrasi Cosmo saat buka | 19 Des |

| H2 | putuskan vertical slice (user-owned memory+accountability / georesearch / simulation) | 19–26 Des |

| H3 | onboarding tim (unfreeze M02/M03/M14; batch B1-B10) | \~15–19 Des |

| H4 | build-share (M17) | 19–26 Des |

| H5 | README + demo script (M18) + hero roles (M13 opsional) | 27 Des–10 Jan |

| H6 | submission pack (M19) + submit | 11–18 Jan |



\### Vertical yang direkomendasikan

User-owned agentic memory + accountability (leverage wallet layer yang sudah jadi) — paling sedikit kerja baru, paling kuat narasinya. Georesearch/simulation = opsi bila ingin wow visual (butuh M10/M21).



\---



\## 5. Dependency Graph (diperbarui)



```

Wallet user-owned (done) → C1/C2/C3 (Concordium) → A1/A2 → A3 submit 9 Des

M18 (shared) → A1/A2 dan H5

Gap: M05/M07/M08/M15 → UI bersih untuk H4/H5

Tim kembali \~15 Des → H3 → M14 batch → H6

H1 register 19 Des → H2 vertical → H4/H5 → H6 submit 18 Jan

M10 (backlog) → M20 georesearch (opsi vertical H2)

```



\---



\## 6. Yang SENGAJA tidak masuk kedua sprint (backlog)

M10 browsing (kecuali dipilih vertical georesearch), M11 persona, M12 telegram, M21 simulation (kecuali vertical), M22 asset-mgmt, M25 rotasi. Freeze tim sampai H3.



\---



\## 7. Cadence + Checklist

\- Harian: jurnal di ZPRO-jurnal; commit per item; gerbang verifikasi sebelum commit.

\- Sprint-1 checklist: \[ ] Workshop 6 \[ ] path SDK \[ ] C1 \[ ] C2 \[ ] C3 \[ ] A1 \[ ] A2 \[ ] A3 submit 9 Des.

\- Sprint-2 checklist: \[ ] H1 \[ ] H2 \[ ] H3 \[ ] H4 \[ ] H5 \[ ] H6 submit 18 Jan.

\- SLA review admin ≤24 jam (setelah tim kembali).



\---



\## 8. Decision Log (perubahan vs dokumen sebelumnya)

| Tanggal | Keputusan | Alasan |

|---|---|---|

| 15 Nov | Concordium demoted (ribet), Cosmo primary | effort solo 3 minggu + checkpoint/video/SDK |

| 18 Nov | Concordium RE-PROMOTED sprint-1; Cosmo sprint-2 | wallet layer sudah bangun separuh brief; timeline berurutan; Workshop 6 = resep |

| 18 Nov | koreksi "Cosmo besok" → 19 Des (\~1 bulan) | kesalahan tanggal saya |

| 18 Nov | file ini = sumber kebenaran status | roadmap sesi02 stale |



\---



\## 9. Next Actions (segera, berurutan)

1\. Tonton Workshop 6 (18 Nov 22:00 WIB) — catat: endpoint Agent Registry MCP, format Agent Card, cara verifikasi badge cross-chain.

2\. Verifikasi Checkpoint 1 di platform Encode (project terlihat).

3\. Baca developer hub + Agent Registry reference → putuskan path SDK.

4\. Desain integrasi C1/C2/C3 (di chat, tanpa kode) → approve → eksekusi.

5\. Sprint-2 menunggu 19 Des (H1).



\*\*Ditutup:\*\* 18 Nov 2026

\*\*Status:\*\* peta ulang berdiri; dua sprint terpisah; Concordium sprint-1 aktif.

