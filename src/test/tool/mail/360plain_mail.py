import re
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

mail_to = "weidongdong@360.cn"


# 读取本地文件获取邮箱的账号和密码
def get_account():
    print('从本地账号文件读取账号密码')
    # 账号密码
    with open('360mail_account.txt', 'r') as f:
        pattern = re.compile('name:(.*?)\npwd:(.*?)$', re.S)

        match = re.search(pattern, f.read())

        if not match:
            print("账号文件格式不匹配")
            exit()

    print('本地账号密码读取成功！')
    return match


def sendmail():
    from_match = get_account()
    mail_from = from_match.group(1)
    mail_from_pwd = from_match.group(2)

    # 构建邮件
    mail_body = 'hi,这是邮件正文，收到请回复！！'
    msg = MIMEText(mail_body, 'plain', 'utf-8')
    msg['From'] = formataddr(['冬来冬往', mail_from])
    msg['To'] = formataddr(['尊敬的用户', mail_to])
    msg['Subject'] = '一封慰问信'

    server = smtplib.SMTP('mail.corp.qihoo.net')
    server.login(mail_from, mail_from_pwd)
    server.sendmail(mail_from, [mail_to, ], msg.as_string())
    server.quit()


if __name__ == '__main__':
    sendmail()
