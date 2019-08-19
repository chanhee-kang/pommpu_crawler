#-*- coding:utf-8 -*-
import requests
import re
import pandas as pd
import time

from bs4 import BeautifulSoup

class MainHandler :
    def __init__(self):
        self.baseUrl = None
        self.params = None

        self.endYear = None
        self.endMonth = None
        self.endDay = None


    def setEnv(self):
        self.baseUrl = "http://www.ppomppu.co.kr/search_bbs.php"
        self.params = dict( search_type = 'sub_memo',
                            page_no = 1,
                            keyword = '',
                            page_size = 20,
                            bbs_id = '',
                            order_type = 'date',
                            bbs_cate = 1 )


    def getCleanTag(self, tag):
        return re.sub('<.+?>', '', str(tag), 0).strip()

    def getSearchingItems(self, keyword, endDate):

        self.params['keyword'] = keyword
        self.params['page_no'] = 1

        # get Page Info
        data = requests.get(self.baseUrl, params = self.params)
        soup = BeautifulSoup(data.content, 'html.parser')
        _tInfoLen = len(soup.find('div','pagination').find_all('a'))
        tPage = 0
        if (_tInfoLen == 11):
            tPage = int(self.getCleanTag(soup.find('div','pagination').find_all('a')[9]))
        else :
            tPage = int(self.getCleanTag(soup.find('div','pagination').find_all('a')[4]))

        # crawling Loop
        loopAct = True
        X = {'href':[], 'text':[], 'title':[], 'boardType':[], 'hitCount':[],
             'date':[], 'likeCount':[], 'dislikeCount':[] }

        for i in range(1, tPage+1):
            if (loopAct == False) : break
            time.sleep(3)

            self.params['page_no'] = i
            data = requests.get(self.baseUrl, params = self.params)
            soup = BeautifulSoup(data.content, 'html.parser')
            try :
                itemList = soup.find('div', {'id':'result-tab1'}).find_all('div','item')
            except Exception as e:
                print (e)
                break

            for item in itemList :
                try :
                    _text = item.find('p').find('a', href=True)
                    href = _text['href']
                    text = self.getCleanTag(_text)

                    title = self.getCleanTag(item.find('span','title'))

                    _ext = item.find('p','desc').find_all('span')

                    boardType = self.getCleanTag(_ext[0])
                    hitCount = self.getCleanTag(_ext[1])
                    date = self.getCleanTag(_ext[2])
                    _dateCal = int(date.replace(".",""))
                    likeCount = self.getCleanTag(_ext[3])
                    dislikeCount = self.getCleanTag(_ext[4])

                    if (_dateCal < endDate):
                        loopAct = False
                        break

                    X['href'].append(href)
                    X['text'].append(text)
                    X['title'].append(title)
                    X['boardType'].append(boardType)
                    X['hitCount'].append(hitCount)
                    X['date'].append(date)
                    X['likeCount'].append(likeCount)
                    X['dislikeCount'].append(dislikeCount)
                except Exception as e : print(e)
        return X


    def run(self):
        self.setEnv()

        keyword = "배달의민족 김봉진"
        endYear = 2018
        endMonth = 6
        endDay = 30

        endDate = int(str(endYear) + str(endMonth).zfill(2) + str(endDay).zfill(2))

        result = self.getSearchingItems(keyword, endDate)

        DB = pd.DataFrame(result)
        DB.to_csv('result.csv')


if __name__ == "__main__":
    MH = MainHandler()
    MH.run()
