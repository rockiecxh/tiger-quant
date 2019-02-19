import os

from tigeropen.common.consts import Language
from tigeropen.common.util.signature_utils import read_private_key
from tigeropen.tiger_open_config import TigerOpenClientConfig


def get_client_config():
    """
    https://www.itiger.com/openapi/info 开发者信息获取
    :return:
    """
    is_sandbox = False
    client_config = TigerOpenClientConfig(sandbox_debug=is_sandbox)
    client_config.private_key = read_private_key(os.path.expanduser('~/.ssh/tigerbroker_rsa_private_key.pem'))
    client_config.tiger_id = '20150138'
    client_config.account = '20190130215629871'
    client_config.language = Language.en_US

    return client_config
