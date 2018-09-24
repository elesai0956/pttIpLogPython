import sys
import telnetlib
import time
import datetime
import re

user 	 = '1USER'.encode('big5')
#1USER改自己帳號
password = 'PASSWORD'.encode('big5')
#PASSWORD改自己密碼
testTime = 3
#testTime 單位是小時

class User:
    def __init__(self,name):
        self.name=name
        self.all=''
        self.ip=''
        self.last=''
        self.money=''
        self.post=''

starttime = time.strftime('%Y-%m-%d-%H-%M-%S')
starttimeC = time.time()



print('--start ',starttime)
host = 'ptt.cc'

target_list = []
target_list.append(User('USFed'.encode('big5')))
target_list.append(User('PiGold'.encode('big5')))
target_list.append(User('NTUTW'.encode('big5')))
target_list.append(User('Honer'.encode('big5')))
target_list.append(User('MassaIT'.encode('big5')))
target_list.append(User('tigerpo'.encode('big5')))
target_list.append(User('Foxxconn'.encode('big5')))
target_list.append(User('APPiiER'.encode('big5')))
target_list.append(User('CHBank'.encode('big5')))
target_list.append(User('Esuny'.encode('big5')))
target_list.append(User('MMHOHO'.encode('big5')))
target_list.append(User('FANG4'.encode('big5')))
target_list.append(User('Usoop'.encode('big5')))
target_list.append(User('GAman'.encode('big5')))
target_list.append(User('KLIMO'.encode('big5')))
target_list.append(User('beta24'.encode('big5')))
target_list.append(User('MoAB'.encode('big5')))
target_list.append(User('eebbc'.encode('big5')))
target_list.append(User('MacBK'.encode('big5')))
target_list.append(User('MBenz'.encode('big5')))
target_list.append(User('AoBoCo'.encode('big5')))
target_list.append(User('NCTUEEE'.encode('big5')))
target_list.append(User('Caney'.encode('big5')))
target_list.append(User('newAC'.encode('big5')))
target_list.append(User('gogoPro'.encode('big5')))
target_list.append(User('namiO'.encode('big5')))
target_list.append(User('ISPNet'.encode('big5')))


# create objs(target_list)

for target in target_list:
    print(target)
    

telnet = telnetlib.Telnet(host)
time.sleep(2)

content = telnet.read_very_eager().decode('big5', 'ignore')
# print(content)
print('--login')

if u"系統過載" in content:
	print('系統過載, 請稍後再來')
	sys.exit(0)

if u"請輸入代號" in content:
	print('輸入帳號中...')
	telnet.write(user + b"\r\n")
	print('輸入密碼中...')
	telnet.write(password + b"\r\n")
	time.sleep(2)
	
content = telnet.read_very_eager().decode('big5', 'ignore')

if u"請按任意鍵繼續" in content:
    print("資訊頁面，按任意鍵繼續...")
    telnet.write(b"\r\n")
    time.sleep(2)
if u"密碼不對" in content:
    print("密碼不對或無此帳號。程式結束")
    sys.exit()
if u"您想刪除其他重複登入" in content:
    print("刪除其他重複登入的連線....")
    telnet.write(b"y\r\n")
    time.sleep(5)
if u"您要刪除以上錯誤嘗試" in content:
    print("刪除以上錯誤嘗試...")
    telnet.write(b"y\r\n")
    time.sleep(2)
if u"您有一篇文章尚未完成" in content:
    print('刪除尚未完成的文章....')
    # 放棄尚未編輯完的文章
    telnet.write(b"q\r\n")
    time.sleep(2)

time.sleep(2)
content = telnet.read_very_eager().decode('big5', 'ignore')
if u"休閒聊天區" in content:
    print("now in 主功能表 enter 休閒聊天區")
    telnet.write(b"t\r\n")
time.sleep(2)

def checkip(target):
    time.sleep(2)
    content = telnet.read_very_eager().decode('big5', 'ignore')
    if u"聊天說話" in content:
        print("now in 聊天說話 enter 查詢網友")
        telnet.write(b"q\r\n")
        time.sleep(2)

        time.sleep(2)
        content = telnet.read_very_eager().decode('big5', 'ignore')
    if u"請輸入使用者代號" in content:
        print("now in 查詢網友 , 請輸入使用者代號")
        print("now in 查詢網友 , 查",target.name)
        telnet.write(target.name + b"\r\n")
        time.sleep(2)

        time.sleep(2)
        content = telnet.read_very_eager().decode('big5', 'ignore')
    if u"ＩＤ暱稱" in content:
        #print('con::',content)
        #print('all::',target.all)
        if target.all != content:
            target.all=content
            tmpStr = content.split('五子棋')[0]
            tmpStr = re.sub("\x1b\[[\d*;?]*\d*[a-zA-Z0-9]", "", tmpStr)
            tmpStr=tmpStr.replace('\n','')
            tmpStr=tmpStr.replace('\r','')
            tmpStr=tmpStr.replace('《ＩＤ暱稱》','')
            tmpStr=tmpStr.replace('《經濟狀況》',',')
            tmpStr=tmpStr.replace('《登入次數》',',')
            tmpStr=tmpStr.replace('《有效文章》',',')
            tmpStr=tmpStr.replace('《目前動態》',',')
            tmpStr=tmpStr.replace('《私人信箱》',',')
            tmpStr=tmpStr.replace('《上次上站》',',')
            tmpStr=tmpStr.replace('《上次故鄉》',',')
            tmpStr=tmpStr.replace('《 ','\n')
            tmpStr=tmpStr.replace(' ','')
            
            file = open(starttime, 'a', encoding = 'UTF-8')
            file.write(tmpStr)            
            print('tmpStr::',tmpStr)
            file.close()
            tmpip=tmpStr.split(',')[-1]
            print('tmpip::',tmpip)
            target.ip=tmpip
            for ipA in target_list:
                if ipA.ip==tmpip and ipA.name !=target.name:
                    print('FUCKING SAME IP',ipA.name,target.name,ipA.ip)
        else:
             print(target.name,"::same content")
# parse(content)
        telnet.write(b"\r\n")
        print('回到聊天說話')
        time.sleep(2)

while True:
  endttimeC = time.time()
  print(starttimeC,endttimeC,endttimeC-starttimeC,testTime*60*60)
 
  for target in target_list:
        checkip(target) 
  if endttimeC-starttimeC > testTime*60*60:
    break

time.sleep(2)
telnet.close()
print('--telnet close')
print('--finish')
sys.exit()

	
