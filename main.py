#!/usr/bin/evn python
#coding:utf-8

#python MyWords
#Author      : Yuangy
#Mail        : 178404013@qq.com
#Create      : 2017-05-20
#Version     : 1.0
#Descriptoin : my own dict for englist vocabulary study

import sys
import re
import os
import dbapi

try:
  import xml.etree.cElementTree as ET
except ImportError:
  import xml.etree.ElementTree as ET

class MyDict:
    '''applicantion class '''
    def __init__(self,config):
        self.cfg = self.configure(config)


    def configure(self):
        if not os.path.exists(self.cfg):
            print("configure file not exists!")
            sys.exit(1)
        try:
            tree=ET.parse(self.cfg)
            root=tree.getroot()

        except Exception,e:
            print("xml parse fail! %s" % (e))
            sys.exit(1)

    def run(self):
        pass

class View:
    '''MVC mode view'''
    def __init__(self,module):
        self.module = module

class Control:
    '''MVC mode control'''
    def __init__(self,module):
        self.module = module

if __name__ == '__main__':
    main()

