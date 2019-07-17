import MeCab
from collections import namedtuple

Morpheme = namedtuple("Morpheme", "surface pos pos_s1 pos_s2 pos_s3 conj form")


class Tokenizer:
    """

    """
    def __init__(self, **kwargs):
        """

        Args:
            **kwargs:
        """
        self.__mecab = MeCab.Tagger(**kwargs)
        self.__mecab.parse("Initialize parse.")

    def tokenize(self, text):
        """

        Args:
            text:

        Returns:

        """
        return [m.surface for m in self.__iter_morpheme(text)]

    def tokenize_with_nlp(self, text):
        """

                Args:
                    text:

                Returns:

                """
        return [m for m in self.__iter_morpheme(text)]

    def __iter_morpheme(self, text):
        """

        Args:
            text:

        Returns:

        """
        node = self.__mecab.parseToNode(text)
        node = node.next
        while node:
            surface = node.surface.encode('utf-8')[:node.length].decode('utf-8')
            features = node.feature.split(",")
            if surface != "":
                yield Morpheme(surface, *features[:6])

            node = node.next




#################TEST#################
# mecab_tokenizer = Tokenizer()
# tokens =  mecab_tokenizer.tokenize("意識混濁")
# print (tokens)