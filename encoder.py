#!/usr/bin/env python3
# usage: python thisfile.py infile.wav outfile.1b

import sys

f_in = open(sys.argv[1], 'rb')
f_out = open(sys.argv[2], 'wb')
# Skip WAV header
f_in.seek(44)

samples = [f_in.read(2) for i in range(8)]
while all(x for x in samples):
    out_byte = 0
    for s in samples:
        out_byte = out_byte << 1
        if int(s[1]) & 0x80 == 0:
            out_byte |= 1
    f_out.write(out_byte.to_bytes(1, byteorder="little"))
    samples = [f_in.read(2) for i in range(8)]
