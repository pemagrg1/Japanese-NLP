import MeCab
from collections import namedtuple

Morpheme = namedtuple("Morpheme", "surface pos pos_s1 pos_s2 pos_s3 conj form")


class POSTagger:
    """

    """
    def __init__(self, **kwargs):
        """

        Args:
            **kwargs:
        """
        self.__mecab = MeCab.Tagger(**kwargs)
        self.__mecab.parse("Initialize parse.")

    def pos_tag(self, text):
        """

        Args:
            text:

        Returns:

        """
        dict = {}
        for m in self.__iter_morpheme(text):
            if m.surface != "":
               dict[m.surface]=m.pos
        return dict
        # return [m.surface for m in self.__iter_morpheme(text)]


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
            yield Morpheme(surface, *features[:6])

            node = node.next

###TEST####
# mecab_pos = POSTagger()
# pos_tags =  mecab_pos.pos_tag("意識混濁")
# print (pos_tags)