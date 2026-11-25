#!/usr/bin/env python3
"""Sum up 24 November 2026's world news in one image.

Draws a 1024x1024 front-page infographic with PIL and writes it as a
PNG. No network, no randomness: the same input always produces the
same bytes. Run:  MAKEFUN_OUTPUT_DIR=out python3 source.py
"""

import os

from PIL import Image, ImageDraw, ImageFont

WIDTH = 1024
HEIGHT = 1024
BG = (13, 22, 38)
PANEL = (24, 36, 58)
PANEL_ALT = (28, 42, 66)
INK = (240, 244, 250)
MUTED = (178, 190, 206)
GOLD = (245, 197, 66)
GREEN = (46, 204, 113)
RED = (231, 76, 60)
BLUE = (84, 153, 199)
PURPLE = (155, 89, 182)
ORANGE = (230, 126, 34)
TEAL = (26, 188, 156)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
BOLD = os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf")
REG = os.path.join(FONT_DIR, "DejaVuSans.ttf")


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_width):
    """Split text into lines that fit max_width, word by word."""
    words = text.split()
    lines = []
    current = ""
    for word in words:
        trial = word if not current else current + " " + word
        if draw.textlength(trial, font=fnt) <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_wrapped(draw, x, y, text, fnt, color, max_width, leading):
    """Draw wrapped text, return the y just below the last line."""
    for line in wrap(draw, text, fnt, max_width):
        draw.text((x, y), line, font=fnt, fill=color)
        y += leading
    return y


def story_card(draw, box, accent, tag, headline, body):
    """One news card: coloured left bar, tag, headline, body text."""
    x0, y0, x1, y1 = box
    draw.rounded_rectangle(box, radius=14, fill=PANEL)
    draw.rectangle([x0, y0 + 14, x0 + 8, y1 - 14], fill=accent)
    inner = x0 + 24
    width = x1 - inner - 20
    tag_font = font(BOLD, 19)
    head_font = font(BOLD, 26)
    body_font = font(REG, 20)
    draw.text((inner, y0 + 16), tag, font=tag_font, fill=accent)
    y = y0 + 46
    y = draw_wrapped(draw, inner, y, headline, head_font, INK, width, 31)
    draw_wrapped(draw, inner, y + 6, body, body_font, MUTED, width, 25)


def main():
    img = Image.new("RGB", (WIDTH, HEIGHT), BG)
    draw = ImageDraw.Draw(img)

    # Header band.
    draw.rectangle([0, 0, WIDTH, 128], fill=(10, 17, 30))
    draw.rectangle([0, 128, WIDTH, 132], fill=GOLD)
    draw.text((48, 22), "24 NOVEMBER 2026", font=font(BOLD, 58),
              fill=INK)
    draw.text((48, 88), "THE WORLD IN ONE IMAGE  —  TUESDAY",
              font=font(BOLD, 22), fill=GOLD)

    # Feature story: Nvidia / Huang.
    fx0, fy0, fx1, fy1 = 32, 152, 992, 308
    draw.rounded_rectangle([fx0, fy0, fx1, fy1], radius=14, fill=PANEL_ALT)
    draw.rectangle([fx0, fy0 + 14, fx0 + 10, fy1 - 14], fill=GREEN)
    draw.text((64, fy0 + 16), "TECH  •  NVIDIA", font=font(BOLD, 21),
              fill=GREEN)
    draw.text((64, fy0 + 46), "Huang is back at Nvidia",
              font=font(BOLD, 40), fill=INK)
    draw_wrapped(draw, 64, fy0 + 100,
                 "Nvidia reinstates Jensen Huang as CEO after Trump "
                 "pressure. Shares jump +31% in a day.",
                 font(REG, 24), MUTED, fx1 - 64 - 32, 31)
    draw.text((fx1 - 240, fy0 + 18), "+31%", font=font(BOLD, 44),
              fill=GREEN)

    # Six remaining stories in a 2 x 3 grid.
    stories = [
        (BLUE, "UKRAINE  •  WAR AT SEA",
         "Ukraine sinks a Russian warship",
         "7 sea drones sank the corvette Merkury "
         "at Benghazi. The UN seeks a probe."),
        (RED, "SPACE  •  NATO",
         "NATO vows to defend space",
         "Alliance responds after reports of a Russian nuclear "
         "weapon in orbit."),
        (PURPLE, "JUSTICE  •  ICJ",
         "Myanmar guilty of genocide",
         "The ICJ rules Myanmar committed genocide against the "
         "Rohingya; 14 nations back it."),
        (ORANGE, "INDONESIA  •  BANTEN",
         "Factory fire kills 26",
         "Blaze at a sweets factory in Banten: at least "
         "26 dead, dozens missing."),
        (TEAL, "MARKETS  •  STOCKS",
         "Stocks rally as AI sell-off ends",
         "S&P 500 +4.73%, Nikkei +3.91% as Nvidia relief "
         "lifts markets."),
        (GOLD, "ENERGY  •  HORMUZ",
         "Three tankers hit mines",
         "Three tankers strike mines in the Strait of Hormuz, "
         "a key oil chokepoint."),
    ]
    margin = 32
    gap = 16
    cell_w = (WIDTH - 2 * margin - gap) // 2
    cell_h = 168
    top = 324
    for i, (accent, tag, headline, body) in enumerate(stories):
        col = i % 2
        row = i // 2
        x0 = margin + col * (cell_w + gap)
        y0 = top + row * (cell_h + gap)
        story_card(draw, (x0, y0, x0 + cell_w, y0 + cell_h),
                   accent, tag, headline, body)

    # Also-in-the-news strip.
    ay0 = top + 3 * cell_h + 2 * gap + 16
    draw.rounded_rectangle([32, ay0, 992, ay0 + 84], radius=14,
                           fill=(10, 17, 30))
    draw.text((56, ay0 + 12), "ALSO TODAY",
              font=font(BOLD, 20), fill=GOLD)
    draw_wrapped(draw, 56, ay0 + 40,
                 "COP31 ends with no deal  •  5.6 quake hits Nepal  •  "
                 "First foreign astronaut joins China's space station",
                 font(REG, 21), MUTED, 992 - 56 - 24, 27)

    # Footer.
    draw.rectangle([0, 968, WIDTH, HEIGHT], fill=(10, 17, 30))
    draw.text((48, 984), "24 NOVEMBER 2026  •  SOURCES: AP, THE GUARDIAN, "
              "BBC, PRINCIPIA, 10THINGS",
              font=font(REG, 18), fill=MUTED)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.png")
    img.save(out_path, format="PNG", optimize=True)
    print("wrote", out_path)


if __name__ == "__main__":
    main()
