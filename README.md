[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/jonjet155/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/jonjet155/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

# The World in One Day — Monday 23 November 2026

One image summing up 23 November 2026's world news: 41 stories on a single 1024×1024 page — 13 illustrated panels (COP31 collapse, Hormuz attacks, the AI market rout, the Banten factory fire and more) plus 28 more stories in the ALSO ON list, a world map with numbered pins, a six-number stat strip and a DATE CHECK footer.

Every panel is code-drawn flat 2D vector art (no generated photos); the page was rendered with Pillow on the build machine. The entry itself is a single PNG: `entry.png`.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

`main.py` is stdlib-only: it copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`. Nothing is installed, no network is needed, and running it twice produces identical bytes.

## License

MIT — see `LICENSE`.

