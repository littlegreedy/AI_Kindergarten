import configparser
import requests
import json
import base64
import os

cf = configparser.ConfigParser()
cpath = os.path.dirname(os.path.realpath(__file__))
cfgpath = os.path.join(cpath, "init.ini")
cf.read(cfgpath,encoding="utf-8")
sec = cf.sections()

class Body_detection:
    def __init__(self,pt):
        self.AK = cf.get("bd","bd_api")
        self.SK = cf.get("bd","bd_sdk")
        self.img = pt
        self.headers = {"Content-Type":"application/x-www-form-urlencoded;charset = UTF-8"}
    def access_Token(self):
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+self.AK+'&client_secret='+self.SK
        response = requests.get(host,headers = self.headers)
        json_result = json.loads(response.text)
        #print(json_result['access_token'])
        return json_result['access_token']
   
    def base64_Img(self,img):
        p = open(img,'rb')
        p_base64_Data = base64.b64encode(p.read())
        print(p_base64_Data)
        return p_base64_Data
    def gan(self):
        img_Base64 = self.base64_Img(self.img)
        request_url = "https://aip.baidubce.com/rest/2.0/video-classify/v1/body_danger"
        post_data = {"image":img_Base64}
        access_token = self.access_Token()
        request_url = request_url+"?access_token="+access_token
        response = requests.post(url = request_url,data = post_data,headers = self.headers)
        json_result = json.loads(response.text)
        print(json_result)
    
if __name__=='__main__':
    pt="1.jpg"
    #input("请输入图片途径：")
    baiduDetect=Body_detection(pt)   
    baiduDetect.gan()
#json_result=json.loads(response.text)
#print(json_result)

