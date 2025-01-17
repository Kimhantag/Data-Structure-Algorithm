#LineEditor
#2018015027 김한탁
#라인 편집기 기능

class ArrayList:
    def __init__( self ):
        self.items = []
    def insert(self, pos, elem):
        self.items.insert(pos, elem)
    def delete(self, pos):
        return self.items.pop(pos)
    def isEmpty(self): 
        return self.size() == 0        
    def getEntry(self, pos):
        return self.items[pos]
    def find(self, item): 
        return self.items.index(item)        
    def size(self): 
        return len(self.items)
    def clear(self):
        self.items = []
    def replace(self, pos, elem): 
        self.items[pos] = elem
    def sort(self): 
        self.items.sort()
    def merge(self, lst): 
        self.items.extend(lst)
    def display(self, msg='ArrayList:'):
        print(msg, '항목수=', self.size(), self.items) 
        
def myLineEditor() :
    list= ArrayList()
    while True:
        command = input("[메뉴선택] i-입력, d-삭제, r-변경, p-출력, ㅣ-파일읽기, s-저장, q-종료=> ")
                        
        if command == 'i':
            pos=int(input(" 입력행 번호:"))
            str=input(" 입력행 내용: ")
            list.insert(pos, str)
        elif command == 'd':
            pos=int(input(" 삭제행 번호: "))
            list.delete(pos)
        elif command == 'r':
            pos=int(input(" 변경행 번호:"))
            str=input(" 변경행 내용: ")
            list.replace(pos, str)
        elif command == 'q' : return