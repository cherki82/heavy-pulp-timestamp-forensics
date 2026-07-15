# Heavy Pulp timestamp discontinuity report

Source: `Heavy_Pulp_-_Somewhere_in_Sedona_v38gk3.mp4`

Source SHA-256: `9fbcd936366c423ae0c25b500f90ecf0b7534bfa8da1e394549edd1c0d4ffdf6`

## Findings

- **100 sustained timestamp discontinuities** were found.
- **45 transient timestamp glitches** were found: 34 one-frame glitches, 9 two-frame glitches, and 2 compound glitches.
- Four sustained displayed datetimes run backward: events 4, 48, 74, and 98.
- Five sustained transitions are blended/cross-faded rather than occurring between two adjacent clean frames: events 29, 41, 42, 86, and 97.
- The first legible timestamp appears at frame 51. That initial appearance is not counted as a discontinuity.
- A separate all-frame meridiem audit found two sustained AM/PM transitions and **no transient AM/PM glitches**.
- No timestamp is visible in 94 frames: 0–50, 187–223, and 6992–6997.

Where the timestamp is visible, the displayed date is `SEP 10 2001` through frame 6896 and `SEP 11 2001` from frame 6897 through frame 6991. In the sustained table, events 1–6 are AM, event 7 crosses from AM to PM, events 8–99 are PM, and event 100 crosses from PM to AM.

## Frame and time conventions

- The video is constant-frame-rate H.264: 720 × 528, 30 fps, 6,998 frames, 233.267 seconds.
- Frame numbers are zero-based. A frame's video time is `frame / 30`.
- Values in the **Video boundary**, **Video time**, and **Video-frame time** fields are elapsed positions within the video, so AM/PM does not apply to them. Every displayed camera-clock time is explicitly marked AM or PM.
- For an abrupt transition `a → b`, frame `a` is the last frame showing the old clock and frame `b` is the first frame showing the new clock.
- For a cross-fade, the listed frames are the last clean old frame and first clean new frame. Frames between them contain a visual mixture of both timestamp states.
- Clock values were read by direct visual inspection of the source frames. Temporal differencing of the timestamp glyph area was used to locate candidates; generic OCR output was not used as the evidentiary read.

## Signed gap conventions

- A sustained **Signed timestamp gap** is `after displayed datetime − before displayed datetime`, including AM/PM and the displayed date.
- Positive gaps begin with `+`. Negative gaps begin with `−` and are also labeled **negative**.
- For a cross-fade, the gap uses the last clean old timestamp and first clean new timestamp.
- Event 100 is `+10:55:54`, not negative: its clock face moves from 7:07 PM to 6:03 AM, but the displayed date advances from `SEP 10` to `SEP 11`.
- A transient **Signed display changes** cell gives the signed difference for each consecutive arrow in its timestamp sequence.

## Total signed time gap

Using the requested convention—add every positive sustained timestamp gap and subtract every negative sustained timestamp gap—the totals are:

- Positive gaps: `+108,400 seconds`
- Negative gaps: `−39,504 seconds`
- **Net signed gap: `+68,896 seconds` (`19:08:16`)**

The arithmetic is `108,400 − 39,504 = 68,896 seconds`. Transient glitches are excluded because they are momentary display excursions rather than sustained missing intervals. This total measures discontinuities in the displayed timestamp; by itself, it does not prove that exactly 68,896 seconds of original recording was physically removed.

## Complete AM/PM frame audit

All 6,998 decoded frames were evaluated separately for the meridiem marker. A fixed-position glyph comparison classified every visible marker; all 40 visible low-confidence frames, both state changes, and every timestamp-visibility boundary were then inspected directly. OCR was not used.

| Source frames | Video-frame time | Frames | Result |
|:---|:---|---:|:---|
| 0–50 | 00:00.000–00:01.667 | 51 | no visible timestamp |
| 51–186 | 00:01.700–00:06.200 | 136 | **AM** |
| 187–223 | 00:06.233–00:07.433 | 37 | no visible timestamp |
| 224–593 | 00:07.467–00:19.767 | 370 | **AM** |
| 594–6896 | 00:19.800–03:49.867 | 6,303 | **PM** |
| 6897–6991 | 03:49.900–03:53.033 | 95 | **AM** |
| 6992–6997 | 03:53.067–03:53.233 | 6 | no visible timestamp |

The only meridiem changes are:

- Frame 593 → 594 at video time `00:19.800`: `12:52:27 AM → 01:21:20 PM`.
- Frame 6896 → 6897 at video time `03:49.900`: `07:07:51 PM → 06:03:45 AM`. The displayed date simultaneously changes from `SEP 10 2001` to `SEP 11 2001`.

Supporting audit material:

- [Per-frame AM/PM ledger](supporting_frames/ampm_frame_audit.txt) — one status for each of the 6,998 frames.
- [Both meridiem transitions](supporting_frames/ampm_transition_evidence.png).
- [Timestamp visibility boundaries](supporting_frames/ampm_visibility_boundaries.png).
- Low-confidence visual review: [page 1](supporting_frames/ampm_low_confidence_review_1.png), [page 2](supporting_frames/ampm_low_confidence_review_2.png), [page 3](supporting_frames/ampm_low_confidence_review_3.png), and [page 4](supporting_frames/ampm_low_confidence_review_4.png).

## Supporting frame links

Every table row now includes a **view frames** link. Each link opens a labeled PNG evidence strip containing the relevant lower-right region decoded from the source video:

- Abrupt discontinuities show at minimum the last old frame and first new frame. Where a two-panel strip could be visually ambiguous, adjacent old/new context frames are also included.
- Cross-fades show the last clean old frame, a midpoint blend frame, and the first clean new frame.
- Transient glitches show the preceding frame, every anomalous frame, and the following frame.

The evidence region is source coordinates x=480–719 and y=445–527. It is stored in lossless PNG and enlarged 3× with nearest-neighbor scaling so the displayed pixels are not interpolated. Labels are placed outside the source-frame pixels.

### Evidence screenshot verification

All 145 event-linked strips were compared visually with their report rows and the adjacent decoded source frames. A second pixel-level provenance check verified that every image panel is the exact x=480–719, y=445–527 region from the source frame identified in its label, enlarged only by 3× nearest-neighbor scaling.

That review corrected six affected rows and rebuilt their strips with additional context: sustained events 31, 38, 42, 64, and 82, and transient event 26. The corrections cover three one-second reads, two frame-boundary selections, and one glitch duration. No other linked screenshot/description mismatch was found.

## Sustained discontinuities

| # | Video boundary | Source frames | Timestamp before → after | Type | Signed timestamp gap | Evidence |
|---:|:---|:---|:---|:---|:---:|:---:|
| 1 | 00:05.667 | 169 → 170 | 10:52:04 AM → 10:53:01 AM | abrupt | +00:00:57 | [view frames](supporting_frames/sustained_001_frames_0169_0170.png) |
| 2 | 00:08.467 | 253 → 254 | 10:53:01 AM → 10:54:27 AM | abrupt | +00:01:26 | [view frames](supporting_frames/sustained_002_frames_0253_0254.png) |
| 3 | 00:12.367 | 370 → 371 | 10:54:30 AM → 10:54:36 AM | abrupt | +00:00:06 | [view frames](supporting_frames/sustained_003_frames_0370_0371.png) |
| 4 | 00:16.067 | 481 → 482 | 10:54:39 AM → 12:01:27 AM | abrupt; backward | −10:53:12 (negative) | [view frames](supporting_frames/sustained_004_frames_0481_0482.png) |
| 5 | 00:17.767 | 532 → 533 | 12:01:28 AM → 12:35:27 AM | abrupt | +00:33:59 | [view frames](supporting_frames/sustained_005_frames_0532_0533.png) |
| 6 | 00:18.933 | 567 → 568 | 12:35:28 AM → 12:52:27 AM | abrupt | +00:16:59 | [view frames](supporting_frames/sustained_006_frames_0567_0568.png) |
| 7 | 00:19.800 | 593 → 594 | 12:52:27 AM → 01:21:20 PM | abrupt; AM→PM | +12:28:53 | [view frames](supporting_frames/sustained_007_frames_0593_0594.png) |
| 8 | 00:22.067 | 661 → 662 | 01:21:22 PM → 01:46:27 PM | abrupt | +00:25:05 | [view frames](supporting_frames/sustained_008_frames_0661_0662.png) |
| 9 | 00:35.800 | 1073 → 1074 | 01:46:40 PM → 02:01:32 PM | abrupt | +00:14:52 | [view frames](supporting_frames/sustained_009_frames_1073_1074.png) |
| 10 | 00:39.533 | 1185 → 1186 | 02:01:35 PM → 02:08:32 PM | abrupt | +00:06:57 | [view frames](supporting_frames/sustained_010_frames_1185_1186.png) |
| 11 | 00:40.133 | 1203 → 1204 | 02:08:32 PM → 02:08:49 PM | abrupt | +00:00:17 | [view frames](supporting_frames/sustained_011_frames_1203_1204.png) |
| 12 | 00:45.533 | 1365 → 1366 | 02:08:54 PM → 02:08:59 PM | abrupt | +00:00:05 | [view frames](supporting_frames/sustained_012_frames_1365_1366.png) |
| 13 | 00:47.533 | 1425 → 1426 | 02:09:00 PM → 02:11:30 PM | abrupt | +00:02:30 | [view frames](supporting_frames/sustained_013_frames_1425_1426.png) |
| 14 | 00:49.600 | 1487 → 1488 | 02:11:32 PM → 02:12:27 PM | abrupt | +00:00:55 | [view frames](supporting_frames/sustained_014_frames_1487_1488.png) |
| 15 | 00:52.167 | 1564 → 1565 | 02:12:29 PM → 02:12:55 PM | abrupt | +00:00:26 | [view frames](supporting_frames/sustained_015_frames_1564_1565.png) |
| 16 | 00:53.733 | 1611 → 1612 | 02:12:56 PM → 02:18:27 PM | abrupt | +00:05:31 | [view frames](supporting_frames/sustained_016_frames_1611_1612.png) |
| 17 | 00:55.133 | 1653 → 1654 | 02:18:28 PM → 02:24:49 PM | abrupt | +00:06:21 | [view frames](supporting_frames/sustained_017_frames_1653_1654.png) |
| 18 | 00:56.333 | 1689 → 1690 | 02:24:50 PM → 02:27:27 PM | abrupt | +00:02:37 | [view frames](supporting_frames/sustained_018_frames_1689_1690.png) |
| 19 | 00:59.933 | 1797 → 1798 | 02:27:30 PM → 02:28:38 PM | abrupt | +00:01:08 | [view frames](supporting_frames/sustained_019_frames_1797_1798.png) |
| 20 | 01:03.400 | 1901 → 1902 | 02:28:41 PM → 02:30:27 PM | abrupt | +00:01:46 | [view frames](supporting_frames/sustained_020_frames_1901_1902.png) |
| 21 | 01:06.900 | 2006 → 2007 | 02:30:30 PM → 02:33:27 PM | abrupt | +00:02:57 | [view frames](supporting_frames/sustained_021_frames_2006_2007.png) |
| 22 | 01:10.000 | 2099 → 2100 | 02:33:30 PM → 02:33:32 PM | abrupt | +00:00:02 | [view frames](supporting_frames/sustained_022_frames_2099_2100.png) |
| 23 | 01:11.033 | 2130 → 2131 | 02:33:32 PM → 02:37:01 PM | abrupt | +00:03:29 | [view frames](supporting_frames/sustained_023_frames_2130_2131.png) |
| 24 | 01:13.733 | 2211 → 2212 | 02:37:03 PM → 02:42:27 PM | abrupt | +00:05:24 | [view frames](supporting_frames/sustained_024_frames_2211_2212.png) |
| 25 | 01:14.700 | 2240 → 2241 | 02:42:27 PM → 02:42:32 PM | abrupt | +00:00:05 | [view frames](supporting_frames/sustained_025_frames_2240_2241.png) |
| 26 | 01:16.433 | 2292 → 2293 | 02:42:33 PM → 02:42:56 PM | abrupt | +00:00:23 | [view frames](supporting_frames/sustained_026_frames_2292_2293.png) |
| 27 | 01:20.100 | 2402 → 2403 | 02:42:59 PM → 02:45:27 PM | abrupt | +00:02:28 | [view frames](supporting_frames/sustained_027_frames_2402_2403.png) |
| 28 | 01:22.233 | 2466 → 2467 | 02:45:28 PM → 02:47:11 PM | abrupt | +00:01:43 | [view frames](supporting_frames/sustained_028_frames_2466_2467.png) |
| 29 | 01:24.800–01:25.200 | 2544 → 2556 | 02:47:42 PM → 03:17:53 PM | cross-fade | +00:30:11 | [view frames](supporting_frames/sustained_029_frames_2544_2550_2556.png) |
| 30 | 01:30.500 | 2714 → 2715 | 03:17:58 PM → 03:36:27 PM | abrupt | +00:18:29 | [view frames](supporting_frames/sustained_030_frames_2714_2715.png) |
| 31 | 01:33.033 | 2790 → 2791 | 03:36:29 PM → 03:37:52 PM | abrupt | +00:01:23 | [view frames](supporting_frames/sustained_031_frames_2789_2790_2791_2792.png) |
| 32 | 01:35.333 | 2859 → 2860 | 03:37:54 PM → 03:44:18 PM | abrupt | +00:06:24 | [view frames](supporting_frames/sustained_032_frames_2859_2860.png) |
| 33 | 01:36.167 | 2884 → 2885 | 03:44:18 PM → 03:52:39 PM | abrupt | +00:08:21 | [view frames](supporting_frames/sustained_033_frames_2884_2885.png) |
| 34 | 01:37.633 | 2928 → 2929 | 03:52:40 PM → 03:58:42 PM | abrupt | +00:06:02 | [view frames](supporting_frames/sustained_034_frames_2928_2929.png) |
| 35 | 01:38.733 | 2961 → 2962 | 03:58:42 PM → 03:58:49 PM | abrupt | +00:00:07 | [view frames](supporting_frames/sustained_035_frames_2961_2962.png) |
| 36 | 01:41.433 | 3042 → 3043 | 03:58:51 PM → 03:59:04 PM | abrupt | +00:00:13 | [view frames](supporting_frames/sustained_036_frames_3042_3043.png) |
| 37 | 01:43.733 | 3111 → 3112 | 03:59:06 PM → 04:04:23 PM | abrupt | +00:05:17 | [view frames](supporting_frames/sustained_037_frames_3111_3112.png) |
| 38 | 01:44.767 | 3142 → 3143 | 04:04:24 PM → 04:04:45 PM | abrupt | +00:00:21 | [view frames](supporting_frames/sustained_038_frames_3141_3142_3143_3144.png) |
| 39 | 01:45.800 | 3173 → 3174 | 04:04:46 PM → 04:04:59 PM | abrupt | +00:00:13 | [view frames](supporting_frames/sustained_039_frames_3173_3174.png) |
| 40 | 01:49.633 | 3288 → 3289 | 04:05:02 PM → 04:05:05 PM | abrupt | +00:00:03 | [view frames](supporting_frames/sustained_040_frames_3288_3289.png) |
| 41 | 01:50.333–01:50.433 | 3310 → 3313 | 04:05:05 PM → 04:05:08 PM | cross-fade | +00:00:03 | [view frames](supporting_frames/sustained_041_frames_3310_3311_3313.png) |
| 42 | 01:51.167–01:51.233 | 3335 → 3337 | 04:05:08 PM → 04:10:01 PM | cross-fade | +00:04:53 | [view frames](supporting_frames/sustained_042_frames_3334_3335_3336_3337_3338.png) |
| 43 | 01:52.633 | 3378 → 3379 | 04:10:02 PM → 04:24:44 PM | abrupt | +00:14:42 | [view frames](supporting_frames/sustained_043_frames_3378_3379.png) |
| 44 | 01:53.767 | 3412 → 3413 | 04:24:45 PM → 04:24:50 PM | abrupt | +00:00:05 | [view frames](supporting_frames/sustained_044_frames_3412_3413.png) |
| 45 | 01:54.600 | 3437 → 3438 | 04:24:50 PM → 04:24:52 PM | abrupt | +00:00:02 | [view frames](supporting_frames/sustained_045_frames_3437_3438.png) |
| 46 | 01:55.300 | 3458 → 3459 | 04:24:52 PM → 04:32:16 PM | abrupt | +00:07:24 | [view frames](supporting_frames/sustained_046_frames_3458_3459.png) |
| 47 | 01:56.833 | 3504 → 3505 | 04:32:17 PM → 04:36:50 PM | abrupt | +00:04:33 | [view frames](supporting_frames/sustained_047_frames_3504_3505.png) |
| 48 | 01:59.800 | 3593 → 3594 | 04:36:52 PM → **04:36:39 PM** | abrupt; backward | −00:00:13 (negative) | [view frames](supporting_frames/sustained_048_frames_3593_3594.png) |
| 49 | 02:01.533 | 3645 → 3646 | 04:36:40 PM → 04:42:40 PM | abrupt | +00:06:00 | [view frames](supporting_frames/sustained_049_frames_3645_3646.png) |
| 50 | 02:03.800 | 3713 → 3714 | 04:42:42 PM → 04:44:43 PM | abrupt | +00:02:01 | [view frames](supporting_frames/sustained_050_frames_3713_3714.png) |
| 51 | 02:07.333 | 3819 → 3820 | 04:44:46 PM → 04:44:48 PM | abrupt | +00:00:02 | [view frames](supporting_frames/sustained_051_frames_3819_3820.png) |
| 52 | 02:09.167 | 3874 → 3875 | 04:44:49 PM → 04:45:13 PM | abrupt | +00:00:24 | [view frames](supporting_frames/sustained_052_frames_3874_3875.png) |
| 53 | 02:10.100 | 3902 → 3903 | 04:45:13 PM → 04:46:20 PM | abrupt | +00:01:07 | [view frames](supporting_frames/sustained_053_frames_3902_3903.png) |
| 54 | 02:11.567 | 3946 → 3947 | 04:46:21 PM → 04:46:25 PM | abrupt | +00:00:04 | [view frames](supporting_frames/sustained_054_frames_3946_3947.png) |
| 55 | 02:11.967 | 3958 → 3959 | 04:46:25 PM → 04:49:43 PM | abrupt | +00:03:18 | [view frames](supporting_frames/sustained_055_frames_3958_3959.png) |
| 56 | 02:15.167 | 4054 → 4055 | 04:49:46 PM → 04:55:17 PM | abrupt | +00:05:31 | [view frames](supporting_frames/sustained_056_frames_4054_4055.png) |
| 57 | 02:18.167 | 4144 → 4145 | 04:55:19 PM → 04:56:17 PM | abrupt | +00:00:58 | [view frames](supporting_frames/sustained_057_frames_4144_4145.png) |
| 58 | 02:20.800 | 4223 → 4224 | 04:56:19 PM → 04:56:42 PM | abrupt | +00:00:23 | [view frames](supporting_frames/sustained_058_frames_4223_4224.png) |
| 59 | 02:26.333 | 4389 → 4390 | 04:56:47 PM → 05:00:35 PM | abrupt | +00:03:48 | [view frames](supporting_frames/sustained_059_frames_4389_4390.png) |
| 60 | 02:29.800 | 4493 → 4494 | 05:00:38 PM → 05:03:27 PM | abrupt | +00:02:49 | [view frames](supporting_frames/sustained_060_frames_4493_4494.png) |
| 61 | 02:31.167 | 4534 → 4535 | 05:03:28 PM → 05:07:27 PM | abrupt | +00:03:59 | [view frames](supporting_frames/sustained_061_frames_4534_4535.png) |
| 62 | 02:33.100 | 4592 → 4593 | 05:07:28 PM → 05:09:23 PM | abrupt | +00:01:55 | [view frames](supporting_frames/sustained_062_frames_4592_4593.png) |
| 63 | 02:34.600 | 4637 → 4638 | 05:09:24 PM → 05:09:33 PM | abrupt | +00:00:09 | [view frames](supporting_frames/sustained_063_frames_4637_4638.png) |
| 64 | 02:35.700 | 4670 → 4671 | 05:09:34 PM → 05:09:37 PM | abrupt | +00:00:03 | [view frames](supporting_frames/sustained_064_frames_4669_4670_4671_4672.png) |
| 65 | 02:36.900 | 4706 → 4707 | 05:09:37 PM → 05:18:50 PM | abrupt | +00:09:13 | [view frames](supporting_frames/sustained_065_frames_4706_4707.png) |
| 66 | 02:39.733 | 4791 → 4792 | 05:18:52 PM → 05:18:54 PM | abrupt | +00:00:02 | [view frames](supporting_frames/sustained_066_frames_4791_4792.png) |
| 67 | 02:39.933 | 4797 → 4798 | 05:18:54 PM → 05:21:43 PM | abrupt | +00:02:49 | [view frames](supporting_frames/sustained_067_frames_4797_4798.png) |
| 68 | 02:40.500 | 4814 → 4815 | 05:21:43 PM → 05:22:13 PM | abrupt | +00:00:30 | [view frames](supporting_frames/sustained_068_frames_4814_4815.png) |
| 69 | 02:41.767 | 4852 → 4853 | 05:22:14 PM → 05:22:27 PM | abrupt | +00:00:13 | [view frames](supporting_frames/sustained_069_frames_4852_4853.png) |
| 70 | 02:42.167 | 4864 → 4865 | 05:22:27 PM → 05:22:35 PM | abrupt | +00:00:08 | [view frames](supporting_frames/sustained_070_frames_4864_4865.png) |
| 71 | 02:42.733 | 4881 → 4882 | 05:22:35 PM → 05:35:45 PM | abrupt | +00:13:10 | [view frames](supporting_frames/sustained_071_frames_4881_4882.png) |
| 72 | 02:43.933 | 4917 → 4918 | 05:35:46 PM → 05:38:59 PM | abrupt | +00:03:13 | [view frames](supporting_frames/sustained_072_frames_4917_4918.png) |
| 73 | 02:46.200 | 4985 → 4986 | 05:39:01 PM → 05:44:49 PM | abrupt; low contrast | +00:05:48 | [view frames](supporting_frames/sustained_073_frames_4985_4986.png) |
| 74 | 02:48.200 | 5045 → 5046 | 05:44:50 PM → **05:41:56 PM** | abrupt; backward | −00:02:54 (negative) | [view frames](supporting_frames/sustained_074_frames_5045_5046.png) |
| 75 | 02:49.767 | 5092 → 5093 | 05:41:57 PM → 05:44:19 PM | abrupt | +00:02:22 | [view frames](supporting_frames/sustained_075_frames_5092_5093.png) |
| 76 | 02:52.100 | 5162 → 5163 | 05:44:36 PM → 05:45:01 PM | abrupt | +00:00:25 | [view frames](supporting_frames/sustained_076_frames_5162_5163.png) |
| 77 | 02:53.400 | 5201 → 5202 | 05:45:02 PM → 05:46:41 PM | abrupt | +00:01:39 | [view frames](supporting_frames/sustained_077_frames_5201_5202.png) |
| 78 | 02:55.900 | 5276 → 5277 | 05:46:43 PM → 05:47:01 PM | abrupt | +00:00:18 | [view frames](supporting_frames/sustained_078_frames_5276_5277.png) |
| 79 | 02:57.267 | 5317 → 5318 | 05:47:02 PM → 05:47:55 PM | abrupt | +00:00:53 | [view frames](supporting_frames/sustained_079_frames_5317_5318.png) |
| 80 | 02:58.833 | 5364 → 5365 | 05:47:56 PM → 05:48:01 PM | abrupt | +00:00:05 | [view frames](supporting_frames/sustained_080_frames_5364_5365.png) |
| 81 | 03:04.733 | 5541 → 5542 | 05:48:06 PM → 05:49:33 PM | abrupt | +00:01:27 | [view frames](supporting_frames/sustained_081_frames_5541_5542.png) |
| 82 | 03:08.067 | 5641 → 5642 | 05:49:36 PM → 05:55:40 PM | abrupt | +00:06:04 | [view frames](supporting_frames/sustained_082_frames_5640_5641_5642_5643.png) |
| 83 | 03:09.733 | 5691 → 5692 | 05:55:41 PM → 05:58:10 PM | abrupt | +00:02:29 | [view frames](supporting_frames/sustained_083_frames_5691_5692.png) |
| 84 | 03:13.167 | 5794 → 5795 | 05:58:11 PM → 06:02:34 PM | abrupt; low contrast | +00:04:23 | [view frames](supporting_frames/sustained_084_frames_5794_5795.png) |
| 85 | 03:16.933 | 5907 → 5908 | 06:02:37 PM → 06:05:27 PM | abrupt | +00:02:50 | [view frames](supporting_frames/sustained_085_frames_5907_5908.png) |
| 86 | 03:17.300–03:17.500 | 5919 → 5925 | 06:05:27 PM → 06:12:08 PM | cross-fade | +00:06:41 | [view frames](supporting_frames/sustained_086_frames_5919_5922_5925.png) |
| 87 | 03:21.767 | 6052 → 6053 | 06:12:11 PM → 06:12:14 PM | abrupt | +00:00:03 | [view frames](supporting_frames/sustained_087_frames_6052_6053.png) |
| 88 | 03:24.767 | 6142 → 6143 | 06:12:16 PM → 06:12:45 PM | abrupt | +00:00:29 | [view frames](supporting_frames/sustained_088_frames_6142_6143.png) |
| 89 | 03:26.300 | 6188 → 6189 | 06:12:46 PM → 06:13:01 PM | abrupt | +00:00:15 | [view frames](supporting_frames/sustained_089_frames_6188_6189.png) |
| 90 | 03:27.467 | 6223 → 6224 | 06:13:02 PM → 06:13:10 PM | abrupt | +00:00:08 | [view frames](supporting_frames/sustained_090_frames_6223_6224.png) |
| 91 | 03:28.067 | 6241 → 6242 | 06:13:10 PM → 06:13:15 PM | abrupt | +00:00:05 | [view frames](supporting_frames/sustained_091_frames_6241_6242.png) |
| 92 | 03:29.767 | 6292 → 6293 | 06:13:16 PM → 06:13:39 PM | abrupt | +00:00:23 | [view frames](supporting_frames/sustained_092_frames_6292_6293.png) |
| 93 | 03:31.133 | 6333 → 6334 | 06:13:40 PM → 06:13:54 PM | abrupt | +00:00:14 | [view frames](supporting_frames/sustained_093_frames_6333_6334.png) |
| 94 | 03:33.800 | 6413 → 6414 | 06:13:56 PM → 06:14:28 PM | abrupt | +00:00:32 | [view frames](supporting_frames/sustained_094_frames_6413_6414.png) |
| 95 | 03:35.133 | 6453 → 6454 | 06:14:28 PM → 06:16:01 PM | abrupt | +00:01:33 | [view frames](supporting_frames/sustained_095_frames_6453_6454.png) |
| 96 | 03:38.133 | 6543 → 6544 | 06:16:03 PM → 06:16:27 PM | abrupt | +00:00:24 | [view frames](supporting_frames/sustained_096_frames_6543_6544.png) |
| 97 | 03:42.600–03:42.867 | 6678 → 6686 | 06:16:31 PM → 06:16:37 PM | cross-fade | +00:00:06 | [view frames](supporting_frames/sustained_097_frames_6678_6682_6686.png) |
| 98 | 03:48.867 | 6865 → 6866 | 06:16:42 PM → **06:14:37 PM** | abrupt; backward | −00:02:05 (negative) | [view frames](supporting_frames/sustained_098_frames_6865_6866.png) |
| 99 | 03:49.467 | 6883 → 6884 | 06:14:37 PM → 07:07:51 PM | abrupt | +00:53:14 | [view frames](supporting_frames/sustained_099_frames_6883_6884.png) |
| 100 | 03:49.900 | 6896 → 6897 | 07:07:51 PM → **06:03:45 AM** | abrupt; date rollover; PM→AM | +10:55:54 | [view frames](supporting_frames/sustained_100_frames_6896_6897.png) |

## Transient out-of-sequence glitches

The bold middle value or sequence is the anomalous display. These events return to the prior value, except where the compound sequence itself is described.

| # | Video time | Source frame(s) | Duration | Timestamp sequence | Signed display changes | Evidence |
|---:|:---|:---|:---|:---|:---:|:---:|
| 1 | 00:22.867 | 686 | 1 frame | 01:46:27 PM → **01:46:23 PM** → 01:46:27 PM | −00:00:04; +00:00:04 | [view frames](supporting_frames/transient_001_frames_0685_0686_0687.png) |
| 2 | 00:24.933 | 748 | 1 frame | 01:46:29 PM → **01:46:27 PM** → 01:46:29 PM | −00:00:02; +00:00:02 | [view frames](supporting_frames/transient_002_frames_0747_0748_0749.png) |
| 3 | 00:29.467 | 884 | 1 frame | 01:46:34 PM → **01:46:27 PM** → 01:46:34 PM | −00:00:07; +00:00:07 | [view frames](supporting_frames/transient_003_frames_0883_0884_0885.png) |
| 4 | 00:49.200 | 1476 | 1 frame | 02:11:31 PM → **02:11:30 PM** → 02:11:31 PM | −00:00:01; +00:00:01 | [view frames](supporting_frames/transient_004_frames_1475_1476_1477.png) |
| 5 | 00:51.367 | 1541 | 1 frame | 02:12:28 PM → **02:12:27 PM** → 02:12:28 PM | −00:00:01; +00:00:01 | [view frames](supporting_frames/transient_005_frames_1540_1541_1542.png) |
| 6 | 00:51.767 | 1553 | 1 frame | 02:12:29 PM → **02:12:27 PM** → 02:12:29 PM | −00:00:02; +00:00:02 | [view frames](supporting_frames/transient_006_frames_1552_1553_1554.png) |
| 7 | 00:58.267 | 1748 | 1 frame | 02:27:28 PM → **02:27:27 PM** → 02:27:28 PM | −00:00:01; +00:00:01 | [view frames](supporting_frames/transient_007_frames_1747_1748_1749.png) |
| 8 | 00:59.167 | 1775 | 1 frame | 02:27:29 PM → **02:27:27 PM** → 02:27:29 PM | −00:00:02; +00:00:02 | [view frames](supporting_frames/transient_008_frames_1774_1775_1776.png) |
| 9 | 01:02.000 | 1860 | 1 frame | 02:28:40 PM → **02:28:39 PM** → 02:28:40 PM | −00:00:01; +00:00:01 | [view frames](supporting_frames/transient_009_frames_1859_1860_1861.png) |
| 10 | 01:02.233–01:02.267 | 1867–1868 | 2 frames | 02:28:40 PM → **02:28:39 PM** → 02:28:40 PM | −00:00:01; +00:00:01 | [view frames](supporting_frames/transient_010_frames_1866_1867_1868_1869.png) |
| 11 | 01:08.567 | 2057 | 1 frame | 02:33:28 PM → **02:33:27 PM** → 02:33:28 PM | −00:00:01; +00:00:01 | [view frames](supporting_frames/transient_011_frames_2056_2057_2058.png) |
| 12 | 01:09.367 | 2081 | 1 frame | 02:33:29 PM → **02:33:27 PM** → 02:33:29 PM | −00:00:02; +00:00:02 | [view frames](supporting_frames/transient_012_frames_2080_2081_2082.png) |
| 13 | 01:09.767 | 2093 | 1 frame | 02:33:29 PM → **02:33:27 PM** → 02:33:29 PM | −00:00:02; +00:00:02 | [view frames](supporting_frames/transient_013_frames_2092_2093_2094.png) |
| 14 | 01:17.233–01:17.267 | 2317–2318 | 2 frames | 02:42:56 PM → **02:42:55 PM** → 02:42:56 PM | −00:00:01; +00:00:01 | [view frames](supporting_frames/transient_014_frames_2316_2317_2318_2319.png) |
| 15 | 01:26.833–01:26.867 | 2605–2606 | 2 frames | 03:17:54 PM → **03:17:53 PM** → 03:17:54 PM | −00:00:01; +00:00:01 | [view frames](supporting_frames/transient_015_frames_2604_2605_2606_2607.png) |
| 16 | 01:27.100 | 2613 | 1 frame | 03:17:54 PM → **03:17:53 PM** → 03:17:54 PM | −00:00:01; +00:00:01 | [view frames](supporting_frames/transient_016_frames_2612_2613_2614.png) |
| 17 | 01:27.833–01:27.867 | 2635–2636 | 2 frames | 03:17:55 PM → **03:17:54 PM** → 03:17:55 PM | −00:00:01; +00:00:01 | [view frames](supporting_frames/transient_017_frames_2634_2635_2636_2637.png) |
| 18 | 01:29.300 | 2679 | 1 frame | 03:17:57 PM → **03:17:53 PM** → 03:17:57 PM | −00:00:04; +00:00:04 | [view frames](supporting_frames/transient_018_frames_2678_2679_2680.png) |
| 19 | 01:43.200 | 3096 | 1 frame | 03:59:05 PM → **03:59:04 PM** → 03:59:05 PM | −00:00:01; +00:00:01 | [view frames](supporting_frames/transient_019_frames_3095_3096_3097.png) |
| 20 | 01:46.900 | 3207 | 1 frame | 04:05:00 PM → **04:04:57 PM** → 04:05:00 PM | −00:00:03; +00:00:03 | [view frames](supporting_frames/transient_020_frames_3206_3207_3208.png) |
| 21 | 01:47.000 | 3210 | 1 frame | 04:05:00 PM → **04:04:57 PM** → 04:05:00 PM | −00:00:03; +00:00:03 | [view frames](supporting_frames/transient_021_frames_3209_3210_3211.png) |
| 22 | 01:49.300 | 3279 | 1 frame | 04:05:02 PM → **04:04:59 PM** → 04:05:02 PM | −00:00:03; +00:00:03 | [view frames](supporting_frames/transient_022_frames_3278_3279_3280.png) |
| 23 | 01:58.033–01:58.067 | 3541–3542 | 2 frames | 04:36:51 PM → **04:36:50 PM** → 04:36:51 PM | −00:00:01; +00:00:01 | [view frames](supporting_frames/transient_023_frames_3540_3541_3542_3543.png) |
| 24 | 02:05.200 | 3756 | 1 frame | 04:44:44 PM → **04:44:43 PM** → 04:44:44 PM | −00:00:01; +00:00:01 | [view frames](supporting_frames/transient_024_frames_3755_3756_3757.png) |
| 25 | 02:05.900 | 3777 | 1 frame | 04:44:45 PM → **04:44:43 PM** → 04:44:45 PM | −00:00:02; +00:00:02 | [view frames](supporting_frames/transient_025_frames_3776_3777_3778.png) |
| 26 | 02:07.033–02:07.067 | 3811–3812 | 2 frames | 04:44:46 PM → **04:44:43 PM** → 04:44:46 PM | −00:00:03; +00:00:03 | [view frames](supporting_frames/transient_026_frames_3810_3811_3812_3813.png) |
| 27 | 02:13.833–02:13.867 | 4015–4016 | 2 frames | 04:49:44 PM → **04:49:43 PM** → 04:49:44 PM | −00:00:01; +00:00:01 | [view frames](supporting_frames/transient_027_frames_4014_4015_4016_4017.png) |
| 28 | 02:16.733 | 4102 | 1 frame | 04:55:18 PM → **04:55:17 PM** → 04:55:18 PM | −00:00:01; +00:00:01 | [view frames](supporting_frames/transient_028_frames_4101_4102_4103.png) |
| 29 | 02:17.500 | 4125 | 1 frame | 04:55:19 PM → **04:55:17 PM** → 04:55:19 PM | −00:00:02; +00:00:02 | [view frames](supporting_frames/transient_029_frames_4124_4125_4126.png) |
| 30 | 02:19.933 | 4198 | 1 frame | 04:56:18 PM → **04:56:17 PM** → 04:56:18 PM | −00:00:01; +00:00:01 | [view frames](supporting_frames/transient_030_frames_4197_4198_4199.png) |
| 31 | 02:39.567 | 4787 | 1 frame | 05:18:52 PM → **05:18:53 PM** → 05:18:52 PM | +00:00:01; −00:00:01 | [view frames](supporting_frames/transient_031_frames_4786_4787_4788.png) |
| 32 | 02:53.100–02:53.167 | 5193–5195 | compound | 05:45:01 PM → **05:45:02 PM → 05:45:01 PM → 05:45:02 PM** | +00:00:01; −00:00:01; +00:00:01 | [view frames](supporting_frames/transient_032_frames_5192_5193_5194_5195_5196.png) |
| 33 | 02:55.567 | 5267 | 1 frame | 05:46:43 PM → **05:46:41 PM** → 05:46:43 PM | −00:00:02; +00:00:02 | [view frames](supporting_frames/transient_033_frames_5266_5267_5268.png) |
| 34 | 03:00.700 | 5421 | 1 frame | 05:48:02 PM → **05:48:01 PM** → 05:48:02 PM | −00:00:01; +00:00:01 | [view frames](supporting_frames/transient_034_frames_5420_5421_5422.png) |
| 35 | 03:01.433 | 5443 | 1 frame | 05:48:03 PM → **05:47:59 PM** → 05:48:03 PM | −00:00:04; +00:00:04 | [view frames](supporting_frames/transient_035_frames_5442_5443_5444.png) |
| 36 | 03:05.900–03:05.933 | 5577–5578 | 2 frames | 05:49:34 PM → **05:49:33 PM** → 05:49:34 PM | −00:00:01; +00:00:01 | [view frames](supporting_frames/transient_036_frames_5576_5577_5578_5579.png) |
| 37 | 03:06.967–03:07.033 | 5609–5611 | compound | 05:49:34 PM → **05:49:32 PM (2 frames) → 05:49:35 PM** | −00:00:02; +00:00:03 | [view frames](supporting_frames/transient_037_frames_5608_5609_5610_5611_5612.png) |
| 38 | 03:09.600–03:09.633 | 5688–5689 | 2 frames | 05:55:41 PM → **05:55:40 PM** → 05:55:41 PM | −00:00:01; +00:00:01 | [view frames](supporting_frames/transient_038_frames_5687_5688_5689_5690.png) |
| 39 | 03:10.900 | 5727 | 1 frame | 05:58:11 PM → **05:58:10 PM** → 05:58:11 PM | −00:00:01; +00:00:01 | [view frames](supporting_frames/transient_039_frames_5726_5727_5728.png) |
| 40 | 03:11.100 | 5733 | 1 frame | 05:58:11 PM → **05:58:10 PM** → 05:58:11 PM | −00:00:01; +00:00:01 | [view frames](supporting_frames/transient_040_frames_5732_5733_5734.png) |
| 41 | 03:16.067 | 5882 | 1 frame | 06:02:36 PM → **06:02:34 PM** → 06:02:36 PM | −00:00:02; +00:00:02 | [view frames](supporting_frames/transient_041_frames_5881_5882_5883.png) |
| 42 | 03:20.567 | 6017 | 1 frame | 06:12:10 PM → **06:12:03 PM** → 06:12:10 PM | −00:00:07; +00:00:07 | [view frames](supporting_frames/transient_042_frames_6016_6017_6018.png) |
| 43 | 03:23.933 | 6118 | 1 frame | 06:12:16 PM → **06:12:14 PM** → 06:12:16 PM | −00:00:02; +00:00:02 | [view frames](supporting_frames/transient_043_frames_6117_6118_6119.png) |
| 44 | 03:24.500 | 6135 | 1 frame | 06:12:16 PM → **06:12:14 PM** → 06:12:16 PM | −00:00:02; +00:00:02 | [view frames](supporting_frames/transient_044_frames_6134_6135_6136.png) |
| 45 | 03:40.500 | 6615 | 1 frame | 06:16:29 PM → **06:16:27 PM** → 06:16:29 PM | −00:00:02; +00:00:02 | [view frames](supporting_frames/transient_045_frames_6614_6615_6616.png) |

## Final multi-jump sequence

The final section contains three consecutive discontinuities in 1.033 seconds of video:

`06:16:42 PM` (frame 6865) → **−00:02:05 (negative)** → `06:14:37 PM` (frame 6866) → **+00:53:14** → `07:07:51 PM` (frame 6884) → **+10:55:54** → `06:03:45 AM` (frame 6897, now `SEP 11 2001`).

This is distinct from the short transient glitches: each new value persists until the next edit.
