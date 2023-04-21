import time

import null
import requests
import json
import requests
import random
from bs4 import BeautifulSoup as bs
import psycopg2








url_base="https://lkdr.nalog.ru/api/v1/receipt"
fresh_token='Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ7XCJhdXRoVHlwZVwiOlwiU01TXCIsXCJsb2dpblwiOlwiNzk3NzcxNDg1OTJcIixcImlkXCI6NDcwOTAwNixcImRldmljZUlkXCI6XCJneGI0QVk2ZldmamNLSzN5NTNDak1cIixcInBob25lXCI6XCI3OTc3NzE0ODU5MlwifSIsImV4cCI6MTY4MjA4MTA4NX0.NHy-ZIzSAVqv-CkHkQMNrDlWOIX4dWm-Jj7LdDwroZUb5kFqkdYEE0oOrJkX5U4qZodt2qseTLwLGvA5g_2Rxw'
headers={"Authorization":fresh_token}
key={"limit":10,"offset":0, "orderBy":"RECEIVE_DATE:DESC"}
re=requests.post(url_base,  headers=headers, json=key )
print(re.status_code)
#print(re.text)
reJSON=re.text
#print(reJSON)
full=json.loads(reJSON)
for item in full['receipts']:
            shoper=item['createdDate'],item['totalSum'],item['kktOwner']
            print(shoper)
            str_key = {"key":item['key']}
            takeProduct=requests.post("https://lkdr.nalog.ru/api/v1/receipt/fiscal_data", headers=headers, json=str_key)
            #print(takeProduct.text+"\n")
            text=takeProduct.text
            fill=json.loads(text)
            for items in fill['items']:
             print("Продукты:"+items['name'])

            print()




#fullBuyer=json.loads('buyer')


#receipts=full["receipts"]
#full=json.loads(re)
#print(receipts)

"""
URL_Template="https://lkdr.nalog.ru/api/v1/user/profile"
r=requests.get(URL_Template)
print(r.status_code)
print(r.text)"""


"""
text2="sitekey=hfU4TD7fJUI7XcP5qRphKWgnIR5t9gXAxTRqdQJk"
lang="&lang=ru&test=false"
text3="rdata=%7B%22a1%22%3A%22LFeKQJgDQLLRwg%3D%3D%3B0%22%2C%22a2%22%3A%22%3B1%22%2C%22a3%22%3A%22PeJ3FnL%2B8pV5g5zx1vVfbA%3D%3D%3B2%22%2C%22a4%22%3A%22r%2Fs9ZmSAk4UboDSMkI6HUJzdMQZfbqFZ9IMmwJauMKIOUw%3D%3D%3B3%22%2C%22a5%22%3A%22%2Bf7vVyB%2FUdWedQ%3D%3D%3B4%22%2C%22a6%22%3A%22Qi0%3D%3B5%22%2C%22a7%22%3A%22uX1qB74ZSAi0ow%3D%3D%3B6%22%2C%22a8%22%3A%22osJE4y7HBGk3Dg%3D%3D%3B7%22%2C%22a9%22%3A%22UOIOP4w0hSgWQA%3D%3D%3B8%22%2C%22b1%22%3A%22AZ%2Fac%2BuO4IxsOA%3D%3D%3B9%22%2C%22b2%22%3A%22I2jzRm%2FQSYa2xQ%3D%3D%3B10%22%2C%22b3%22%3A%222O%2BH5WV8R27xBg%3D%3D%3B11%22%2C%22b4%22%3A%22DtgcGtVESUc%3D%3B12%22%2C%22b5%22%3A%22BaRA%2FPAFmXM1XQ%3D%3D%3B13%22%2C%22b6%22%3A%229d44ESj80nk%3D%3B14%22%2C%22b7%22%3A%221xX7D8jqPKUtkw%3D%3D%3B15%22%2C%22b8%22%3A%224I%2B7PjP%2B3IS7Wg%3D%3D%3B16%22%2C%22b9%22%3A%22fBReJrFy%2BqxNzg%3D%3D%3B17%22%2C%22c1%22%3A%22FrsPKw%3D%3D%3B18%22%2C%22c2%22%3A%228rgt3%2Bxmz70bdR%2B8ApNq1w%3D%3D%3B19%22%2C%22c3%22%3A%22jcfahT600yZWNmtaVNbJ%2Bg%3D%3D%3B20%22%2C%22c4%22%3A%22hz9PGm7zRqI%3D%3B21%22%2C%22c5%22%3A%22EcnEFF%2Bu2WI%3D%3B22%22%2C%22c6%22%3A%22WvWcSw%3D%3D%3B23%22%2C%22c7%22%3A%22x6Ra%2FRhli%2FA%3D%3B24%22%2C%22c8%22%3A%22UUIprAMymVg%3D%3B25%22%2C%22c9%22%3A%22R2ZYr5znmBY%3D%3B26%22%2C%22d1%22%3A%22Azju9dsNOgKE04LEaGDC5srIampeh2nXx8sxzjdyO3P%2BVQ96%2F0FjypyywMhFqfdmU57%2Ff%2F2%2B%3B27%22%2C%22d2%22%3A%222Aw%3D%3B28%22%2C%22d3%22%3A%22esTCve6%2Bxlqdww%3D%3D%3B29%22%2C%22d4%22%3A%22vzQwqm%2F0Cq4%3D%3B30%22%2C%22d5%22%3A%22mNf3DQfycU6I0Q%3D%3D%3B31%22%2C%22d7%22%3A%22yq5ueJvFttY%3D%3B32%22%2C%22d8%22%3A%22c8LiyjRnNHrRtG9gDreli%2FOxZTwc4QVlZVQ%3D%3B33%22%2C%22d9%22%3A%22b3chKln6KLw%3D%3B34%22%2C%22e1%22%3A%22VjpI6zUppwSMCQ%3D%3D%3B35%22%2C%22e2%22%3A%22o1LsPcu1pjO4sg%3D%3D%3B36%22%2C%22e3%22%3A%22UyM5EycsairniA%3D%3D%3B37%22%2C%22e4%22%3A%22cI8%2BXt%2BNOWU%3D%3B38%22%2C%22e5%22%3A%2212aPJcE%2FApt0FA%3D%3D%3B39%22%2C%22e6%22%3A%22EGGpYZAenqQ%3D%3B40%22%2C%22e7%22%3A%22buzukuLOWs8%3D%3B41%22%2C%22e8%22%3A%220vqUgDCJfYg%3D%3B42%22%2C%22e9%22%3A%2285EIpGN%2Fqv8%3D%3B43%22%2C%22f1%22%3A%22M0K8TN%2F0zQqSPw%3D%3D%3B44%22%2C%22f2%22%3A%22oxvlYYCXu%2BY%3D%3B45%22%2C%22f3%22%3A%22sBYxuOhDTELbtw%3D%3D%3B46%22%2C%22f4%22%3A%22NFdTwmg7OWQ%3D%3B47%22%2C%22f5%22%3A%22S0UsgpxGbcbx9w%3D%3D%3B48%22%2C%22f6%22%3A%22urgiZgqizg9RBQ%3D%3D%3B49%22%2C%22f7%22%3A%22SLTdh02GFE4z%2Bw%3D%3D%3B50%22%2C%22f8%22%3A%22rurc%2FiQ%2BxqO28w%3D%3D%3B51%22%2C%22f9%22%3A%22XvmymwYLvOI%3D%3B52%22%2C%22g1%22%3A%22guEh3AVDNCc%3D%3B53%22%2C%22g2%22%3A%22PdLibqJQdwK3AA%3D%3D%3B54%22%2C%22g3%22%3A%22X626KYPBWoo%3D%3B55%22%2C%22g4%22%3A%22fBVzAB29Z20%3D%3B56%22%2C%22g5%22%3A%22wpEoUJHXMYk%3D%3B57%22%2C%22g6%22%3A%224SBmKzREZ85KAA%3D%3D%3B58%22%2C%22g7%22%3A%22VRXSywzBIl8%3D%3B59%22%2C%22g8%22%3A%222srh9cL2%2BlQ%3D%3B60%22%2C%22g9%22%3A%22lJ9%2Bgmzlf%2BA%3D%3B61%22%2C%22h1%22%3A%22cVIJgdLtaZvlvw%3D%3D%3B62%22%2C%22h2%22%3A%226SoC59c03CwfVQ%3D%3D%3B63%22%2C%22h3%22%3A%222I63OQqXi6GblQ%3D%3D%3B64%22%2C%22h4%22%3A%22CjhJ1wQrRgTbnA%3D%3D%3B65%22%2C%22h5%22%3A%22J4wxeXg5YXA%3D%3B66%22%2C%22h6%22%3A%22YIuFXNsDKqHKcA%3D%3D%3B67%22%2C%22h7%22%3A%22H6clnynX4v7TSraBaQ5m%2BjcEtJb4MXr9bc0eksR2M0ZGNTPhtrB%2FbUKQDNKHWf7H2APYBU7fLqadi1K1tgmADFqnKJ8p1%2FX%2Bh0r0gXwOffozBIyWuTFq%2FWfNFZLUdmpGDzV84aGwPm1HkA3Skln2x50D2gVF32CmiIsctf8JgQxMpyefPtfw%2FpJKt4FtDjX6EwSNlv0xZ%2F1nzTOSyHYkRhU1duGtsGptAJA%3D%3B68%22%2C%22h8%22%3A%22UUmFrngPeg%2BMQw%3D%3D%3B69%22%2C%22h9%22%3A%22dCdirpa4BIVPlA%3D%3D%3B70%22%2C%22i1%22%3A%22PlOVN%2Fiugiw%3D%3B71%22%2C%22i2%22%3A%22sF83ClJYEZL0mQ%3D%3D%3B72%22%2C%22i3%22%3A%22WBpMVA0n%2FO4FuA%3D%3D%3B73%22%2C%22i4%22%3A%22mgvMMZKx%2Fag17A%3D%3D%3B74%22%2C%22i5%22%3A%225bW%2FmZYafAN0kg%3D%3D%3B75%22%2C%22i6%22%3A%2263%2FGWA%3D%3D%3B76%22%2C%22z1%22%3A%22OmoTtnjLPda3POop7n2Me%2F8TGb%2Fx4rcI5aR5q0T67VuEZaKvTnbmZowdcb0ZW7Wt6CyRZ0z0kFMFZ4bS0wIXmQ%3D%3D%3B77%22%2C%22z2%22%3A%22TTA49P1bq1bjESphmwIA8ONWYAybQsgknEiUcy%2Byeqn9D1vy0A9OcdmwpCHpR9yX4kZ0Eo%2Bp7nGVx9cr6XnhvA%3D%3D%3B78%22%2C%22z3%22%3A%22iXrkGKAJ10Z5jA%3D%3D%3B79%22%2C%22z6%22%3A%22MsqG18CO8ZzsLWLX%3B80%22%2C%22z7%22%3A%22IeQ8PYvpOqx8tWxa%3B81%22%2C%22z8%22%3A%22DhGySKiQQb1h1xYv%3B82%22%2C%22z9%22%3A%22JurdMmihm6Nkcw%3D%3D%3B83%22%2C%22y1%22%3A%22P5uhs9U1G92zxg%3D%3D%3B84%22%2C%22y2%22%3A%22F57%2BpGq3nXSEhg%3D%3D%3B85%22%2C%22y3%22%3A%22eUp6qM%2FhHto7QA%3D%3D%3B86%22%2C%22y4%22%3A%22%2B%2FbrKOPq5Vjipg%3D%3D%3B87%22%2C%22y5%22%3A%22za6kb6HcbdjdnA%3D%3D%3B88%22%2C%22y6%22%3A%22YfICKaXbJlFGlA%3D%3D%3B89%22%2C%22y7%22%3A%22%2ByRJP%2BXQ5MRbfy3c%3B90%22%2C%22y8%22%3A%22bAn4NcTXWmXccQ%3D%3D%3B91%22%2C%22y9%22%3A%22BkfECVDBP4yYtg%3D%3D%3B92%22%2C%22y10%22%3A%22ng1cFiEa4suqJQ%3D%3D%3B93%22%2C%22x1%22%3A%22wH5tri1QnJybYg%3D%3D%3B94%22%2C%22x2%22%3A%22KXGS4Oia4%2BT0TQ%3D%3D%3B95%22%2C%22x3%22%3A%22cip%2FKHCSIcawLg%3D%3D%3B96%22%2C%22x4%22%3A%22YIiajv4GS9Xcwg%3D%3D%3B97%22%2C%22x5%22%3A%22SlUmsdDsAVsql35l%3B98%22%2C%22z5%22%3A%22Mam3fzuc1ak%3D%3B99%22%2C%22z4%22%3A%22HEDqcqhZvrtWDIKtJ5o%3D%3B100%22%2C%22v%22%3A%226.3.1%22%2C%22pgrdt%22%3A%225AgJnauOfBXoydCXbNoBxbTikqo%3D%3B101%22%2C%22pgrd%22%3A%229JlbyT%2Bh%2FZOPECg4KvtYLjkDJctbDFpu4pJtnKUoXPPNkbjY4%2F1OL7mDE8mvE%2Fs%2FAM0EdKNZuiEkaqBODDz2T%2FqV3%2BKw3%2BD0TpNKue4b1UC%2Bf7oha0UTVAHxhT%2FrQG35M9V3exII3cidXwfSr5FaGHiauKQOhzfYYVxjkt8qYRnkhHJ3SLPZHfSQCHLUShI7wl63ybvT%2FdMI0vEE6QHvFhEFRwY%3D%22%7D&key="

#sess=requests.Session()
re=requests.post("https://captcha-api.yandex.ru/check?host=captcha-api.yandex.ru", text2, timeout=3000)
print(re.status_code)
print("Запрос на получение капчи:"+re.text)



time.sleep(5)
fulltext=re.json()
key=fulltext['captcha']
key1=key['key']
result=text3+key1+"&"+text2+lang
re1=requests.post("https://captcha-api.yandex.ru/check?host=lkdr.nalog.ru", result)
print(re1.status_code)
print("Запрос на прохождение капчи"+re1.text)
st=re1.json()
status=st['spravka']
print(status)


phone=input()
time.sleep(15)
data={"phone":phone}#"deviceInfo":{"sourceDeviceId":"96TiSsdia-qAqHCdbqhRf","sourceType":"WEB","appVersion":"1.0.0","metaDetails":{"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57"}}}
data["captchaToken"]=status
     #{"phone":"79777148592","deviceInfo":{"sourceDeviceId":"96TiSsdia-qAqHCdbqhRf","sourceType":"WEB","appVersion":"1.0.0","metaDetails":{"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57"}}}
data={'phone':phone,'captchaToken':status, 'deviceInfo':{'sourceDeviceId':'_rxU_5F6x0gco4fwHULIZ','sourceType':'WEB','appVersion':'1.0.0','metaDetails':{'userAgent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0'}}}
#print(type(data))
print(data)
json_obj=json.dumps(data)
print(type(json_obj))
re2=requests.post("https://lkdr.nalog.ru/api/v2/auth/challenge/sms/start", json=data)
print(re2.status_code)
print(re2.text)





code=input("Введи код из смс")
verify={"challengeToken":"bbd8f9b1-30f5-4bf0-bf17-11cce4e81b70","phone":"79777148592","code":code}#"deviceInfo":{"sourceDeviceId":"_rxU_5F6x0gco4fwHULIZ","sourceType":"WEB","appVersion":"1.0.0","metaDetails":{"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0"}}}
re3=requests.post("https://lkdr.nalog.ru/api/v1/auth/challenge/sms/verify" )
#,"captchaToken":status,"deviceInfo":{"sourceDeviceId":"_rxU_5F6x0gco4fwHULIZ","sourceType":"WEB","appVersion":"1.0.0","metaDetails":{"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0"}}


"""



