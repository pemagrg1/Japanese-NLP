import gensim


w2v_path = "ja.text.model"
w2v_model =gensim.models.Word2Vec.load(w2v_path)

word1 = "トイレ"
word2 = "洗面所"

similarity_score = w2v_model.similarity(word1,word2)
print ("Similarity score:",similarity_score)
"""
Similarity score: 0.74636817
"""
print ("Most similar word to word1",w2v_model.most_similar([word1]))
"""
Most similar word to word1 [('便所', 0.7914901971817017), ('洗面所', 0.7463681697845459), ('水洗トイレ', 0.6963348388671875), ('シャワー室', 0.6686856746673584), ('浴室', 0.6619090437889099), ('公衆便所', 0.6546213626861572), ('喫煙室', 0.6422077417373657), ('公衆トイレ', 0.6295166015625), ('待合室', 0.6250226497650146), ('便器', 0.6183037757873535)]
"""