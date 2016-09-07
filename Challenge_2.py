# Author - Anwaar Bastien
# Code2040 Challenge

import requests

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