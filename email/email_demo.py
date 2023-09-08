import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

# email config
sender_addr = 'xxx@qq.com'
receiver_addr = 'zhoytou@gmail.com'

# smtp server config
smtp_server = 'smtp.qq.com'
smtp_port = 465
smtp_username = 'xxx@qq.com'
smtp_password = 'xxx'


def sendEmail(subject: str, body: str, df_attchment: pd.DataFrame):
    """
    将统计结果发送邮件
    Args:
    """
    # create message object instance
    message = MIMEMultipart()
    message['From'] = sender_addr
    message['To'] = receiver_addr
    message['Subject'] = subject
    # add the message body
    message.attach(MIMEText(body, 'plain'))
    # add the message attachment
    attachment = MIMEApplication(df_attchment.to_csv(index=False), 'csv')
    attachment.add_header('Content-Disposition', 'attachment', filename='attachment.csv')
    message.attach(attachment)

    # setup the connection and send the message
    try:
        smtp = smtplib.SMTP_SSL(smtp_server, smtp_port)
        smtp.login(smtp_username, smtp_password)
        smtp.sendmail(sender_addr, receiver_addr, message.as_string())
        smtp.quit()
        print('邮件发送成功')
    except smtplib.SMTPException as e:
        print('邮件发送失败:', str(e))


if __name__ == "__main__":
    pass
