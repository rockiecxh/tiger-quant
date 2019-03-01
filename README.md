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

#####ETF价格叠加图
~~~
python line_overlay.py
~~~
![Alt text](/test/1.png "ETF价格叠加图")

#####ETF累计收益率
~~~
python yield_rate.py
~~~
![Alt text](/test/2.png "ETF累计收益率")

#####以SPY为基准的线性回归
~~~
python stock_relation.py
~~~
![Alt text](/test/3.png "以SPY为基准的线性回归")