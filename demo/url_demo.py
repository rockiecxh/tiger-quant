import requests
import urllib3

if __name__ == '__main__':
    requests.packages.urllib3.disable_warnings()

    url = 'https://www.futunn.com/quote-api/get-kline?stock_id=206370&market_type=2&type=3'
    http = urllib3.PoolManager()
    # r = http.request('GET', 'https://api.investing.com/api/financialdata/6408/historical/chart/?interval=P1W&pointscount=120')
    # r = requests.get(url, verify=False)
    # print(r.content)

    headers = {
        'authority': 'www.futunn.com',
        'method': 'GET',
        'path': '/quote-api/get-kline?stock_id=206370&market_type=2&type=3',
        'scheme': 'https',
        'accept': 'application / json, text / plain, * / *',
        'futu-x-csrf-token': 'JwIN6r9LXoElwIrywdohqA==-r42haXguKjR91EyI5L+C53kYQEI=',
        'cookie': 'cipher_device_id=1587611063160717; device_id=1587611063160717; FUTU_TOOL_STAT_UNIQUE_ID=15943941010357975; _ga_XG64WM4H33=GS1.1.1621604419.13.1.1621606167.0; _gcl_au=1.1.131945464.1658052516; _fbp=fb.1.1658052516789.1443890330; _csrf=mfm3UCzOlHOUkzjETACktiXjEuLapjXT; Hm_lvt_f3ecfeb354419b501942b6f9caf8d0db=1659835793; futunn_lang=zh-CN; PHPSESSID=mjlepl3hiboitb0klvslk56hd0; _uetvid=71965bb0cd0811eb854cf34de2c9fd0b; _ga_K1RSSMGBHL=GS1.1.1659836517.6.1.1659836619.0; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22ftv1AtuTPV8fiWrU1ao6rxQ3VY7c%2Fzedl%2Bkg2S5kgqMo8TMMeDVj1fGqVhyRr%2BIrBSKx%22%2C%22%24device_id%22%3A%22171a4fe420474f-0bbb721c1e21f-30657701-1296000-171a4fe4205764%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com.hk%2F%22%2C%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%2C%22first_id%22%3A%22ftv1AtuTPV8fiWrU1ao6rxQ3VY7c%2Fzedl%2Bkg2S5kgqMo8TMMeDVj1fGqVhyRr%2BIrBSKx%22%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTgyMGJhMGY5YTcyMTMtMDJhZTU2MWIxYzI5ZGJlLTFjNTI1NjM1LTEyOTYwMDAtMTgyMGJhMGY5YThhZTEiLCIkaWRlbnRpdHlfbG9naW5faWQiOiJmdHYxQXR1VFBWOGZpV3JVMWFvNnJ4UTNWWTdjL3plZGwra2cyUzVrZ3FNbzhUTU1lRFZqMWZHcVZoeVJyK0lyQlNLeCJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22ftv1AtuTPV8fiWrU1ao6rxQ3VY7c%2Fzedl%2Bkg2S5kgqMo8TMMeDVj1fGqVhyRr%2BIrBSKx%22%7D%7D; Hm_lpvt_f3ecfeb354419b501942b6f9caf8d0db=1659851337; tgw_l7_route=95db51d9431dfc9dd9b07b93baf6d779; locale=zh-cn; quote-csrf=5Z5syhkSKWFGUTlx4WH7mQrBdR0=; _gid=GA1.2.858906291.1660053513; _gat_UA-71722593-3=1; _ga_EJJJZFNPTW=GS1.1.1660053516.7.1.1660053521.0; _ga=GA1.1.605114244.1608431796; _ga_XECT8CPR37=GS1.1.1660053516.3.1.1660053521.0'

    }
    response = requests.get(url=url, headers=headers, verify=False)
    print(response.text)
