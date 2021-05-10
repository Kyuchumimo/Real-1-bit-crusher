#!/usr/bin/env python3

import sys
import wave

if len(sys.argv) != 4:
    print("Usage: python thisfile.py infile.1b outfile.wav samplerate", file=sys.stderr)
    exit(1)

f_in = open(sys.argv[1], 'rb')
wave_out = wave.open(sys.argv[2], 'wb')
wave_out.setnchannels(1)
wave_out.setsampwidth(2)
wave_out.setframerate(int(sys.argv[3]))

in_byte = f_in.read(1)
while in_byte:
    in_byte_int = int.from_bytes(in_byte, byteorder="little")
    output_bytes = b''
    for bit in range(8):
        if in_byte_int & 0x80 > 0:
            output_value = 8192
        else:
            output_value = 65536 - 8192
        in_byte_int = in_byte_int << 1
        output_bytes += output_value.to_bytes(2, byteorder="little")
    wave_out.writeframes(output_bytes)
    in_byte = f_in.read(1)

wave_out.close()
