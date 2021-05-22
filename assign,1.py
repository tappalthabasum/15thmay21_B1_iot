#1.program
n = [386,462,47,418,344,236,375,823,56,597,978,328,615,953,345,399,162,758,219,918,237,412,566,826,248,866,950,626,949,687,217,815,67,104,58,512,24,892,894,767,553,81,379,843,831,445,742,717,958,743,527]



for x in n:
    if x == 237:
        print(x)
        break;
    elif x % 2 == 0:
        print(x)
#2.program
colour_list_1 = set(["white","black","red"])
colour_list_2 = set(["red","green"])
print(colour_list_1.difference(colour_list_2))
#3.program
import string, sys
def ispangram(str1,alphabet = string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <=set(str1.lower())

print(ispangram('the quick brown fox jumps over the  lazy dog'))

#4.program
n = 5
n1 = int("%s" %n)
n2 = int("%s%s" %(n,n))
n3 = int("%s%s%s" %(n,n,n))
print(n1+n2+n3)
#5.program
s= input('enter string:')
s= s.split('#')
s1 = s[0].split()
s2 = s[1].split()
s1 = [int(i) for i in s1]
s2 = [int(i) for i in s2]
print(s1)
print(s2)

 #6.program
items = "without,hello,bag,world"
words = [word for word in items.split(',')]
print(','.join(sorted(list(set(words)))))

#7.program
d = {'rahul':57,'kishore':87,'vidya':67,'raakhi':79}
print(max(d,key = d.get))
 #8.program
a = "hello world!123"
d=l=0
for c in a:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
    print("letters",l)
    print("digits",d)
###9.program
d = {'name':['akash','rahul','vishakha','akshay','soniya','vikas'],
     'subjects':['python','java','python','c','python','java'],
     'ratings':['8.4','8.2','8','9','7.8','5.6']}
newdata = {'name':[],'ratings':[]}
index = 0
for sub in d['subjects']:
    if(sub == 'python'):
        newdata['name'].append(d['name'][index])
        newdata['ratings'].append(d['ratings'][index])
        index += 1

print('new dictionary of students :',newdata)

#10.program
n  = 3
divBY7 = [i for i in range(0,n) if (i%7==0)]
print(divBY7)

def divChecker(n):
    for i in range(n):
        if i %7 == 0:
            value = True
        else:
            value = False
            print(i,value)

divChecker(n)
#11.program
pos = {"x":0,"y":0}

while True:
    
    n = input( "UP = 5,DOWN = 3,LEFT = 3,RIGHT = 2")
    if not n:
        break
    
    direction,steps=n.split()
    if direction=='UP':
        pos["y"]+=int(steps)
    elif direction=='DOWN':
        pos["y"]-=int(steps)
    elif direction=='LEFT':
        pos["x"]-=int(steps)
    elif direction=='RIGHT':
        pos["x"]+=int(steps)
print(int(round((pos["x"]**2+pos["y"]**2)**0.5)))


