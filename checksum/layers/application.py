"""
bidirectional reliable byte stream

"""
from checksum.utils.rich_console import console
from checksum.utils import parser, decoder
from checksum.utils.static import String


class APP:
    key2bit = {
        String.data_payload: -1
    }

    key2dec = {

    }

    @classmethod
    def parse_top(cls, stream: str, base, recursive=False):
        assert stream != "" and stream is not None, "NULL STREAM"

        console.rule("[bold green] application layer parsing [/bold green]")

        key2val, stream_hex_deprived = parser.parse(cls.key2bit, stream, base)
        key2exp = decoder.decode(cls.key2bit, key2val, cls.key2dec)

        for key in key2exp.keys():
            if key in cls.key2dec.keys():
                console.print(f"{key} : [bold red italic]{key2exp[key]}[/bold red italic]")
            else:
                console.print(f"{key} : [black]{key2exp[key]}[/black]")

        console.rule("[bold green]EOF[/bold green]")
