# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 21:10:06 2018

@author: Administrator
"""
#

#from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = 'xinihe@163.com'
password = 'nh310018'
smtp_server = 'smtp.163.com'
to_addr = 'ni.he@qq.com'

msg = MIMEText('hello Again, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自国际商学院的问候……', 'utf-8').encode()

server = smtplib.SMTP()
server.connect(smtp_server, 25)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()