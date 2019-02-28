import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels import regression


def normalize(df: pd.DataFrame, column: str):
    """
    数据归一化
    :param df: DataFrame
    :param column: 列名
    :return:
    """
    normalized_data = (df[column] - df[column].mean()) / df[column].std()
    normalized_data = normalized_data.values
    return normalized_data


def beta(market_returns: pd.DataFrame, stock_returns: pd.DataFrame):
    """
    计算 Beta 值, 最佳数据为4-6年的市场数据
    :param market_returns: 市场回报率
    :param stock_returns: 股票回报率
    :return: Beta值
    """
    covariance = np.cov(stock_returns, market_returns)
    beta_value = covariance[0, 1] / covariance[1, 1]
    return beta_value


def alpha_beta(market_returns: pd.DataFrame, stock_returns: pd.DataFrame):
    """
    计算 Alpha Beta 值, 最佳数据为4-6年的市场数据
    :param market_returns: 市场回报率
    :param stock_returns: 股票回报率
    :return: Alpha, Beta值
    """
    market_returns = sm.add_constant(market_returns)
    model = regression.linear_model.OLS(stock_returns, market_returns).fit()

    return model.params[0], model.params[1]


def log_return(begin_price: float, end_price: float):
    """
    计算对数收益率
    :param begin_price: 开始的价格
    :param end_price: 结束的价格
    :return: 对数收益率
    """
    return np.log(begin_price) - np.log(end_price)

