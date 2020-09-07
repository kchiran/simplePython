import math

testList = [0,'1',2,3,4,5, 'ram', 'shyam', 'harry', 'sita', 'gita', 'shiva', 'shambho', 6, True]
print([x for x in testList if isinstance(x,int) and not isinstance(x,bool)])
print([x for x in testList if isinstance(x,str) and not isinstance(x,bool)])
