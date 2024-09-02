import argparse

# from pprint import pprint
# import binascii
import json

import bencoder  # copied from https://github.com/utdemir/bencoder, and modified a bit


# def bstons(obj, encoding):
#     if isinstance(obj, dict):
#         obj = {key.decode(encoding): value for key, value in obj.items()}
#         for key, value in obj.items():
#             nv = bstons(value, encoding)
#             obj[key] = nv
#         return obj
#     if isinstance(obj, list):
#         tempList = []
#         for el in obj:
#             nl = bstons(el, encoding)
#             tempList.append(nl)
#         return tempList
#     if isinstance(obj, bytes):
#         try:
#             obj = obj.decode()
#         except UnicodeDecodeError:  # decoding pieces key's value will throw this error
#             obj = binascii.hexlify(obj).decode(encoding)
#         return obj
#     if isinstance(obj, int):
#         return obj
#     raise ValueError("something went wrong")


def main():
    parser = argparse.ArgumentParser(description="Display contents of a .torrent file in json")

    # Add arguments with appropriate types and help messages
    parser.add_argument("torrent_file", help="Input file path")
    parser.add_argument("-p", "--pieces", action="store_true", help="Show Pieces")

    # Parse the arguments
    args = parser.parse_args()

    # Access the parsed arguments
    torrent_file = args.torrent_file
    showPieces = args.pieces

    f = open(torrent_file, "rb")
    d = bencoder.decode(f.read())
    if not showPieces:
        del d["info"]["pieces"]  # That's a long hash

    # d = bstons(d, "utf-8")

    print(json.dumps(d, indent=2))


if __name__ == "__main__":
    main()
