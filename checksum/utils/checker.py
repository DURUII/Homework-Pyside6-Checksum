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


def check(stream_hex: str, stream_checksum: str, base=16):
    if base == 2:
        stream_hex = bin2hex(stream_hex)

    stream_hex, stream_checksum = map(nip_prefix, (stream_hex, stream_checksum))

    print_hex(stream_hex)

    _sum = 0

    for i in range(4, len(stream_hex) + 1, 4):
        _sum += int(stream_hex[i - 4:i], 16)
        # console.print(f"{stream_hex[i - 4:i]}+={hex(_sum)}")

    while len(hex(_sum)) > 6:
        _sum = double_sum(hex(_sum))
        console.print(f"double_sum: {hex(_sum)}")

    console.print(f"complement: {complement(hex(_sum))}")
    valid = int(complement(hex(_sum)), 16) == int(stream_checksum, 16)
    console.print("[purple bold]checksum_valid?: [/purple bold]" + f"[bold red]{str(valid)}[/bold red]")

    return valid


if __name__ == '__main__':
    # https://blog.csdn.net/stephenxu111/article/details/12945893
    check("0x450000285aee000040060000ac140a06b7028f6c", "0x2359")
    check("0xac140a06b7028f6c00060014f3ca01bbb9969aada133fc975010100000000000", "0xbbb5")
