def text_to_binary(text):
    # Convert text to binary representation
    binary_text = ''.join(format(ord(char), '08b') for char in text)
    return binary_text

def swap(text, i, j):
    # Swap text[i] and text[j] 
    text[i], text[j] = text[j], text[i]

def swap_2d(array_2d, coords_1: tuple, coords_2: tuple):
    x1, y1 = coords_1
    x2, y2 = coords_2
    array_2d[x1][y1], array_2d[x2][y2] = array_2d[x2][y2], array_2d[x1][y1]


def initial_permutation(plain_text):
    if len(plain_text) != 128:
        raise ValueError("Plain text must be 128 bits long")
    plain_text = list(plain_text)

    ip_table = list(range(128))
    ip_table = [32*i % 127 for i in range(127)]
    ip_table.append(127)
    plain_text = [plain_text[i] for i in ip_table]
    return "".join(plain_text) 


def final_permutation(plain_text):
    if len(plain_text) != 128:
        raise ValueError("Plain text must be 128 bits long")
    plain_text = list(plain_text)

    fp_table = list(range(128))
    fp_table = [2*i % 127 for i in range(127)]
    fp_table.append(127)
    plain_text = [plain_text[i] for i in fp_table]
    return "".join(plain_text) 


def s0():
    DES_S0 = [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
    ]

    return [{bin(index)[2:].zfill(4): bin(value)[2:].zfill(4) for index, value in enumerate(line)} for line in DES_S0]

def binary_sum(a, b):
    # Sum two binary numbers
    return bin(int(a, 2) + int(b, 2))[2:].zfill(len(a))

def binary_xor(a, b):
    # XOR two binary numbers
    return bin(int(a, 2) ^ int(b, 2))[2:].zfill(len(a))

def binary_to_decimal(binary):
    # Convert binary number to decimal
    return int(binary, 2)


#utiliser la fonction ecluide etendu
def s_i(s_i_previous, plain_text):
    s_i_current = [{key: value for key, value in line.items()} for line in s_i_previous]
    bit_blocks = [plain_text[i:i+4] for i in range(0, len(plain_text), 4)]
    index_blocks = [bin(index)[2:].zfill(4) for index in range(16)]
    for index, index_box in enumerate(bit_blocks):
        for index_bits in index_blocks:
            i = binary_sum(index_bits, s_i_current[index][index_bits])
            i = binary_to_decimal(i)
            j = s_i_current[i][index_bits]
            x1, y1 = index, index_bits
            x2, y2 = index, j
            swap_2d(s_i_current, (x1, y1), (x2, y2))
    return s_i_current
            


def s_i_inverse(s_i_previous, plain_text):
    ...
