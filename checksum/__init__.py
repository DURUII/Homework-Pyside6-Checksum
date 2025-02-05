def dict2html(key2exp):
    html = []

    if key2exp is not None:
        for key in key2exp.keys():
            content = key2exp[key]

            if type(content) == list:
                _tmp = []
                for item in content:
                    _tmp.append(f"""<div>{item}</div>""")
                content = ''.join(_tmp)

            html.append(f"""<div>
                <span style="color: blue; font-weight: bold;">{key}:</span>
                <span>{content}</span>
            </div>""")

        html.append("<br><br>")
        return "".join(html)

    else:
        return ""


def parse_html(e):
    link = dict2html(e['link'])
    network = dict2html(e['network'])
    transport = dict2html(e['transport'])
    return link, network, transport


def process_html(e):
    network = dict2html(e['network'])
    transport = dict2html(e['transport'])
    return network, transport


class Data:
    key2exp_hub = {
        "link": None,
        "network": None,
        "transport": None,
        "application": None
    }

    pseudo = 'pseudo'
    reset = 'reset'
    detail = 'detail'
    double_sum = 'double_sum'
    complement = 'complement'
    result = 'result'

    process_hub = {
        "network": None,
        "transport": None,
    }


data = Data()
dataset = data.key2exp_hub
process_dataset = data.process_hub
