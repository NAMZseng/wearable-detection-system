# wearable-detection-backend 后端API

## 统一说明

所有API接口均为POST方式，同时需在HTTP头字段设置conten-type为JSON格式
- Content-Type: application/json;charset=UTF-8


## 获取血压预测值

### URL

http://10.1.89.11:8000/api/get_bp_predict/

### 传参

```json
{
    "ecg":[1.05518648,1.07711683,1.06342479, ......],
    "ppg":[1.05831795,1.05752789,1.05436850, ......]
}
```
注：ecg，ppg各有625条，具体示例数据见文件test_data.csv

### 返回值

```json
{
  "SBP":134,
  "DBP":84
}
```


## 用户注册

### URL
http://10.1.89.11:8000/api/register/

### 传参

```json
{
  "username":"user_test",
  "phone":18406580000,
  "password":"xxxx",
  "sex":"male",
  "birthday":"2021-07-13"
}
```
注：
- sex设置的可选值为 “male” 和 “female”
- 安卓前端在获取用户输入的注册信息后，需检验各项信息是否非空，手机号格式是否正确（应为11位），同时要对密码进行加密传输

### 返回值

-1：昵称已被注册 <br>
-2：手机已被注册 <br>
0：注册成功

