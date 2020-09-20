import requests
import json
import base64
import urllib.request
# coding=utf-8
class Face_comparison:
    def __init__(self, pt, pt1):
        self.AK = 'pCsHtBtMhc9ncGzhAZ73Wy71'
        self.SK = 'zCkGWmlo9WHuNgUVvBKWVpKwvNzR5Gk7'
        self.img = pt
        self.img1 = pt1
        self.headers = {"Content-Type": "application/json;charset = UTF-8"}

    def access_Token(self):
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + self.AK + '&client_secret=' + self.SK
        response = requests.get(host, headers=self.headers)
        json_result = json.loads(response.text)
        # print(json_result['access_token'])
        return json_result['access_token']
    
    def base64_Img(self,pt,pt1):
        f = open(pt, 'rb')
        f2 = open(pt1, 'rb')
        img_test1 = base64.b64encode(f.read())
        img_test2 = base64.b64encode(f2.read())

        params = json.dumps(
            [{"image": '' + str(img_test1, 'utf-8') + '', "image_type": "BASE64", "face_type": "LIVE",
              "quality_control": "LOW"},
             {"image": '' + str(img_test2, 'utf-8') + '', "image_type": "BASE64", "face_type": "LIVE",
              "quality_control": "LOW"}])
        return params
    def gan(self):
           
        request_url = "https://aip.baidubce.com/rest/2.0/face/v3/match"
        # params=urlencode(params)
        #access_token = '这里需要你自行填入'
        params=self.base64_Img(self.img,self.img1)
        request = urllib.request.Request(url=request_url, data=params.encode("utf-8"))
        
        request.add_header('Content-Type', 'application/json')
        response = urllib.request.urlopen(request)
        
        access_token = self.access_Token()
        request_url = request_url+"?access_token="+access_token
        response = requests.post(url = request_url,data = params,headers = self.headers) 
        json_result = json.loads(response.text)
    
        if(json_result['error_msg'] ==  'SUCCESS'):
            return json_result['result']['score']
        else:
            print("对比失败，原因："+json_result['error_msg'])
            return 10
            

#       