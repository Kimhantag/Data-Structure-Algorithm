
def insert(bag, e):
    bag.append(e)
def remove(bag, e):
    bag.remove(e)

myBag=[]
insert(myBag, '휴대폰')
insert(myBag, '지갑')
insert(myBag, '손수건')
insert(myBag, '빗')
insert(myBag, '자료구조')
insert(myBag, '야구공')
print('가방속의 물건:', myBag)

insert(myBag, '빗')
remove(myBag, '손수건')
print('가방속의 물건:', myBag)






