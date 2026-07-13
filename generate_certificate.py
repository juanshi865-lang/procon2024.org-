#!/usr/bin/env python3
"""
PROCON 2024 Best Paper Award Certificate — Landscape Edition
Designed with premium academic award styling
"""

import os, tempfile, shutil
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Spacer

OUTPUT_DIR = os.path.expanduser("~/Desktop")
OUTPUT_PDF = os.path.join(OUTPUT_DIR, "PROCON_2024_Best_Paper_Award_Certificate.pdf")

# Color palette — premium academic style
NAVY_DEEP = colors.HexColor("#0b1a33")
NAVY = colors.HexColor("#1a2d50")
NAVY_MID = colors.HexColor("#2a4070")
GOLD = colors.HexColor("#c8a45c")
GOLD_LIGHT = colors.HexColor("#e8d4a0")
GOLD_DARK = colors.HexColor("#a8863a")
DARK = colors.HexColor("#1e1e1e")
CHARCOAL = colors.HexColor("#3a3a3a")
GRAY = colors.HexColor("#666666")
GRAY_LIGHT = colors.HexColor("#999999")
GRAY_PALE = colors.HexColor("#cccccc")
WHITE = colors.white
CREAM = colors.HexColor("#faf7f0")
PARCHMENT = colors.HexColor("#f5f0e6")
GOLD_BG = colors.HexColor("#fef9e7")


def draw_certificate(c, doc):
    w, h = landscape(A4)  # 841.89 x 595.28 (landscape)

    # ===================== BACKGROUND =====================
    # Outer parchment gradient
    steps = 120
    for i in range(steps):
        t = i / steps
        r = 245 + int((250 - 245) * t)
        g = 240 + int((245 - 240) * t)
        b = 230 + int((235 - 230) * t)
        c.setFillColorRGB(r/255, g/255, b/255)
        c.rect(0, i * h / steps, w, h / steps + 1, stroke=0, fill=1)

    # ===================== DECORATIVE BORDER SYSTEM =====================
    margin = 14 * mm
    ox, oy = margin, margin
    pw = w - 2 * margin
    ph = h - 2 * margin

    # 1. Outermost border — navy double line
    c.setStrokeColor(NAVY)
    c.setLineWidth(2.5)
    c.rect(ox, oy, pw, ph, stroke=1, fill=0)

    c.setStrokeColor(NAVY)
    c.setLineWidth(0.5)
    c.rect(ox + 4, oy + 4, pw - 8, ph - 8, stroke=1, fill=0)

    # 2. Gold accent border
    c.setStrokeColor(GOLD)
    c.setLineWidth(0.8)
    c.rect(ox + 8, oy + 8, pw - 16, ph - 16, stroke=1, fill=0)

    # ===================== CORNER ORNAMENTS =====================
    # Gold corner blocks with inset diamond
    cd = 14
    corner_positions = [
        (ox + 8, oy + 8),  # bottom-left
        (ox + pw - 8 - cd, oy + 8),  # bottom-right
        (ox + 8, oy + ph - 8 - cd),  # top-left
        (ox + pw - 8 - cd, oy + ph - 8 - cd),  # top-right
    ]
    for cx, cy in corner_positions:
        # Gold square
        c.setFillColor(GOLD)
        c.rect(cx, cy, cd, cd, stroke=0, fill=1)
        # White diamond inset
        c.setFillColor(PARCHMENT)
        c.saveState()
        c.translate(cx + cd/2, cy + cd/2)
        c.rotate(45)
        c.rect(-3, -3, 6, 6, stroke=0, fill=1)
        c.restoreState()

    # ===================== TOP BANNER =====================
    banner_h = 20 * mm
    banner_y = oy + ph - 8 - banner_h
    c.setFillColor(NAVY_DEEP)
    c.rect(ox + 8, banner_y, pw - 16, banner_h, stroke=0, fill=1)

    # Gold underline for banner
    c.setFillColor(GOLD)
    c.rect(ox + 8, banner_y - 1.5, pw - 16, 1.5, stroke=0, fill=1)

    # Banner text — white
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(w/2, banner_y + 13*mm,
        "International Workshop on Programmability for Cloud Networks and Applications")

    c.setFont("Helvetica", 7.5)
    c.setFillColor(colors.HexColor("#d0d0d0"))
    c.drawCentredString(w/2, banner_y + 7*mm,
        "Held in conjunction with the International Teletraffic Congress (ITC)  |  Founded 1955  |  Technically co-sponsored by IEEE Communications Society")

    # ===================== GOLD ACCENT BAR (below banner area) =====================
    gold_bar_y = banner_y - 6 * mm
    bar_width = 70 * mm
    c.setFillColor(GOLD)
    c.rect(w/2 - bar_width/2, gold_bar_y - 0.5, bar_width, 0.8, stroke=0, fill=1)

    # ===================== BADGE: PROCON 2024 =====================
    badge_y = gold_bar_y - 8 * mm
    badge_w = 55 * mm
    badge_h = 8 * mm
    # Badge background
    c.setFillColor(NAVY)
    c.roundRect(w/2 - badge_w/2, badge_y - badge_h/2, badge_w, badge_h, 4, stroke=0, fill=1)
    # Badge text
    c.setFillColor(GOLD_LIGHT)
    c.setFont("Helvetica-Bold", 8)
    c.drawCentredString(w/2, badge_y - 2.5, "PROCON 2024  •  BEST PAPER AWARD")

    # ===================== CERTIFICATE BODY =====================
    # "This certificate is presented to"
    c.setFont("Helvetica", 11)
    c.setFillColor(CHARCOAL)
    c.drawCentredString(w/2, h - 58*mm, "This certificate is presented to")

    # Recipient name — large, elegant
    name_y = h - 65*mm
    c.setFont("Helvetica-Bold", 28)
    c.setFillColor(NAVY_DEEP)
    c.drawCentredString(w/2, name_y, "Yinan Qian")

    # Affiliation
    c.setFont("Helvetica", 8.5)
    c.setFillColor(GRAY)
    c.drawCentredString(w/2, name_y - 9*mm,
        "Pinterest, Inc., San Francisco, CA  ·  Tufts University, Medford, MA, United States")

    # "in recognition of..."
    c.setFont("Helvetica", 10.5)
    c.setFillColor(CHARCOAL)
    c.drawCentredString(w/2, name_y - 16*mm,
        "in recognition of the outstanding paper entitled")

    # Paper title — italic with gold
    c.setFont("Helvetica-BoldOblique", 11.5)
    c.setFillColor(NAVY)
    c.drawCentredString(w/2, name_y - 22*mm,
        "Adaptive Load Balancing for Multi-Tier CDN Edge Networks:")
    c.drawCentredString(w/2, name_y - 25.5*mm,
        "A Reinforcement Learning Approach")

    # Awarded line
    c.setFont("Helvetica", 10.5)
    c.setFillColor(CHARCOAL)
    c.drawCentredString(w/2, name_y - 31*mm,
        "selected as the recipient of the PROCON 2024 Best Paper Award")
    c.drawCentredString(w/2, name_y - 34*mm,
        "by the Technical Program Committee.")

    # ===================== HONORS LINE (gold separator) =====================
    sep_y = name_y - 39*mm
    c.setStrokeColor(GOLD)
    c.setLineWidth(0.4)
    c.line(w/2 - 60*mm, sep_y, w/2 + 60*mm, sep_y)

    # ===================== SIGNATURE SECTION =====================
    sig_area_y = sep_y - 18*mm
    sig_spacing = 55 * mm

    # --- Left: General Chair ---
    left_x = w/2 - sig_spacing - 15*mm
    c.setStrokeColor(GRAY)
    c.setLineWidth(0.5)
    c.line(left_x - 20*mm, sig_area_y, left_x + 35*mm, sig_area_y)

    c.setFillColor(NAVY_DEEP)
    c.setFont("Helvetica-Bold", 8.5)
    c.drawCentredString(left_x + 7.5*mm, sig_area_y - 4*mm, "Prof. Roberto Bifulco")

    c.setFillColor(GRAY)
    c.setFont("Helvetica", 7)
    c.drawCentredString(left_x + 7.5*mm, sig_area_y - 8*mm, "General Chair, PROCON 2024")
    c.setFont("Helvetica", 6.5)
    c.drawCentredString(left_x + 7.5*mm, sig_area_y - 11*mm, "NEC Laboratories Europe / TU Munich")

    # --- Center: TPC Chair ---
    c.setStrokeColor(GRAY)
    c.setLineWidth(0.5)
    c.line(w/2 - 30*mm, sig_area_y, w/2 + 30*mm, sig_area_y)

    c.setFillColor(NAVY_DEEP)
    c.setFont("Helvetica-Bold", 8.5)
    c.drawCentredString(w/2, sig_area_y - 4*mm, "Dr. Fulvio Risso")

    c.setFillColor(GRAY)
    c.setFont("Helvetica", 7)
    c.drawCentredString(w/2, sig_area_y - 8*mm, "TPC Chair, PROCON 2024")
    c.setFont("Helvetica", 6.5)
    c.drawCentredString(w/2, sig_area_y - 11*mm, "Politecnico di Torino")

    # --- Right: Workshop Co-Chair ---
    right_x = w/2 + sig_spacing + 15*mm
    c.setStrokeColor(GRAY)
    c.setLineWidth(0.5)
    c.line(right_x - 35*mm, sig_area_y, right_x + 20*mm, sig_area_y)

    c.setFillColor(NAVY_DEEP)
    c.setFont("Helvetica-Bold", 8.5)
    c.drawCentredString(right_x - 7.5*mm, sig_area_y - 4*mm, "Prof. Stefano Salsano")

    c.setFillColor(GRAY)
    c.setFont("Helvetica", 7)
    c.drawCentredString(right_x - 7.5*mm, sig_area_y - 8*mm, "Workshop Co-Chair, PROCON 2024")
    c.setFont("Helvetica", 6.5)
    c.drawCentredString(right_x - 7.5*mm, sig_area_y - 11*mm, "University of Rome \"Tor Vergata\"")

    # ===================== GOLD SEAL (right side) =====================
    seal_cx = w - 50*mm
    seal_cy = oy + 50*mm
    seal_r = 18*mm

    # Outer circle
    c.setStrokeColor(GOLD)
    c.setLineWidth(1.5)
    c.circle(seal_cx, seal_cy, seal_r, stroke=1, fill=0)

    # Inner circle
    c.setStrokeColor(GOLD)
    c.setLineWidth(0.5)
    c.circle(seal_cx, seal_cy, seal_r - 3*mm, stroke=1, fill=0)

    # Fill
    c.setFillColor(GOLD_BG)
    c.circle(seal_cx, seal_cy, seal_r - 3.5*mm, stroke=0, fill=1)

    # Seal text
    c.setFillColor(NAVY)
    c.setFont("Helvetica-Bold", 5.5)
    c.drawCentredString(seal_cx, seal_cy + 6*mm, "PROCON")
    c.setFont("Helvetica", 5)
    c.drawCentredString(seal_cx, seal_cy + 1*mm, "Best Paper")
    c.drawCentredString(seal_cx, seal_cy - 3*mm, "Award")
    c.setFont("Helvetica-Bold", 5)
    c.drawCentredString(seal_cx, seal_cy - 7*mm, "2024")

    # ===================== DATE LINE =====================
    date_y = sig_area_y - 18*mm
    c.setFillColor(GRAY)
    c.setFont("Helvetica", 7.5)
    c.drawCentredString(w/2, date_y, "Conferred: 2024")

    # ===================== BOTTOM FOOTER =====================
    # Navy footer bar
    footer_h = 8 * mm
    footer_y = oy + 8
    c.setFillColor(NAVY_DEEP)
    c.rect(ox + 8, footer_y, pw - 16, footer_h, stroke=0, fill=1)

    # Gold top line for footer
    c.setFillColor(GOLD)
    c.rect(ox + 8, footer_y + footer_h, pw - 16, 1.2, stroke=0, fill=1)

    c.setFillColor(colors.HexColor("#a0a0b0"))
    c.setFont("Helvetica-Oblique", 6)
    c.drawCentredString(w/2, footer_y + 5*mm,
        "Certificate of Best Paper Award  |  PROCON 2024  |  procon2024.org")
    c.drawCentredString(w/2, footer_y + 1*mm,
        "International Workshop on Programmability for Cloud Networks and Applications")


def generate_certificate():
    temp_cert = tempfile.mktemp(suffix=".pdf")

    class CertDoc(BaseDocTemplate):
        def __init__(self, *a, **kw):
            BaseDocTemplate.__init__(self, *a, **kw)
            lw, lh = landscape(A4)
            self.t_cert = PageTemplate(
                id='cert',
                frames=Frame(0, 0, lw, lh, id='c'),
                onPage=draw_certificate
            )
            self.addPageTemplates([self.t_cert])

    doc = CertDoc(temp_cert, pagesize=landscape(A4))
    story = [Spacer(0.1*mm, 0.1*mm)]
    doc.build(story)
    return temp_cert


def main():
    print("Generating PROCON 2024 Best Paper Award Certificate (Landscape Edition)...")
    cert_pdf = generate_certificate()
    shutil.copy2(cert_pdf, OUTPUT_PDF)
    os.remove(cert_pdf)
    print(f"Certificate saved to: {OUTPUT_PDF}")
    print("Done!")


if __name__ == "__main__":
    main()
