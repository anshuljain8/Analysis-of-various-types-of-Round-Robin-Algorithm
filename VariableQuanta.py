import time
def min(A):
    min=A[0]
    for i in range(len(A)):
        if min>A[i]:
            min=A[i]
    return A.index(min)

def max(A):
    max=A[0]
    for i in range(len(A)):
        if max<A[i]:
            max=A[i]
    return A.index(max)

class Dup_process:
    def __init__(self, id, bt, ar):
        self.id = id
        self.bt = bt
        self.ar = ar


class Existing_Processes:
    def __init__(self,id=[],bt=[],ar=[]):
        self.id=id
        self.bt=bt
        self.ar=ar



    def set_id_bt_ar(self,id,bt,ar):
        self.id.append(id)
        self.bt.append(bt)
        self.ar.append(ar)



    def FindWaitingTime(self,wt,q):
        readyQueue=[]
        context=[]
        quantam=0
        t=0
        n=len(wt)
        dup_process=Dup_process(self.id[:],self.bt[:],self.ar[:])
        k=0
        z=dup_process.ar[0]
        for i in range(len(dup_process.ar)):
            if dup_process.ar[i]!=z:
                k=1
        sequence=''
        #for same arrival time:
        if k==0:
            for i in range(len(self.ar)):
                idx=min(dup_process.bt)
                readyQueue.append([dup_process.id.pop(idx),dup_process.bt.pop(idx),dup_process.ar.pop(idx)])
            t=z
            n=len(readyQueue)
            quantam=(readyQueue[n-1][1]+readyQueue[n-2][1])/2
            while len(readyQueue)>0:
                n=len(readyQueue)
                for i in range(n):
                    current=readyQueue.pop(0)
                    if current[1]>quantam:
                        t=t+quantam
                        current[1]=current[1]-quantam
                        context.append(current[0])
                        if len(context) >= 2:
                            if context[-1] == context[-2]:
                                context.pop()
                        sequence=sequence+'P'+str(current[0]+1)+str([quantam])+'->'
                    else:
                        t=t+current[1]
                        wt[current[0]]=t-self.bt[current[0]]
                        context.append(current[0])
                        if len(context) >= 2:
                            if context[-1] == context[-2]:
                                context.pop()
                        sequence=sequence+'P'+str(current[0]+1)+str([current[1]])+'->'
                        current[1]=0

                    if current[1]!=0:
                        readyQueue.append(current)

                if len(readyQueue)!=0:
                    currentbt = []
                    for i in range(len(readyQueue)):
                        currentbt.append(readyQueue[i][1])
                    idx=max(currentbt)
                    quantam=(quantam+currentbt[idx])/2
            print('sequence is' )
            print(sequence)
        #for different arrival time:
        else:
            requestQueue=[]
            for i in range(len(self.ar)):
                idx=min(dup_process.ar)
                requestQueue.append([dup_process.id.pop(idx),dup_process.bt.pop(idx),dup_process.ar.pop(idx)])
            quantam=requestQueue[0][1]
            t=requestQueue[0][2]
            readyQueue.append(requestQueue.pop(0))
            first_time=0
            while(readyQueue):
                if(first_time==0):
                    current=readyQueue.pop(0)
                    context.append(current[0])
                    if len(context) >= 2:
                        if context[-1] == context[-2]:
                            context.pop()
                    sequence=sequence+'P'+str(current[0]+1)+str([quantam])+'->'
                    t=t+quantam
                    current[1]=current[1]-quantam
                    wt[current[0]]=t-self.bt[current[0]]-self.ar[current[0]]

                    while len(requestQueue)>0:
                        if (t >= requestQueue[0][2]):
                            readyQueue.append(requestQueue.pop(0))
                        else:
                            break
                    arrival_list=[]
                    for i in range(len(readyQueue)):
                        arrival_list.append(readyQueue[i])
                    arrival_list.sort(key=lambda arrival_list: arrival_list[2])
                    readyQueue.sort(key=lambda readyQueue: readyQueue[1])
                    if(len(arrival_list)>1):
                        quantam=((quantam+readyQueue[-1][1])/2)-((arrival_list[0][2]+arrival_list[1][2])/2)
                    else:
                        quantam=((quantam+readyQueue[-1][1])/2)-(arrival_list[0][2])


                else:
                    arrival_list=[]
                    for i in range(len(readyQueue)):
                        arrival_list.append(readyQueue[i])
                    arrival_list.sort(key=lambda arrival_list: arrival_list[2])
                    if(((quantam+readyQueue[-1][1])/2)-(arrival_list[0][2]/2)>0):
                        quantam=((quantam+readyQueue[-1][1])/2)-(arrival_list[0][2]/2)
                    else:
                        quantam=quantam
                n=len(readyQueue)
                for i in range(n):
                    current=readyQueue.pop(0)
                    if current[1]>quantam:
                        t=t+quantam
                        current[1]=current[1]-quantam
                        context.append(current[0])
                        if len(context) >= 2:
                            if context[-1] == context[-2]:
                                context.pop()
                        sequence=sequence+'P'+str(current[0]+1)+str([quantam])+'->'
                    else:
                        t=t+current[1]
                        wt[current[0]]=t-self.bt[current[0]]-self.ar[current[0]]
                        context.append(current[0])
                        if len(context) >= 2:
                            if context[-1] == context[-2]:
                                context.pop()
                        sequence=sequence+'P'+str(current[0]+1)+str([current[1]])+'->'
                        current[1]=0

                    if current[1]!=0:
                        readyQueue.append(current)
                first_time+=1
        print('The Sequence is: ')
        print(sequence)
        print('Number of context switches are:',len(context))
        return len(context)


