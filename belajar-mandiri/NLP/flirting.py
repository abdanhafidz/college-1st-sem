import nltk

from nltk.tokenize import sent_tokenize, word_tokenize
prompt = "Haloooo Lagi apaa nih?"
words = word_tokenize(prompt)
tags = nltk.pos_tag(words)
print("Hati - hati user akan masuk ke tahap berikutnya dengan membalas `kalau aku sih lagi mikirin kamu` ")