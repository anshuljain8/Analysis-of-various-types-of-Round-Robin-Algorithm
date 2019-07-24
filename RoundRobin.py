def min_index(A):
    min=A[0]
    for i in range(len(A)):
        if min>A[i]:
            min=A[i]
    return A.index(min)

class Dup_process:
    def __init__(self, id, bt, ar):
        self.id = id
        self.bt = bt
        self.ar = ar


class Processes:

    def __init__(self,id=[],bt=[],ar=[]):
        self.id=id
        self.bt=bt
        self.ar=ar



    def set_id_bt_ar(self,id,bt,ar):
        self.id.append(id)
        self.bt.append(bt)
        self.ar.append(ar)



    def FindWaitingTime(self,wt,quantam):
        readyQueue=[]
        t=0
        n=len(wt)
        context=[]
        dup_process=Dup_process(self.id[:],self.bt[:],self.ar[:])
        requestQueue=[]
        sequence=''
        for i in range(len(self.ar)):
            idx=min_index(dup_process.ar)
            requestQueue.append([dup_process.id.pop(idx),dup_process.bt.pop(idx),dup_process.ar.pop(idx)])
        readyQueue.append(requestQueue.pop(0))
        t=readyQueue[0][2]
        while len(readyQueue)>0:
            current=readyQueue.pop(0)
            if current[1]>quantam:
                t=t+quantam
                current[1]=current[1]-quantam
                context.append(current[0])
                if len(context) >= 2:
                    if context[-1] == context[-2]:
                        context.pop()
                sequence=sequence+'P'+str(current[0])+str([quantam])+'->'
            else:
                t=t+current[1]
                wt[current[0]]=t-self.bt[current[0]]-self.ar[current[0]]
                context.append(current[0])
                if len(context) >= 2:
                    if context[-1] == context[-2]:
                        context.pop()
                sequence = sequence + 'P'+str(current[0]+1) +str([current[1]])+ '->'
                current[1]=0
            while len(requestQueue) > 0:
                if t >= requestQueue[0][2]:
                    readyQueue.append(requestQueue.pop(0))
                else:
                    break
            if current[1]!=0:
                readyQueue.append(current)
        print('sequence is' )
        print(sequence)

        print('Number of context switches are:',len(context))

        return len(context)


