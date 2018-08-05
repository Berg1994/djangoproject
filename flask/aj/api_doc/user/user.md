#### 请求地址

> POST /user/register/

#### `request params`

- mobile str '手机号'
- imagecode str '验证码'
- passwd str '密码1'
- passwd2 str '确认密码2'

#### `response params`

- 失败响应 ： {’code':1000,'msg':验证码错误} 

  {'code':1001,'msg':'请填写完整参数'}

- 成功响应： {'code':200，'msg':'请求成功'}

- msg str '响应信息'

- code int '状态码'

  