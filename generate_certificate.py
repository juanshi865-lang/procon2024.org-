#!/usr/bin/env python3
"""
PROCON 2024 Best Paper Award Certificate
- Workshop: International Workshop on Programmability for Cloud Networks and Applications
- General Chair: Prof. Roberto Bifulco
- TPC Chair: Dr. Fulvio Risso
- Workshop Co-Chair: Prof. Stefano Salsano
- Award to: Yinan Qian
- Paper: Adaptive Load Balancing for Multi-Tier CDN Edge Networks:
          A Reinforcement Learning Approach
"""

import os, tempfile, shutil
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Spacer

OUTPUT_DIR = os.path.expanduser("~/Desktop")
OUTPUT_PDF = os.path.join(OUTPUT_DIR, "PROCON_2024_Best_Paper_Award_Certificate.pdf")

# Colors — academic/formal style
PRIMARY = colors.HexColor("#0b1a33")       # Deep navy (PROCON brand)
PRIMARY_LIGHT = colors.HexColor("#162d50")
GOLD = colors.HexColor("#c8a45c")
GOLD_LIGHT = colors.HexColor("#e0c86a")
GOLD_DARK = colors.HexColor("#a8863a")
DARK = colors.HexColor("#1a1a1a")
GRAY = colors.HexColor("#555555")
GRAY_LIGHT = colors.HexColor("#999999")
WHITE = colors.white
CREAM = colors.HexColor("#faf8f0")
BLUE_ACCENT = colors.HexColor("#2563eb")


def draw_certificate(c, doc):
    w, h = A4  # 595.27 x 841.89 pt

    # === BACKGROUND ===
    c.setFillColor(CREAM)
    c.rect(0, 0, w, h, stroke=0, fill=1)

    # === OUTER BORDER (gold, thick) ===
    margin = 22 * mm
    ox, oy = margin, margin
    pw = w - 2 * margin
    ph = h - 2 * margin
    c.setStrokeColor(GOLD)
    c.setLineWidth(2.5)
    c.rect(ox, oy, pw, ph, stroke=1, fill=0)

    # === MIDDLE BORDER (navy) ===
    inner_margin = 5 * mm
    c.setStrokeColor(PRIMARY)
    c.setLineWidth(0.8)
    c.rect(ox + inner_margin, oy + inner_margin,
           pw - 2 * inner_margin, ph - 2 * inner_margin, stroke=1, fill=0)

    # === INNER BORDER (gold, thin) ===
    c.setStrokeColor(GOLD)
    c.setLineWidth(0.4)
    c.rect(ox + inner_margin + 3, oy + inner_margin + 3,
           pw - 2 * inner_margin - 6, ph - 2 * inner_margin - 6, stroke=1, fill=0)

    # === CORNER ORNAMENTS — gold diamonds ===
    c.setFillColor(GOLD)
    cd = 10
    corners = [
        (ox + inner_margin + 3, oy + inner_margin + 3),
        (ox + pw - inner_margin - 3 - cd, oy + inner_margin + 3),
        (ox + inner_margin + 3, oy + ph - inner_margin - 3 - cd),
        (ox + pw - inner_margin - 3 - cd, oy + ph - inner_margin - 3 - cd),
    ]
    for cx, cy in corners:
        c.rect(cx, cy, cd, cd, stroke=0, fill=1)
        c.setFillColor(WHITE)
        c.circle(cx + cd/2, cy + cd/2, 2.2, stroke=0, fill=1)
        c.setFillColor(GOLD)

    # === GOLD ACCENT BARS (top and bottom inside border) ===
    bar_left = ox + inner_margin + 6
    bar_right = ox + pw - inner_margin - 6
    bar_width = bar_right - bar_left

    # Top gold bar
    top_bar_y = oy + ph - inner_margin - 3 - 28
    c.setFillColor(GOLD)
    c.rect(bar_left, top_bar_y, bar_width, 1.2, stroke=0, fill=1)

    # Bottom gold bar
    bot_bar_y = oy + inner_margin + 3 + 32
    c.rect(bar_left, bot_bar_y, bar_width, 1.2, stroke=0, fill=1)

    # === TOP SECTION ===
    c.setFillColor(PRIMARY)

    # ORG NAME — full name
    c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(w/2, h - 38*mm,
        "International Workshop on Programmability for")
    c.drawCentredString(w/2, h - 42*mm,
        "Cloud Networks and Applications")

    # Subtitle — ITC affiliation
    c.setFont("Helvetica", 8)
    c.setFillColor(GRAY)
    c.drawCentredString(w/2, h - 47*mm,
        "Held in conjunction with the International Teletraffic Congress (ITC) — Founded 1955")

    # Edition badge
    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(GOLD)
    c.drawCentredString(w/2, h - 51*mm, "PROCON 2024")

    # === CERTIFICATE TITLE ===
    c.setFillColor(PRIMARY)
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(w/2, h - 58*mm, "BEST PAPER AWARD")

    # Thin separator line
    sep_y = h - 61*mm
    c.setStrokeColor(GOLD)
    c.setLineWidth(0.6)
    c.line(w/2 - 50*mm, sep_y, w/2 + 50*mm, sep_y)

    # === BODY TEXT ===
    c.setFont("Helvetica", 11)
    c.setFillColor(DARK)

    c.drawCentredString(w/2, h - 66*mm, "This certificate is presented to")

    # Name — large, bold, gold
    c.setFont("Helvetica-Bold", 22)
    c.setFillColor(GOLD)
    c.drawCentredString(w/2, h - 71*mm, "Yinan Qian")
    c.setFillColor(GRAY)
    c.setFont("Helvetica-Oblique", 9)
    c.drawCentredString(w/2, h - 75*mm, "Pinterest, Inc. / Tufts University, United States")

    # Body text
    c.setFont("Helvetica", 11)
    c.setFillColor(DARK)
    c.drawCentredString(w/2, h - 81*mm,
        "in recognition of the outstanding paper entitled")

    # Paper title in italic
    c.setFont("Helvetica-BoldOblique", 11)
    c.setFillColor(PRIMARY)
    c.drawCentredString(w/2, h - 85*mm,
        "Adaptive Load Balancing for Multi-Tier CDN Edge Networks:")
    c.drawCentredString(w/2, h - 88.5*mm,
        "A Reinforcement Learning Approach")

    c.setFont("Helvetica", 11)
    c.setFillColor(DARK)
    c.drawCentredString(w/2, h - 94*mm,
        "selected as the recipient of the PROCON 2024 Best Paper Award")
    c.drawCentredString(w/2, h - 97.5*mm,
        "by the Technical Program Committee.")

    # === SIGNATURE SECTION ===
    sig_area_y = h - 118*mm

    c.setStrokeColor(GRAY)
    c.setLineWidth(0.4)

    # General Chair (left)
    left_x = 55*mm
    c.line(left_x - 10*mm, sig_area_y, left_x + 60*mm, sig_area_y)
    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(PRIMARY)
    c.drawCentredString(left_x + 25*mm, sig_area_y - 12, "Prof. Roberto Bifulco")
    c.setFont("Helvetica", 7.5)
    c.setFillColor(GRAY)
    c.drawCentredString(left_x + 25*mm, sig_area_y - 20, "General Chair")
    c.drawCentredString(left_x + 25*mm, sig_area_y - 28, "PROCON 2024")
    c.setFont("Helvetica", 6.5)
    c.drawCentredString(left_x + 25*mm, sig_area_y - 35, "NEC Laboratories Europe / TU Munich")

    # TPC Chair (center)
    center_x = w/2
    c.line(center_x - 35*mm, sig_area_y, center_x + 35*mm, sig_area_y)
    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(PRIMARY)
    c.drawCentredString(center_x, sig_area_y - 12, "Dr. Fulvio Risso")
    c.setFont("Helvetica", 7.5)
    c.setFillColor(GRAY)
    c.drawCentredString(center_x, sig_area_y - 20, "TPC Chair")
    c.drawCentredString(center_x, sig_area_y - 28, "PROCON 2024")
    c.setFont("Helvetica", 6.5)
    c.drawCentredString(center_x, sig_area_y - 35, "Politecnico di Torino")

    # Workshop Co-Chair (right)
    right_x = w - 55*mm
    c.line(right_x - 60*mm, sig_area_y, right_x + 10*mm, sig_area_y)
    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(PRIMARY)
    c.drawCentredString(right_x - 25*mm, sig_area_y - 12, "Prof. Stefano Salsano")
    c.setFont("Helvetica", 7.5)
    c.setFillColor(GRAY)
    c.drawCentredString(right_x - 25*mm, sig_area_y - 20, "Workshop Co-Chair")
    c.drawCentredString(right_x - 25*mm, sig_area_y - 28, "PROCON 2024")
    c.setFont("Helvetica", 6.5)
    c.drawCentredString(right_x - 25*mm, sig_area_y - 35, "University of Rome \"Tor Vergata\"")

    # === SANCTION LINE ===
    c.setFont("Helvetica-Oblique", 7)
    c.setFillColor(GRAY_LIGHT)
    sanction_y = sig_area_y - 48
    c.drawCentredString(w/2, sanction_y,
        "This award is conferred by the Organizing Committee of the International Workshop on")
    c.drawCentredString(w/2, sanction_y - 10,
        "Programmability for Cloud Networks and Applications (PROCON), held in conjunction with")
    c.drawCentredString(w/2, sanction_y - 20,
        "the International Teletraffic Congress (ITC). Technically co-sponsored by the IEEE Communications Society.")

    # === GOLD LINE at bottom inside border ===
    c.setFillColor(GOLD)
    c.rect(bar_left, oy + inner_margin + 8, bar_width, 0.6, stroke=0, fill=1)

    # === SEAL AREA (bottom left) ===
    seal_x = ox + inner_margin + 12
    seal_y = oy + inner_margin + 4
    seal_w, seal_h = 55, 32
    c.setStrokeColor(GOLD)
    c.setLineWidth(0.6)
    c.setFillColor(colors.HexColor("#fef9e7"))
    c.roundRect(seal_x, seal_y, seal_w, seal_h, 3, stroke=1, fill=1)
    c.setFont("Helvetica-Bold", 6.5)
    c.setFillColor(GOLD)
    c.drawCentredString(seal_x + seal_w/2, seal_y + seal_h/2 + 6, "PROCON")
    c.setFont("Helvetica", 5.5)
    c.drawCentredString(seal_x + seal_w/2, seal_y + seal_h/2 - 1, "Best Paper Award")
    c.drawCentredString(seal_x + seal_w/2, seal_y + seal_h/2 - 8, "OFFICIAL SEAL")

    # === FOOTER TEXT ===
    c.setFont("Helvetica-Oblique", 6)
    c.setFillColor(GRAY_LIGHT)
    c.drawCentredString(w/2, oy + inner_margin - 2,
        "Certificate of Best Paper Award  |  PROCON 2024  |  Held in conjunction with ITC")
    c.drawCentredString(w/2, oy + inner_margin - 8,
        "International Workshop on Programmability for Cloud Networks and Applications")


def generate_certificate():
    """Generate the standalone certificate PDF."""
    temp_cert = tempfile.mktemp(suffix=".pdf")

    class CertDoc(BaseDocTemplate):
        def __init__(self, *a, **kw):
            BaseDocTemplate.__init__(self, *a, **kw)
            w, h = A4
            self.t_cert = PageTemplate(
                id='cert',
                frames=Frame(0, 0, w, h, id='c'),
                onPage=draw_certificate
            )
            self.addPageTemplates([self.t_cert])

    doc = CertDoc(temp_cert, pagesize=A4)
    story = [Spacer(0.1*mm, 0.1*mm)]
    doc.build(story)

    return temp_cert


def main():
    print("Generating PROCON 2024 Best Paper Award Certificate...")

    cert_pdf = generate_certificate()
    shutil.copy2(cert_pdf, OUTPUT_PDF)
    os.remove(cert_pdf)

    print(f"Certificate saved to: {OUTPUT_PDF}")
    print("Done!")


if __name__ == "__main__":
    main()
