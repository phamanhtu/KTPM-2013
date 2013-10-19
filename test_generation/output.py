# Phạm Anh Tú/ K55CLC
import unittest
import inspect
import itertools
from input import main

#swap two number
def swap(a, b):
    t = b
    b = a
    a = t
 
#sort two array have len equal
def sortTwoArray(Arr1, Arr2):
    Arr1={}
    Arr2={}
    for i in range(0,len(Arr1)):
        if Arr1[i] > Arr1[i+1]:
            swap(Arr1[i], Arr1[i+1])
            swap(Arr2[i], Arr2[i+1])
 
doc = inspect.getdoc(main)
docs = doc.splitlines()
 
#normalization string
def normalization(text):    
    variable,words = text.split(":")
    words=words.strip()
    num = words.replace("][", ";")
    num2 = num.replace("]", "")
    num3 = num2.replace("[", "")
    number = num3.split(";")  
    
    Arr1 = {}
    Arr2 = {}
    k = 0
    i = 0
    while i < len(number) :
        Arr1[k] = int(number[i])
        Arr2[k] = int(number[i+1])
        i = i+2
        k = k+1
    sortTwoArray(Arr1, Arr2)

    count = 0
    for i in range(0, len(Arr1)-1):
        if Arr1[i+1] <= Arr2[i]:
            count = count + 1
    if count > 0:
        raise Exception("wrong input!")
    else:    
        num1 = sorted(number, key=int)
        final_array = []
        b = int(0)
        i = 0
        while True:
            x = int(num1[b])
            y = int(num1[b+1])
            ans = (x + y)/2
            final_array.append(ans)
            b = b + 2
            if b == len(num1):
                break
        return final_array

#Ket hop 2 mang
'''def mergeArray(L1,L2):
    leng1=len(L1)
    leng2=len(L2)
    b=[]
    for i in range(0,leng1):
        for j in range(0,leng2):
                str1 = L1[i]
                str2 = L2[j] 
                d = str(str1)+';'+ str(str2)
                b.append(d)
    return b'''

#Tao test cases
def testCase(docs):
    bigArray=[]
    i = 0
    for line in docs:
        bigArray.append(normalization(line))
        i = i+1
    a = list(itertools.product(*bigArray))
    return a

class Test(unittest.TestCase):
    pass

def test_generator(a,b):
    def test(self):
        self.assertEqual(a,b)
    return test

result = testCase(docs)

i=0
if __name__ == '__main__':
    for t in result:
        test_name = 'testName'+str(i)
        test = test_generator(main(*t),"tam giac deu")
        setattr(Test, test_name, test)
        i = i+1
    unittest.main()