import string

text = "Przykladowy Tekst"

def encodeBase64(text: str):
    # tablica znaków do kodowania
    asciiTable = ''.join([string.ascii_uppercase,string.ascii_lowercase,string.digits,"+/"])
    # zapis Octets 
    octets = ''.join(format(ord(i), '08b') for i in text)
    # zapis Sextets
    n = 6
    sextets = [(octets[i:i + n]) for i in range(0, len(octets), n)]
    # padding
    sextets[-1] = sextets[-1].ljust(6,'0')
    # codowanie
    sextets= [asciiTable[int(sextets[i],2)] for i in range(0,len(sextets))]
    return "".join(sextets)

print(encodeBase64(text))