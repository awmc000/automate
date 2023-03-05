# English to Pig Latin
print('Enter a message to translate to Pig Latin:')
message = input()

VOWELS = ('a','e','i','o','u','y')

pigLatin = []
for word in message.split():
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]
