
import requests
from mysqltools import MysqlTools

 
u="http://haimo.testgoup.com/haimo/sass/systemUser/release/getLogin"
d={"userName":"admin","password":"e10adc3949ba59abbe56e057f20f883e"}
res=requests.post(url=u,json=d)
token=res.json()['data'][0]['token']

assert res.status_code==200
assert res.json()['msg']=='登录成功'
print(res.json()['msg'])

#新增用户
username="zhangsan18"
U='http://haimo.testgoup.com/haimo/sass/systemUser/addSystemUser'
h={'token':token}
d={'autograph': "http://heimerclin.oss-cn-chengdu.aliyuncs.com/upload/2022/5/8/e9545f94-6828-4f27-82ff-346249432c8c.jpeg",
'loginAccount': username,
'loginPassword': "260cae85918b63de23152cd0a68805f1",
'phone': "13666666668",
'realName': "pzzzz"}
res=requests.post(url=U,json=d,headers=h)
print(res.json())
assert res.json()['code']==1
print(res.json())



# sql='select * from  tb_system_user  where login_account="{}"'.format(username)
# q_res=MysqlTools().query(sql)
# print(q_res)
# assert len(q_res)!= 0
# print("添加用户成功")


#查询
# u1="http://haimo.testgoup.com/haimo/sass/systemUser/listSystemUser/1/10"
# d1={'loginAccount': "zhangsan13"}
# h1={'token':token}
# res=requests.post(url=u1,json=d1,headers=h1)
# print(res.json())

# assert res.status_code==200
# assert res.json()['code']== 1
