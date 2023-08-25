
def enc(char, shift):
    enc_char = chr((ord(char) + shift) % 127) #Increase the number by shift, mod 127.
    return enc_char
    
def dec(char, shift):
    dec_char = chr((ord(char) - shift) % 127) #Decrease the number by shift, mod 127.
    return dec_char

