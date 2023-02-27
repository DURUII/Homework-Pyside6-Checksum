from checksum import Data
from checksum.utils.rich_console import console
from checksum.utils.formatter import nip_prefix, print_hex, bin2hex


# 按位取补：https://blog.csdn.net/whatday/article/details/104051481
def complement(n4: str):
    n4 = nip_prefix(n4).zfill(4)
    n4 = list(n4)
    for i in range(len(n4)):
        n4[i] = nip_prefix(hex(15 - int(n4[i], 16)))
    return hex(int(''.join(n4), 16))


# https://www.bilibili.com/video/BV1fD4y1q7Dj
def double_sum(stream_hex: str):
    stream_hex = nip_prefix(stream_hex)
    # FIXME
    l = int(stream_hex[-4:], 16)
    r = int(stream_hex[:-4], 16)
    return l + r


def check(stream_hex: str, stream_checksum: str, base=16, pseudo=True):
    if base == 2:
        stream_hex = bin2hex(stream_hex)

    stream_hex, stream_checksum = map(nip_prefix, (stream_hex, stream_checksum))

    process = {Data.pseudo: pseudo,
               Data.reset: print_hex(stream_hex),
               Data.detail: [],
               Data.double_sum: [],
               Data.complement: [],
               Data.result: False}

    _sum = 0
    _tmp = 0
    for i in range(4, len(stream_hex) + 1, 4):
        _tmp += int(stream_hex[i - 4:i], 16)
        process[Data.detail].append(
            f"{hex(_sum).rjust(10, ' ')} + {(hex(int(stream_hex[i - 4:i], 16))).rjust(10, ' ')} = {hex(_tmp).rjust(10, ' ')}")
        _sum = _tmp
        # console.print(f"{stream_hex[i - 4:i]}+={hex(_sum)}")

    while len(hex(_sum)) > 6:
        _sum = double_sum(hex(_sum))
        process[Data.double_sum].append(f"{hex(_sum)}")
        # console.print(f"double_sum: {hex(_sum)}")

    console.print(f"complement: {complement(hex(_sum))}")
    process[Data.complement].append(
        f"{hex(_sum)} + {hex(int(stream_checksum, 16))} = {hex(_sum + int(stream_checksum, 16))}")

    valid = int(complement(hex(_sum)), 16) == int(stream_checksum, 16)
    console.print("[purple bold]checksum_valid?: [/purple bold]" + f"[bold red]{str(valid)}[/bold red]")

    process[Data.result] = valid
    return process


if __name__ == '__main__':
    # https://blog.csdn.net/stephenxu111/article/details/12945893
    check("0x450000285aee000040060000ac140a06b7028f6c", "0x2359")
    check("0xac140a06b7028f6c00060014f3ca01bbb9969aada133fc975010100000000000", "0xbbb5")
