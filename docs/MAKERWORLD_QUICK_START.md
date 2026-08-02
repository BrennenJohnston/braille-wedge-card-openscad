# MakerWorld Quick Start — Braille Wedge Card

This guide takes you from "I want a braille card someone can read with their
fingers" to a downloadable, print-ready STL, using
[`Braille_Wedge_Card_STL_Generator.scad`](../Braille_Wedge_Card_STL_Generator.scad)
on [MakerWorld](https://makerworld.com/)'s Parametric Model Maker. That one
file is the whole upload — there is nothing else to download.

The card prints **leaning back at 75° from the print bed**, standing on its own
break-away support fins, and comes off the printer ready to read. No embosser,
no paper, no post-processing beyond snapping the fins off.

If the MakerWorld customizer is difficult with your screen reader, skip to
section 8 — the same generator runs in an accessibility-first browser tool that
also translates your text for you.

---

## 1. What to include

Braille takes roughly three times the space of print, so deciding what to leave
out is the real design work. The Braille Authority of North America's test for a
contact card is a good one for any small braille surface: **can someone identify
me and contact me with just this information?** If yes, you have enough.

- The card **auto-sizes to fit whatever you paste**, so there is no fixed
  capacity to plan around. What limits you is your print bed: the generator
  warns in the console when the effective face passes **250 mm** in either
  direction.
- At the default spacing — `cell_spacing` 7.0 mm across, `line_spacing` 10.0 mm
  down — a 20-line card is about **209 mm tall**. Most consumer printers can
  take that; check yours.
- BANA's four-line contact-card layout is **name**, **organization**, **phone
  number**, **e-mail address**. Job titles, mailing addresses, fax numbers, and
  websites are usually the first things to cut.
- Braille a phone number as `#123.456.7890` — periods, not hyphens or
  parentheses. In Unified English Braille a period keeps *numeric mode* active
  so the whole number needs only one number sign (`⠼`), but a **hyphen ends
  numeric mode** and every group after it needs a fresh number sign. The same
  ten digits cost 13 cells with periods and 15 with hyphens.
- If the text will not fit one sensible card, do not fight it — see the
  multi-card layout in section 3, step 6.

## 2. Translate your text

MakerWorld's customizer cannot translate English for you. You paste
**pre-translated Unicode braille** — the dot characters in the range
U+2800–U+28FF, such as `⠓⠑⠇⠇⠕`.

1. Open a braille translator such as
   <https://www.branah.com/braille-translator>.
2. Choose **Grade 1** (uncontracted, one cell per letter) or **Grade 2**
   (contracted, where common words and letter groups are shortened). Grade 1 is
   clearest for names and contact details; Grade 2 fits more text in the same
   space and is what most adult braille readers read fluently.
3. Make sure the output is **Unicode braille**, not ASCII/BRF braille. Unicode
   braille looks like dot patterns (`⠓⠑⠇⠇⠕`); ASCII braille looks like ordinary
   letters and punctuation and will not work.
4. Copy the Unicode braille output.
5. Translate **each line separately** so you control where the lines break.

Automatic translation is not the same as a certified transcription. For anything
public, medical, or legal, have a UEB-certified transcriber check it.

## 3. Using the customizer

1. Go to MakerWorld → **Create** → **Parametric Model Maker** and upload
   **only** `Braille_Wedge_Card_STL_Generator.scad`.
2. Paste your braille into `Line_1` through `Line_8` in the **Text Input -
   Pre-Translated Braille** section, one line per field. Leave unused fields
   empty. The defaults are `Line_1` = `⠓⠑⠇⠇⠕` ("hello") and `Line_2` =
   `⠺⠕⠗⠇⠙` ("world") — replace them.
3. For lines 9 through 20, open **More Braille Lines (Advanced)** and use
   `Line_9` … `Line_20`. They live in their own section so twelve usually-empty
   boxes do not bury everything below them.
4. Leave `auto_size_card` set to `On`. The card then sizes its face to your text
   plus `auto_size_margin_mm` (default 6 mm) on every side. This is also the
   safe mode: when the card auto-sizes, "text too long" and "too many lines"
   cannot happen, because the grid is built from your content.
5. To fix the card at a specific size instead, set `auto_size_card` to `Off` and
   use `card_face_width_mm` (default 200 mm) and `card_face_height_mm` (default
   100 mm). In this mode you are responsible for `grid_columns` (default 26
   cells per row) and `grid_rows` (default 8) being large enough.
6. If your text needs more than one card, set `card_layout` to `All cards` in
   the **Multi-Card Layout** section. Your lines are split into groups of
   `rows_per_card` (default 8) and every card is laid out front to back on the
   bed with `card_gap_mm` (default 5 mm) between footprints, so the whole set
   prints in one job.
7. Turn `show_warnings` to `On` in the **Warnings** section before you render.
   MakerWorld gives you no console, so this is the only way to see input
   problems — they appear as red 3D text floating above the card in the preview.
   The text is preview-only and is **never** part of the exported STL, so you
   can leave it on.
8. Generate and render, then download the STL.

Everything else has a working default. The parameters worth knowing about:

| Section | What it controls |
|---------|------------------|
| Support Fins | Fin spacing, offset, thickness; bridge count, size, contact; brim |
| Expert Mode - Shape Selection | `dot_shape`: `Rounded` (default) or `Cone` |
| Expert Mode - Card Shape | `face_angle_deg` (default 75) and `card_thickness_mm` (default 1.5) |
| Expert Mode - Braille Spacing | Cell, line, and dot spacing; manual grid capacity; braille nudge offsets |
| Braille Dot Shape - Rounded / Cone | Dot dimensions for the selected shape |
| Rendering Quality | `render_quality` (default `Medium`) and `cone_segments` |

## 4. Printing it

**Print it exactly as modeled.** Do not rotate it, and do not add slicer
supports. The card already leans at 75° and the fins already stand behind it
with a modelled brim underneath.

| Setting | Value | Why |
|---------|-------|-----|
| Layer height | 0.1 mm | Noticeably smoother dots |
| Material | PLA or PETG | Both tested |
| Supports | none | The fins are the support |
| Brim | optional | One is already modelled under each fin |
| Outer wall speed | 30–40 mm/s or slower | A thin leaning card rings badly at speed |
| Acceleration | modest; input shaping on if available | Same reason |

Why 0.1 mm matters more here than usual: braille standards cap dot height at
0.9 mm, so the number of layers in a dot — and therefore how smooth it feels —
is set almost entirely by layer height. There is no other lever.

After the print: flex or snip the fins off the back of the card, then deburr the
small nubs the bridges leave with a fingernail or fine sandpaper.

Do not add lightening holes to the fins. The extra head motion and vibration
cost a thin leaning part more than the saved filament is worth.

## 5. Tuning the break-away fins

Two symptoms, two dials, opposite directions. `bridge_contact_mm` (default
0.3 mm) is how far each snap-off bridge merges into the back of the card.

- **Fins fall over or bridges break mid-print:** raise `bridge_contact_mm`
  toward 0.4 mm, raise `bridge_count` (default 6), or lower `fin_interval_mm`
  (default 25 mm) so more fins share the load.
- **Fins will not snap off cleanly:** lower `bridge_contact_mm` toward 0.2 mm,
  or reduce `bridge_width_mm` / `bridge_height_mm` (both default 0.5 mm).

If you would rather use your slicer's supports, set `support_fins` to `Off` and
the bare leaning card is exported — but then you must add supports yourself, and
they will touch the back face.

## 6. Why we designed it this way

### The card leans back 75°, not flat

**The decision:** the braille face sits at 75° from the print bed
(`face_angle_deg`, adjustable 60–90°).

**The evidence:**

> **Puerta, Crnovrsanin, South, Dunne — "The Effect of Orientation on the
> Readability and Comfort of 3D-Printed Braille," CHI 2024.** DOI
> [10.1145/3613904.3642719](https://doi.org/10.1145/3613904.3642719)
>
> Why it matters: braille printed on a face angled **75°–90°** from the print
> bed was read significantly faster and more comfortably than flat-printed
> braille, because near-vertical printing moves the layer seams off the surface
> the finger reads. **75°** rather than 90° is the working choice here because it
> reduces the overhang under each dot.

**Why not 90°, if 90° also read well?** Because of what happens underneath each
dot. On a near-vertical face the dots stick sideways out of a wall, so the
underside of every dot is an overhang. At 90° that overhang is nearly
horizontal and needs support or prints rough; at 75° the whole face tilts back
15° and the dot undersides become gentle cone-shaped overhangs that print
support-free. 75° buys the readability of vertical printing without the overhang
problem.

**What happens if you change it:** below about 70° the seams start creeping back
onto the reading surface and you lose the benefit the whole design exists for.
Above 80° the dot undersides get harder to print cleanly. The entire wedge
geometry — the leaning card, the fins behind it, the brim under the fins — exists
only to make 75° printable without slicer supports.

### The dots are a dome on a tapered base

**The decision:** the default `Rounded` dot is a 1.6 mm base tapering to a
1.4 mm dome, 0.35 mm of base plus 0.35 mm of dome — **0.7 mm total height on a
1.6 mm base**.

**The evidence:**

> **2010 ADA Standards for Accessible Design, §703.** <https://archive.ada.gov/>
>
> Why it matters: §703.3 fixes the braille dot envelope (base 1.5–1.6 mm, height
> 0.6–0.9 mm, domed not pointed).

> **ISO 17049:2013, *Accessible design — Application of braille on signage,
> equipment and appliances*.** <https://www.iso.org/standard/58090.html>
>
> Why it matters: where ADA and ISO 17049 overlap — dot base **1.5–1.6 mm**, dot
> height **0.6–0.7 mm** — is the safest target for a model that may be read by
> someone trained on either standard.

**Why a base under the dome at all?** A pure spherical dome on a 1.6 mm base
physically cannot exceed 0.8 mm tall — a hemisphere is as tall as it gets. The
tapered base section is what lets the dot reach the upper part of the legal
height range while keeping the legal base width, and it is also what turns the
dot's underside into a printable overhang when the card leans. Both standards
want dots **domed, not pointed**, which is why `Rounded` is the default;
`dot_shape = Cone` exists because some printers render a truncated cone more
cleanly than a dome.

### Spacing comes from BANA, not from the dot size

**The decision:** `cell_spacing` 7.0 mm, `line_spacing` 10.0 mm, `dot_spacing`
2.5 mm within a cell.

**The evidence:**

> **BANA, *Size and Spacing of Braille Characters*.**
> <https://brailleauthority.org/size-and-spacing-braille-characters>
>
> Why it matters: the source for cell spacing, line spacing, and within-cell dot
> spacing. Dots that are geometrically legal but spaced wrong are unreadable.

**What happens if you change it:** a reading finger is calibrated to this pitch,
so shrinking it to fit more text makes the card harder to read, not more useful.
The generator refuses the physically impossible cases — it warns when
`cell_spacing` drops below `dot_spacing * 2` (cells overlap) or when
`line_spacing` drops below `dot_spacing * 2` plus a dot diameter (rows collide) —
but everything between "impossible" and "standard" is your call, and it is not a
good place to economise.

### Why a parametric upload at all

Two ASSETS papers are the reason this ships as an OpenSCAD script rather than a
fixed STL:

> **Siu, Kim, Miele, Follmer — "shapeCAD: An Accessible 3D Modelling Workflow
> for the Blind and Visually-Impaired Via 2.5D Shape Displays," ASSETS 2019.**
> DOI [10.1145/3308561.3353782](https://doi.org/10.1145/3308561.3353782)
>
> Why it matters: identifies that mainstream CAD is visually dependent enough to
> force blind designers to work through sighted intermediaries, and builds its
> accessible workflow **on OpenSCAD** specifically because the design is text.

> **Zhang, Li, Yu, Faruqi, Xie, Kim, Fan, Forbes, Wobbrock, Guo, He —
> "A11yShape: AI-Assisted 3-D Modeling for Blind and Low-Vision Programmers,"
> ASSETS 2025.** DOI
> [10.1145/3663547.3746362](https://doi.org/10.1145/3663547.3746362)
>
> Why it matters: four blind and low-vision programmers independently produced
> 12 models in OpenSCAD — "tasks that were previously impossible without
> assistance from sighted individuals."

A parameter panel over a script is something you can drive alone. A mesh editor
is not.

## 7. Troubleshooting

MakerWorld's Parametric Model Maker has **no visible OpenSCAD console**, so the
warnings this model writes with `echo()` are invisible there. Set
`show_warnings` to `On` in the **Warnings** section to get the three most
important ones as red 3D text above the card in the preview. That text is
preview-only and never exported.

### `INVALID CHARACTERS`

Red 3D text (and console `WARNING: Line N contains non-braille characters.
Re-translate at branah.com with Unicode Braille output.`).

One of your `Line_N` fields holds something that is not Unicode braille — typed
English, ASCII/BRF braille, or a stray space from another alphabet. Re-translate
and copy the **Unicode braille** output. On MakerWorld the 3D warning does not
tell you which line; check each field for characters that look like ordinary
letters rather than dot patterns.

### `TEXT TOO LONG`

Red 3D text (and console `WARNING: Line N is X cells but capacity is Y.`).

A line is wider than `grid_columns`. **This can only happen when
`auto_size_card` is `Off`** — in auto mode the grid is built from your content,
so it cannot overflow. Fixes, in order of preference:

1. Set `auto_size_card` to `On`.
2. Raise `grid_columns` in **Expert Mode - Braille Spacing**.
3. Shorten or split the line.

### `TOO MANY LINES`

Red 3D text (and console `WARNING: text uses X lines but grid_rows is Y.`).

You filled more `Line_N` fields than `grid_rows` allows, again only possible
with `auto_size_card` = `Off` and `card_layout` = `Single`. Set `auto_size_card`
to `On`, raise `grid_rows`, or switch `card_layout` to `All cards`.

### The card is bigger than my print bed

Console only — **not visible on MakerWorld.** The symptom is what you see in the
preview: a card whose face exceeds 250 mm in width or height, or an All-cards
layout needing more than 250 mm of bed depth.

Diagnose it by arithmetic instead. Your card's face is roughly
`longest line in cells × 7 mm` wide and `number of lines × 10 mm` tall, plus
`2 × auto_size_margin_mm`. Fixes: shorten lines, lower `auto_size_margin_mm`,
or switch to `card_layout` = `All cards`. In All-cards mode, lower `card_gap_mm`
or raise `rows_per_card` to shrink the total bed depth.

### The dots feel rough

Print at 0.1 mm layers and slow the outer wall to 30–40 mm/s. If they are still
rough, try `dot_shape` = `Cone`, which some printers render more cleanly than a
dome.

### Braille cells or rows are overlapping

Console only — the symptom is visible in the preview as dots running into each
other. You have lowered `cell_spacing` below `dot_spacing × 2`, or
`line_spacing` below `dot_spacing × 2` plus a dot diameter. Return them to the
defaults: 7.0 mm, 10.0 mm, and 2.5 mm.

## 8. Alternative: OpenSCAD Assistive Forge

If the MakerWorld customizer is hard to use with your screen reader — or you
would rather not create an account — the same generator runs in
**[OpenSCAD Assistive Forge](https://openscad-assistive-forge.pages.dev/)**,
an accessibility-first browser customizer. Deep link straight to this model:

<https://openscad-assistive-forge.pages.dev/?example=braille-wedge-card>

What the Forge does that MakerWorld cannot:

- **It translates your braille for you.** Type plain English and liblouis —
  compiled to WebAssembly and running on your own device — produces Unicode
  braille. MakerWorld's customizer has no translator, so there you must paste
  braille you translated elsewhere. This model's Forge default is
  **UEB Grade 1** (`en-ueb-g1.ctb`); UEB Grade 2 and US Grade 1 and 2 are
  available in the same picker, and there is a manual Unicode braille editor if
  you want to override a translation by hand.
- **The interface is built for screen readers and keyboards.** Live status
  announcements, a documented keyboard map matching OpenSCAD desktop (F4
  preview, F5/F6 render, F7 download), light/dark/high-contrast themes, and a
  Basic mode that hides the advanced parameters.
- **Presets** you can save, reload, and share as a link.
- **It works offline.** Installable as a desktop app; after the first visit the
  renderer, the braille tables, and this model are cached locally.
- **Filenames describe the model.** A card containing "hello" downloads as
  `Braille Card hello.stl` rather than a hash.

Nothing leaves your device in either tool: MakerWorld renders on its servers,
the Forge renders in your browser with OpenSCAD compiled to WebAssembly.

The braille sign and braille charm generators are in the Forge too, under the
same **Braille Card Customizer** program.

## 9. Resources

- [Branah braille translator](https://www.branah.com/braille-translator) — set
  the output to Unicode braille
- [BANA *Size and Spacing of Braille Characters*](https://brailleauthority.org/size-and-spacing-braille-characters)
- [BANA *Business Cards Fact Sheet* (PDF, approved March 2024)](https://www.brailleauthority.org/sites/default/files/2024-10/Business%20Cards%20Fact%20Sheet.pdf)
- [The Rules of Unified English Braille (ICEB)](https://iceb.org/ueb.html)
- [2010 ADA Standards for Accessible Design](https://archive.ada.gov/)
- [Round Table *Guidelines for Producing Accessible 3D Prints* (2024)](https://printdisability.org/guidelines/3d-prints/)
  — the published standard for tactile print design, including a Blind Makers
  section
- [Smith-Kettlewell *3D Printing for Blind & Low Vision Makers*](https://www.ski.org/technical-file/3d-printing-for-bvi-makers/)
  — printer and slicer guidance for the part of the workflow this model cannot
  cover
- [This project on GitHub](https://github.com/BrennenJohnston/braille-wedge-card-openscad)
- Deeper research write-ups in [`docs/`](.): print stability and path selection,
  dot geometry and slicer quality, customizer usability
- For complex cases — international phone numbers, multiple languages,
  credentials — work with a **UEB-certified transcriber**.
