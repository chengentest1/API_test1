import json
import os

import requests
import xlrd

from jieko_modify.FileUtil import FileUtile
pa=os.path.dirname(os.path.dirname(__file__))
os.path.join(pa)

class HttpRquests:
    def sendGetRequest(self,url,args):
        resp=requests.get(url,args)
        return resp
    def sendPostRequest(self,url,data,headers):
        data = json.dumps(data)
        resp=requests.post(url,data,headers=headers)
        return resp

if __name__=="__main__":
    # kk = os.path.dirname(os.path.dirname(__file__))
    # filepath=kk+'/data_resource/user_data.xlsx'
    p=HttpRquests()
    # f=FileUtile(r'C:\Users\cheng\PycharmProjects\testAPI\data_resource\user_data.xlsx')
    f=FileUtile()
    h=f.read_excel_h_w()[0]
    w=f.read_excel_h_w()[1]
    for a in range(1,h):
        testName=f.read_excel(a,0)
        host=f.read_excel(a,1)
        path=f.read_excel(a,2)
        method=f.read_excel(a,3)
        type_text=f.read_excel(a,4)
        userName=f.read_excel(a,5)
        passwd=f.read_excel(a,6)
        excepted=f.read_excel(a,7)
        result=f.read_excel(a,8)
        status=f.read_excel(a,9)
        # url=host+path
        url='http://127.0.0.1:5000/api/user/reg/'
        if (method=='get'):
            str1=p.sendGetRequest(url,args=userName)
        if method.lower()=='post':
            if type_text=='json':
                headers={'content_type':'application/json'}
                data={"name":userName,'passwd':passwd}
                # data=json.dumps(data)
                # t=requests.post(url,data,headers=headers)
                t=p.sendPostRequest(url,data,headers)
                print(t.status_code)


                # str1=p.sendPostRequest(url,headers=headers,data=data)
                # print(str1.status_code)
                # print(url)
                # print(str1)
# h=FileUtile(r'C:\Users\cheng\PycharmProjects\testAPI\data_resource\user_data.xlsx')
# f=h.filepath
# print(f)