#!/usr/bin/env python
# https://en.bitcoin.it/wiki/Protocol_documentation#Addresses

import hashlib
import base58

# ECDSA bitcoin Public Key
#pubkey = '04c335d94e062103d2f2081a1b71183c4130cf79ec86ea11f47a3827bad0fe1c6f5385c9d7869c07809232cc356f2172ffcec45c3d524de9ea82356623ce03e2ef'
# See 'compressed form' at https://en.bitcoin.it/wiki/Protocol_documentation#Signatures
#compress_pubkey = False

def is_pubkey_compress(pubkey,compress_pubkey):
    if (compress_pubkey):
        if (ord(bytearray.fromhex(pubkey[-2:])) % 2 == 0):
            pubkey_compressed = '02'
        else:
            pubkey_compressed = '03'
        pubkey_compressed += pubkey[2:66]
        hex_str = bytearray.fromhex(pubkey_compressed)
    else:
        hex_str = bytearray.fromhex(pubkey)
    return hex_str

def hash160(hex_str):
    sha = hashlib.sha256()
    rip = hashlib.new('ripemd160')
    sha.update(hex_str)
    rip.update( sha.digest() )
    #print( "key_hash = \t" + rip.hexdigest() )
    return rip.hexdigest()  # .hexdigest() is hex ASCII

def address(pubkey, compress_pubkey):
    sha = hashlib.sha256()
    sha.update( bytearray.fromhex('00' + hash160(is_pubkey_compress(pubkey, compress_pubkey))) )
    checksum = sha.digest()
    sha = hashlib.sha256()
    sha.update(checksum)
    checksum = sha.hexdigest()[0:8]
    return (base58.b58encode( bytes(bytearray.fromhex('00' + hash160(is_pubkey_compress(pubkey,compress_pubkey)) + checksum)) )).decode('utf-8')


if __name__ == "__main__":
    print(address(pubkey, compress_pubkey))