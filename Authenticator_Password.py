import string
import random
import time

def repeat():
    s1 = list(string.ascii_uppercase) # ABCD
    s2 = list(string.ascii_lowercase) # abcd
    s3 = list(string.digits) # 01234
    s4 = list(string.punctuation)
    all = s1+s2+s3+s4

    characters_num = 10

    random.shuffle(s1)  # ABCD --> CBDA
    random.shuffle(s2)  # abcd --> dbca
    random.shuffle(s3)  # 01234 --> 31240
    random.shuffle(s4)  # .,-: --> :-.,

    part1 = round(characters_num*(30/100))
    part2 = round(characters_num*(20/100))
    password = []

    for i in range(part1):  # capitalLetters and smallLetters 60% of the password
        password.append(s1[i])
        password.append(s2[i])

    for i in range(part2):  # punctuations and digits 40% of the password
        password.append(s3[i])
        password.append(s4[i])
    password = "".join(random.sample(all,characters_num))

    print("Your New Password Is: "+password)
    for T in range(10, 0, -1):
        time.sleep(1)
        print(T)
    repeat()

repeat()















