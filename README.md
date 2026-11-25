# Sum up 24 November's world news in one image

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/Airdropzon/makefun-news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/Airdropzon/makefun-news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

Entry for the make.fun bounty "Sum up 24 November's world news in one image"
($100 pool, top places share the prize).

The image is a front-page infographic of Tuesday 24 November 2026:

- **Huang is back at Nvidia** — Nvidia reinstates Jensen Huang as chief
  executive days after he resigned, reportedly after pressure from
  President Trump; shares jump 31% in a day.
- **Ukraine sinks a Russian warship** — Zelensky confirms seven sea drones
  sank the corvette Merkury at Benghazi, Libya; the UN seeks a probe.
- **Nuclear weapon in space?** — NATO vows to defend space after reports
  Russia may put a nuclear weapon in orbit as soon as next month.
- **Myanmar guilty of genocide** — the ICJ rules Myanmar committed genocide
  against the Rohingya; fourteen nations back the verdict.
- **Factory fire kills 26 in Indonesia** — blaze at a sweets factory in
  Banten leaves at least 26 dead and dozens missing.
- **Markets** — S&P 500 up 4.73% and Nikkei up 3.91% as Nvidia relief ends
  the AI sell-off.
- **Hormuz** — three tankers hit mines in the Strait of Hormuz.

Also: COP31 ends with no deal, a 5.6 quake hits Nepal, and the first
foreign astronaut joins China's space station.

Sources: AP, The Guardian, BBC, Principia, 10things.

## How it works

`main.py` (Python 3, standard library only) writes the pre-rendered
`entry.png` (1024×1024, built by `draw_entry.py` with PIL and embedded
below as base64) to `$MAKEFUN_OUTPUT_DIR/entry.png` (or `/output/entry.png`).
No network, deterministic: both runs write the same bytes.

Run it: `MAKEFUN_OUTPUT_DIR=out python3 main.py`
