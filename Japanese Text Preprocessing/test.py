from ja_word_tokenize import Tokenizer
from ja_sentence_tokenize import SentenceTokenizer

sent_tokenizer = SentenceTokenizer()
mecab_tokenizer = Tokenizer()

tokens =  mecab_tokenizer.tokenize("意識混濁")
print (tokens)

sentence_tokens = sent_tokenizer.tokenize("我輩は猫である。名前はまだない")
print (sentence_tokens)