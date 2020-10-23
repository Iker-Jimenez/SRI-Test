#!/usr/bin/env python3
import base64
import hashlib
import sys, getopt

def checksum(binary_data_as_string):
    digest_sha384 = hashlib.sha384(binary_data_as_string).digest()
    hash_base64 = base64.b64encode(digest_sha384).decode()
    return 'sha384-{}'.format(hash_base64)


def usage():
    print ('sri_gen.py -i <inputfile>')


def main(argv):
    if len(argv) == 0:
        usage()
    try:
        opts, args = getopt.getopt(argv,"hi:",["ifile="])
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)
    if len(opts) == 0:
        print("Unrecognised option")
        usage()
    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
            print('Input file is', inputfile)

            with open(inputfile, 'rb') as f:
                print(checksum(f.read()))
        else:
            assert False, "unhandled option"

if __name__ == "__main__":
   main(sys.argv[1:])

