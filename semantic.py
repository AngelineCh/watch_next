import spacy

nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# Cat - monkey - banana: It's interesting that the similarity between monkey-banana is much higher than the cat-banana.

print("\nExample: Fish-Bird-Sea\n")
example1 = nlp("fish")
example2 = nlp("bird")
example3 = nlp("sea")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

print("\n\n\n")
tokens = nlp("cat apple monkey banana")
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "Why is my cat on the car"

sentences = ["Where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)


# Example file sm/md: Brings up a warning that the small model we're using has no word vectors loaded
# as it doesn't ship with word vectors and only uses context-sensitive tensors.