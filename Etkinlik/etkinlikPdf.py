from fpdf import FPDF
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

from django.http import HttpResponse

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def pdf_creates(etkinlikler, mail):
    mails_ = f'{mail.split("@")[0]}.pdf'
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
    pdf.output(f'{BASE_DIR}/static/{mails_}', 'F')

    response = HttpResponse(open(f'{BASE_DIR}/static/{mails_}', 'rb').read())

    response['Content-Disposition'] = f'attachment; filename={mails_}'
    return response

# def email_gonder(mail):
#     msg = MIMEMultipart()
#     file1 = f'{BASE_DIR}/{mail.split("@")[0]}.pdf'
#     msg.attach(MIMEText(open(file1,"rb").read()))
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('ozguryazilim.tr@gmail.com', 'OIV_0YTR(XrBTjZ8')
#
#     server.sendmail('Email', f'{mail}', msg.as_string())
#     server.close()


# def pdf_sil(name):
#     os.remove(f'{BASE_DIR}/{name}')

# email_gonder('yunusileri.tr@gmail.com')
# mail = 'yunusileri.tr@gmail.com'
# print(f'{BASE_DIR}/{mail.split("@")[0]}.pdf')
