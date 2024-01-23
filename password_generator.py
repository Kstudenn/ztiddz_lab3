import random
import string



def generatePassword():    
    # Ustalona minimalna i maksymalna długość hasła
    MIN_PASS_LEN = 8
    MAX_PASS_LEN = 12
    chars = [
    string.ascii_lowercase,
    string.ascii_uppercase,
    string.digits,
    string.punctuation]
    passwordLen = random.randint(MIN_PASS_LEN,MAX_PASS_LEN)
    size = int(passwordLen)
    password = ''

    for x in range(len(chars)-1):
        draw = (random.randint(1,int(size/2)))
        size -= draw
        password += ''.join(random.choice(chars[x]) for i in range(draw))
    password += ''.join(random.choice(chars[3]) for i in range(size))

    return ''.join(random.sample(password,len(password)))

print(generatePassword())