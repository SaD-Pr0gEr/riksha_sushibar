def parse_query_param_from_string(string: str) -> dict:
    params_raw = string.split('&')
    params = {}
    for param in params_raw:
        split_param = param.split('=')
        if len(split_param) == 2:
            params[split_param[0]] = split_param[-1]
    return params


def parse_query_params_from_url(url: str) -> dict:
    split_url = url.split('?')
    if len(split_url) != 2:
        return {}
    return parse_query_param_from_string(split_url[-1])


def fix_url_query_params(url: str, **query_params) -> str:
    host = url.split('?')[0]
    params = parse_query_params_from_url(url)
    params |= query_params
    return host + '?' + '&'.join((
        str(key) + '=' + str(value)
        for key, value in params.items()
    ))
