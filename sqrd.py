#!/usr/bin/env python3
# -*-coding: utf-8-*-

import sys
import argparse

# Alignment pattern coordinates
alignment_pattern_array = [
    [],
    [6, 18],
    [6, 22],
    [6, 26],
    [6, 30],
    [6, 34],
    [6, 22, 38],
    [6, 24, 42],
    [6, 26, 46],
    [6, 28, 50],
    [6, 30, 54],
    [6, 32, 58],
    [6, 34, 62],
    [6, 26, 46, 66],
    [6, 26, 48, 70],
    [6, 26, 50, 74],
    [6, 30, 54, 78],
    [6, 30, 56, 82],
    [6, 30, 58, 86],
    [6, 34, 62, 90],
    [6, 28, 50, 72, 94],
    [6, 26, 50, 74, 98],
    [6, 30, 54, 78, 102],
    [6, 28, 54, 80, 106],
    [6, 32, 58, 84, 110],
    [6, 30, 58, 86, 114],
    [6, 34, 62, 90, 118],
    [6, 26, 50, 74, 98, 122],
    [6, 30, 54, 78, 102, 126],
    [6, 26, 52, 78, 104, 130],
    [6, 30, 56, 82, 108, 134],
    [6, 34, 60, 86, 112, 138],
    [6, 30, 58, 86, 114, 142],
    [6, 34, 62, 90, 118, 146],
    [6, 30, 54, 78, 102, 126, 150],
    [6, 24, 50, 76, 102, 128, 154],
    [6, 28, 54, 80, 106, 132, 158],
    [6, 32, 58, 84, 110, 136, 162],
    [6, 26, 54, 82, 110, 138, 166],
    [6, 30, 58, 86, 114, 142, 170],
]

# version information table (version 7 or higher)
version_information_table = [
    0x07C94,
    0x085BC,
    0x09A99,
    0x0A4D3,
    0x0BBF6,
    0x0C762,
    0x0D847,
    0x0E60D,
    0x0F928,
    0x10B78,
    0x1145D,
    0x12A17,
    0x13532,
    0x149A6,
    0x15683,
    0x168C9,
    0x177EC,
    0x18EC4,
    0x191E1,
    0x1AFAB,
    0x1B08E,
    0x1CC1A,
    0x1D33F,
    0x1ED75,
    0x1F250,
    0x209D5,
    0x216F0,
    0x228BA,
    0x2379F,
    0x24B0B,
    0x2542E,
    0x26A64,
    0x27541,
    0x28C69,
]

# Format information table
format_information_table = [
    "000000000000000",
    "000010100110111",
    "000101001101110",
    "000111101011001",
    "001000111101011",
    "001010011011100",
    "001101110000101",
    "001111010110010",
    "010001111010110",
    "010011011100001",
    "010100110111000",
    "010110010001111",
    "011001000111101",
    "011011100001010",
    "011100001010011",
    "011110101100100",
    "100001010011011",
    "100011110101100",
    "100100011110101",
    "100110111000010",
    "101001101110000",
    "101011001000111",
    "101100100011110",
    "101110000101001",
    "110000101001101",
    "110010001111010",
    "110101100100011",
    "110111000010100",
    "111000010100110",
    "111010110010001",
    "111101011001000",
    "111111111111111",
]

# Data code Word number table (M(00), L(01), H(10), Q(11))
data_code_num_table = [
    [  16,   19,    9,   13],
    [  28,   34,   16,   22],
    [  44,   55,   26,   34],
    [  64,   80,   36,   48],
    [  86,  108,   46,   62],
    [ 108,  136,   60,   76],
    [ 124,  156,   66,   88],
    [ 154,  194,   86,  110],
    [ 182,  232,  100,  132],
    [ 216,  274,  122,  154],
    [ 254,  324,  140,  180],
    [ 290,  370,  158,  206],
    [ 334,  428,  180,  244],
    [ 365,  461,  197,  261],
    [ 415,  523,  223,  295],
    [ 453,  589,  253,  325],
    [ 507,  647,  283,  367],
    [ 563,  721,  313,  397],
    [ 627,  795,  341,  445],
    [ 669,  861,  385,  485],
    [ 714,  932,  406,  512],
    [ 782, 1006,  442,  568],
    [ 860, 1094,  464,  614],
    [ 914, 1174,  514,  664],
    [1000, 1276,  538,  718],
    [1062, 1370,  596,  754],
    [1128, 1468,  628,  808],
    [1193, 1531,  661,  871],
    [1267, 1631,  701,  911],
    [1373, 1735,  745,  985],
    [1455, 1843,  793, 1033],
    [1541, 1955,  845, 1115],
    [1631, 2071,  901, 1171],
    [1725, 2191,  961, 1231],
    [1812, 2306,  986, 1286],
    [1914, 2434, 1054, 1354],
    [1992, 2566, 1096, 1426],
    [2102, 2702, 1142, 1502],
    [2216, 2812, 1222, 1582],
    [2334, 2956, 1276, 1666],
]

# RS block number table (M(00), L(01), H(10), Q(11))
RS_block_num_table = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 2, 2],
    [2, 1, 4, 2],
    [2, 1, 4, 4],
    [4, 2, 4, 4],
    [4, 2, 5, 6],
    [4, 2, 6, 6],
    [5, 2, 8, 8],
    [5, 4, 8, 8],
    [5, 4, 11, 8],
    [8, 4, 11, 10],
    [9, 4, 16, 12],
    [9, 4, 16, 16],
    [10, 6, 18, 12],
    [10, 6, 16, 17],
    [11, 6, 19, 16],
    [13, 6, 21, 18],
    [14, 7, 25, 21],
    [16, 8, 25, 20],
    [17, 8, 25, 23],
    [17, 9, 34, 23],
    [18, 9, 30, 25],
    [20, 10, 32, 27],
    [21, 12, 35, 29],
    [23, 12, 37, 34],
    [25, 12, 40, 34],
    [26, 13, 42, 35],
    [28, 14, 45, 38],
    [29, 15, 48, 40],
    [31, 16, 51, 43],
    [33, 17, 54, 45],
    [35, 18, 57, 48],
    [37, 19, 60, 51],
    [38, 19, 63, 53],
    [40, 20, 66, 56],
    [43, 21, 70, 59],
    [45, 22, 74, 62],
    [47, 24, 77, 65],
    [49, 25, 81, 68],
]

# Table in alphanumerical mode
alphanumeric_table = [
    "0", "1", "2", "3", "4", "5",
    "6", "7", "8", "9", "A", "B",
    "C", "D", "E", "F", "G", "H",
    "I", "J", "K", "L", "M", "N",
    "O", "P", "Q", "R", "S", "T",
    "U", "V", "W", "X", "Y", "Z",
    " ", "$", "%", "*", "+", "-",
    ".", "/", ":",
]

# Colored output
def stdoutColor(text, color):
    dic = {"red": 31, "green": 32, "blue": 34}
    sys.stdout.write("\x1b[1m\x1b[{0}m{1}\x1b[0m".format(dic[color], text))


# Module drawing
def printModule(c):
    if c == 0:
        sys.stdout.write("\x1b[47m  \x1b[0m")
    elif c == 1:
        sys.stdout.write("\x1b[40m  \x1b[0m")
    elif c == 2:
        sys.stdout.write("\x1b[44m  \x1b[0m")
    else:
        sys.stderr.write(u"error: illegal color\n")
        sys.exit(1)


# QR code data drawing
def showData(data):
    for y in range(len(data)):
        for x in range(len(data)):
            printModule(data[x][y])
        print("")


# Is the finder pattern correct?
def checkFinder(data, xoffset, yoffset):
    for x in range(7):
        for y in range(7):
            if x == 0 or y == 0 or x == 6 or y == 6 or ((2 <= x <= 4) and (2 <= y <= 4)):
                if data[xoffset + x][yoffset + y] == 0:
                    return False
            else:
                if data[xoffset + x][yoffset + y] == 1:
                    return False
    return True


# Hamming distance calculation
def hammingDistance(s1, s2):
    if len(s1) != len(s2):
        sys.stderr.write(u"error: different string lengths\n")
        sys.exit(1)
    r = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            r += 1
    return r


# Mask pattern
def mask(pat, x, y):
    if pat == 0:
        return (x + y) % 2 == 0
    if pat == 1:
        return y % 2 == 0
    if pat == 2:
        return x % 3 == 0
    if pat == 3:
        return (x + y) % 3 == 0
    if pat == 4:
        return ((x // 3) + (y // 2)) % 2 == 0
    if pat == 5:
        return (x * y) % 2 + (x * y) % 3 == 0
    if pat == 6:
        return ((x * y) % 2 + (x * y) % 3) % 2 == 0
    if pat == 7:
        return ((x * y) % 3 + (x + y) % 2) % 2 == 0
    sys.stderr.write(u"error: illegal pattern\n")
    sys.exit(1)


# Convert from alpha exponent of GF(2^8) to vector representation
def index2vector(index):
    index2vector_table = [
        None, 1, 2, 4, 8, 16, 32, 64, 128, 29, 58, 116, 232, 205, 135, 19,
        38, 76, 152, 45, 90, 180, 117, 234, 201, 143, 3, 6, 12, 24, 48, 96,
        192, 157, 39, 78, 156, 37, 74, 148, 53, 106, 212, 181, 119, 238, 193, 159,
        35, 70, 140, 5, 10, 20, 40, 80, 160, 93, 186, 105, 210, 185, 111, 222,
        161, 95, 190, 97, 194, 153, 47, 94, 188, 101, 202, 137, 15, 30, 60, 120,
        240, 253, 231, 211, 187, 107, 214, 177, 127, 254, 225, 223, 163, 91, 182, 113,
        226, 217, 175, 67, 134, 17, 34, 68, 136, 13, 26, 52, 104, 208, 189, 103,
        206, 129, 31, 62, 124, 248, 237, 199, 147, 59, 118, 236, 197, 151, 51, 102,
        204, 133, 23, 46, 92, 184, 109, 218, 169, 79, 158, 33, 66, 132, 21, 42,
        84, 168, 77, 154, 41, 82, 164, 85, 170, 73, 146, 57, 114, 228, 213, 183,
        115, 230, 209, 191, 99, 198, 145, 63, 126, 252, 229, 215, 179, 123, 246, 241,
        255, 227, 219, 171, 75, 150, 49, 98, 196, 149, 55, 110, 220, 165, 87, 174,
        65, 130, 25, 50, 100, 200, 141, 7, 14, 28, 56, 112, 224, 221, 167, 83,
        166, 81, 162, 89, 178, 121, 242, 249, 239, 195, 155, 43, 86, 172, 69, 138,
        9, 18, 36, 72, 144, 61, 122, 244, 245, 247, 243, 251, 235, 203, 139, 11,
        22, 44, 88, 176, 125, 250, 233, 207, 131, 27, 54, 108, 216, 173, 71, 142
	]
    if index == None:
        return 0b00000000
    else:
        return index2vector_table[(index % 255) + 1]


# Conversion of vector representation to alpha exponent of GF(2^8)
def vector2index(v):
    vector2index_table = [
        None, 255, 1, 25, 2, 50, 26, 198, 3, 223, 51, 238, 27, 104, 199, 75,
        4, 100, 224, 14, 52, 141, 239, 129, 28, 193, 105, 248, 200, 8, 76, 113,
        5, 138, 101, 47, 225, 36, 15, 33, 53, 147, 142, 218, 240, 18, 130, 69,
        29, 181, 194, 125, 106, 39, 249, 185, 201, 154, 9, 120, 77, 228, 114, 166,
        6, 191, 139, 98, 102, 221, 48, 253, 226, 152, 37, 179, 16, 145, 34, 136,
        54, 208, 148, 206, 143, 150, 219, 189, 241, 210, 19, 92, 131, 56, 70, 64,
        30, 66, 182, 163, 195, 72, 126, 110, 107, 58, 40, 84, 250, 133, 186, 61,
        202, 94, 155, 159, 10, 21, 121, 43, 78, 212, 229, 172, 115, 243, 167, 87,
        7, 112, 192, 247, 140, 128, 99, 13, 103, 74, 222, 237, 49, 197, 254, 24,
        227, 165, 153, 119, 38, 184, 180, 124, 17, 68, 146, 217, 35, 32, 137, 46,
        55, 63, 209, 91, 149, 188, 207, 205, 144, 135, 151, 178, 220, 252, 190, 97,
        242, 86, 211, 171, 20, 42, 93, 158, 132, 60, 57, 83, 71, 109, 65, 162,
        31, 45, 67, 216, 183, 123, 164, 118, 196, 23, 73, 236, 127, 12, 111, 246,
        108, 161, 59, 82, 41, 157, 85, 170, 251, 96, 134, 177, 187, 204, 62, 90,
        203, 89, 95, 176, 156, 169, 160, 81, 11, 245, 22, 235, 122, 117, 44, 215,
        79, 174, 213, 233, 230, 231, 173, 232, 116, 214, 244, 234, 168, 80, 88, 175
    ]
    return vector2index_table[v]


# Multiplication on GF(2^8)
def mulGF256(v1, v2):
    if v1 == 0b00000000 or v2 == 0b00000000:
        return 0b00000000
    else:
        return index2vector(vector2index(v1) + vector2index(v2))


# Syndrome calculation
def calcSyndrome(RS_block, index):
    s = 0b00000000  # Vector representation
    for i in range(len(RS_block)):
        s ^= mulGF256(RS_block[i], index2vector(index * i))
        # print(index, bin(s))
    return s


# Determinant of matrix A_ij with GF(2^8) as a component
def detGF256(A):
    if len(A) != len(A[0]):
        sys.stderr.write(u"error: not a square matrix\n")
        sys.exit(1)
    size = len(A)
    if size == 1:
        return A[0][0]
    # Sweep out
    for i in range(size - 1):
        if A[i][i] == 0b00000000:
            continue
        for j in range(i + 1, size):
            if A[j][i] == 0b00000000:
                continue
            v = index2vector(vector2index(A[j][i]) - vector2index(A[i][i]))
            for k in range(size):
                A[j][k] ^= mulGF256(A[i][k], v)
    # Multiply
    s = 0b00000001
    for i in range(size):
        s = mulGF256(s, A[i][i])
    return s


# Calculation of simultaneous linear equations by sweep method
# (A: Augmented coefficient matrix with n rows and n + 1 columns)
def solveSE(A):
    size = len(A)
    # Sweep out
    for i in range(size - 1):
        if A[i][i] == 0b00000000:
            continue
        for j in range(i + 1, size):
            if A[j][i] == 0b00000000:
                continue
            v = index2vector(vector2index(A[j][i]) - vector2index(A[i][i]))
            for k in range(size + 1):
                A[j][k] ^= mulGF256(A[i][k], v)
    # Backward substitution
    xs = []
    for i in range(size):
        x = A[-(i + 1)][-1]
        for j in range(i):
            x ^= mulGF256(xs[j], A[-(i + 1)][-2 - j])
        if A[-(i + 1)][-2 - i] == 0b00000000:  # Error correction failed because the solution is not uniquely determined.
            sys.stderr.write(u"error: error correction failed. Please consider the specification of the -no-correction option\n")
            sys.exit(1)
        x = mulGF256(x, index2vector(-vector2index(A[-(i + 1)][-2 - i])))
        xs.append(x)
    xs.reverse()
    return xs


# Calculation of error position polynomial \ sigma(\ alpha ^ {index})
def calcSigma(sigmas, index):
    s = 0b00000000
    for i in range(len(sigmas)):
        s ^= mulGF256(sigmas[-1 - i], index2vector(index * i))
    s ^= index2vector(index * len(sigmas))
    return s


# Main
if __name__ == "__main__":
    # ---------------- Preprocessing -----------------
    # Command line argument analysis
    parser = argparse.ArgumentParser(description="sqrd - Strong QR Decoder")
    parser.add_argument("-e", "--error-correction", help=u"error correction level (1: L 0: M 3: Q 2: H)")
    parser.add_argument("-m", "--mask", help=u"mask pattern (0-7)")
    parser.add_argument("-n", "--no-correction", action="store_true", help=u"do not correct data blocks")
    parser.add_argument("-v", "--verbose", action="store_true", help=u"show more information")
    parser.add_argument("FILE", nargs="?", default="-", help=u"input file (default is standard input)")
    args = parser.parse_args()

    # ---------------- Reading data ----------------
    # Read text data
    if args.FILE == "-":
        text = sys.stdin.read()
    else:
        stream = open(args.FILE, "r")
        text = stream.read()
        stream.close()
    lines = text.split("\n")
    width = len(lines[0])
    for i in range(width):
        if len(lines[i]) != width:
            sys.stderr.write(u"error: input is not square\n")
            sys.exit(1)
    # Calculation of version(version)
    if (width - 21) % 4 != 0 or width < 21 or 177 < width:
        sys.stderr.write(u"error: edge length is wrong\n")
        sys.exit(1)
    version = (width - 21) // 4 + 1
    if args.verbose:
        print(u"version:\t{0} ({1}x{1})".format(version, width))
    # Creation of 2D array data[x][y]
    data = []
    for i in range(width):
        data.append([])
    for line in lines:
        for i in range(len(line)):
            if line[i] in "XxOo#1":  # dark module
                data[i].append(1)
            elif line[i] in "_- 0":  # light module
                data[i].append(0)
            elif line[i] in "?":  # unknown
                data[i].append(2)
            else:
                sys.stderr.write(u"error: contains invalid characters\n")
                sys.exit(1)
    # Display of read data
    if args.verbose:
        print(u"read data:")
        showData(data)

    # ---------------- Checking fixed patterns -----------------
    # Is the finder pattern correct?
    if checkFinder(data, 0, 0) and checkFinder(data, width - 7, 0) and checkFinder(data, 0, width - 7):
        valid_finder_pattern = True
    else:
        valid_finder_pattern = False
    if args.verbose:
        print("")
        if valid_finder_pattern:
            stdoutColor("[OK] ", "green")
        else:
            stdoutColor("[NG] ", "red")
        print(u"position detection pattern")
    # Is the separator correct?
    valid_separator = True
    for i in range(8):
        if (
            data[i][7] == 1
            or data[7][i] == 1
            or data[width - 8 + i][7] == 1
            or data[width - 8][i] == 1
            or data[i][width - 8] == 1
            or data[7][width - 8 + i] == 1
        ):
            valid_separator = False
    if args.verbose:
        if valid_separator:
            stdoutColor("[OK] ", "green")
        else:
            stdoutColor("[NG] ", "red")
        print(u"separation pattern")
    # Is the timing pattern correct?
    valid_timing_pattern = True
    for i in range(width - 16):
        if data[8 + i][6] == i % 2 or data[6][8 + i] == i % 2:
            valid_timing_pattern = False
    if args.verbose:
        if valid_timing_pattern:
            stdoutColor("[OK] ", "green")
        else:
            stdoutColor("[NG] ", "red")
        print(u"timing pattern")
    # Is the alignment pattern correct?
    valid_alignment_pattern = True
    array = alignment_pattern_array[version - 1]
    for x in array:
        for y in array:
            if not (
                (x < 9 and y < 9) or (width - 10 < x and y < 9) or (x < 9 and width - 10 < y)
            ):  # Exclude if it overlaps with the position detection pattern
                for i in range(-2, -2 + 5):
                    for j in range(-2, -2 + 5):
                        if max(abs(i), abs(j)) == 1:
                            if data[x + i][y + j] == 1:
                                valid_alignment_pattern = False
                        else:
                            if data[x + i][y + j] == 0:
                                valid_alignment_pattern = False
    if args.verbose:
        if valid_alignment_pattern:
            stdoutColor("[OK] ", "green")
        else:
            stdoutColor("[NG] ", "red")
        print(u"alignment pattern")
    # Creating is_data_module[x][y]
    is_data_module = []
    for x in range(width):
        t = []
        for y in range(width):
            if (x <= 8 and y <= 8) or (width - 8 <= x and y <= 8) or (x <= 8 and width - 8 <= y) or x == 6 or y == 6:
                t.append(False)
            else:
                t.append(True)
        is_data_module.append(t)
    for x in array:  # Exclude alignment pattern
        for y in array:
            if not (
                (x < 9 and y < 9) or (width - 10 < x and y < 9) or (x < 9 and width - 10 < y)
            ):  # Exclude if it overlaps with the position detection pattern
                for i in range(-2, -2 + 5):
                    for j in range(-2, -2 + 5):
                        is_data_module[x + i][y + j] = False
    if 7 <= version:
        for i in range(6):  # Exclude lower left version information
            for j in range(3):
                is_data_module[i][-11 + j] = False
        for j in range(6):  # Exclude version information in the upper right
            for i in range(3):
                is_data_module[-11 + i][j] = False

    # ---------------- Checking version information -----------------
    if 7 <= version:
        # version information at the bottom left
        left_bottom = ""
        for i in range(6):
            for j in range(3):
                if data[i][-11 + j] == 1:
                    left_bottom += "1"
                elif data[i][-11 + j] == 0:
                    left_bottom += "0"
                elif data[i][-11 + j] == 2:
                    left_bottom += "?"
        left_bottom = left_bottom[::-1]
        if args.verbose:
            print(u"\nversion information (lower left):\t\t{0}".format(left_bottom))
        # version information on the upper right
        right_top = ""
        for j in range(6):
            for i in range(3):
                if data[-11 + i][j] == 1:
                    right_top += "1"
                elif data[-11 + i][j] == 0:
                    right_top += "0"
                elif data[-11 + i][j] == 2:
                    right_top += "?"
        right_top = right_top[::-1]
        if args.verbose:
            print(u"\nversion information (upper right):\t\t{0}".format(right_top))
        # Synthesis of two version information
        composed = ""
        diff_format = False
        for i in range(18):
            if left_bottom[i] == "?" and right_top[i] == "?":
                composed += "?"
            elif left_bottom[i] == "?":
                composed += right_top[i]
            elif right_top[i] == "?":
                composed += left_bottom[i]
            elif left_bottom[i] == right_top[i]:
                composed += left_bottom[i]
            else:
                diff_format = True
                composed += left_bottom[i]
        if args.verbose:
            if diff_format:
                stdoutColor("[NG] ", "red")
            else:
                stdoutColor("[OK] ", "green")
            print(u"consistency of two versions")
            print(u"version information (composite):\t\t{0}".format(composed))
        # Error correction
        version_information = composed.replace("?", "0")  # Fill unknown modules with 0s
        min_hamming_distance = 18
        index = -1
        for i in range(32):
            d = hammingDistance(version_information, "{0:018b}".format(version_information_table[i]))
            if d < min_hamming_distance and d <= 3:
                index = i
        if index == -1:  # Error correction failure
            if args.verbose:
                stdoutColor("[NG] ", "red")
                print(u"Error correction of version information")
        else:
            if args.verbose:
                stdoutColor("[OK] ", "green")
                print(u"error correction")
            version_information = "{0:018b}".format(version_information_table[index])
            if args.verbose:
                print(u"version information (after error correction):\t{0}".format(version_information))

    # ---------------- Checking format information -----------------
    # Is the always dark module correct?
    if data[8][4 * version + 9] == 0:
        valid_always_black = False
    else:
        valid_always_black = True
    if args.verbose:
        print("")
        if valid_always_black:
            stdoutColor("[OK] ", "green")
        else:
            stdoutColor("[NG] ", "red")
        print(u"always dark module")
    # Getting format information
    format_mask = "101010000010010"
    # Horizontal format information
    yoko = ""
    for i in range(15):
        if i <= 5:
            if data[i][8] == 1:
                yoko += "1"
            elif data[i][8] == 0:
                yoko += "0"
            elif data[i][8] == 2:
                yoko += "?"
        elif i == 6:
            if data[i + 1][8] == 1:
                yoko += "1"
            elif data[i + 1][8] == 0:
                yoko += "0"
            elif data[i + 1][8] == 2:
                yoko += "?"
        else:
            if data[width - 8 + i - 7][8] == 1:
                yoko += "1"
            elif data[width - 8 + i - 7][8] == 0:
                yoko += "0"
            elif data[width - 8 + i - 7][8] == 2:
                yoko += "?"
    if args.verbose:
        print(u"format information (horizontal):\t\t{0}".format(yoko))
    # Vertical format information
    tate = ""
    for i in range(15):
        if i <= 6:
            if data[8][width - 1 - i] == 1:
                tate += "1"
            elif data[8][width - 1 - i] == 0:
                tate += "0"
            elif data[8][width - 1 - i] == 2:
                tate += "?"
        elif i <= 8:
            if data[8][8 - (i - 7)] == 1:
                tate += "1"
            elif data[8][8 - (i - 7)] == 0:
                tate += "0"
            elif data[8][8 - (i - 7)] == 2:
                tate += "?"
        else:
            if data[8][5 - (i - 9)] == 1:
                tate += "1"
            elif data[8][5 - (i - 9)] == 0:
                tate += "0"
            elif data[8][5 - (i - 9)] == 2:
                tate += "?"
    if args.verbose:
        print(u"format information (vertical):\t\t\t{0}".format(tate))
    # Composite of vertical and horizontal format information
    composed = ""
    diff_format = False
    for i in range(15):
        if yoko[i] == "?" and tate[i] == "?":
            composed += "?"
        elif yoko[i] == "?":
            composed += tate[i]
        elif tate[i] == "?":
            composed += yoko[i]
        elif yoko[i] == tate[i]:
            composed += yoko[i]
        else:
            diff_format = True
            composed += yoko[i]
    if args.verbose:
        if diff_format:
            stdoutColor("[NG] ", "red")
        else:
            stdoutColor("[OK] ", "green")
        print(u"vertical and horizontal format information consistency")
        print(u"format information (composite):\t\t\t{0}".format(composed))
    composed_unmask = "".join(["0" if x == y else "1" if x in "01" and y in "01" else "?" for (x, y) in zip(composed, format_mask)])
    if args.verbose:
        print(u"format information (unmasked):\t\t\t{0}".format(composed_unmask))
    # Error correction
    format_information = composed_unmask.replace("?", "0")  # Fill unknown modules with 0s
    min_hamming_distance = 15
    index = -1
    for i in range(32):
        d = hammingDistance(format_information, format_information_table[i])
        if d < min_hamming_distance and d <= 3:
            index = i
    if index == -1:  # Error correction failure
        if args.verbose:
            stdoutColor("[NG] ", "red")
            print(u"error correction of format information")
        if "?" in composed_unmask[:5] and not (
            args.error_correction != None and args.mask != None
        ):  # The data part is all unknown and no argument is specified.
            sys.stderr.write(u"error: the data part of the format information is unknown, and error correction failed\n")
            sys.exit(1)
        elif "?" in composed_unmask[:2] and args.error_correction == None:  # Error correction level unknown, no arguments specified
            sys.stderr.write(u"error: the data part of the format information is unknown, and error correction failed\n")
            sys.exit(1)
        elif "?" in composed_unmask[2:5] and args.mask == None:  # The mask pattern is unknown and no arguments are specified.
            sys.stderr.write(u"error: the data part of the format information is unknown, and error correction failed\n")
            sys.exit(1)
        else:  # Error correction failed, but the data part was safe or I set it myself
            format_information = composed_unmask
    else:
        if args.verbose:
            stdoutColor("[OK] ", "green")
            print(u"error correction")
        format_information = format_information_table[index]
        if args.verbose:
            print(u"format information (after error correction):\t{0}".format(format_information))
    # Get error correction level
    if args.error_correction != None:
        error_correction_level = int(args.error_correction, 0)
    else:
        error_correction_level = int(format_information[:2], 2)
    if error_correction_level == 0b01:
        m = "L"
    if error_correction_level == 0b00:
        m = "M"
    if error_correction_level == 0b11:
        m = "Q"
    if error_correction_level == 0b10:
        m = "H"
    if args.verbose:
        print(u"\nerror correction level:\t{0:02b} ({1})".format(error_correction_level, m))
    # Get mask pattern
    if args.mask != None:
        mask_pattern = int(args.mask, 0)
    else:
        mask_pattern = int(format_information[2:5], 2)
    if args.verbose:
        if mask_pattern == 0:
            m = "(x + y) mod 2 = 0"
        if mask_pattern == 1:
            m = "y mod 2 = 0"
        if mask_pattern == 2:
            m = "x mod 3 = 0"
        if mask_pattern == 3:
            m = "(x + y) mod 3 = 0"
        if mask_pattern == 4:
            m = "((x // 3) + (y // 2)) mod 2 = 0"
        if mask_pattern == 5:
            m = "(x * y) mod 2 + (x * y) mod 3 = 0"
        if mask_pattern == 6:
            m = "((x * y) mod 2 + (x * y) mod 3) mod 2 = 0"
        if mask_pattern == 7:
            m = "((x * y) mod 3 + (x + y) mod 2) mod 2 = 0"
        print(u"mask pattern:\t\t{0:2} [{1}]".format(mask_pattern, m))

    # ---------------- Unmask -----------------
    # Unmask
    for y in range(width):
        for x in range(width):
            if is_data_module[x][y] and mask(mask_pattern, x, y):
                if data[x][y] == 0:
                    data[x][y] = 1
                elif data[x][y] == 1:
                    data[x][y] = 0
    if args.verbose:
        print(u"\ndata after unmasking:")
        showData(data)

    # ---------------- Read code word string -----------------
    # Read code word string
    blocks = []
    block = ""
    count = 0
    x = width - 1
    y = width - 1
    while True:
        if x < 0 or y < 0:
            break
        if is_data_module[x][y]:
            block += "?" if data[x][y] == 2 else str(data[x][y])
            count += 1
            if count == 8:
                blocks.append(block)
                block = ""
                count = 0
        tx = x if x < 7 else x - 1  # Consider timing pattern
        if tx % 2 == 1:
            x -= 1
        else:
            if (tx // 2) % 2 == 1:
                # Go up
                if y == 0:
                    x -= 1
                else:
                    y -= 1
                    x += 1
            else:
                # Go down
                if y == width - 1:
                    if (tx // 2) == 3:  # Skip vertical timing pattern
                        x -= 1
                    x -= 1
                else:
                    y += 1
                    x += 1
    if args.verbose:
        print(u"\ntotal number of code words: {0}".format(len(blocks)))
        print(u"data blocks: {0}".format(repr(blocks)))
    # Divide into RS blocks
    RS_blocks = []
    block_num = RS_block_num_table[version - 1][error_correction_level]
    offset = data_code_num_table[version - 1][error_correction_level]
    for i in range(block_num):
        t = []
        for j in range(offset // block_num):  # Data part
            t.append(blocks[j * block_num + i])
        if offset % block_num != 0:  # if there is a fraction
            remain = offset % block_num
            if (block_num - remain) <= i:
                t.append(blocks[(offset // block_num) * block_num + (i - (block_num - remain))])
        for j in range((len(blocks) - offset) // block_num):  # Error correction code part
            t.append(blocks[offset + j * block_num + i])
        t.reverse()
        RS_blocks.append(t)
    if args.verbose:
        print(u"number of RS blocks: {0}".format(len(RS_blocks)))
        print(u"after RS block split:")
        for i in range(len(RS_blocks)):
            print("{0}".format(repr(RS_blocks[i])))
    # Count the number of codewords containing unknown modules
    unknown_code_nums = []
    for bs in RS_blocks:
        s = 0
        for c in bs:
            if "?" in c:
                s += 1
        unknown_code_nums.append(s)
    if args.verbose:
        print(u"\nnumber of unknown data codes in each RS block: {0}".format(repr(unknown_code_nums)))
    # Fill unknown module with 0
    for i in range(block_num):
        for j in range(len(RS_blocks[i])):
            RS_blocks[i][j] = int(RS_blocks[i][j].replace("?", "0"), 2)
    # Error correction
    # Find the number of error corrections
    if version == 1:
        if error_correction_level == 0b01:  # L
            limit_error_correction_num = 2
        elif error_correction_level == 0b00:  # M
            limit_error_correction_num = 4
        elif error_correction_level == 0b11:  # Q
            limit_error_correction_num = 6
        elif error_correction_level == 0b10:  # H
            limit_error_correction_num = 8
    elif version == 2 and error_correction_level == 0b01:
        limit_error_correction_num = 4
    elif version == 3 and error_correction_level == 0b01:
        limit_error_correction_num = 7
    else:
        limit_error_correction_num = (len(blocks) - offset) // block_num // 2
    if args.verbose:
        print(u"\nnumber of error corrections: {0}".format(limit_error_correction_num))
    for i in range(block_num):  # Correct error individually for each RS block
        if args.verbose:
            print(u"\nRS block {0}".format(i))
        # If the number of unknown modules exceeds the number of error corrections, it cannot be corrected.
        if limit_error_correction_num < unknown_code_nums[i]:
            if args.verbose:
                print(u"\nnumber of blocks containing unknown modules exceeds number of error corrections")
            continue
        # Syndrome calculation
        syndrome_length = (len(blocks) - offset) // block_num  # error correction number, len(syndromes)
        if args.verbose:
            print(u"syndrome number:\t{0}".format(syndrome_length))
        syndromes = []
        for j in range(syndrome_length):
            syndromes.append(calcSyndrome(RS_blocks[i], j))
        if args.verbose:
            print(u"syndrome: {0}".format(repr(list(map("{0:#04x}".format, syndromes)))))
        no_error = True
        for j in range(syndrome_length):
            if syndromes[j] != 0b00000000:
                no_error = False
        if args.verbose:
            if no_error:
                stdoutColor("[NO] ", "green")
            else:
                stdoutColor("[YES] ", "red")
            print(u"necessity of error correction")
        if no_error or args.no_correction:  # No error
            continue  # to the next block
        # Calculation of the number of errors
        for size in range(syndrome_length // 2 - 1, 0, -1):
            # Create augmented coefficient matrix
            A = []
            for j in range(size):
                row = []
                for k in range(size):
                    row.append(syndromes[j + k])
                A.append(row)
            det = detGF256(A)
            if det != 0b00000000:
                break
        num_error = len(A)
        if args.verbose:
            print(u"number of errors:\t{0}".format(num_error))
        # Calculation of error position variable \ sigma_i
        A = []
        for j in range(num_error):
            row = []
            for k in range(num_error + 1):
                row.append(syndromes[j + k])
            A.append(row)
        sigmas = solveSE(A)
        sigmas.reverse()
        if args.verbose:
            print(u"coefficient of error position polynomial: {0}".format(repr(sigmas)))
        # Calculation of error position
        indexes = []
        for j in range(len(RS_blocks[i])):
            s = calcSigma(sigmas, j)
            if s == 0b00000000:
                indexes.append(j)
        if args.verbose:
            print(u"wrong position: {0}".format(repr(indexes)))
        # Find the size of the error
        A = []
        for j in range(len(indexes)):
            row = []
            for k in range(len(indexes)):
                row.append(index2vector(j * indexes[k]))
            row.append(syndromes[j])
            A.append(row)
        errors = solveSE(A)
        if args.verbose:
            print(u"error size: {0}".format(repr(list(map("{0:08b}".format, errors)))))
        # Correct errors
        for j in range(len(indexes)):
            RS_blocks[i][indexes[j]] ^= errors[j]
        if args.verbose:
            print(u"error corrected RS block: {0}".format(repr(list(map("{0:08b}".format, RS_blocks[i])))))
    list(map(lambda xs: xs.reverse(), RS_blocks))

    # ---------------- Read data -----------------
    # Final data byte sequence retrieval
    data_bytes = []
    for i in range(len(RS_blocks)):
        data_bytes.extend(RS_blocks[i][: offset // block_num + (1 if (block_num - (offset % block_num)) <= i else 0)])
    if args.verbose:
        print(u"\nfinal data byte sequence: {0} ({1} bytes)".format(repr(list(map("{0:#04x}".format, data_bytes))), len(data_bytes)))
    data_bits = ""
    for block in data_bytes:
        data_bits += "{0:08b}".format(block)
    if args.verbose:
        print(u"final data bit string: {0}".format(data_bits))
    # Repeat until you finish reading the data
    data = []
    while len(data_bits) != 0:
        # Get mode indicator
        if len(data_bits[:4]) != 4:
            sys.stderr.write(u"\nEnd because the number of remaining bits is less than 4 bits\n")
            break
        mode = int(data_bits[:4], 2)
        m = ""
        if mode == 0b0001:
            m = u"number"
        elif mode == 0b0010:
            m = u"alphanumericals"
        elif mode == 0b0100:
            m = u"8-bit bytes"
        elif mode == 0b1110:
            m = u"filled grass code word"
        elif mode == 0b0000:
            m = u"termination pattern"
        else:
            sys.stderr.write(u"error: unsupported mode specifier\n")
            sys.exit(1)
        if args.verbose:
            print(u"\nmode specifier:\t\t{0} ({1})".format("{0:04b}".format(mode), m))
        data_bits = data_bits[4:]
        # When it's a number
        if mode == 0b0001:
            # Get character count specifier
            if version <= 9:
                length_indicator_length = 10
            elif version <= 26:
                length_indicator_length = 12
            else:
                length_indicator_length = 16
            length = int(data_bits[:length_indicator_length], 2)
            data_bits = data_bits[length_indicator_length:]
            if args.verbose:
                print(u"number of characters:\t{0:4}".format(length))
            # Read the data
            for i in range((length + 2) // 3):
                if i == (length + 2) // 3 - 1:  # last 1 or 2 digits
                    if length % 3 == 0:
                        num = int(data_bits[:10], 2)
                        data_bits = data_bits[10:]
                        data.extend(list(map(ord, "{0:03d}".format(num))))
                    elif length % 3 == 1:
                        num = int(data_bits[:4], 2)
                        data_bits = data_bits[4:]
                        data.extend(list(map(ord, "{0:01d}".format(num))))
                    else:
                        num = int(data_bits[:7], 2)
                        data_bits = data_bits[7:]
                        data.extend(list(map(ord, "{0:02d}".format(num))))
                else:
                    print(data_bits[:10])
                    num = int(data_bits[:10], 2)
                    data_bits = data_bits[10:]
                    data.extend(list(map(ord, str(num))))
            if args.verbose:
                print(u"decoded data:", repr(list(map("{0:#04x}".format, data))))
        # When it is alphanumerical
        if mode == 0b0010:
            # Get character count specifier
            if version <= 9:
                length_indicator_length = 9
            elif version <= 26:
                length_indicator_length = 11
            else:
                length_indicator_length = 13
            length = int(data_bits[:length_indicator_length], 2)
            data_bits = data_bits[length_indicator_length:]
            if args.verbose:
                print(u"number of characters:\t{0:4}".format(length))
            # Read the data
            for i in range((length + 1) // 2):
                if i == (length + 1) // 2 - 1:  # last 1 or 2 digits
                    if length % 2 == 0:
                        if data_bits[:11] == "":
                            break
                        else:
                            num = int(data_bits[:11], 2)
                        data_bits = data_bits[11:]
                        data.extend([ord(alphanumeric_table[num // 45]), ord(alphanumeric_table[num % 45])])
                    else:
                        num = int(data_bits[:6], 2)
                        data_bits = data_bits[6:]
                        data.extend([ord(alphanumeric_table[num])])
                else:
                    if data_bits[:11] == "":
                        break
                    else:
                        num = int(data_bits[:11], 2)
                        data_bits = data_bits[11:]
                        data.extend([ord(alphanumeric_table[num // 45]), ord(alphanumeric_table[num % 45])])
            if args.verbose:
                print(u"decoded data:", repr(list(map("{0:#04x}".format, data))))
        # 8-bit bytes
        if mode == 0b0100:
            # Get character count specifier
            if version <= 9:
                length_indicator_length = 8
            else:
                length_indicator_length = 16
            length = int(data_bits[:length_indicator_length], 2)
            data_bits = data_bits[length_indicator_length:]
            length = min(length, len(data_bits) // 8)
            if args.verbose:
                print(u"number of characters:\t{0:4}".format(length))
            # Read the data
            for i in range(length):
                data.append(int(data_bits[:8], 2))
                data_bits = data_bits[8:]
            if args.verbose:
                print(u"decoded data:", repr(list(map("{0:#04x}".format, data))))
                print(u"decoded data:", repr(list(map(chr, data))))
        # At the end pattern
        if mode == 0b0000:
            break
        if args.verbose:
            print("\ndecoded string: {0}".format("".join(list(map(chr, data)))))
            print("\nremaining bit strings: {0}".format(data_bits))
    if args.verbose:
        print("")
    print("".join(list(map(chr, data))))
