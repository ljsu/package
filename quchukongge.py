def trim(s):
	n=len(s)
	if(n==0 or(s[0]!=' ' and s[n-1]!=' ')):
		return s
	elif (s[0]==' '):
		return trim(s[1:])#递归处理
	else: 
		return trim(s[:-1])