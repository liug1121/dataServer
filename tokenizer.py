# encoding=utf-8
import jieba

class Analyzer:
    def __init__(self):
        pass
    def cutWords(self, strWords):
        segWords = jieba.cut(strWords, cut_all=False)
        return segWords