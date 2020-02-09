import unittest
import os
from BSTestRunner import BSTestRunner
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from operateDB import operateDb
from Redis import operateRedis


def send_mail(latest_report):
    f=open(latest_report,'rb')
    mail_content=f.read()
    f.close()

    smtpserver = 'smtp.163.com'

    user = 'gujiancheng1989@163.com'
    password = 'gu15925686072'

    sender = 'gujiancheng1989@163.com'
    receives = ['1046662346@qq.com', '2819992623@qq.com']
    subject = '我的练习自动化测试报告'
    send_file = open(latest_report, 'rb').read()

    att = MIMEText(send_file, 'base64', 'utf-8')
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment;filename="'+report_name+'"'




    msgRoot = MIMEMultipart()
    msgRoot.attach(MIMEText(mail_content, 'html', 'utf-8'))
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


def latest_report(report_dir):
    lists = os.listdir(report_dir)
    print(lists)

    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))

    print("the latest report is " + lists[-1])

    file = os.path.join(report_dir, lists[-1])
    print(file)
    return file



if __name__ == '__main__':

    #插入数据库所需要的数据
    oPDb = operateDb.operateDb()
    oPDb.insert("可以执行插入的数据insert into * from student;")

    # 插入用例所需要的Redis数据
    InsertRedis =operateRedis.operateRedis()
    InsertRedis.set("gjc5","NJX5")

    report_dir='./test_report'
    test_dir='./test_case'



    discover = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")
    now=time.strftime("%Y-%m-%d~%H_%M_%S")
    report_name=report_dir+'/'+now+'result.html'



    with open(report_name,'wb') as f:
        runner=BSTestRunner(stream=f,title='test report',description='test result')
        runner.run(discover)
    f.close()

    # 清理插入的数据库数据
    oPDb.delete("可以执行插入的数据delete from student;")

    # 清理所需要的Redis数据
    InsertRedis.remove("gjc5")

    latest_report=latest_report(report_dir)
    send_mail(latest_report)
    print("这是一个完整的测试步骤！！！")






