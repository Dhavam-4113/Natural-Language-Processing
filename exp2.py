import nltk
from nltk.tokenize import word_tokenize
from nltk import HiddenMarkovModelTagger

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

text = input("Enter a sentence:")

tokens = word_tokenize(text)

tagged_words = HiddenMarkovModelTagger(tokens)

print("\nTokens:")
print(tokens)

print("\nHiddenMarkovModel Tags:")
for word,tag in tagged_words:
    print(word,"->", tag)

print("\nTag Meanings:")
print("NN -> Noun")
print("VB -> Verb")
print("JJ -> Adjective")
print("RB -> Adverb")
print("PRP -> Pronoun")
print("DT -> Determiner")

print("\nTotal Words:",len(tokens))