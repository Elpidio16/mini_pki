class SBox:
    def __init__(self):
        # Define a simple 8x8 S-box. In a real cryptographic scenario, S-boxes are carefully designed.
        self.s_box = [
            0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5,
            0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
            0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0,
            0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
            0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC,
            0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
            0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A,
            0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
        ]

    def substitute(self, byte):
        # Perform the substitution based on the S-box
        return self.s_box[byte]

# Example usage
sbox = SBox()

# Substitute a byte using the S-box
original_byte = 0xA5
substituted_byte = sbox.substitute(original_byte)

print(f"Original Byte: {hex(original_byte)}")
print(f"Substituted Byte: {hex(substituted_byte)}")

s_box
