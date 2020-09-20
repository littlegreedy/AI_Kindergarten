import requests
import json
import base64

# coding=utf-8
class Face_comparison:
    def __init__(self, pt, pt1):
        self.img = pt
        self.img1 = pt1
        self.headers = {"Content-Type": "application/json;charset = UTF-8"}

    def access_Token(self):
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + self.AK + '&client_secret=' + self.SK
        response = requests.get(host, headers=self.headers)
        json_result = json.loads(response.text)
        # print(json_result['access_token'])
        return json_result['access_token']

    def base64_Img(self, img, img1):
        with open(img, 'rb') as p:
            pic = base64.b64decode(p.read())
            self.tryDecode(pic)  # 默认用 UTF-8 进行解码
            self.tryDecode(pic, "ascii")  # 尝试用 ASCII 进行解码
            self.tryDecode(pic, "GB2312")  # 尝试用 GB2312 进行解码
            print(pic)

            #print(pic.decode( ))

    def tryDecode(s, decoding="utf-8"):
        try:
            print(s.decode(decoding))
        except UnicodeDecodeError as err:
            print(err)


        with open(img1, 'rb') as p1:
            pic1 = base64.b64decode(p1.read())
            print("------------------------------")
            print(pic1)
            print("------------------------------")
        post_data = [{"image": str(pic, 'utf-8'),
                      "image_type": "BASE64",
                      "face_type": "CERT"},
                     {"image": str(pic1, 'utf-8'),
                      "image_type": "BASE64",
                      "face_type": "LIVE"
                      }]
        return post_data

    def gan(self):
        data = self.base64_Img(pt, pt1)
        request_url = "https://aip.baidubce.com/rest/2.0/face/v3/match"
        access_token = self.access_Token()
        request_url = request_url + "?access_token=" + access_token
        print("------------------------------")
        print(data)
        print("------------------------------")
        response = requests.post(url=request_url, data=data, headers=self.headers)
        json_result = json.loads(response.text)
        # print(json_result['result'])

    def jjj(self):
        # encoding:utf-8
        import urllib.request
        import json
        import base64
        import tkinter.messagebox
        import ast

        '''
        人脸对比
        '''
        request_url = "https://aip.baidubce.com/rest/2.0/face/v3/match"
        filename1 = '1.jpg'
        filename2 = '1.jpg'
        f = open(filename1, 'rb')
        f2 = open(filename2, 'rb')
        img_test1 = base64.b64encode(f.read())
        img_test2 = base64.b64encode(f2.read())

        params = json.dumps(
            [{"image": '' + str(img_test1, 'utf-8') + '', "image_type": "BASE64", "face_type": "LIVE",
              "quality_control": "LOW"},
             {"image": '' + str(img_test2, 'utf-8') + '', "image_type": "BASE64", "face_type": "IDCARD",
              "quality_control": "LOW"}])
        # params=urlencode(params)
        #access_token = '这里需要你自行填入'
        request_url = request_url + "?access_token=" + self.access_Token()
        request = urllib.request.Request(url=request_url, data=params.encode("utf-8"))
        request.add_header('Content-Type', 'application/json')
        response = urllib.request.urlopen(request)
        content = response.read()
        if content:
            print(content)
        content = content.decode("utf-8")
        content = ast.literal_eval(content)
        print(content['result']['score'])
        tkinter.messagebox.showinfo('图片相似度', "两个人的相似度为：%d" % content['result']['score'] + "%")
#        if json_result:
#           print(json_result['result']['score'])
#           print(json_result['face_list'])
#
if __name__ == '__main__':
    pt = "1.jpg"
    pt1 = "1.jpg"
    b=Face_comparison(pt, pt1)
    b.jjj()
    #baiduDetect = Face_comparison(pt, pt1)
    #baiduDetect.gan()
