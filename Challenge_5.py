# Author - Anwaar Bastien
# Code2040 Challenge

import requests
import json
from datetime import datetime, timedelta


'''Post inital request '''

initreq = {'token': 'a7063e277631887fc81e0ed9a3a437f5', 'github': 'https://github.com/abastien236/Code2040.git'}
r1 = requests.post('http://challenge.code2040.org/api/register', data = initreq)
print(r1.text)

########

'''Reverse Challenge Post'''

r2 = requests.post('http://challenge.code2040.org/api/reverse', {'token': 'a7063e277631887fc81e0ed9a3a437f5'})
#print(r2.text)

def reversed_string(a_string):
    return a_string[::-1]

retStr = reversed_string(r2.text)
#print(retStr)

retChal = {'token': 'a7063e277631887fc81e0ed9a3a437f5', 'string': retStr}
r3 = requests.post('http://challenge.code2040.org/api/reverse/validate', retChal)
print(r3.text)

########

'''Haystack Challenge Post'''

temp = {'token': 'a7063e277631887fc81e0ed9a3a437f5'}
r4 = requests.post('http://challenge.code2040.org/api/haystack', temp)
json_data = json.loads(r4.content)

#print 'Needle' + json_data['needle']
count = 0

for hay in json_data['haystack']:
    if hay == json_data['needle']:
        index = count
    count= count + 1
    #print(f)

#print 'Index is:' + index
retInd = {'token': 'a7063e277631887fc81e0ed9a3a437f5', 'needle': index}
r5 = requests.post('http://challenge.code2040.org/api/haystack/validate', retInd)
print(r5.text)

########

'''Prefix Challenge Post'''
r6 = requests.post('http://challenge.code2040.org/api/prefix', temp)

jsonDic = json.loads(r6.content)
#print(jsonDic)
strArr = []

for text in jsonDic['array']:
    if jsonDic['prefix'] in text:
        continue
    else:
        strArr.append(str(text))

#print strArr

results = {'token': 'a7063e277631887fc81e0ed9a3a437f5', 'array': strArr}
r7 = requests.post('http://challenge.code2040.org/api/prefix/validate', json=results)
print r7.text

########

'''Dating Challenge Post'''

r8 = requests.post('http://challenge.code2040.org/api/dating', temp)
jsonDic = json.loads(r8.content)
#print(jsonDic)

initDate = jsonDic['datestamp']

formatDate = datetime.strptime(initDate, '%Y-%m-%dT%H:%M:%SZ')
#print(formatDate)

timestamp = (formatDate - datetime(1970, 1, 1)).total_seconds()
#print(timestamp)

timestamp += jsonDic['interval']
#print(timestamp)

formatDate = datetime(1970, 1, 1) + timedelta(seconds=timestamp)
ret = (formatDate.strftime('%Y-%m-%dT%H:%M:%SZ'))
#print ret

results = {'token': 'a7063e277631887fc81e0ed9a3a437f5', 'datestamp': ret}
r9 = requests.post('http://challenge.code2040.org/api/dating/validate', json=results)
print r9.text
