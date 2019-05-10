# open and read the text
ge = open("great_expectations_complete.txt").read()

# convert the text to lower case, strip punctuation and split into words
ge = ge.lower()
for punctuation in [',' , ':' , '.' , '"' , '!' , '?' , '–' , '(' , ')' , '\n' , '\r']:
    ge = ge.replace(punctuation, ' ')
all_words = ge.split(" ")

# build up the dict of word counts
word_count = {}
for word in all_words:
    current_count = word_count.get(word, 0)
    new_count = current_count + 1
    word_count[word] = new_count

# iterate over items and print the word if the count is great than 1000
for word, count in word_count.items():
    if count > 1000:
    print(word)