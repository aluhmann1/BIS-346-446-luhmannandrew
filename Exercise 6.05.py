text = ('this is sample text containing words' 
        'this is sample text containing different words')

word_counts = {}

# find unique words and give count
for word in text.split():
    if word in word_counts: 
        word_counts[word] += 1  # updating existing key-value pair
    else:
        word_counts[word] = 1  # insert new key-value pair if none previous

print(f'{"WORD":<12}COUNT')

for word, count in sorted(word_counts.items()):
    if count > 1:
        print(f'{word:<12}{count}')