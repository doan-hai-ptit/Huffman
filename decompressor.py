import pickle
from huffman import remove_padding, decode_data

def decompress(input_path: str, metadata_path: str, output_path: str):
    # Đọc dữ liệu đã nén
    with open(input_path, 'rb') as file:
        byte_data = file.read()

    # Chuyển từ bytes sang chuỗi bit
    bit_string = ''.join(f"{byte:08b}" for byte in byte_data)

    # Gỡ padding
    encoded_bits = remove_padding(bit_string)

    # Tải cây Huffman đã lưu
    with open(metadata_path, 'rb') as meta_file:
        huffman_tree = pickle.load(meta_file)

    # Giải mã
    original_data = decode_data(encoded_bits, huffman_tree)

    # Ghi dữ liệu gốc ra file
    with open(output_path, 'wb') as out_file:
        out_file.write(original_data)

    print(f"Đã giải nén: {input_path}")
    print(f"→ File gốc: {output_path}")
