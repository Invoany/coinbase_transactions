#!/usr/bin/env python
# https://en.bitcoin.it/wiki/Protocol_documentation#Addresses
# https://gist.github.com/circulosmeos/ef6497fd3344c2c2508b92bb9831173f

import hashlib
import base58
import binascii

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

def hex_to_ascii(hex_str):
    hex_str = hex_str.replace(' ', '').replace('0x', '').replace('\t', '').replace('\n', '').replace('\r', '')
    ascii_str = binascii.unhexlify(hex_str)
    #return format(''.join(chr(i) for i in ascii_str))
    ascii_str_no_null=b''
    for i in ascii_str:
        if i in range(0,32) or i > 126 :
            pass
        else:
            ascii_str_no_null = ascii_str_no_null + i.to_bytes(1,'little')
    return (ascii_str_no_null)

if __name__ == "__main__":
    #print(address(pubkey, compress_pubkey))
    #hex_str="04ffff001d027303"
    #print(hex_to_ascii(hex_str))
    pass