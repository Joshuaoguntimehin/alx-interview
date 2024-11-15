#!/usr/bin/python3
"""import statement"""


def validUTF8(data):
    bytes_remaining = 0
    
    for byte in data:
        byte = byte & 0xFF
        
        if bytes_remaining == 0:
            if (byte >> 7)== 0:
                continue
            elif(byte >> 5) == 0b110:
                bytes_remaining = 1
            elif(byte >> 4) == 0b1110:
                bytes_remaining = 2 
            elif (byte >> 3 ) == 0b11110:
                bytes_remaining =3
            else:
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            bytes_remaining -= 1
            
    return bytes_remaining == 0