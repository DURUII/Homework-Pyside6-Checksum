import argparse

from checksum.layers.link import EthernetII

parser = argparse.ArgumentParser()
parser.add_argument('--base', default=16, type=int)
parser.add_argument('--stream', default="""
f8 a2 d6 c4 2e e5 f0 9b b8 0d 6c a7 08 00 45 00
00 51 5e e6 00 00 2f 11 81 63 3b be ad d4 c0 a8
01 18 d3 b3 30 39 00 3d 25 2e ac a6 1f 6c 4e 5d
f6 99 c4 b9 31 72 dc d8 c5 e5 8f 44 86 d0 9f fc 
50 ed f8 94 8c 51 b7 ac c7 aa bb c1 fe f9 67 9b
b1 cd e7 cb 81 e7 a1 ce c4 e0 f7 29 79 22 61
""", type=str)
parser.add_argument('--recursive', default=True, type=bool)
args = parser.parse_args()

EthernetII.parse_ethernet_ii("""
6215a8d007229c297610047308004500004b9a0a000040110000c0a82b21b465f6e6eca21f400037975e023b290125622b7bd18c230200000001010100006a84fd2587843746cad0b4f09e6c2f2949dc976adf7912fe777903
""", args.base, args.recursive)
