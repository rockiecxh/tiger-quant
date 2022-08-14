from futu import *


if __name__ == '__main__':
    SysConfig.set_client_info("MyFutuAPI", 0)
    SysConfig.set_proto_fmt(ProtoFMT.Protobuf)
    quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
    quote_ctx.close()