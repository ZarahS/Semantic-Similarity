# Semantic-Similarity
>This project explores the use of semantic similarity to find similarities between words, sentences, and short passages, using Natural Language Processing (NLP). This program suggests what movie a user should watch next based on the last movie they watched.

## Contents
1. [Natural Language Processing](https://github.com/ZarahS/Semantic-Similarity#natural-language-processing)
2. [Install](https://github.com/ZarahS/Semantic-Similarity#install)
3. [Usage](https://github.com/ZarahS/Semantic-Similarity#usage)

## 1. Natural Language Processing 

Natural Language Processing (NLP) is a field of computer science and artificial intelligence pertaining to the interactions between computers and human (natural) languages. NLP technologies aim to help computers process, understand, and generate human language.

SpaCy is an NLP library in Python, providing pre-trained models and functionalities for tasks such as tokenization, speech tagging, named entity recognition, and dependency parsing. It uses NLP techniques to process human language. To use spaCy, you must first install it and its English language model.

## 2. Install

The spaCy library can be installed by entering the following code into the terminal:

``` 
$ pip3 install spacy
```

To download the english language model, copy the code below:

```
$ python3 -m spacy download en_core_web_md
```

## 3. Usage

To run the programs, install the components above and enter the following into the terminal:
```
$ python semantic.py
```

```
$ python watch_next.py
```
