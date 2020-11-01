def solution(args):
	z=[]
	x=[]
	N = len(args)
	for j in range(N-2):
		if args[j+1]-args[j]==1 and args[j+2]-args[j+1]==1:
			z.append(args[j+1])
	ss = []
	for e in args:
		if not e in z:
			ss.append(e)
		else:
			ss.append('-')
	####################
	r = [ss[0]]
	i = 1
	j = 0
	while i < len(ss):
	    if r[j] != ss[i]:
	        r.append(ss[i])
	        j += 1
	    i += 1
	####################
	alp = r
	c = 0
	while c < len(alp)-1 :
		if type(alp[c]) is int and type(alp[c+1]) is int:
				alp.insert(c+1,',')
		c =c + 1
		pass
	
	makeitastring = ''.join(map(str, alp)) 
	print(makeitastring)
	return makeitastring

solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11])
solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20,21,2453,34523,2345234,36435634,1232413525])
solution([-3,-2,-1,2,10,15,16,18,19,20])
solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20])
solution([1,2,3,4,5])
solution([1,2,3,4,5])
