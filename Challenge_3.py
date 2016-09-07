#Author - Anwaar Bastien
#Code2040 Challenge

import requests
import json

initreq = {'token': 'a7063e277631887fc81e0ed9a3a437f5', 'github': 'https://github.com/abastien236/Code2040.git'}
r1 = requests.post('http://challenge.code2040.org/api/register', data = initreq)
print(r1.text)

r2 = requests.post('http://challenge.code2040.org/api/reverse', {'token': 'a7063e277631887fc81e0ed9a3a437f5'})
print(r2.text)

def reversed_string(a_string):
    return a_string[::-1]

retStr = reversed_string(r2.text)
print(retStr)

retChal = {'token': 'a7063e277631887fc81e0ed9a3a437f5', 'string': retStr}
r3 = requests.post('http://challenge.code2040.org/api/reverse/validate', retChal)
print(r3.text)

temp = {'token': 'a7063e277631887fc81e0ed9a3a437f5'}
r4 = requests.post('http://challenge.code2040.org/api/haystack', temp)
json_data = json.loads(r4.content)

#print 'Needle' + json_data['needle']
count = 0

for f in json_data['haystack']:
    if f == json_data['needle']:
        index = count
    count= count + 1
    #print(f)

#print 'Index is:' + index
retInd = {'token': 'a7063e277631887fc81e0ed9a3a437f5', 'needle': index}
r5 = requests.post('http://challenge.code2040.org/api/haystack/validate', retInd)
#print(r5.text)
