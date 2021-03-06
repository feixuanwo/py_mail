#coding: utf-8
import smtplib
from email.mime.multipart import MIMEMultipart # 导入 MIMEMultipart 类
from email.mime.text import MIMEText # 导入 MIMEText 类
from email.mime.image import MIMEImage # 导入 MIMEImage 类
HOST = "smtp.gmail.com" # 定义 smtp 主机
SUBJECT = u" 业务性能数据报表 " # 定义邮件主题
TO = "testmail@qq.com" # 定义邮件收件人
FROM = "mymail@gmail.com" # 定义邮件发件人
def addimg(src,imgid): # 添加图片函数 , 参数 1：图片路径，参数 2：图片 id
    fp = open(src, 'rb') # 打开文件
    msgImage = MIMEImage(fp.read()) # 创建 MIMEImage 对象，读取图片内容并作为参数
    fp.close() # 关闭文件
    msgImage.add_header('Content-ID', imgid) # 指定图片文件的 Content-ID,<img>
    # 标签 src 用到
    return msgImage # 返回 msgImage 对象
msg = MIMEMultipart('related') # 创建 MIMEMultipart 对象，采用 related 定义内嵌资源
# 的邮件体
# 创建一个 MIMEText 对象， HTML 元素包括表格 <table> 及图片 <img>
msgtext = MIMEText(""" 
<table width="600" border="0" cellspacing="0" cellpadding="4">
 <tr bgcolor="#CECFAD" height="20" style="font-size:14px">
 <td colspan=2>* 官网性能数据 <a href="monitor.domain.com"> 更多 >></a></td>
 </tr>
 <tr bgcolor="#EFEBDE" height="100" style="font-size:13px">
 <td>
 <img src="cid:io"></td><td>
 <img src="cid:key_hit"></td>
 </tr>
 <tr bgcolor="#EFEBDE" height="100" style="font-size:13px">
 <td>
 <img src="cid:men"></td><td>
 <img src="cid:swap"></td>
 </tr>
 </table>""","html","utf-8") #<img> 标签的 src 属性是通过 Content-ID 来引用的
msg.attach(msgtext) #MIMEMultipart 对象附加 MIMEText 的内容
msg.attach(addimg("img/bytes_io.png","io")) # 使用 MIMEMultipart 对象附加 MIMEImage的内容
msg.attach(addimg("img/myisam_key_hit.png","key_hit"))
msg.attach(addimg("img/os_mem.png","men"))
msg.attach(addimg("img/os_swap.png","swap"))
msg['Subject'] = SUBJECT # 邮件主题
msg['From']=FROM # 邮件发件人 , 邮件头部可见
msg['To']=TO # 邮件收件人 , 邮件头部可见
try:
    server = smtplib.SMTP() # 创建一个 SMTP() 对象
    server.connect(HOST,"25") # 通过 connect 方法连接 smtp 主机
    server.starttls() # 启动安全传输模式
    server.login("mymail@gmail.com","mypassword") # 邮箱账号登录校验
    server.sendmail(FROM, TO, msg.as_string()) # 邮件发送
    server.quit() # 断开 smtp 连接
    print " 邮件发送成功！ "
except Exception, e:
    print " 失败： "+str(e)
