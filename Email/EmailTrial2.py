# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 23:15:52 2018

@author: Administrator
"""

import smtplib  
from email.mime.text import MIMEText  
mailto_list=['ni.he@qq.com','xinihe@163.com']           #收件人(列表)  
mail_host="smtp.163.com"            #使用的邮箱的smtp服务器地址，这里是163的smtp地址  
mail_user="xinihe"                           #用户名  
mail_pass="nh310018"                             #密码  
mail_postfix="163.com"                     #邮箱的后缀，网易就是163.com  
def send_mail(to_list,sub,content):  
    me="Mail from IBS"+"<"+mail_user+"@"+mail_postfix+">"  
    msg = MIMEText(content,_subtype='plain')  
    msg['Subject'] = sub  
    msg['From'] = me  
    msg['To'] = ";".join(to_list)                #将收件人列表以‘；’分隔  
    try:  
        server = smtplib.SMTP()  
        server.connect(mail_host, 25)                            #连接服务器  
        server.login(mail_user,mail_pass)               #登录操作  
        server.sendmail(me, to_list, msg.as_string())  
        server.close()  
        return True  
    except: 
        return False  
for i in range(1):                             #发送1封，上面的列表是几个人，这个就填几  
    if send_mail(mailto_list,"来自国际 Congratulation","祝你幸福3"):  #邮件主题和邮件内容  
            #这是最好写点中文，如果随便写，可能会被网易当做垃圾邮件退信  
        print("done!")  
    else:  
        print("failed!")  