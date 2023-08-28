user_input = input("Enter a sentence: ")
words = user_input.split()
reversed_words = [word[::-1] for word in words]
modified_sentence = ' '.join(reversed_words)
print("Modified sentence:", modified_sentence)

