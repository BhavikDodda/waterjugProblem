##Info
Max=[3,5,8]
Start=[3,5,0]
l=len(Start)
Nodes=[]
Nodes.append(Start)
Edges={0:[]}
## Graph generating

def addNew(n,newNode):
    if newNode not in Nodes:
        Nodes.append(newNode)
        Edges[len(Nodes)-1]=[]
    Edges[n].append(Nodes.index(newNode))


def analyze(n):
    getNode=Nodes[n]
    ff=list(filter(lambda x:getNode[x]<Max[x],range(l))) ## getting the positions where it has extra capacity to fill in more water
    for p in ff:
        for i in range(l):
            copyNode=getNode[:]
            copyNode[p]=min(Max[p],getNode[i]+getNode[p])
            newvalfori=getNode[i]-(copyNode[p]-getNode[p])
            if i!=p and newvalfori>=0 and getNode[i]!=0:
                copyNode[i]=newvalfori
                ##print(copyNode,p,i)
                addNew(n,copyNode)



while ([] in list(Edges.values())):
    N=(list(Edges.keys())[list(Edges.values()).index([])])
    analyze(N)


print(f'Nodes {Nodes}',f'Edges {Edges}')
print(f'Number of Nodes: {len(Nodes)}')

## Find path
def NodesPointingToaNode(n):
    #return (list(map(lambda y:list(Edges.keys())[y],list(filter(lambda x:n in list(Edges.values())[x],range(len(list(Edges.values()))))))))
    return ([list(Edges.keys())[y] for y in list(filter(lambda x:n in list(Edges.values())[x],range(len(list(Edges.values())))))])

End=[0,4,4]##Nodes[len(Nodes)-1]
IndexInNodes=Nodes.index(End)
Connections={IndexInNodes:(0,IndexInNodes)}
Next=[IndexInNodes]

while len(Next)>0:
    curr=Next[0]
    Next.pop(0)
    for k in NodesPointingToaNode(curr):
        if k not in Connections.keys():
            Connections[k]=(Connections[curr][0]+1,curr)
            Next.append(k)

Path=[(0,Start)]
while Path[len(Path)-1][0]!=IndexInNodes:
    s=Connections[Path[len(Path)-1][0]][1]
    Path.append((s,Nodes[s]))

answer=[k[1] for k in Path]
print(answer,f'{len(answer)} steps')

