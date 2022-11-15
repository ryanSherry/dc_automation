# My Module
def format_proxy(proxy):
    proxy_parts = proxy.split(':')
    proxy_with_whitelist = {
        'proxy': {
            'https': 'https://{ip_address}:{port}'
            .format(ip_address=proxy_parts[0], port=proxy_parts[1])
        }
    }
    proxy_with_credentials = {
            'proxy': {
                'http': 'http://{user}:{password}@{ip_address}:{port}'
                        .format(user=proxy_parts[2], password=proxy_parts[3], ip_address=proxy_parts[0], port=proxy_parts[1]),
                'https': 'https://{user}:{password}@{ip_address}:{port}'
                .format(user=proxy_parts[2], password=proxy_parts[3], ip_address=proxy_parts[0], port=proxy_parts[1])
            }
    }

    if len(proxy_parts) <= 2:
        return proxy_with_whitelist
    else:
        print(proxy)
        return proxy_with_credentials