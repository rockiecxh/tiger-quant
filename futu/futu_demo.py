import json
import logging
import time

import akshare as ak
from browsermobproxy import Server
from pandas import DataFrame
from pandas.io.json import json_normalize
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from lib.pandas import tuple_2_md5, read_pd_from_cache, write_pd_2_cache
from week_line_overlay import week_line_overlay_plot

"""
def crawl_stock_list(self, _browser: WebDriver, ) -> DataFrame:
    _url = 'https://www.futunn.com/stock/MVIS-US'
    _browser.get(_url)
    time.sleep(3)

    # _stock_list = []
    # _url_list = []
    # stock_elements = _browser.find_elements_by_xpath("//*[contains(@class, 'plusIconTd')]/a")
    # for element in stock_elements:
    #     _tab_url = element.get_attribute('href')
    #     _url_list.append(_tab_url)

    # _option = Select(_browser.find_element_by_id('stocksFilter'))
    # for i in range(1, 4):
    #     _option.select_by_index(i)
    #     time.sleep(4)
    #     stock_elements = _browser.find_elements_by_xpath("//*[contains(@class, 'plusIconTd')]/a")
    #     for element in stock_elements:
    #         _tab_url = element.get_attribute('href')
    #         _url_list.append(_tab_url)

    for _tab_url in _url_list:
        _browser.execute_script("window.open('" + _tab_url + "', '_blank').focus();")

        windows = _browser.window_handles

        time.sleep(2)
        _browser.switch_to.window(windows[1])

        _stock = self.crawl_base_info(_browser)
        try:
            _stock_service.save(_stock)
        except Exception as e:
            logging.error('Save single stock error', e)

        _stock_list.append(_stock)

        _browser.close()
        _browser.switch_to.window(windows[0])

    return _stock_list
"""


def futu_data() -> DataFrame:
    # proxy
    server = Server('/Users/andrew/Downloads/browsermob-proxy-2.1.4/bin/browsermob-proxy')
    server.start()
    proxy = server.create_proxy()
    print('proxy', proxy.proxy)

    chrome_options = Options()
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--proxy-server={0}'.format(proxy.proxy))
    chrome_options.add_argument('auto-open-devtools-for-tabs')
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    browser.maximize_window()

    base_url = 'https://www.futunn.com/stock/MVIS-US'
    proxy.new_har(options={
        'captureContent': True,
        'captureHeaders': True
    })

    browser.get(base_url)

    browser.find_elements_by_xpath("//*[contains(text(), '周K')]")[0].click()

    time.sleep(3)

    result = proxy.har
    json_data = None

    for entry in result['log']['entries']:
        json_url = entry['request']['url']

        logging.info('json url: %s', json_url)
        if json_url.startswith('https://www.futunn.com/quote-api/get-kline'):
            json_data = entry['response']['content']['text']
            logging.info("Weekly data: %s", json_data)

    if json_data is None:
        return None

    dict = json.loads(json_data)
    df = DataFrame.from_dict(dict['data']['list'])
    return df


def get_daily_from_cache(stock_code) -> DataFrame:
    md5 = tuple_2_md5([stock_code])
    # 从文件缓存获取数据
    data = read_pd_from_cache(md5)

    if data is None:
        # data = ak.stock_us_daily(symbol="AAPL", adjust="")
        data = futu_data()

        if not data.empty:
            write_pd_2_cache(data, md5)

    return data


def download_wrap(stock_code):
    data = get_daily_from_cache(stock_code=stock_code)
    # data.index.rename('date', 'time')
    data['symbol'] = stock_code
    data['time'] = data['k']
    data['open'] = data['o']
    data['close'] = data['c']
    data['high'] = data['h']
    data['volume'] = data['v']
    return data


if __name__ == '__main__':
    # aapl = download_wrap('AAPL')
    # aapl = aapl.append(download_wrap('BA'))
    # aapl = aapl.append(download_wrap('TSM'))
    #
    # print(aapl)

    data = download_wrap('AAPL')
    week_line_overlay_plot(data, ['AAPL'])

