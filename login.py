from threading import Thread
import time
import requests
from io import BytesIO
import http.cookiejar as cookielib
from PIL import Image
from base64 import b64decode
import os

requests.packages.urllib3.disable_warnings()

class show_code(Thread):
    def __init__(self,data):
        Thread.__init__(self)
        self.data = data

    def run(self):
        img = Image.open(BytesIO(self.data))  # 打开图片，返回PIL image对象
        img.show()

def is_login(session):
    headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
    url = "https://www.ximalaya.com/revision/main/getCurrentUser"
    try:
        session.cookies.load(ignore_discard=True)
    except Exception:
        pass
    response  = session.get(url,verify=False,headers=headers)
    if response.json()['ret'] == 200:
        print(response.json())
        return session,True
    else:
        return session,False

def login():
    if not os.path.exists(".cookie"):
        os.makedirs('.cookie')
    if not os.path.exists('.cookie/xmly.txt'):
        print("hello")
        with open(".cookie/xmly.txt",'w') as f:
            f.write("")
    session = requests.session()
    session.cookies = cookielib.LWPCookieJar(filename='.cookie/xmly.txt')
    session,status = is_login(session)
    if not status:
        url = "https://passport.ximalaya.com/web/qrCode/gen?level=L"
        response = session.get(url,verify=False)
        data = response.json()
        # with open('qrcode.jpg','wb') as f:
            # f.write(b64decode(data['img']))
        t= show_code(b64decode(data['img']))
        t.start()
        qrId = data['qrId']

        url = 'https://passport.ximalaya.com/web/qrCode/check/%s/%s' % (qrId,int(time.time()*1000))
        while 1:
            response = session.get(url,verify=False)
            data = response.json()
            # code = re.findall("window.wx_code='(.*?)'",response.text)
            # sys.exit()
           
            if data['ret'] == 0:
                # for proc in psutil.process_iter():  # 遍历当前process
                    # try:
                    #     if proc.name() == "Microsoft.Photos.exe":  
                    #         proc.kill()  # 关闭该process
                    # except Exception as e:
                    #     print(e)
                break
            time.sleep(1)
        session.cookies.save()
    return session
if __name__ == '__main__':
    login()