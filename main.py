import os
import argparse
from compressor import compress
from decompressor import decompress

def main():
    parser = argparse.ArgumentParser(description="Huffman Coding - Nén và Giải nén file")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Nén file
    compress_parser = subparsers.add_parser("compress", help="Nén file")
    compress_parser.add_argument("input", help="Tên file gốc (trong thư mục 'input')")
    compress_parser.add_argument("output", help="Tên file đầu ra (trong thư mục 'output')")
    compress_parser.add_argument("metadata", help="Tên file metadata (trong thư mục 'metadata')")

    # Giải nén file
    decompress_parser = subparsers.add_parser("decompress", help="Giải nén file")
    decompress_parser.add_argument("input", help="Tên file đã nén (trong thư mục 'output')")
    decompress_parser.add_argument("metadata", help="Tên file metadata (trong thư mục 'metadata')")
    decompress_parser.add_argument("output", help="Tên file đầu ra (trong thư mục 'output')")

    args = parser.parse_args()

    # Xử lý lệnh compress
    if args.command == "compress":
        input_path = os.path.join("input", args.input)
        output_path = os.path.join("output", args.output)
        metadata_path = os.path.join("metadata", args.metadata)
        compress(input_path, output_path, metadata_path)

    # Xử lý lệnh decompress
    elif args.command == "decompress":
        input_path = os.path.join("output", args.input)
        metadata_path = os.path.join("metadata", args.metadata)
        output_path = os.path.join("output", args.output)
        decompress(input_path, metadata_path, output_path)

if __name__ == "__main__":
    # Tạo các thư mục nếu chưa tồn tại
    os.makedirs("input", exist_ok=True)
    os.makedirs("output", exist_ok=True)
    os.makedirs("metadata", exist_ok=True)

    main()
# python main.py compress input.txt output.huff metadata.json
# python main.py decompress output.huff metadata.json output.txt