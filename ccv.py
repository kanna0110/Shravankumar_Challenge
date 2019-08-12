import re

def validCard(card):
    if (not re.match("^[0-9]{16}$", card)) and (not re.match("^[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}$", card)):
        return False
    card = card.replace('-', '')
    if (not card) or (card[0] not in ['4', '5', '6']):
        return False
    pre = 0
    for i in range(1, len(card) + 1):
        if i == len(card) or card[i] != card[pre]:
            if i - pre >= 4:
                return False
            pre = i
    return True

N = int(input())
for i in range(N):
    card = input()
    if validCard(card):
        print('Valid')
    else:
        print('Invalid')
