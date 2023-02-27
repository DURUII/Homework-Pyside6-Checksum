from checksum.utils.rich_console import console


def bin2hex(stream_bin):
    return hex(int(stream_bin, 2)).zfill(len(stream_bin) // 4)


def print_hex(stream: str, num_sep=2, num_ln=32):
    html = "<br>"
    console.print(f"[bold blue]sum to be checked: [/bold blue]")
    for i in range(len(stream)):
        if i % num_sep == 0 and i != 0:
            console.print(" ", end="")
            html = html + " "
        if i % num_ln == 0 and i != 0:
            console.print("\n", end="")
            html = html + "<br>"
        console.print(f"[bold blue]{stream[i]}[/bold blue]", end="")
        html += stream[i]
    console.print("\n", end="")
    return html


def nip_prefix(stream: str, base=16):
    assert base == 16 or base == 8 or base == 2, "only BIN, OCT, HEX allowed"

    stream = stream.lower().replace('\n', '').replace(' ', '')

    if base == 2:
        stream = stream.replace('0b', '')
        charset = {'0', '1'}
    elif base == 8:
        stream = stream.replace('0o', '')
        charset = {'0', '1', '2', '3', '4', '5', '6', '7'}
    else:
        stream = stream.replace('0x', '')
        charset = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'}

    assert set(stream).issubset(charset), f"Stream Unrecognizable, check {set(stream) - charset}"

    return stream
