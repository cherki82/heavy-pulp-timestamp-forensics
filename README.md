# Heavy Pulp timestamp forensics

Public forensic report: <https://cherki82.github.io/heavy-pulp-timestamp-forensics/>

This repository documents 100 sustained timestamp discontinuities and 45 transient glitches across all 6,998 frames of `Heavy_Pulp_-_Somewhere_in_Sedona_v38gk3.mp4`.

- `index.html` is the published static report.
- `evidence/` contains all linked source-frame evidence and the per-frame AM/PM ledger.
- `reports/` contains the original Sedona-time report and the Provo-time conversion.
- `reports/robinson_temporal_comparison.md` documents the Robinson clock-event, playback, label, repeat, and mirror review, with one limited Heavy Pulp comparison.
- `build_page.py` rebuilds the static page from the source reports and embedded comparison section using only Python's standard library.

Source SHA-256: `9fbcd936366c423ae0c25b500f90ecf0b7534bfa8da1e394549edd1c0d4ffdf6`
