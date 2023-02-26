"""
the THIN WAIST's JOB:

1. deliver packets end-to-end across the Internet, from the SOURCE end to the eventual DESTINATION end.
2. no promises and no guarantees
"""
from checksum.layers.transport import TCP, UDP
from checksum.utils import parser, decoder, checker
from checksum.utils.decoder import type_protocol
from checksum.utils.formatter import nip_prefix
from checksum.utils.static import String
from checksum.utils.rich_console import console


class IPv4:
    key2bit = {
        String.ip_version: 4,
        String.length_header: 4,
        String.type_service: 8,
        String.length_total_packet: 16,
        String.id_packet: 16,
        String.flags: 3,
        String.offset_fragment: 13,
        String.time_to_live: 8,
        String.id_protocol: 8,
        String.checksum: 16,
        String.ip_addr_src: 32,
        String.ip_addr_dst: 32,
        String.data_payload: -1,
    }

    key2dec = {
        String.id_protocol: type_protocol
    }

    @classmethod
    def pseudo_header_ip_bin(cls, key2val):
        ip_addr_src = nip_prefix(bin(int(key2val[String.ip_addr_src], 16)), 2).zfill(4 * 8)
        ip_addr_dst = nip_prefix(bin(int(key2val[String.ip_addr_dst], 16)), 2).zfill(4 * 8)
        id_protocol = nip_prefix(bin(int(key2val[String.id_protocol], 16)), 2).zfill(2 * 8)
        return ip_addr_src + ip_addr_dst + id_protocol

    @classmethod
    def checksum_header(cls, stream_bin_reset, stream_checksum):
        checker.check(nip_prefix(stream_bin_reset)[:160], stream_checksum, base=2)

    @classmethod
    def parse_ipv4(cls, stream: str, base, recursive=False):
        assert stream != "" and stream is not None, "NULL STREAM"

        console.rule("[bold green] network layer parsing [/bold green]")

        # 十六进制存储
        key2val, stream_bin_reset = parser.parse(cls.key2bit, stream, base)
        key2exp = decoder.decode(cls.key2bit, key2val, cls.key2dec)

        for key in key2exp.keys():
            if key in cls.key2dec.keys():
                console.print(f"{key} : [bold red italic]{key2exp[key]}[/bold red italic]")
            else:
                console.print(f"{key} : [black]{key2exp[key]}[/black]")

        cls.checksum_header(stream_bin_reset, key2val[String.checksum])

        if recursive:
            if key2val[String.data_payload] is not None:
                if key2exp[String.id_protocol] == String.tcp:
                    TCP.parse_tcp(key2val[String.data_payload], 16, recursive, pseudo=cls.pseudo_header_ip_bin(key2val))
                elif key2exp[String.id_protocol] == String.udp:
                    UDP.parse_udp(key2val[String.data_payload], 16, recursive, pseudo=cls.pseudo_header_ip_bin(key2val))
                else:
                    assert False, "Transport Protocol Not Supported"
        else:
            console.rule("[bold green]EOF[/bold green]")


# https://www.cnblogs.com/jersey/archive/2011/11/29/2267492.html
class IPv6:
    key2bit = {
        String.ip_version: 4,
        String.type_service: 8,
        String.label_flow: 20,
        String.length_payload: 6,
        String.header_next: 8,
        String.limit_hop: 8,
        String.ip_addr_src: 128,
        String.ip_addr_dst: 128,
        String.data_payload: -1,
    }

    key2dec = {
        String.class_traffic: type_protocol
    }

    @classmethod
    def parse_ipv6(cls, param, param1, recursive):
        pass
