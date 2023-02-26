"""
JOB:

carry the bank over ONE link at a time if given a datagram.
"""

from checksum.layers.network import IPv4
from checksum.utils import parser, decoder
from checksum.utils.rich_console import console
from checksum.utils.decoder import type_ethernet
from checksum.utils.static import String


class EthernetII:
    key2bit = {
        String.mac_addr_dst_ethernet_ii: 6 * 8,
        String.mac_addr_src_ethernet_ii: 6 * 8,
        String.type_ethernet_ii: 2 * 8,
        String.data_payload: -1
    }

    key2dec = {
        String.type_ethernet_ii: type_ethernet,
    }

    @classmethod
    def parse_ethernet_ii(cls, stream: str, base, recursive=False):
        assert stream != "" and stream is not None, "NULL STREAM"

        console.rule("[bold green] link layer parsing [/bold green]")

        # 十六进制存储
        key2val, stream_bin_reset = parser.parse(cls.key2bit, stream, base)
        key2exp = decoder.decode(cls.key2bit, key2val, cls.key2dec)

        for key in key2exp.keys():
            if key in cls.key2dec.keys():
                console.print(f"{key} : [bold red italic]{key2exp[key]}[/bold red italic]")
            else:
                console.print(f"{key} : [black]{key2exp[key]}[/black]")

        if key2val[String.data_payload] is None:
            recursive = False

        if recursive:
            if key2exp[String.type_ethernet_ii] == String.ipv4:
                IPv4.parse_ipv4(key2val[String.data_payload], 16, recursive)
            elif key2exp[String.type_ethernet_ii] == String.ipv6:
                IPv6.parse_ipv6(key2val[String.data_payload], 16, recursive)
            else:
                assert False, "Network Protocol Not Supported"
        else:
            console.rule("[bold green]EOF[/bold green]")
