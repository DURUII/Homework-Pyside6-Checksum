"""

TCP's JOB:

correctly delivered, with any lost/corrupted bank automatically retransmitted if needed
"""
from checksum import dataset, process_dataset
from checksum.layers.application import APP
from checksum.utils.rich_console import console
from checksum.utils import parser, decoder, checker
from checksum.utils.formatter import nip_prefix
from checksum.utils.static import String


class TCP:
    key2bit = {
        String.port_src: 16,
        String.port_dst: 16,
        String.sequence_first_byte: 32,
        String.sequence_acknowledgement: 32,
        String.length_header: 4,  # a.k.a. 数据偏移
        String.reserved: 6,
        String.flags: 6,
        String.size_window: 16,
        String.checksum: 16,
        String.pointer_urgent: 16,
        String.data_payload: -1
    }

    key2dec = {

    }

    @classmethod
    def checksum(cls, stream_bin_reset, stream_checksum):
        process_dataset['transport'] = checker.check(stream_bin_reset, stream_checksum, base=2)

    @classmethod
    def parse_tcp(cls, stream: str, base, recursive=False, **args):
        assert stream != "" and stream is not None, "NULL STREAM"

        console.rule("[bold green] transport layer parsing [/bold green]")

        key2val, stream_bin_reset = parser.parse(cls.key2bit, stream, base)
        key2exp = decoder.decode(cls.key2bit, key2val, cls.key2dec)

        for key in key2exp.keys():
            if key in cls.key2dec.keys():
                console.print(f"{key} : [bold red italic]{key2exp[key]}[/bold red italic]")
            else:
                console.print(f"{key} : [black]{key2exp[key]}[/black]")

        dataset['transport'] = key2exp

        data = stream_bin_reset[160:]

        # 注意长度单位：字节
        stream_bin_reset = args.get("pseudo") \
                           + nip_prefix(bin(len(stream_bin_reset) // 8), 2).zfill(2 * 8) \
                           + nip_prefix(stream_bin_reset, 2)

        if len(data) % 16 != 0:
            stream_bin_reset = stream_bin_reset + "00000000"

        cls.checksum(stream_bin_reset, key2val[String.checksum])

        if key2val[String.data_payload] is None:
            recursive = False

        if recursive:
            APP.parse_top(key2val[String.data_payload], 16, recursive)
        else:
            console.rule("[bold green]EOF[/bold green]")


class UDP:
    key2bit = {
        String.port_src: 16,
        String.port_dst: 16,
        String.length_total_packet: 16,
        String.checksum: 16,
        String.data_payload: -1,
    }

    key2dec = {
    }

    @classmethod
    def checksum(cls, stream_bin_reset, stream_checksum):
        process_dataset['transport'] = checker.check(stream_bin_reset, stream_checksum, base=2)

    @classmethod
    def parse_udp(cls, stream: str, base, recursive=False, **args):
        assert stream != "" and stream is not None, "NULL STREAM"

        console.rule("[bold green] transport layer parsing [/bold green]")

        key2val, stream_bin_reset = parser.parse(cls.key2bit, stream, base)
        key2exp = decoder.decode(cls.key2bit, key2val, cls.key2dec)

        for key in key2exp.keys():
            if key in cls.key2dec.keys():
                console.print(f"{key} : [bold red italic]{key2exp[key]}[/bold red italic]")
            else:
                console.print(f"{key} : [black]{key2exp[key]}[/black]")

        dataset['transport'] = key2exp

        data = stream_bin_reset[64:]

        # TODO 和 UDP 不同，此时长度非自行计算，单位已经为字节
        stream_bin_reset = args.get("pseudo") \
                           + nip_prefix(bin(int(key2val[String.length_total_packet], 16)), 2).zfill(2 * 8) \
                           + nip_prefix(stream_bin_reset, 2)

        if len(data) % 16 != 0:
            stream_bin_reset = stream_bin_reset + "00000000"

        cls.checksum(stream_bin_reset, key2val[String.checksum])

        if key2val[String.data_payload] is None:
            recursive = False

        if recursive:
            APP.parse_top(key2val[String.data_payload], 16)
        else:
            console.rule("[bold green]EOF[/bold green]")
