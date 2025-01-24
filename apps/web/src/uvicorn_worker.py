from uvicorn_worker import UvicornWorker


class CustomUvicornWorker(UvicornWorker):
    CONFIG_KWARGS = {
        "proxy_headers": True,
        "forwarded_allow_ips": "*"
    }