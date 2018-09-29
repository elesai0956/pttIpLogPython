# pttIpLogPython
enter ptt by telnet and log other user IP into local file

env: python3.7 

## 1. setting logging user, password ,and project time
  * user 	 = '1USER'.encode('big5')
  #1USER改自己PTT帳號
  * password = 'PASSWORD'.encode('big5')
  #PASSWORD改自己密碼
  * testTime = 3
  #testTime 單位是小時

## 2. setting target user id
  target_list.append(User('USFed'.encode('big5')))

## 3. project will create a log file
  project will create a file named like 2018-09-24-17-44-48
  content like this
    USFed(美中不踢足球),普通,395次(同天內只計一次),1篇(退:0),不在站上,最近無新信件,09/18/201801:31:35Tue,27.246.34.94
    PiGold(黃金豬仔),家徒四壁,186次(同天內只計一次),0篇(退:0),不在站上,最近無新信件,09/18/201807:36:29Tue,111.71.58.6
    NTUTW(鋁鹽),家徒四壁,53次(同天內只計一次),0篇(退:0),不在站上,最近無新信件,09/19/201823:31:03Wed,223.140.71.227

## 4. log can export as csv file

## 5. example

![pic1](https://imgur.com/hGPoSNv.jpg)
![pic2](https://imgur.com/p8NavA9.jpg)
![pic3](https://imgur.com/cKHSdAL.jpg)





