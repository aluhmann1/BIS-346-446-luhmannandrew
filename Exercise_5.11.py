ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def summarize_letters(string):
    letters = []
    counts = []
    
    for letter in string.lower():
        if letter in ALPHABET:
            if letter in letters:
                index = letters.index(letter)
                counts[index] += 1
            else:
                letters.append(letter)
                counts.append(1)
           
    tuples = list(zip(letters, counts))
    tuples.sort()
    return tuples

panagram = 'Sphinx of black quartz judge my vow'
summary = summarize_letters(panagram)

# display tuple character and count
for char, count in summary:
    print(f'{char}: {count}')

# checking if missing letter
all_letters = True
if len(summary) == len(ALPHABET):
    for item in summary:
        if item[0] not in ALPHABET:
            all_letters = False
            break  
else:
    all_letters = False

if all_letters:
    print(f'"{panagram}" contains all the letters in the alphabet')
else:
    print(f'"{panagram}" does not contain all the letters in the alphabet')
    