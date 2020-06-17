"""
pip install spacy[ja]
! python -m spacy download ja_core_news_lg

"""
import spacy


ja_nlp = spacy.load("ja_core_news_lg")

doc1 = ja_nlp("大和さんは佐藤健の父。佐藤健のお母さんはさくらさん。")

try:
    for ent in doc1.ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_)
except Exception as e:
    print(e)

