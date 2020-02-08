import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtpserver = 'smtp.163.com'

user = 'gujiancheng1989@163.com'
password = 'gu15925686072'

sender = 'gujiancheng1989@163.com'
receives = ['1046662346@qq.com', '2819992623@qq.com']

subject = 'gjc系统接口自动化测试报告'
content = '<html><h1 style="color:red">测试报告在附件中，请下载查看！</h1></html>'

send_file = open(r'F:\Python\NewStudy\Test_Project\test_report\2019-11-03-17_19_01result.html', 'rb').read()

att = MIMEText(send_file, 'base64', 'utf-8')
att['Content-Type'] = 'application/octet-stream'
att['Content-Disposition'] = 'attachment;filename="2019-11-03-17_19_01result.html"'

msgRoot = MIMEMultipart()
msgRoot.attach(MIMEText(content, 'html', 'utf-8'))
msgRoot['Subject'] = subject
msgRoot['From'] = sender
msgRoot['To'] = ','.join(receives)
msgRoot.attach(att)

smtp = smtplib.SMTP_SSL(smtpserver, 465)
smtp.helo(smtpserver)
smtp.ehlo(smtpserver)
smtp.login(user, password)

print("Start send email...")
smtp.sendmail(sender, receives, msgRoot.as_string())
smtp.quit()
print("Send email end!")



