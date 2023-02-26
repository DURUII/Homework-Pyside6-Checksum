from checksum.utils.static import String


def decode(key2bit: dict[str, int], key2val: dict[str, str], key2dec: dict):
    assert set(key2dec.keys()).issubset(key2val.keys()), "weird explainer"

    key2exp = key2val.copy()

    for key in key2dec.keys():
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

    for key in hex2type.keys():
        if int(stream_hex, 16) == int(key, 16):
            return hex2type[key]

    return None


def type_protocol(stream_hex):
    int2type = {
        '6': String.tcp,
        '17': String.udp,
    }

    for key in int2type.keys():
        if int(stream_hex, 16) == int(key, 10):
            return int2type[key]

    return None
