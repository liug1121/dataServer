#create services here
from educationApp.models import Datas, Index
from difflib import SequenceMatcher
import  os
import educationApp.utils as utils
from educationApp.tokenizer import Analyzer
from educationApp.gensimUtils import Similar
class DataService:
    def __init__(self):
        pass

    def getDatas(self, name):
        datas = self.getDatasByIndex(name)
        return datas
    
    def getAllIndex(self, name):
        matcherService = NameMatcherService()
        allIndex = matcherService.getAllIndex(name)
        return allIndex

    def getDatasByIndex(self, index):
        dataName = index
        fileDatas = utils.readJsonFromTxtFile('/Users/liug/Documents/dataSearch/files/' + dataName + '.txt')
        dataNodes = fileDatas['returndata']['datanodes']
        nodesNames = [{'cname':cname['cname'], 'code':cname['code']} for cname in fileDatas['returndata']['wdnodes'][0]['nodes']]
        colName = []
        col2018 = []
        col2017 = []
        col2016 = []
        col2015 = []
        col2014 = []
        col2013 = []
        col2012 = []
        col2011 = []
        col2010 = []
        col2009 = []
        for nodeName in nodesNames:
            cname = nodeName['cname']
            code = nodeName['code']
            colName.append(cname)
            for dataNode in dataNodes:
                if(dataNode['code'] == 'zb.' + code + '_sj.2018'):
                    col2018.append(dataNode['data']['data'])
                if(dataNode['code'] == 'zb.' + code + '_sj.2017'):
                    col2017.append(dataNode['data']['data'])
                if(dataNode['code'] == 'zb.' + code + '_sj.2016'):
                    col2016.append(dataNode['data']['data'])
                if(dataNode['code'] == 'zb.' + code + '_sj.2015'):
                    col2015.append(dataNode['data']['data'])
                if(dataNode['code'] == 'zb.' + code + '_sj.2014'):
                    col2014.append(dataNode['data']['data'])
                if(dataNode['code'] == 'zb.' + code + '_sj.2013'):
                    col2013.append(dataNode['data']['data'])
                if(dataNode['code'] == 'zb.' + code + '_sj.2012'):
                    col2012.append(dataNode['data']['data'])
                if(dataNode['code'] == 'zb.' + code + '_sj.2011'):
                    col2011.append(dataNode['data']['data'])
                if(dataNode['code'] == 'zb.' + code + '_sj.2010'):
                    col2010.append(dataNode['data']['data'])
                if(dataNode['code'] == 'zb.' + code + '_sj.2009'):
                    col2009.append(dataNode['data']['data'])    
        
        tableData = []
        row = 0
        for col in colName:
            data = {"name": col, "2018":col2018[row], "2017":col2017[row], "2016":col2016[row],
             "2015":col2015[row], "2014":col2014[row], "2013":col2013[row], "2012":col2012[row],
             "2011":col2011[row], "2010":col2010[row], "2009":col2009[row]}
            tableData.append(data)
            row = row + 1
        '''
        tableDatas = {'指标':colName,
            '2018': col2018,'2017':col2017,'2016':col2016,'2015':col2015,'2014':col2014,'2013':col2013,'2012':col2012,'2011':col2011,'2010':col2010,'2009':col2009}
        '''
        datas = Datas('', index)
        datas.setDatas(tableData)
        return datas
    
class NameMatcherService:
    def __init__(self):
        pass
    
    def createWordsCorpora(self):
        corpora = []
        for filename in os.listdir('/Users/liug/Documents/dataSearch/files'):
            if filename.endswith(".txt") :
                corpora.append(filename[:-4])
        return corpora
            
    def getIndex(self, nameForMatch):
        analyzer = Analyzer()
        segWords = analyzer.cutWords(nameForMatch)
        wordCorpora = self.createWordsCorpora()
        sim = Similar(Similar.EDUCATION, wordCorpora)
        similaries = sim.similary(nameForMatch)
        index = ''
        for documentNumber, score in sorted(enumerate(similaries), key=lambda x: x[1], reverse=True):
            index = wordCorpora[documentNumber]
            break
        return index
    
    def getAllIndex(self, nameForMatch):
        analyzer = Analyzer()
        segWords = analyzer.cutWords(nameForMatch)
        wordCorpora = self.createWordsCorpora()
        sim = Similar(Similar.EDUCATION, wordCorpora)
        similaries = sim.similary(nameForMatch)
        allIndex = []
        for documentNumber, score in sorted(enumerate(similaries), key=lambda x: x[1], reverse=True):
            index = wordCorpora[documentNumber]
            allIndex.append(index)
        return allIndex
            
    
    