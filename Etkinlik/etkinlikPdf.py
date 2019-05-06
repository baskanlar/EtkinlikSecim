import os

from django.http import HttpResponse, JsonResponse
from fpdf import FPDF

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def pdf_creates(etkinlikler, mail):
    try:
        pdf_ismi = f'{mail.split("@")[0]}.pdf'
        pdf = FPDF()
        pdf.add_page()
        pdf.add_font('DejaVu', '', f'{BASE_DIR}/Etkinlik/DejaVuSansCondensed.ttf', uni=True)
        pdf.set_font('DejaVu', '', 16)
        pdf.write(8, mail)
        pdf.ln(16)
        pdf.set_font('DejaVu', '', 12)
        for txt in etkinlikler:
            pdf.write(8, txt)
            pdf.ln(8)
        pdf.output(f'{BASE_DIR}/static/{pdf_ismi}', 'F')

        response = HttpResponse(open(f'{BASE_DIR}/static/{pdf_ismi}', 'rb').read())
        response['Content-Disposition'] = f'attachment; filename={pdf_ismi}'
        return response
    except FileNotFoundError:
        return JsonResponse({'status': 'PDF Bulunamadı'}, safe=False)
