# pttIpLogPython
enter ptt by telnet and log other user IP into local file

env: python3.7 

1.setting logging user, password ,and project time
user 	 = '1USER'.encode('big5')
#1USER改自己帳號
password = 'PASSWORD'.encode('big5')
#PASSWORD改自己密碼
testTime = 3
#testTime 單位是小時

2.setting target user id
target_list.append(User('USFed'.encode('big5')))

3.project will create a file named like 2018-09-24-17-44-48
example content like this
USFed(美中不踢足球),普通,395次(同天內只計一次),1篇(退:0),不在站上,最近無新信件,09/18/201801:31:35Tue,27.246.34.94
PiGold(黃金豬仔),家徒四壁,186次(同天內只計一次),0篇(退:0),不在站上,最近無新信件,09/18/201807:36:29Tue,111.71.58.6
NTUTW(鋁鹽),家徒四壁,53次(同天內只計一次),0篇(退:0),不在站上,最近無新信件,09/19/201823:31:03Wed,223.140.71.227

can export as csv file

----------
2018.09.24
總之在tech_job被嗆說不是工程師
你可以說我宅 禿 沒女朋友 但是不能說我不是工程師
身為工程師 好像也不能幹嘛 只能查IP
然後手動查了他們IP 3天
覺得自己跟智障一樣

工程師（英語：Engineer）是指那些在工程專業領域的人，
他們使用科學知識來駕馭技術以解決實際問題，並以此為職業。

於是我用了沒學過的PYTHON
主要參考
https://github.com/twtrubiks/PttAutoLoginPost

--開發流程
安裝環境 PYTHON 3.7 ,win 7
能夠跑PttAutoLoginPost
能夠進入查詢網友 印出資料
建立List 一次查詢多人
輸出到檔案
parse所需資料,轉換輸出成csv格式
烤肉
設定時間 在時間內不斷輪轉查詢
如果個人資料完全相同 就不輸出
--Issue
會自己斷線 不想修了
--使用說明
user 	 = '1USER'.encode('big5')
password = 'PASSWORD'.encode('big5')
testTime = 3
