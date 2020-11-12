import settings

with open('high_score.txt', 'w') as hs:
    hs.write('0aasdfgggggggggggggg')

with open('high_score.txt', 'r') as hs:
    text = hs.read()

print(text)

Exception
