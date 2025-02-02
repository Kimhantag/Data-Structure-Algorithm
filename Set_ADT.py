#Set ADT
#2018015027 김한탁
#리스트를 이용한 집합의 구현

class Set:
    def __init__( self ):
        self.items = []
    def size( self ):
        return len( self.items )
    def display( self, msg ):
        print(msg, self.items)
    def contains( self, item):
        return item in self.items
    def insert( self, elem):
        if elem not in self.items :
            self.items.append(elem)
    def delete(self, elem):
        if elem in self.items :
            self.items.remove(elem)
    def union(self, setB):
        setC = Set()
        setC.items=self.items
        for elem in setB.items :
            if elem not in self.items:
                setC.items.append(elem)
        return setC
    def intersect(self, setB):
        setC = Set()
        for elem in setB.items:
            if elem in self.items:
                setC.items.append(elem)
        return setC
    def difference( self, setB):
        setC = Set()
        for elem in self.items:
            if elem not in setB.items:
                setC.items.append(elem)
        return setC
                
setA=Set()
setA.insert('휴대폰')
setA.insert('지갑')
setA.insert('손수건')
setA.display('Set A:')          

setB=Set()
setA.insert('빗')
setA.insert('파이썬 자료구조')
setA.insert('야구공')
setA.insert('지갑')
setA.display('Set B:')   

setB.insert('빗')
setA.delete('손수건')
setA.delete('발수건')
setA.display('Set A:')     
setB.display('Set B:')

setA.union(setB).display('A U B:')
setA.intersect(setB).display('A ^ B:')
setA.difference(setB).display('A -B:')
