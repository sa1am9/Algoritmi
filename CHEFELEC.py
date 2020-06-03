for _ in range(int(input())):
    n=int(input())
    s=list(input())
    coord=list(map(int,input().split()))
    dist =0
    i=0
    with_elect=[]
    for i in range(0,n):
        if s[i]=='1':
            with_elect.append(i)

    if with_elect[0]!=0:
        dist =dist +coord[with_elect[0]]-coord[0]

    if with_elect[len(with_elect)-1]!=n-1:
        dist =dist +coord[n-1]-coord[with_elect[len(with_elect)-1]]

    for j in range(0,len(with_elect)-1):

        if with_elect[j]+1==with_elect[j+1]:
            continue

        if with_elect[j+1]-with_elect[j]-1==1:
            dist =dist +min(coord[with_elect[j]+1]-coord[with_elect[j]],
                            coord[with_elect[j+1]]-coord[with_elect[j]+1])

        else:
            y=min(coord[with_elect[j+1]]-coord[with_elect[j]+1],
                  coord[with_elect[j+1]-1]-coord[with_elect[j]])
            
            for k in range(with_elect[j]+1,with_elect[j+1]-1):
                y=min(y,coord[k]-coord[with_elect[j]]+coord[with_elect[j+1]]-coord[k+1])
            dist =dist +y
    print(dist)
