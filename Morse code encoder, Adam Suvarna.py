#This is the table cipher for morse code!

morse_table_cipher = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', '.': '.-.-.-', ',': '--..--', 
                    '?': '..--..', '\'': '· − − − − ·', 
                    '!': '− · − · − −', '/': '− · · − ·', 
                    '(': '− · − − ·', ')': '− · − − · −', 
                    '&': '· − · · ·', ':': '− − − · · ·', 
                    ';': '− · − · − ·', '=': '− · · · −', 
                    '+': '· − · − ·', '-': '− · · · · −',
                    '_': '· · − − · −', '"': '· − · · − ·',
                    '$': '· · · − · · −', '@': '· − − · − ·', }

#Now to encrypt the given message to morse code:
def encrypt_message(message):
    
    code = ''

    for alphabet in message:
        
        if alphabet != ' ':
            
            code += morse_table_cipher[alphabet] + ' '
        
        else:
            
            code += ' '
 
    
    return code

#Now to decrypt a given message from morse code to English:
def decrypt_message(message):
    
    message += ' '
 
    decode = ''
    
    citext = ''
    
    for alphabet in message:
        
        if (alphabet != ' '):
            
            i = 0
            
            citext += alphabet
        
        else:

            i += 1
 
            if i == 2 :
 
                decode += ' '
            
            else:
                decode += list(morse_table_cipher.keys())[list(morse_table_cipher
                .values()).index(citext)]
                
                citext = ''
 
    return decode

#Now to input the word or phrase you want to encrypt or morse code you want to decrypt:
def main():
    message = input("Enter a word or phrase to be encoded: ")
    
    result = encrypt_message(message.upper())
    
    print (result)
 
    
    message = input("Enter morse code to be decoded: ")
    
    result = decrypt_message(message)
    
    print (result)
 
if __name__ == '__main__':
    main()
