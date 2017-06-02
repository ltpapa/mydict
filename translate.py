#!/usr/bin/env python
#-*- coding:utf-8 -*-

import json
import urllib
api_key = '1932136763'
keyfrom = 'aioiyuuko'
query_url = 'http://fanyi.youdao.com/openapi.do?keyfrom=%s&key=%s&type=data&doctype=json&version=1.1&q=%s'
cData = {
    'errorCode':{
        '0': u'success',
        '20': u'要求翻译的文本过长',
        '30': u'无法进行有效的翻译',
        '40': u'不支持的语言类型',
        '50': u'无效的key',
        '60': u'无词典结果，仅在获取词典结果生效',
        'other': u'查询失败，出现未知错误',
        'noQuery': u"查询失败，有道openapi返回异常"
    },
    'vimEncoding': 'utf-8',
    'info': (query_url, keyfrom, api_key)
}

def dictSearch(queryWords):
    initData = cData['info'][1:] + (urllib.quote(queryWords),)
    queryUrl   = cData['info'][0] % initData
    dataBack   = urllib.urlopen(queryUrl).read().decode('utf-8')
    try:
        dataJson   = json.loads(dataBack)
        doWord(dataJson)
    except ValueError:
        print(cData['errorCode']['noQuery'])

def doWord(searchResult):
    word = {'name':'','translation':'','explains':'','web':''}
    error_code = searchResult['errorCode']
    if error_code == 0:
        queryStr = searchResult['query'].split('\n')
        queryStr = ( (item[0], item[1].strip()) for item in enumerate(queryStr) if item[1].strip() != '' )
        for eachline in queryStr:
            word['name'].append(eachline) 
        tranlas = ( item for item in enumerate(searchResult['translation']) )
        for eachline in tranlas:
            word['translation'].append(eachline)
        if 'basic' in searchResult and 'explains' in searchResult['basic']:
            explains = ( item for item in enumerate(searchResult['basic']['explains']) )
            for eachline in explains:
                word['explains'].append(eachline)
        if 'web' in searchResult:
            webs = ( item for item in enumerate(searchResult['web']) )
            for eachline in webs:
                word['web'].append(eachline)
        return word
    else:
        print(cData['errorCode'][str(error_code)])
        return None
