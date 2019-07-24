import time
Queue1=[]
Queue2=[]
Queue3=[]
quantam1,quantam2,quantam3=34,57,80

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

class Multi_Processes:
    def __init__(self, id=[], bt=[], ar=[]):
        self.id = id
        self.bt = bt
        self.ar = ar

    def set_id_bt_ar(self, id, bt, ar):
        self.id.append(id)
        self.bt.append(bt)
        self.ar.append(ar)

    def insert_current_process(self, requestQueue):

        if requestQueue[0][1] <= quantam1:
            Queue1.append(requestQueue.pop(0))
        elif requestQueue[0][1] <= quantam2:
            Queue2.append(requestQueue.pop(0))
        else:
            Queue3.append(requestQueue.pop(0))

    def FindWaitingTime(self, wt,q):
        context=[]
        global Queue1, Queue2, Queue3, quantam1, quantam2, quantam3
        quantam1, quantam3 =  min(self.bt) , max(self.bt)
        quantam2 = (quantam1 + quantam3) / 2
        t = 0
        n = len(wt)
        dup_process = Dup_process(self.id[:], self.bt[:], self.ar[:])
        requestQueue = []
        sequence = ''
        for i in range(len(self.ar)):
            idx = min_index(dup_process.ar)
            requestQueue.append([dup_process.id.pop(idx), dup_process.bt.pop(idx), dup_process.ar.pop(idx)])
        self.insert_current_process(requestQueue)
        t=requestQueue[0][2]
        l=0
        while len(requestQueue) > 0:
            if t >= requestQueue[0][2]:
                self.insert_current_process(requestQueue)
            l=l+1
            if l==n:
                break

        while len(Queue1) > 0 or len(Queue2) > 0 or len(Queue3) > 0:
            if len(Queue1) > 0:
                current = Queue1.pop(0)
                k = 1
            elif len(Queue2) > 0:
                current = Queue2.pop(0)
                k = 2
            else:
                current = Queue3.pop(0)
                k = 3

            if k == 1:
                t = t + current[1]
                wt[current[0]] = t - self.bt[current[0]] - self.ar[current[0]]
                context.append(current[0])
                if len(context) >= 2:
                    if context[-1] == context[-2]:
                        context.pop()
                sequence += '--->'+'P' + str(current[0] + 1) + str([current[1]])
                current[1] = 0
            elif k == 2:
                t = t + current[1]
                wt[current[0]] = t - self.bt[current[0]] - self.ar[current[0]]
                context.append(current[0])
                if len(context) >= 2:
                    if context[-1] == context[-2]:
                        context.pop()
                sequence += '--->'+'P' + str(current[0] + 1) + str([current[1]])
                current[1] = 0

            else:
                if current[1] <= quantam3:
                    t = t + current[1]
                    wt[current[0]] = t - self.bt[current[0]] - self.ar[current[0]]
                    sequence += '--->'+ 'P' + str(current[0] + 1) + str([current[1]])
                    context.append(current[0])
                    if len(context) >= 2:
                        if context[-1] == context[-2]:
                            context.pop()
                    current[1] = 0
                '''else:
                    t = t + quantam3
                    context.append(current[0])
                    if len(context) >= 2:
                        if context[-1] == context[-2]:
                            context.pop()
                    sequence += '--->'+'P' + str(current[0] + 1) + str([quantam3])
                    current[1] -= quantam3'''
            while len(requestQueue) > 0:
                if t >= requestQueue[0][2]:
                    self.insert_current_process(requestQueue)

            if current[1] != 0:
                if current[1] <= quantam1:
                    Queue1.append(current)
                elif current[1] <= quantam2:
                    Queue2.append(current)
                else:
                    Queue3.append(current)

        print('sequence is')

        print(sequence)

        print('Number of context switches are',len(context))

        return len(context)