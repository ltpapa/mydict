#!/usr/bin/evn python
#coding:utf-8
import dbapi
import re

class ArticleAnalyse:
    '''article analyse'''
    def __init__(self,article):
        self.article = article
        self.num_paragraph = 0
        self.num_cause = 0
        self.num_words = 0
    
    def trip(self):
        '''delete all non english words'''
        self.article = re.sub('[^a-zA-Z:.,!-()[]]')
        self.article = self.article.lower()

    def split_paragraph(self):
        '''split an article into paragraphs'''
        self.paralist = self.article.split("\n")

    def split_cause(self,para):
        '''split a paragraph into cause list'''
        return para.split(".!?")

    def split_word(self,cause):
        '''split a cause into word list'''
        return cause.split(' ')

    def get_causes(self):
        '''get all causes in the article'''
        for c in self.paralist:
            if c != ' ':
                self.causelist.append(self.split_cause(c))

    def get_words(self):
        '''get all words'''
        for w in self.causelist:
            if w != '':
                self.wordlist.append(self.split_word(w))

    def trip_same_words(self):
        '''strip all repeative words'''
        self.wordset = set(self.wordlist)

    def get_article_static(self):
        countdict = {}
        for w in self.wordset:
            countdict[w] = self.wordlist.count(w)
        l = sorted(countdict.items(), key=lambda d:countdict[1])
        for w in l:
            print('%s appear %d times.' % (w,countdict[w]))

    def db_check(self,w):
        return dbapi.getword(w)
