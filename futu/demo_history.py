from futu import *

from lib.chart import PlotDateType
from line_overlay import line_overlay_plot, line_overlay_plot_futu

quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
# 'HK.00700'
ret, data, page_req_key = quote_ctx.request_history_kline('US.BA', start='2019-09-11', end='2019-11-18', max_count=100)  # 每页5个，请求第一页
if ret == RET_OK:
    print(data)
    print(data['code'][0])    # 取第一条的股票代码
    print(data['close'].values.tolist())   # 第一页收盘价转为 list
else:
    print('error:', data)
while page_req_key != None:  # 请求后面的所有结果
    print('*************************************')
    ret, data, page_req_key = quote_ctx.request_history_kline('HK.00700', start='2019-09-11', end='2019-10-18', max_count=5, page_req_key=page_req_key) # 请求翻页后的数据
    if ret == RET_OK:
        print(data)
    else:
        print('error:', data)
print('All pages are finished!')
quote_ctx.close() # 结束后记得关闭当条连接，防止连接条数用尽

# FIXME 用对数坐标替换
line_overlay_plot_futu(data, ['HK.00700'], PlotDateType.MONTH)
