from fpdf import FPDF
import os
# from email.mime.text import MIMEText
import smtplib
# from email.MIMEMultipart import MIMEMultipart
# from email.MIMEImage import MIMEImage
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

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


def email_gonder(mail):
    msg = MIMEMultipart()
    file1 = f'{BASE_DIR}/{mail.split("@")[0]}.pdf'
    msg.attach(MIMEText(open(file1,"rb").read()))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ozguryazilim.tr@gmail.com', 'OIV_0YTR(XrBTjZ8')

    server.sendmail('Email', f'{mail}', msg.as_string())
    server.close()


def pdf_sil(name):
    os.remove(f'{BASE_DIR}/{name}')


# email_gonder('yunusileri.tr@gmail.com')
# mail = 'yunusileri.tr@gmail.com'
# print(f'{BASE_DIR}/{mail.split("@")[0]}.pdf')
