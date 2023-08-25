
#Preconditions: Takes two parameters, a word as string to encrypt
                #and a shift as integer to move the cahracter along.
#Postcondition: Returns an encrypted phrase as a string.
def enc(word, shift):
    enc_phrase = ""                         #Empty string to hold encrypted word.
    for char in word:                       #For each character in the word.
        char = ord(char)                    #Turn it into a number on the ascii table.
        char = (char + shift) % 127         #Increase the number by shift, mod 127.
        enc_phrase = enc_phrase + chr(char) #Add the character to the encrytped string.
    return enc_phrase                       #Return the phrase.
        

def dec(word, shift):
    dec_phrase = ""                         #Empty string to hold decrypted word.
    for char in word:                       #For each character in the word.
        char = ord(char)                    #Turn it into a number on the ascii table.
        char = (char - shift) % 127         #Decrease the number by shift, mod 127.
        dec_phrase = dec_phrase + chr(char) #Add the character to the decrytped string.
    return dec_phrase                       #Return the phrase.



phrase_word = input("Type a word to encrypt: ")
p_shift = int(input("What key shift: "))
ret_phrase = enc(phrase_word, p_shift)
print(ret_phrase)
orig_phrase = dec(ret_phrase, p_shift)
print(orig_phrase)
