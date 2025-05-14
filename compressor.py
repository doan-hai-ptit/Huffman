import pickle
from huffman import (
    calculate_frequency,
    build_huffman_tree,
    build_codes,
    encode_data,
    pad_encoded_data,
    get_byte_array,
)

def compress(input_path: str, output_path: str, metadata_path: str):
    # Đọc dữ liệu gốc (file nhị phân hoặc text)
    with open(input_path, 'rb') as file:
        data = file.read()
    # Tính tần suất và xây cây Huffman
    freq_map = calculate_frequency(data)
    huffman_tree = build_huffman_tree(freq_map)
    code_map = build_codes(huffman_tree)

    # Mã hóa dữ liệu
    encoded_bits = encode_data(data, code_map)
    padded_bits = pad_encoded_data(encoded_bits)
    byte_data = get_byte_array(padded_bits)

    # Ghi dữ liệu nén ra file
    with open(output_path, 'wb') as out_file:
        out_file.write(byte_data)

    # Lưu bảng mã và cây Huffman (dạng nhị phân) để giải nén sau
    with open(metadata_path, 'wb') as meta_file:
        pickle.dump(huffman_tree, meta_file)

    print(f"Đã nén: {input_path}")
    print(f"→ File nén: {output_path}")
    print(f"→ Metadata: {metadata_path}")
    print(f"Kích thước trước: {len(data)} byte, sau: {len(byte_data)} byte")
