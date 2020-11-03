import requests, os
from ep import ep_decode
from pathDecode import path_decode
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from threading import Thread
from login import login

session = login()
# session = requests.session()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}


# http://audiofreepay.xmcdn.com 为不能用
# https://www.ximalaya.com/revision/play/v1/audio?id=258187832&ptype=1
# url = "https://mpay.ximalaya.com/mobile/track/pay/279998907/?device=pc"
# url = "https://mpay.ximalaya.com/mobile/track/pay/244130607/?device=pc"

# https://www.ximalaya.com/revision/play/v1/show?id=257754992&sort=0&size=30&ptype=1
class XiMaLaYa(object):
    def __init__(self, albumId):
        self.albumId = albumId
        self.t_list = []
        self.run_t = 7
        self.save_dir = "./downloads"
        self.start_index = 1
        self.get_detail()
        self.m4a_path = os.path.join(self.save_dir, 'm4a')
        self.mp3_path = os.path.join(self.save_dir, 'mp3')
        if not os.path.exists(self.m4a_path):
            os.makedirs(self.m4a_path)
        if not os.path.exists(self.mp3_path):
            os.makedirs(self.mp3_path)
        self.update_index()  # 更新开始位置
        self.get_tracks_list()
        for t in self.t_list:
            t.join()

        # self.convert()

    def update_index(self):
        index_list = [int(file.split('-')[0]) for file in os.listdir(self.m4a_path)]
        while True:
            if self.start_index in index_list:
                self.start_index += 1
            else:
                break
        print(self.start_index)

    def convert(self):
        for file in os.listdir(self.m4a_path):
            m4afile_path = os.path.join(self.m4a_path, file)
            mp3file_path = os.path.join(self.mp3_path, file.replace(".m4a", ".mp3"))
            command = 'ffmpeg.exe -y -i "%s" -ar 44100 -ac 2 -acodec mp3 "%s"' % (m4afile_path, mp3file_path)
            os.system(command)

    def get_detail(self):
        url = "https://www.ximalaya.com/revision/album?albumId=" + str(self.albumId)
        data = requests.get(url, verify=False, headers=headers).json()
        albumTitle = data['data']['mainInfo']['albumTitle'].replace('|', '-').replace(":", "-")
        self.save_dir = os.path.join(self.save_dir, albumTitle)
        detailRichIntro = data['data']['mainInfo']["detailRichIntro"]
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)
        # print(detailRichIntro)

    def get_tracks_list(self):
        albumId = self.albumId
        for pageNum in range(1, 10):
            url = "https://www.ximalaya.com/revision/album/v1/getTracksList?albumId=%s&pageNum=%s&pageSize=1000" % (
            albumId, pageNum)
            data = requests.get(url, headers=headers, verify=False).json()
            if data['ret'] == 200:
                if data['data']['tracks'] != []:
                    for trackItem in data['data']['tracks']:
                        if trackItem['index'] >= self.start_index:
                            self.get_m4a_url(trackItem)
                else:
                    break

    def get_m4a_url(self, trackItem):
        trackId = trackItem["trackId"]
        title = str(trackItem['index']) + "-" + trackItem['title']
        url = "https://mpay.ximalaya.com/mobile/track/pay/%s/?device=pc" % trackId
        data = session.get(url, verify=False).json()
        url = ''
        if data['ret'] == 0:
            # print("接口1")
            fileId = data['fileId']
            seed = data['seed']
            ep = data['ep']
            domain = data['domain']
            apiVersion = data['apiVersion']
            arg = ep_decode(ep)
            arg['duration'] = data['duration']
            filename = path_decode(seed, fileId)
            url = domain + '/download/' + apiVersion + "/" + filename + '?'
            for key, value in arg.items():
                url = url + key + '=' + str(value) + '&'
            else:
                url = url[:-1]
        else:
            print("接口2")
            url = "https://www.ximalaya.com/revision/play/v1/audio?id=%s&ptype=1" % trackId
            try:
                res = session.get(url, verify=False, headers=headers)
                data = res.json()
                url = data['data']['src']
            except Exception as e:
                print(Exception)
                print(url)
                print(res)
        if url == '' or url is None:
            print("收费资源，未能获取到下载url")
            return
        t = Thread(target=self.download_m4a, args=(url, title))
        t.start()
        self.t_list.append(t)
        if len(self.t_list) == self.run_t:
            for t in self.t_list:
                t.join()
            self.t_list = []

    def download_m4a(self, url, title):
        title = title.replace(" ", "-").replace('|', '-').replace(":", "-").replace("/", "-").replace("\\", "-")
        data = requests.get(url, verify=False).content
        filename = os.path.join(self.m4a_path, title + '.m4a')
        with open(filename, 'wb') as f:
            f.write(data)
        print(title)


if __name__ == '__main__':
    # ximalaya = XiMaLaYa(24495603) #鬼吹灯续·四部合集（周建龙）
    # ximalaya = XiMaLaYa(40121646) #三体（全集）| 有声小说，刘慈欣作品，王明军演播
    # ximalaya = XiMaLaYa(37881116) #生死禁地之香巴拉-周建龙播讲
    # ximalaya = XiMaLaYa(40544228) #捍宝|民国盗墓探险 抗日热血（周建龙播讲）
    # ximaLaya = XiMaLaYa(12169392) #末代土司
    # ximaLaya = XiMaLaYa(8274546) #周建龙演播-《五大贼王1-7合集》
    # ximalaya = XiMaLaYa(18995802) #张震讲故事·惊魂季I
    # ximalaya = XiMaLaYa(30355758) #张震讲故事·惊魂季 II | 全新作品
    # ximaLaya = XiMaLaYa(9287330) #周建龙演播——骗枭（单集版）
    # ximalaya = XiMaLaYa(10321421) #张居正 | 茅盾文学奖获奖作品，周建龙演播（单集版）
    # ximalaya = XiMaLaYa(20504282) #彩妆（演播：周建龙）
    # ximalaya = XiMaLaYa(13017183) #我闯入了疯子的世界-周建龙
    # ximalaya = XiMaLaYa(34220825) #遮天（辰东作品，头陀渊&小桃红精品双播）
    # ximalaya = XiMaLaYa(30816438) #三体（全六季）| 精品广播剧
    # ximalaya = XiMaLaYa(30575436) #活着（致敬经典-余华著，一种侃侃、一刀苏苏演播）
    # ximalaya = XiMaLaYa(22630007) #平凡的世界 | 路遥代表作，杨晨、张震演播
    # ximalaya = XiMaLaYa(7769841) #毛泽东与蒋介石
    # ximalaya = XiMaLaYa(35772167) #鬼吹灯 第二部 5-8卷丨周建龙（黄皮子坟等4本合集）
    ximalaya = XiMaLaYa(24495603)  # 马东
