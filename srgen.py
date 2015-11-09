import base64
import hashlib

def checksum(binary_data_as_string):
    digest_sha256 = hashlib.sha256(binary_data_as_string).digest()
    hash_base64 = base64.b64encode(digest_sha256).decode()
    return 'sha256-{}'.format(hash_base64)





with open('sri_test.js', 'rb') as f:
	print checksum(f.read())