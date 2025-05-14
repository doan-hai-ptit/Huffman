import heapq
from collections import defaultdict

# Node của cây Huffman
class Node:
    def __init__(self, char=None, freq=0):
        self.char = char        # ký tự
        self.freq = freq        # tần suất
        self.left = None        # nhánh trái
        self.right = None       # nhánh phải

    def __lt__(self, other):
        return self.freq < other.freq

# Đếm tần suất byte trong dữ liệu
def calculate_frequency(data: bytes):
    freq = defaultdict(int)
    for byte in data:
        freq[byte] += 1
    return freq

# Tạo cây Huffman từ bảng tần suất
def build_huffman_tree(freq_map):
    heap = [Node(char, freq) for char, freq in freq_map.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    print(f"Đã tạo cây Huffman với Node đầu {heap[0].char} và tần suất {heap[0].freq}")
    return heap[0] if heap else None

# Duyệt cây để tạo bảng mã Huffman
def build_codes(node, current_code="", code_map={}):
    if node is None:
        return

    if node.char is not None:
        code_map[node.char] = current_code
        return

    build_codes(node.left, current_code + "0", code_map)
    build_codes(node.right, current_code + "1", code_map)

    return code_map

# Mã hóa dữ liệu thành chuỗi bit
def encode_data(data: bytes, code_map: dict):
    print(code_map)
    encoded_bits = ''.join(code_map[byte] for byte in data)
    print(f"{data} -> {encoded_bits} {len(encoded_bits)} bits")
    return encoded_bits

# Đệm chuỗi bit để vừa byte
def pad_encoded_data(encoded_bits):
    extra_padding = 8 - len(encoded_bits) % 8
    encoded_bits += "0" * extra_padding
    padded_info = "{0:08b}".format(extra_padding)
    return padded_info + encoded_bits

# Chuyển chuỗi bit sang bytes
def get_byte_array(padded_bits):
    b = bytearray()
    for i in range(0, len(padded_bits), 8):
        byte = padded_bits[i:i+8]
        b.append(int(byte, 2))
    return bytes(b)

# Giải mã chuỗi bit thành dữ liệu gốc
def decode_data(encoded_bits, root):
    decoded_bytes = bytearray()
    current = root
    for bit in encoded_bits:
        current = current.left if bit == "0" else current.right
        if current.char is not None:
            decoded_bytes.append(current.char)
            current = root
    return bytes(decoded_bytes)

# Gỡ đệm
def remove_padding(padded_bits):
    padded_info = padded_bits[:8]
    extra_padding = int(padded_info, 2)
    encoded_bits = padded_bits[8:]
    return encoded_bits[:-extra_padding]