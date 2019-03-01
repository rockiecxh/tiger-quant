# tiger-quant 是根据老虎量化平台的数据来做一些简单的指数分析案例

#####1、如何配置
~~~
# 新建配置文件
~/config/env.properties

# 老虎量化平台ID与账号
tiger_id=xxx
tiger_account=xxx
~~~

#####老虎开放平台私钥路径
~~~
~/.ssh/tigerbroker_rsa_private_key.pem
~~~

#####2、如何使用

#####获取指定代码的相关系数并以热力图的方式展现
~~~
python correlation_coefficient.py
~~~

#####ETF价格叠加图
~~~
python line_overlay.py
~~~
![Alt text](/test/1.png "ETF价格叠加图")