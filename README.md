# wearable-detection-backend 后端API

## 统一说明

所有API接口均为POST方式，同时需在HTTP头字段设置conten-type为JSON格式
- Content-Type: application/json;charset=UTF-8


## 获取血压预测值

### URL

http://10.1.89.11:8000/api/get_bp_predict/

### 传参
注：ecg，ppg各有625条，具体示例数据见文件test_data.csv

```json
{
    "ecg":[1.05518648,1.07711683,1.06342479, ......],
    "ppg":[1.05831795,1.05752789,1.05436850, ......]
}
```

### 返回值

```json
{
  "SBP":134,
  "DBP":84
}
```
