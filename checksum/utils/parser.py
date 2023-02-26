from checksum.utils.formatter import nip_prefix
from ..utils.static import String


def parse(key2bit: dict[str, int], stream: str, base: int):
    # 删前缀并检查
    stream = nip_prefix(stream, base)
    len_orig = len(stream)

    # 转换为二进制
    stream = bin(int(stream, base)) if base != 2 else stream
    stream = stream.lstrip("0b")

    # FIXME 补零（以原始长度测算）
    if base == 16:
        len_zeros = len_orig * 4 - len(stream)
        zeros = "".join(['0' for _ in range(len_zeros)])
        stream = zeros + stream

    # FIXME 补零（以现有长度测算）
    # if len(stream) % base != 0:
    #     len_zeros = (len(stream) // base + 1) * base - len(stream)
    #     zeros = ""
    #     for i in range(len_zeros):
    #         zeros = zeros + "0"
    #     stream = zeros + stream

    # 解析二进制流
    key2val = {}
    starter = 0

    # 用于置零校验位
    reset = 0

    for key in key2bit.keys():
        len_bit = key2bit[key]

        if key == String.checksum:
            reset = starter

        assert starter + len_bit <= len(stream), f"stream is inadequate for parsing"

        if len_bit > 0:
            key2val[key] = hex(int(stream[starter:starter + len_bit], 2))

        elif len_bit == -1:
            # 主要针对无数据部分的数据包
            if stream[starter:] != "":
                key2val[key] = hex(int(stream[starter:], 2))
            else:
                key2val[key] = None

        else:
            assert False, f"key2bit wrongful, with len_bit = {len_bit}"

        starter += len_bit

    stream_bin_reset = str(stream)
    if String.checksum in key2bit.keys():
        stream_bin_reset = stream[:reset] \
                           + str("".join(['0' for _ in range(key2bit[String.checksum])])) \
                           + stream[reset + key2bit[String.checksum]:]

    # 十六进制存储
    return key2val, stream_bin_reset
