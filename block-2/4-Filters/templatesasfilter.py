arr=[1,-1,1,1,-1,1,0,-1,0,-1,0,0,0,1,-1,-1,-1,0,0,0,1,0,-1]
template=[0,0,1,-1]

def checkbestcorrelation(array , template):
    score=[]
    for i in range(len(array)- len(template)):
        tmp=0
        for j in range(len(template)):
             if template[j]==array[i+j] :
                 tmp=tmp+1
        score.append(tmp)
    result=score.index(max(score))
    print(score)
    return(result)
result=checkbestcorrelation(arr , template)
print(result)
