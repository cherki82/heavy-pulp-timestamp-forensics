# Tyler Robinson footage — timestamp and edit review

Prepared July 15, 2026. This appendix applies the same event convention used for *Heavy Pulp — Somewhere in Sedona* to footage presented during the July 6–10, 2026 preliminary hearing in *State of Utah v. Tyler James Robinson*.

The CourtTV files are recordings of a courtroom monitor, not clean exports of the underlying exhibits. Findings describe what is encoded in the reviewed files. They do not establish how the original surveillance systems stored or exported footage, and descriptions of the hearing evidence are not adjudicated facts.

## Event convention

- Frame numbers are zero-based decoded display frames.
- Day 2 runs at `30000/1001` frames per second.
- An abrupt boundary `a → b` is the last old frame followed by the first sustained new frame in the same camera view.
- The signed gap is `after displayed datetime − before displayed datetime`.
- “Intermediate seconds not shown” subtracts the ordinary one-second transition from that displayed-clock advance.
- Timestamps were read visually from exact source crops. OCR located candidates but was not treated as the evidentiary read; enhanced panels sit separately beneath the source pixels.

## Four frame-exact, within-camera clock discontinuities

| # | Day 2 video boundary | Source frames | Displayed clock before → after | View / scene evidence | Signed gap | Intermediate seconds not shown | Evidence |
|---:|:---|:---|:---|:---|:---:|---:|:---|
| 1 | `06:32.225 → 06:32.259` | `11,755 → 11,756` | `SEP 10 2025 11:53:17 AM → 11:54:30 AM` | Same exterior stair/tunnel view; person remains at the upper-left edge | **+00:01:13** | **72** | [exact timestamp pixels](../evidence/robinson_stair_115317_to_115430.png), [full view](../evidence/robinson_stair_full_view.png) |
| 2 | `09:06.146 → 09:06.179` | `16,368 → 16,369` | `SEP 10 2025 12:15:59 PM → 12:17:00 PM` | Same `CS - Roof - West - Overview Camera 4` view; moving white vehicle changes position | **+00:01:01** | **60** | [exact timestamp pixels](../evidence/robinson_day02_02_parking_121559_to_121700.png), [full view](../evidence/robinson_day02_02_parking_full_view.png) |
| 3 | `09:07.046 → 09:07.080` | `16,395 → 16,396` | `SEP 10 2025 12:17:01 PM → 12:17:04 PM` | Same Camera 4 view; same vehicle advances abruptly | **+00:00:03** | **2** | [exact timestamp pixels](../evidence/robinson_day02_03_parking_121701_to_121704.png), [full view](../evidence/robinson_day02_03_parking_full_view.png) |
| 4 | `09:07.247 → 09:07.280` | `16,401 → 16,402` | `SEP 10 2025 12:17:04 PM → 12:17:06 PM` | Same Camera 4 view; same vehicle advances again | **+00:00:02** | **1** | [exact timestamp pixels](../evidence/robinson_day02_04_parking_121704_to_121706.png), [full view](../evidence/robinson_day02_04_parking_full_view.png) |

The four adjacent displayed-clock changes total `+00:02:19` (139 seconds). After subtracting the four ordinary one-second transitions, the boundaries contain **135 intermediate clock seconds not shown**.

At ordinary playback speed, the first two patterns can reasonably appear to be `11:53:17 → 11:54:33` and `12:15:58 → 12:17:00 → 12:17:04`. Frame stepping establishes the exact adjacent boundaries above and exposes the brief `11:54:30–33`, `12:15:59`, `12:17:01`, and `12:17:04–06` states.

The Camera 4 block runs from frame 15,173 (`12:15:20 PM`) to frame 16,789 (`12:17:17 PM`): 117 displayed-clock seconds over approximately 53.92 seconds of CourtTV video. Its three boundaries account for exactly 63 excess seconds beyond ordinary transitions (`60 + 2 + 1`). No additional minute-scale positive clock advance is needed to reconcile that block.

## Large clock changes at camera switches — not counted as events

| Day 2 boundary | Source frames | Displayed clock | Camera change | Evidence |
|:---|:---|:---|:---|:---|
| `08:26.239 → 08:26.272` | `15,172 → 15,173` | `12:10:07 PM → 12:15:20 PM` | Camera 1 → Camera 4 | [timestamp pixels](../evidence/robinson_day02_camera_1_to_4_timeline_change.png) |
| `09:20.193 → 09:20.226` | `16,789 → 16,790` | `12:17:17 PM → 12:22:11 PM` | Camera 4 → Camera 1 | [timestamp pixels](../evidence/robinson_day02_camera_4_to_1_timeline_change.png) |

These changes remain useful scene-map facts, but the camera label and viewpoint change at the same boundary. They are therefore not classified as within-camera discontinuities.

## Other timestamp, playback, label, and repeat findings

### Stair/tunnel playback hold

The courtroom-player image remains at `11:53:07 AM` at Day 2 frames 6,300 and 11,200 even though their CourtTV video positions are `03:30.210` and `06:13.707`. A black/player interruption occupies frames 6,572–6,738, after which the same view and displayed second return. Playback later advances to `11:53:17` before event 1.

This is classified as a courtroom playback hold followed by a 73-second visible-clock discontinuity. It is not evidence that the surveillance camera itself stopped recording. Other high pixel-difference candidates in the held portion retained `11:53:07`; the former frames 11,807→11,808 candidate reads `11:54:35` on both sides. Those are filmed-monitor refresh/compression changes, not additional clock events.

### Missing or obscured clock pixels

- Day 1 contains two black/player interruptions followed by returns to the same residential view. No embedded timestamp or camera label is recoverable after levels, CLAHE, and corner/border enhancement, so the intervening source time cannot be measured. [Enhancement audit](../evidence/robinson_day01_no_timestamp_audit.png).
- Day 3's 449-frame booking-area clip forms one continuous view; no clock or camera label was recovered after enhancement.
- In some Day 2 views, white clock text falls on a nearly white background and cannot be read completely.
- CourtTV's opaque lower-third covers the leading timestamp fields in the later Day 2 night segment. Enhancement cannot reconstruct pixels that are covered or absent.
- The Day 4 Camera 1 replay runs continuously from approximately `12:24:17 PM` through `12:24:40 PM`, with no sustained forward or backward jump.

### Same area under different labels

The same feature-matched diagonal stair view appears under:

| Day 2 frames | Label shown |
|:---|:---|
| `2,095–2,657` | `Parking - Level 2 - Stairs - NE` |
| `5,982–6,132` | `Parking - Level 1 - Stairs - NE` |
| `13,788–13,960` | `Parking - Level 2 - Stairs - NE` |

The first-to-middle comparison produced 81 normal-orientation RANSAC inliers versus 6 after horizontal flipping. [Conflicting-label evidence](../evidence/robinson_same_stairs_conflicting_labels.jpg).

The same physical parking area is also shown by distinct `Overview Camera 1`, `Camera 4`, and `Camera 2` viewpoints. Camera 1 appears before and after the Camera 4 insert. This is overlapping coverage by different cameras, not identical footage under a different name. [Camera 1/4 overlap](../evidence/robinson_parking_camera_1_4_overlap.jpg).

### Official FBI file: consecutive repeat

The [official FBI video](https://www.fbi.gov/video-repository/utah-valley-shooting-video-091025.mp4/view) is 995 frames at 10 fps. It presents the same 177-frame / 17.7-second action block three times consecutively:

| Presentation | FBI source frames | Video interval | Start state |
|---:|:---|:---|:---|
| 1 | `146–322` | `14.6–32.2 s` | wide frame displaying `12:23:49 PM`; then digital crop/track |
| 2 | `323–499` | `32.3–49.9 s` | resets to the same wide `12:23:49 PM` frame |
| 3 | `500–676` | `50.0–67.6 s` | resets to the same wide `12:23:49 PM` frame again |

More than 95% of aligned frames remained below a mean-squared-error score of 8. The timestamp is cropped out during much of the tracked material, so content duplication—not a readable adjacent clock pair—establishes the repeats.

### Horizontal-mirror audit

All 13 repeated-view and cross-source feature comparisons favored normal orientation. The conflicting diagonal-stair label comparison produced 81 normal-orientation inliers versus 6 when flipped; the Camera 1/4 parking comparison produced 51 versus 5. **No horizontal-flip candidate survived feature scoring or visual review.**

## The only direct Heavy Pulp comparison

The cross-dataset comparison is restricted to Robinson event 1 and Heavy Pulp events 2–3 in Provo-adjusted time:

| Sequence | Displayed clock boundary |
|:---|:---|
| Robinson event 1 | `SEP 10 2025 11:53:17 AM → 11:54:30 AM` |
| Heavy Pulp event 2, Provo | `SEP 10 2001 11:53:01 AM → 11:54:27 AM` |
| Heavy Pulp event 3, Provo | `SEP 10 2001 11:54:30 AM → 11:54:36 AM` |

The Robinson jump and Heavy Pulp event 2 omit the same clock labels from `11:53:18` through `11:54:26`, inclusive: **69 shared absent seconds**. Heavy Pulp event 3 starts exactly at Robinson's `11:54:30` adjacent-frame destination. Robinson reaches `11:54:33` 0.63 CourtTV seconds later, inside Heavy Pulp event 3's range.

The start times are not identical, Heavy Pulp event 2 ends three seconds before Robinson's destination, and the calendar years differ by 24 years. This is a numerical timestamp comparison, not a finding of shared source, event, editor, or chain of custody.

Evidence:

- [CourtTV Day 2 at Robinson event 1](https://www.youtube.com/watch?v=y6ofpz6ReuE&t=3083s)
- [Robinson event 1 timestamp pixels](../evidence/robinson_stair_115317_to_115430.png)
- [Heavy Pulp event 2 source evidence](../evidence/sustained_002_frames_0253_0254.png)
- [Heavy Pulp event 3 source evidence](../evidence/sustained_003_frames_0370_0371.png)

No Heavy Pulp comparison is drawn from the other Robinson clock events, camera changes, phone/message times, reporting times, labels, repeats, or interruptions.

## Sources and integrity

- CourtTV broadcasts: [Day 1](https://www.youtube.com/watch?v=6fq2kCMVMXI), [Day 2](https://www.youtube.com/watch?v=y6ofpz6ReuE), [Day 3](https://www.youtube.com/watch?v=szsmK2Ul9XY), [Day 4](https://www.youtube.com/watch?v=89ZKQIHaJpM), and [Day 5](https://www.youtube.com/watch?v=bFwe5CwDudk).
- Day 2 extracted file SHA-256: `f9bafe5699d236e01f90b89f2e5580c4a196955ad3970406e5b3e023e9d243f8`.
- Official FBI file SHA-256: `d9287290bf7bae6c060897790b3372cb3df6a01498e812e38ddc2c5cb7d73851`.
- Heavy Pulp comparison data: [Provo report](timestamp_forensic_report_provo_ut.md) and [CSV ledger](../timestamp_event_data.csv).
