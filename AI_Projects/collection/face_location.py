

import requests
import json
import base64
import cv2

from collection.face_detection import Face_detection
from collection.face_comparison import Face_comparison
from collection.queryImp import Query,Cha,Op,Cl
from collection.B_P import b_p



class Face_location:
    def __init__(self,p,pt):
        self.AK = 'ePpG0hWbFmPsKdYXGKPaVWOn'
        self.SK = '7izxOMFcUyTn3wcOfUwyoavhqt0zRrFj'
        self.p = p
        self.img = pt
        self.headers = {"Content-Type":"application/json;charset = UTF-8"}
        self.h='127.0.0.1'
        self.user='root'
        self.password='1000'
        self.port=3308
        self. db='ssms'
    def access_Token(self):
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+self.AK+'&client_secret='+self.SK
        response = requests.get(host,headers = self.headers)
        json_result = json.loads(response.text)
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
                "face_field":"face_shape",
                "max_face_num":10,
                "face_type":"LIVE"
               }
        access_token = self.access_Token()
        request_url = request_url+"?access_token="+access_token
        response = requests.post(url = request_url,data = post_data,headers = self.headers)
        json_result = json.loads(response.text)
        return json_result
    
    
    
    
    def cut(self):
        db = Op(self.h,self.user,self.password,self.port,self.db)
        img = cv2.imread(self.p)
        ti=0
        c = self.gan()
        for i in c['result']['face_list']:
            left = i['location']['left']
            top = i['location']['top']
            wdlf = i['location']['width']+i['location']['left']
            hgtp = i['location']['height']+i['location']['top']
            
            l=int(left)
            t=int(top)
            w=int(wdlf)
            h=int(hgtp)
            w1=img.shape[1]-w
            h1=img.shape[0]-h
            
            ll=l-l*0.05
            tt=t-t*0.05
            ww=w+w1*0.03
            hh=h+h1*0.03
            
            img = cv2.imread(self.img)
            
            first=img[int(tt):int(hh),int(ll):int(ww)]
            cv2.imwrite('cher.jpg',first)
            ps = "cher.jpg"
            q_result = Query(db)
            t=13
            #time()
            for a in range(0,t): 
                #读取数据库的图片
                ku = b_p(a,db)
                
                number = Face_comparison(ps,ku)
                n = number.gan()
            
                if n >= 97:
                    detection = Face_detection(ps)
                
                    try:
                        result = detection.gan()
                        ex = result['result']['face_list'][0]['emotion']['type']
                        nu = q_result[a][0]
                        ti = Cha(db,ex,nu,ti)
                    except Exception:
                        print("识别不出来")
                        
                else:
                    continue
            
        for i in c['result']['face_list']:
            left = i['location']['left']
            top = i['location']['top']
            wdlf = i['location']['width']+i['location']['left']
            hgtp = i['location']['height']+i['location']['top']
            
            l=int(left)
            t=int(top)
            w=int(wdlf)
            h=int(hgtp)
            w1=img.shape[1]-w
            h1=img.shape[0]-h
            
            ll=l-l*0.05
            tt=t-t*0.05
            ww=w+w1*0.03
            hh=h+h1*0.03
            
            img = cv2.imread(self.img)
            
            cv2.rectangle(img,(int(ll),int(tt)),(int(ww),int(hh)),(0,255,0),-1)
            cv2.imwrite('time.jpg',img)
        print(ti)
        Cl(db)

        
        
#json_result=json.loads(response.text)
#print(json_result)

