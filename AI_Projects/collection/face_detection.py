
import requests
import json
import base64

#截图嵌套使用
class Face_detection:
    def __init__(self,pt):
        self.AK = 'cvoEh4L8cvUDZLO1Hc2HoLBH'
        self.SK = '0XdWfNEi26aLtzztD8sgle5hyyOYo8rG' 
        self.img = pt
        self.headers = {"Content-Type":"application/json;charset = UTF-8"}
    def access_Token(self):
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+self.AK+'&client_secret='+self.SK
        response = requests.get(host,headers = self.headers)
        json_result = json.loads(response.text)
        #print(json_result['access_token'])
        return json_result['access_token']

    def base64_Img(self,img):
        p = open(img,'rb')
        p_base64_Data = base64.b64encode(p.read())
        return p_base64_Data
    def gan(self):
        img_Base64 = self.base64_Img(self.img)
        request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
        post_data = {
                "image":img_Base64,
                "image_type":"BASE64",
                "face_field":"expression,quality,emotion",
                "max_face_number":1,
                "face_type":"LIVE"
               }
        access_token = self.access_Token()
        request_url = request_url+"?access_token="+access_token
        response = requests.post(url = request_url,data = post_data,headers = self.headers)
        json_result = json.loads(response.text)
        return json_result
    

#json_result=json.loads(response.text)
#print(json_result)

