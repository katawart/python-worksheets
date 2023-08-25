#Credit: H Mcgowan
#Reference: Tao, Y () RSA Cryptosystem  https://www.cse.cuhk.edu.hk/~taoyf/course/bmeg3120/notes/rsa.pdf 
#Author: R Hunt

import rsamaths

#Preconditions: p, q, e are all Integers that are prime numbers.
#Postconditions: Return a public and private key.
def generate_keys(p, q, e):
    n = p*q                                 #n is used in both keys.
    print("n",n)                
    phi_n = (p-1)*(q-1)                     #phi_n, used to generate d later.
    print("phi(n)",phi_n)
    d = rsamaths.find_mod_inverse(e, phi_n) #Uses Euclidean Algorithm.
    print("d", d)
    print("public key", [n,e])
    print("private key", [n,d])
    public_key = n,e                        #Public key is n,e
    private_key = n,d                       #Private key is n,d
    return public_key, private_key          #Returns public and private keys
    

#Preconditions: Takes a phrase as string, and the public key as list of two elements.
#Postconditions: Returns and encrypted phrase.
def encrypt(phrase, public_key):
    enc_phrase = ""                                     #Empty string to hold the encrypted phrase.
    m = 0                                               #To hold the integer value fo a character.
    for i in phrase:
        m = pow(ord(i), public_key[1]) % public_key[0]  # (i^public_key[1]) MOD public_key[0]
        print(m)
        enc_phrase = enc_phrase + chr(m)                #Adds the character m to the enc_phrase.
        m = 0                                           #Reset m
    return enc_phrase                                   #Return encrypted phrase.



#Preconditions: Takes a phrase as string, and the private key as list of two elements.
#Postconditions: Returns and decrypted phrase.
def decrypt(phrase, private_key):
    dec_phrase = ""
    m = 0
    for i in phrase:
        m = pow(ord(i), private_key[1]) % private_key[0]
        print(m)
        dec_phrase = dec_phrase + chr(m)
        m = 0
    return dec_phrase


p_val = int(input("p:",))
q_val = int(input("q:",))
e_val = int(input("e:",))
pub_key, priv_key = generate_keys(p_val, q_val, e_val)
result = encrypt("a", pub_key)
print(result)
print(decrypt(result, priv_key))

#Valid p, q, e
#23, 37, 85
#7, 31, 7

