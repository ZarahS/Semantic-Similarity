import spacy
nlp = spacy.load('en_core_web_md')

print("EXAMPLE 1")
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
print("\n")

# The similarity between cat and monkey is high showing that the model recognizes that they are both animals.
# The model shows a high similarity between "monkey" and "banana",  relative to "cat" and "banana",
# this means that it recognizes that monkeys eat bananas. This is interesting as it shows that the model 
# has learned to understand the relationships between words in terms of their context and usage.

print("MY EXAMPLE")
word1 = nlp("kitten")
word2 = nlp("puppy")
word3 = nlp("fruit")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
print("\n")

# As expected "kitten" and "puppy" have a strong similarity,  the model recognizes they are baby animals
# The second and third scores are low so the model recognizes that they are semantically different.

print("EXAMPLE 2")
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
      print(token1.text, token2.text, token1.similarity(token2))
print("\n")


print("EXAMPLE 3")
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
      similarity = nlp(sentence).similarity(model_sentence)
      print(sentence + " - ",  similarity)

# Run the example file with the simpler language model "en_core_web_sm" 
# Write a note on what you notice is different from the model "en_core_web_md".

# A userWarning message pops up when running this file with "en_core_web_sm" 
# indicating that this model hasn't been trained with word vectors but own vectors can be loaded ot
# a larger model can be used. The md model comes with vectors loaded.

# The "en_core_web_md" is a larger, more complex model with more parameters and therefore more information, 
# while the "en_core_web_sm" is a smaller, simpler model with fewer parameters. 
# This results in "en_core_web_md" having more accurate similarity scores and the ability 
# to capture more nuanced relationships between words.
