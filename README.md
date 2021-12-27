strong-qr-decoder
=================

Strong QR code decoder

Features
========

- If the error correction fails, the data portion is forcibly read.
- The error correction level and mask pattern can be specified manually.
- The `--verbose` option gives detailed output.

Usage
=====

```
% ./sqrd.py --help
usage: sqrd.py [-h] [-e ERROR_CORRECTION] [-m MASK] [-n] [-v] [FILE]

sqrd - Strong QR Decoder

positional arguments:
  FILE                  input file (default is standard input)

optional arguments:
  -h, --help            show this help message and exit
  -e ERROR_CORRECTION, --error-correction ERROR_CORRECTION
                        error correction level (1: L 0: M 3: Q 2: H)
  -m MASK, --mask MASK  mask pattern (0-7)
  -n, --no-correction   do not correct data blocks
  -v, --verbose         show more information
```

How to use
==========

Insert the QR code as text data.

- `'X', 'x', 'O', 'o', '#', '1'` are treated as dark modules.
- `'_', '-', ' ', '0'` are treated as light modules.
- `'?'` is treated as an unknown module (it will be treated as a light module after unmasking).


Example
=======

Save the following data as `qr.txt`.
```
XXXXXXX_X_XX_X____XXXXXXX
X_____X_XXX_XXX_X_X_____X
X_XXX_X_XX______X_X_XXX_X
X_XXX_X____X_X__X_X_XXX_X
X_XXX_X__X_XXXXX__X_XXX_X
X_____X_X__X_X_X__X_____X
XXXXXXX_X_X_X_X_X_XXXXXXX
________X__X_XX_X________
__XXX_X_X__XXX___XXX__XXX
XX_XX__X__X__X_XXX_X__X__
X___X_X_X_XX__X__XXX___XX
XX_X_X__X_XXX_____X____XX
_X_X__XXX__X_X_X_XX_X_X_X
X_X_______XXXX_XX__X_X___
X_XX__X_X_XXX_X___X__X_XX
X_X_____XX_XX___XXXX___X_
X_X_X_X_X_X___X_XXXXXXX_X
________XX_X_X__X___X_XX_
XXXXXXX____X__XXX_X_XX_XX
X_____X__X_X_X_XX___X__X_
X_XXX_X_X_XXXXXXXXXXXXX__
X_XXX_X_X__XXX____X_X___X
X_XXX_X_X__X_X_X__XX____X
X_____X___X_XX_X_X_XX___X
XXXXXXX____X__X_X__XX__XX
```

When executed, the decoding result will be displayed.
```
% ./sqrd.py qr.txt
sample_data
```
