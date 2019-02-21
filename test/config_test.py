from tigeropen.common.consts import BarPeriod

from lib.date import get_today, date_delta
from tiger.config import get_bars_from_cache


def test_get_bars_from_cache():
    stocks = ['QQQ', 'SPY', 'TLT', 'USO', 'IAU']

    data = get_bars_from_cache(None, symbols=stocks, period=BarPeriod.MONTH,
                               begin_time=get_today(), end_time=date_delta(-52 * 10))

    assert data is not None

