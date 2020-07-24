'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0

    if len(word) <= 2:
        if word == "th":
            count += 1
    elif word[0:2] == 'th':
        word = word[2:]
        count += 1
        count += count_th(word)
    else:
        word = word[1:]
        count += count_th(word)

    return count

print(count_th('asethasth'))
