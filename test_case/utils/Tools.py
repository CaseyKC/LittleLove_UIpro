import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from conf.setting import MAIL_ASCII, MAIL_HEADER, MAIL_FROM, MAIL_TO, SMTP_SERVER, MAIL_CONTENT,MAIL_FROM_PASSWORD




def send_mail(file):
    msg = MIMEMultipart()
    msg.attach(MIMEText(MAIL_CONTENT, 'plain', MAIL_ASCII))
    # 邮件附件
    f = open(file, 'rb')
    mail_body = f.read()
    f.close()
    msg.attach(MIMEText(mail_body, 'html', MAIL_ASCII))
    att = MIMEText(mail_body, 'base64', MAIL_ASCII)
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment; filename="%s"' % file.split('\\')[-1]
    msg.attach(att)
    msg['Subject'] = Header(MAIL_HEADER, MAIL_ASCII)
    msg['From'] = MAIL_FROM
    msg['To'] = MAIL_TO
    smtp = smtplib.SMTP_SSL(host=SMTP_SERVER['host'], port=SMTP_SERVER['port'])
    smtp.login(MAIL_FROM, MAIL_FROM_PASSWORD)
    smtp.sendmail(MAIL_FROM, msg['To'].split(';'), msg.as_string())
    smtp.quit()
