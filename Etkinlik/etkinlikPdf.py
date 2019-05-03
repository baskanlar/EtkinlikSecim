from fpdf import FPDF
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def pdf_creates(etkinlikler, mail):
    print(mail)
    pdf = FPDF()
    pdf.add_page()
    pdf.add_font('DejaVu', '', f'{BASE_DIR}/Etkinlik/DejaVuSansCondensed.ttf',
                 uni=True)
    pdf.set_font('DejaVu', '', 16)
    pdf.write(8, mail)
    pdf.ln(16)
    pdf.set_font('DejaVu', '', 12)
    for txt in etkinlikler:
        pdf.write(8, txt)
        pdf.ln(8)
    pdf.output(f'{mail.split("@")[0]}.pdf', 'F')


def pdf_sil(name):
    os.remove(f'{BASE_DIR}/{name}')
