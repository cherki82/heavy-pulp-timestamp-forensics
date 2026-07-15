#!/usr/bin/env python3
from pathlib import Path
import html
import re


ROOT = Path(__file__).resolve().parent
ORIGINAL = (ROOT / "reports/timestamp_forensic_report.md").read_text()
PROVO = (ROOT / "reports/timestamp_forensic_report_provo_ut.md").read_text()


def table_rows(document: str, start: str, end: str | None = None) -> list[list[str]]:
    section = document.split(start, 1)[1]
    if end:
        section = section.split(end, 1)[0]
    rows = []
    for line in section.splitlines():
        if re.match(r"^\| \d+ \|", line):
            rows.append([cell.strip() for cell in line.strip().strip("|").split("|")])
    return rows


def clean(value: str) -> str:
    return html.escape(value.replace("**", "").replace("`", ""))


def evidence_path(value: str) -> str:
    match = re.search(r"supporting_frames/([^)]+)", value)
    if not match:
        raise ValueError(f"No evidence path in {value}")
    return f"evidence/{match.group(1)}"


def event_cards(kind: str, original_rows: list[list[str]], provo_rows: list[list[str]]) -> str:
    cards = []
    for source, converted in zip(original_rows, provo_rows, strict=True):
        number = int(source[0])
        negative = "negative" in source[5]
        image = evidence_path(source[-1])
        if kind == "sustained":
            details = f"""
              <dl class="facts">
                <div><dt>Video boundary</dt><dd>{clean(source[1])}</dd></div>
                <div><dt>Source frames</dt><dd>{clean(source[2])}</dd></div>
                <div><dt>Type</dt><dd>{clean(source[4])}</dd></div>
                <div><dt>Signed gap</dt><dd class="{'negative' if negative else 'positive'}">{clean(source[5])}</dd></div>
              </dl>
              <p class="clock"><span>Sedona source</span>{clean(source[3])}</p>
              <p class="clock clock--provo"><span>Provo equivalent</span>{clean(converted[3])}</p>
            """
        else:
            details = f"""
              <dl class="facts">
                <div><dt>Video time</dt><dd>{clean(source[1])}</dd></div>
                <div><dt>Source frame(s)</dt><dd>{clean(source[2])}</dd></div>
                <div><dt>Duration</dt><dd>{clean(source[3])}</dd></div>
                <div><dt>Signed changes</dt><dd>{clean(source[5])}</dd></div>
              </dl>
              <p class="clock"><span>Sedona source</span>{clean(source[4])}</p>
              <p class="clock clock--provo"><span>Provo equivalent</span>{clean(converted[4])}</p>
            """
        cards.append(f"""
          <article class="event{' event--negative' if negative else ''}" id="{kind}-{number:03d}">
            <div class="event__copy">
              <p class="event__eyebrow">{kind} event</p>
              <h3><a href="#{kind}-{number:03d}">#{number:03d}</a></h3>
              {details}
            </div>
            <figure class="strip">
              <a href="{image}"><img loading="lazy" src="{image}" alt="Source-frame evidence strip for {kind} event {number}"></a>
              <figcaption>Original Sedona-time source pixels. Open for full resolution.</figcaption>
            </figure>
          </article>
        """)
    return "\n".join(cards)


sustained_original = table_rows(ORIGINAL, "## Sustained discontinuities", "## Transient")
sustained_provo = table_rows(PROVO, "## Sustained discontinuities", "## Transient")
transient_original = table_rows(ORIGINAL, "## Transient out-of-sequence glitches", "## Final")
transient_provo = table_rows(PROVO, "## Transient out-of-sequence glitches", "## Final")
assert len(sustained_original) == len(sustained_provo) == 100
assert len(transient_original) == len(transient_provo) == 45

gallery_files = [
    ("Both meridiem transitions", "ampm_transition_evidence.png"),
    ("Timestamp visibility boundaries", "ampm_visibility_boundaries.png"),
    ("Low-confidence AM/PM review, page 1", "ampm_low_confidence_review_1.png"),
    ("Low-confidence AM/PM review, page 2", "ampm_low_confidence_review_2.png"),
    ("Low-confidence AM/PM review, page 3", "ampm_low_confidence_review_3.png"),
    ("Low-confidence AM/PM review, page 4", "ampm_low_confidence_review_4.png"),
]
gallery = "\n".join(
    f'<figure><a href="evidence/{file}"><img loading="lazy" src="evidence/{file}" alt="{label}"></a><figcaption>{label}</figcaption></figure>'
    for label, file in gallery_files
)

page = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#07100e">
  <meta name="description" content="Frame-by-frame forensic analysis of 100 sustained timestamp discontinuities and 45 transient glitches in Heavy Pulp — Somewhere in Sedona.">
  <meta property="og:title" content="Timestamp Discontinuity Analysis — Heavy Pulp">
  <meta property="og:description" content="Frame-by-frame analysis of 6,998 frames, documenting 100 sustained timestamp discontinuities and 45 transient out-of-sequence readings.">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://cherki82.github.io/heavy-pulp-timestamp-forensics/">
  <meta property="og:image" content="https://cherki82.github.io/heavy-pulp-timestamp-forensics/evidence/ampm_transition_evidence.png">
  <title>Timestamp Discontinuity Analysis — Heavy Pulp</title>
  <style>
    :root {{
      --ink: #e6ece4;
      --muted: #9aaba2;
      --paper: #07100e;
      --panel: #0d1915;
      --panel-2: #12231d;
      --line: #294036;
      --green: #8dffb3;
      --amber: #ffc857;
      --red: #ff6b5f;
      --serif: "Iowan Old Style", "Palatino Linotype", Palatino, Georgia, serif;
      --mono: "IBM Plex Mono", "SFMono-Regular", Consolas, "Liberation Mono", monospace;
    }}
    * {{ box-sizing: border-box; }}
    html {{ scroll-behavior: smooth; background: var(--paper); }}
    body {{ margin: 0; color: var(--ink); background:
      linear-gradient(rgba(141,255,179,.035) 1px, transparent 1px),
      linear-gradient(90deg, rgba(141,255,179,.025) 1px, transparent 1px), var(--paper);
      background-size: 100% 32px, 32px 100%; font-family: var(--serif); line-height: 1.55; }}
    a {{ color: var(--green); text-underline-offset: .2em; }}
    img {{ display: block; }}
    .skip {{ position: absolute; left: -9999px; }}
    .skip:focus {{ left: 1rem; top: 1rem; z-index: 10; padding: .75rem 1rem; background: var(--amber); color: #111; }}
    .wrap {{ width: min(1180px, calc(100% - 2rem)); margin-inline: auto; }}
    header {{ padding: 5rem 0 3rem; border-bottom: 1px solid var(--line); }}
    .kicker, .event__eyebrow {{ margin: 0; color: var(--amber); font: 700 .72rem/1.2 var(--mono); letter-spacing: .18em; text-transform: uppercase; }}
    h1 {{ max-width: 16ch; margin: .6rem 0 1.4rem; font-size: clamp(2.8rem, 7vw, 6.5rem); font-weight: 500; letter-spacing: -.055em; line-height: .9; }}
    .lede {{ max-width: 720px; font-size: clamp(1.2rem, 2.1vw, 1.65rem); color: #c7d1cb; }}
    .hero-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 1px; margin-top: 3rem; background: var(--line); border: 1px solid var(--line); }}
    .metric {{ min-height: 130px; padding: 1.2rem; background: rgba(7,16,14,.95); }}
    .metric strong {{ display: block; color: var(--green); font: 500 clamp(2rem, 5vw, 4rem)/1 var(--mono); letter-spacing: -.06em; }}
    .metric span {{ display: block; margin-top: .65rem; color: var(--muted); font: .74rem/1.3 var(--mono); text-transform: uppercase; }}
    nav {{ position: sticky; top: 0; z-index: 5; overflow-x: auto; background: rgba(7,16,14,.92); border-bottom: 1px solid var(--line); backdrop-filter: blur(14px); }}
    nav .wrap {{ display: flex; gap: 1.4rem; padding-block: .9rem; white-space: nowrap; }}
    nav a {{ color: var(--muted); font: 700 .7rem/1 var(--mono); letter-spacing: .08em; text-decoration: none; text-transform: uppercase; }}
    nav a:hover {{ color: var(--amber); }}
    main > section {{ padding: 5.5rem 0; border-bottom: 1px solid var(--line); }}
    h2 {{ margin: 0 0 1.2rem; font-size: clamp(2.2rem, 5vw, 4.8rem); font-weight: 500; letter-spacing: -.045em; line-height: .95; }}
    h3 {{ margin: .35rem 0 1.2rem; font: 500 clamp(2rem, 4vw, 3.6rem)/1 var(--mono); letter-spacing: -.08em; }}
    h3 a {{ color: var(--ink); text-decoration: none; }}
    .section-intro {{ max-width: 760px; margin-bottom: 3rem; font-size: 1.15rem; color: #bdc9c2; }}
    .callout {{ display: grid; grid-template-columns: 1fr 2fr; gap: 2rem; padding: 2rem; background: var(--panel); border: 1px solid var(--line); border-left: 4px solid var(--amber); }}
    .callout strong {{ color: var(--amber); font: 500 clamp(2.5rem, 6vw, 5rem)/1 var(--mono); letter-spacing: -.08em; }}
    .columns {{ columns: 2 320px; column-gap: 3rem; }}
    .columns p:first-child {{ margin-top: 0; }}
    .downloads {{ display: flex; flex-wrap: wrap; gap: .7rem; margin-top: 2rem; }}
    .button {{ padding: .75rem 1rem; border: 1px solid var(--line); background: var(--panel); color: var(--ink); font: 700 .74rem/1 var(--mono); text-decoration: none; text-transform: uppercase; }}
    .button:hover {{ border-color: var(--green); color: var(--green); }}
    .event-list {{ display: grid; gap: 1rem; }}
    .event {{ display: grid; grid-template-columns: minmax(250px, 330px) minmax(0, 1fr); background: rgba(13,25,21,.9); border: 1px solid var(--line); border-left: 4px solid var(--green); scroll-margin-top: 4rem; }}
    .event--negative {{ border-left-color: var(--red); }}
    .event__copy {{ padding: 1.25rem; }}
    .facts {{ display: grid; grid-template-columns: 1fr 1fr; gap: .85rem; margin: 0 0 1.2rem; }}
    .facts div {{ min-width: 0; }}
    dt, .clock span {{ display: block; margin-bottom: .2rem; color: var(--muted); font: 700 .62rem/1.2 var(--mono); letter-spacing: .08em; text-transform: uppercase; }}
    dd {{ margin: 0; font: .8rem/1.35 var(--mono); overflow-wrap: anywhere; }}
    .positive {{ color: var(--green); }} .negative {{ color: var(--red); }}
    .clock {{ margin: .65rem 0 0; font: .8rem/1.45 var(--mono); }}
    .clock--provo {{ color: var(--amber); }}
    .strip {{ min-width: 0; margin: 0; padding: 1rem; overflow-x: auto; background: #050806; border-left: 1px solid var(--line); }}
    .strip a {{ display: block; width: max-content; }}
    .strip img {{ width: auto; max-width: none; height: clamp(205px, 26vw, 327px); border: 1px solid #26352e; }}
    figcaption {{ margin-top: .55rem; color: var(--muted); font: .65rem/1.3 var(--mono); }}
    .audit-grid {{ display: grid; grid-template-columns: repeat(2, minmax(0,1fr)); gap: 1rem; }}
    .audit-grid figure {{ margin: 0; padding: 1rem; background: var(--panel); border: 1px solid var(--line); overflow: auto; }}
    .audit-grid img {{ width: 100%; min-width: 520px; height: auto; }}
    .method-list {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 1px; padding: 0; list-style: none; background: var(--line); border: 1px solid var(--line); }}
    .method-list li {{ padding: 1.4rem; background: var(--panel); }}
    .method-list b {{ display: block; margin-bottom: .5rem; color: var(--amber); font: .7rem/1.2 var(--mono); text-transform: uppercase; }}
    footer {{ padding: 4rem 0; color: var(--muted); font: .75rem/1.6 var(--mono); }}
    code {{ color: var(--amber); font-family: var(--mono); overflow-wrap: anywhere; }}
    @media (max-width: 820px) {{
      header {{ min-height: auto; padding-top: 5rem; }}
      .hero-grid {{ grid-template-columns: 1fr 1fr; }}
      .event {{ grid-template-columns: 1fr; }}
      .strip {{ border-left: 0; border-top: 1px solid var(--line); }}
      .strip img {{ height: 240px; }}
      .callout, .method-list {{ grid-template-columns: 1fr; }}
      .audit-grid {{ grid-template-columns: 1fr; }}
    }}
    @media (prefers-reduced-motion: reduce) {{ html {{ scroll-behavior: auto; }} }}
  </style>
</head>
<body>
  <a class="skip" href="#content">Skip to report</a>
  <header>
    <div class="wrap">
      <p class="kicker">Forensic timestamp report · <cite>Heavy Pulp — Somewhere in Sedona</cite></p>
      <h1>Timestamp discontinuity analysis</h1>
      <p class="lede">Frame-by-frame examination of 6,998 decoded frames identified 100 sustained clock discontinuities and 45 transient out-of-sequence readings. Each event is linked to source-frame evidence; Provo equivalents apply a one-hour historical time-zone conversion.</p>
      <div class="hero-grid" aria-label="Report summary">
        <div class="metric"><strong>6,998</strong><span>frames examined</span></div>
        <div class="metric"><strong>100</strong><span>sustained discontinuities</span></div>
        <div class="metric"><strong>45</strong><span>transient readings</span></div>
        <div class="metric"><strong>+68,896</strong><span>net signed seconds</span></div>
      </div>
    </div>
  </header>
  <nav aria-label="Report sections"><div class="wrap">
    <a href="#finding">Finding</a><a href="#method">Method</a><a href="#timezone">Time zones</a><a href="#pattern">Pattern analysis</a><a href="#sustained">100 sustained</a><a href="#transient">45 transient</a><a href="#ampm">AM/PM audit</a>
  </div></nav>
  <main id="content">
    <section id="finding"><div class="wrap">
      <p class="kicker">Calculated result</p><h2>Net signed discontinuity: 68,896 seconds.</h2>
      <div class="callout"><strong>+68,896s</strong><div><p>Positive sustained gaps total <code>+108,400 seconds</code>. Four backward jumps total <code>−39,504 seconds</code>. Applying the requested signed convention yields <code>+68,896 seconds</code>, or <code>19:08:16</code>.</p><p>This is a discontinuity total derived from displayed timestamps. It is not, by itself, proof that exactly the same duration of original recording was physically removed.</p></div></div>
      <div class="downloads"><a class="button" href="reports/timestamp_forensic_report.md">Original Sedona-time report</a><a class="button" href="reports/timestamp_forensic_report_provo_ut.md">Provo-time duplicate</a><a class="button" href="evidence/ampm_frame_audit.txt">6,998-frame AM/PM ledger</a></div>
    </div></section>
    <section id="method"><div class="wrap">
      <p class="kicker">Method and controls</p><h2>Frame-level review and verification.</h2>
      <p class="section-intro">The 720×528 H.264 source contains 6,998 frames at a constant 30 fps. Candidate changes were located through temporal differencing in the lower-right timestamp region; the displayed values were then read by direct visual inspection.</p>
      <ul class="method-list">
        <li><b>Frame convention</b>Zero-based frame numbers. Video time equals frame ÷ 30.</li>
        <li><b>Evidence crop</b>Source coordinates x=480–719 and y=445–527, saved as lossless PNG.</li>
        <li><b>Scaling</b>3× nearest-neighbor enlargement. Labels sit outside source pixels.</li>
        <li><b>Provenance</b>All 145 linked strips and 363 panels were matched to their labeled source frames.</li>
        <li><b>Visibility</b>No timestamp appears in frames 0–50, 187–223, or 6992–6997.</li>
        <li><b>Hash</b><code>9fbcd936366c423ae0c25b500f90ecf0b7534bfa8da1e394549edd1c0d4ffdf6</code></li>
      </ul>
    </div></section>
    <section id="timezone"><div class="wrap">
      <p class="kicker">Historical local time</p><h2>Provo conversion: add one hour.</h2>
      <div class="columns"><p>For September 10–11, 2001, Sedona used Mountain Standard Time (<code>UTC−07:00</code>) while Provo observed Mountain Daylight Time (<code>UTC−06:00</code>). Every camera-clock value therefore moves forward exactly one hour.</p><p>Frame numbers, elapsed video positions, event order, classifications, and signed gaps do not change. The evidence images remain immutable source extractions and display the original Sedona time; each card supplies the Provo equivalent in amber.</p><p>The source date reads <code>SEP 10 2001</code> through frame 6896 and <code>SEP 11 2001</code> from frame 6897 through 6991.</p></div>
    </div></section>
    <section id="pattern"><div class="wrap">
      <p class="kicker">Exploratory cryptographic review</p><h2>No recoverable code identified.</h2>
      <div class="columns"><p>No defensible plaintext emerged from A1Z26/modulo-26, ASCII, modulo-128/256, digit-sum, time-component, parity-bit, Caesar, or single-byte XOR interpretations. Of 100 signed durations, 81 are unique; only the pair <code>5, 23</code> repeats, and no three-number sequence repeats.</p><p>The clear non-random feature is the destination second: 18 sustained jumps land at <code>:27</code>, including 13 of the first 30 events; another eight land at <code>:01</code>. Full-frame review shows those <code>:27</code> entries lead into different scenes, consistent with a recurring source-clip or edit anchor rather than a repeated visual symbol.</p><p>The absolute-gap modulo-26 index of coincidence is <code>0.0394</code>, close to the random-alphabet baseline <code>0.0385</code>. The four negative events occur at irregular indices 4, 48, 74, and 98. A strong cipher cannot be excluded without a key or known plaintext, but the durations provide no positive evidence of one.</p></div>
    </div></section>
    <section id="sustained"><div class="wrap">
      <p class="kicker">Complete event ledger</p><h2>100 sustained discontinuities.</h2>
      <p class="section-intro">For abrupt transitions, the boundary identifies the last old frame and first new frame. Cross-fades identify the last unblended old state, transition imagery, and first unblended new state. Red rules mark backward time.</p>
      <div class="event-list">{event_cards('sustained', sustained_original, sustained_provo)}</div>
    </div></section>
    <section id="transient"><div class="wrap">
      <p class="kicker">Momentary anomalies</p><h2>45 transient glitches.</h2>
      <p class="section-intro">These clock values briefly move out of sequence and return. The evidence strips include the preceding frame, every anomalous frame, and the following frame. The set comprises 34 one-frame, nine two-frame, and two compound glitches.</p>
      <div class="event-list">{event_cards('transient', transient_original, transient_provo)}</div>
    </div></section>
    <section id="ampm"><div class="wrap">
      <p class="kicker">Independent meridiem audit</p><h2>Every frame classified.</h2>
      <p class="section-intro">All 6,998 decoded frames were separately evaluated for the AM/PM marker. The only meridiem changes occur at frames 593→594 and 6896→6897; the latter coincides with the SEP 10→SEP 11 date change. No transient AM/PM glitches were found.</p>
      <div class="audit-grid">{gallery}</div>
    </div></section>
  </main>
  <footer><div class="wrap"><p>Published July 15, 2026 · Source video: <code>Heavy_Pulp_-_Somewhere_in_Sedona_v38gk3.mp4</code></p><p>This page preserves the source-evidence distinction: PNG pixels show the embedded Sedona clock; Provo equivalents are calculated text.</p></div></footer>
</body>
</html>
"""

(ROOT / "index.html").write_text(page)
print(f"wrote index.html with {len(sustained_original)} sustained and {len(transient_original)} transient events")
