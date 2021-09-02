Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # question 2
>>> 5**9
1953125
>>> 3//2
1
>>> 7/3
2.3333333333333335
>>> 6==6
True
>>> a=20; a+=30; a%=3; print(a)
2
>>> True * False
0
>>> True & False
False
>>> True and False
False
>>> ((6>3) and (7<4) or (18==3)) and (9>3)
False
>>> True is False
False
>>> False in 'False'
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    False in 'False'
TypeError: 'in <string>' requires string as left operand, not bool
>>> ((True=Ffalse
  
SyntaxError: invalid syntax
>>> ((True==False) or (False > True)) and (False <= True)
False
>>> 
>>> # question 3
>>> s1='nice to have it'
>>> s2=' here'
>>> s1+s2
'nice to have it here'
>>> 
>>> # question 4
>>> a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
>>> a[3][1][2]
['hello']
>>> 
>>> # question 5
>>> a.insert(0,s1)
>>> a.append(s2)
>>> print(a)
['nice to have it', 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7, ' here']
>>> 
>>> # question 6
>>> numbers = [386,462,47,418,987,344,236,375,823,566,597,978,328,615,953,345,399,162,758,219,918,237,412,566,826,248,866,950,626,949,687,217,815,67,104,58,512,24,892,767,553,81,379,843,831,445,742,717,958,743,958,742,527]
>>> for x in numbers:
	if x==237:
	    print(x)
	    break;
	elif x%2==0:
	    print(x)

	    
386
462
418
344
236
566
978
328
162
758
918
237
>>> 
>>> # question 7
>>> color_list_1=set(["White","Black","Red"])
>>> color_list_2=set(["Red","Green"])
>>> 
>>> color_list_1.difference(color_list_2)
{'Black', 'White'}
>>> 
>>> # question 9
>>> a = int(input("Input an integer : "))
Input an integer : 5
>>> n1 = int("%5"%a)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    n1 = int("%5"%a)
ValueError: incomplete format
>>> n1 = int( "%5" % a )
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    n1 = int( "%5" % a )
ValueError: incomplete format
>>> n1 = ("%s" % a)
>>> n2 = ("%s%s" % (a,a))
>>> n3 = ("%s%s%s" % (a,a,a))
>>> print(n1+n2+n3)
555555
>>> 