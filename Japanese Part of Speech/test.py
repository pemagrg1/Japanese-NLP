from mecab_pos import POSTagger

mecab_pos = POSTagger()
pos_tags =  mecab_pos.pos_tag("意識混濁")
print (pos_tags)