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
- 安卓前端在获取用户输入的注册信息后，需检验各项信息是否非空，手机号格式是否正确（应为11位），同时要对密码进行加密后再传输。加密代码可参考如下：

```
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

   /**
     * 使用MD5算法加密字符串
     * @param string 待加密字符串，如用户登录密码
     * @param slat 盐值
     * @return MD5算法加密后对应的16进制字符串，长度为32
     */
    public static String md5(String string, String slat) {
        MessageDigest md5 = null;
        try {
            md5 = MessageDigest.getInstance("MD5");

            // 加盐值的目的是为加大MD5破解的难度，提高安全性。
            byte[] bytes = md5.digest((string + slat).getBytes());

            String result = "";

            // 将bytes数组中的每个数据转成对应16进制的字符串，方便显示
            // 注： 若直接使用new String(byte[] b)，则得到的字符串会存在乱码
            for (byte b : bytes) {
                // 当byte数据向上转型为int型时，java会默认保持高位不变。
                // 所有对于负数，转型后高24位就会全补1，造成结果错误。所以要通过& 0xff运算来将高24位置0。
                String temp = Integer.toHexString(b & 0xff);

                // 保证每个byte数据都转成两位字符串，使得最后对应的16进制字符串为长度为32
                if (temp.length() == 1) {
                    temp = "0" + temp;
                }
                result += temp;
            }
            return result;
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        }
        return "";
    }
```
另：关于MD5相关介绍可参考https://github.com/NAMZseng/Notes/blob/master/%E5%85%B6%E4%BB%96/MD5%E7%AE%97%E6%B3%95.md

### 返回值

-1：昵称已被注册 <br>
-2：手机已被注册 <br>
0：注册成功

