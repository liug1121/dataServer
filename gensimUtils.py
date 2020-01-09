# encoding=utf-8
from gensim import corpora, models, similarities
import jieba
import os
class Similar:
    EDUCATION = 1
    instance = None
    
    def __new__(cls, type, ducuments):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            cls.instance.type = type
            cls.instance.create(ducuments)
        return cls.instance

    def getType(self):
        return self.type
    
    def create(self, documents):
        wordCorpora = []
        for document in documents:
            segWords = [word for word in jieba.cut(document)]
            wordCorpora.append(segWords)
        self.dictionary = corpora.Dictionary(wordCorpora)
        bowCorpus = [self.dictionary.doc2bow(text) for text in wordCorpora]
        self.tfidfModel = models.TfidfModel(bowCorpus)
        self.similarityIndex = similarities.SparseMatrixSimilarity(self.tfidfModel[bowCorpus], num_features = len(self.dictionary.keys()))
    
    def similary(self, words):
        segWords = [word for word in jieba.cut(words)]
        segWordsVec = self.dictionary.doc2bow(segWords)
        similarities = self.similarityIndex[self.tfidfModel[segWordsVec]]
        return similarities  
    
def createWordsCorpora():
    corpora = []
    for filename in os.listdir('/Users/liug/Documents/dataSearch/files'):
        if filename.endswith(".txt") :
            corpora.append(filename[:-4])
    return corpora
wordCorpora = createWordsCorpora()
sim = Similar(Similar.EDUCATION, wordCorpora)
similaries = sim.similary("高中毕业生数")
for documentNumber, score in sorted(enumerate(similaries), key=lambda x: x[1], reverse=True):
    print(wordCorpora[documentNumber] + ',               ' + str(score))
    #index = wordCorpora[documentNumber]


    