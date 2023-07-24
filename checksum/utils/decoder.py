from checksum.utils.static import String


def decode(key2bit: dict[str, int], key2val: dict[str, str], key2dec: dict):
    assert set(key2dec.keys()).issubset(key2val.keys()), "weird explainer"

    key2exp = key2val.copy()

    for key in key2dec:
        key2exp[key] = key2dec[key](key2exp[key])

    return key2exp


# https://blog.csdn.net/weixin_43580872/article/details/118977590
def type_ethernet(stream_hex):
    hex2type = {
        '0x0800': String.ipv4,
        '0x0806': String.arp,
        '0x0835': String.rarp,
        '0x86DD': String.ipv6,
    }

    return next(
        (
            value
            for key, value in hex2type.items()
            if int(stream_hex, 16) == int(key, 16)
        ),
        None,
    )


def type_protocol(stream_hex):
    int2type = {
        '6': String.tcp,
        '17': String.udp,
    }

    return next(
        (
            value
            for key, value in int2type.items()
            if int(stream_hex, 16) == int(key, 10)
        ),
        None,
    )
