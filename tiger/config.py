import os

from tigeropen.common.consts import Language
from tigeropen.common.util.signature_utils import read_private_key
from tigeropen.quote.quote_client import QuoteClient
from tigeropen.tiger_open_config import TigerOpenClientConfig
from properties.p import Property


def get_client_config():
    """
    https://www.itiger.com/openapi/info 开发者信息获取
    :return:
    """
    # Load tiger account information
    prop = Property()
    prop_loader = prop.load_property_files(os.path.expanduser('~/config/env.properties'))
    tiger_id = prop_loader.get('tiger_id')
    tiger_account = prop_loader.get('tiger_account')

    is_sandbox = False
    client_config = TigerOpenClientConfig(sandbox_debug=is_sandbox)
    client_config.private_key = read_private_key(os.path.expanduser('~/.ssh/tigerbroker_rsa_private_key.pem'))
    client_config.tiger_id = tiger_id
    client_config.account = tiger_account
    client_config.language = Language.en_US

    return client_config


def get_quote_client():
    """
    获取 QuoteClient
    :return: QuoteClient
    """
    config = get_client_config()
    quant_client = QuoteClient(config)

    return quant_client
