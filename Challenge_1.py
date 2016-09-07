# Author - Anwaar Bastien
# Code2040 Challenge

import requests

'''Post inital request '''

initreq = {'token': 'a7063e277631887fc81e0ed9a3a437f5', 'github': 'https://github.com/abastien236/Code2040.git'}
r1 = requests.post('http://challenge.code2040.org/api/register', data = initreq)
print(r1.text)

