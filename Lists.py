#LISTS
l=[10,20,30,40,50]
l.extend([60,70])
print(l)
#l.append([60,70])
#print(l)
#l.extend('python')
#print(l)
#l.append('python')
#print(l)
#l.insert(5,60)
#print(l)
#l1=l
#print(id(l),id(l1))
#l.append(60)
#print(l,l1)
#l1=l.copy()
#l.append(60)
#print(l,l1)
#print(id(l),id(l1))
#print(l,l.pop())
#print(l,l.pop(2))
#print(l,l.remove(50))
#l.clear()
#print(l,id(l))
#del l
#print(l)
#l.sort()
#print(l)
#l.reverse()
#print(l)
#l=sorted(l)
#print(l)
#print(l.index(40))
#print(l.count(10))
#print(l + [60])
#print(l * 2)

#TUPLE
#t=tuple(l)
#print(t)
#t=('a','b',10,20)
#k=list(t)
#print(k)

#DICTIONARY
d={'name':'Teja','rollno':520}
#print(d)
#print(d['name'])
#d['phno']=1234567890
#print(d)
#print(d.get('name'))
#print(d.get('age'))
#print(d.get('age',20))
#print(d.get('age','key does not exists'))
#print(d.setdefault('name'))
#print(d.setdefault('age'))
#print(d)
#print(d.setdefault('age',19))
#print(d)
#for key in d:
#	print(key,d[key])
#print(d.keys())
#print(d.values())
#print(d.items())
#l1=[10,20]
#l2=[40,50]
#d1=dict(zip(l1,l2))
#print(d1)
#l=[1,2,3]
#d1=dict.fromkeys(l,0)
#print(d1)
#d1={1:1,2:4}
#d.update(d1)
#print(d)
#r=d.pop('rollno')
#print(d,r)
#r=d.popitem()
#print(d,r)
#d.clear()
#print(d)
#del d
#print(d)
