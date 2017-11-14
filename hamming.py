def hamming(str, str1):
    ham = 0

    for i in range(0, 15):
        if str[i] != str1[i]:
            ham += 1

    return ham
