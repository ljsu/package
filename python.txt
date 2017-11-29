汉诺塔的移动
def move(n,a,buffer,c):
	if(n==1):
		print(a,"->",c)
		return 
	move(n-1,a,c,buffer)#将a中最上面的n-1个通过c移到b
	move (1,a,buffer,c)#再将a中最下面的那个通过b移到c
	move(n-1,buffer,a,c)#最后将b中的n-1通过a移到c
move(3,"a","b","c")