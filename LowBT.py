import math
import statistics

def min(A):
    min = A[0]
    for i in range(len(A)):
        if min > A[i]:
            min = A[i]
    return A.index(min)


def medianfind(readyQueue):
    s = []
    for i in range(len(readyQueue)):
        s.append(readyQueue[i][1])
    return statistics.median(s)


def highest(readyQueue):
    h = 0
    for i in range(len(readyQueue)):
        if readyQueue[i][1] >= h:
            h = readyQueue[i][1]
    return h
class Dup_process:
    def __init__(self, id, bt, ar):
        self.id = id
        self.bt = bt
        self.ar = ar


class LowBT_Processes:
    def __init__(self, id=[], bt=[], ar=[]):
        self.id = id
        self.bt = bt
        self.ar = ar

    def set_id_bt_ar(self, id, bt, ar):
        self.id.append(id)
        self.bt.append(bt)
        self.ar.append(ar)

    def FindWaitingTime(self, wt, quantam):
        readyQueue = []
        t = 0
        n = len(wt)
        dup_process = Dup_process(self.id[:], self.bt[:], self.ar[:])
        requestQueue = []
        sequence = ''
        context=[]
        for i in range(len(dup_process.ar)):
            idx = min(dup_process.ar)
            requestQueue.append([dup_process.id.pop(idx), dup_process.bt.pop(idx), dup_process.ar.pop(idx)])
        readyQueue.append(requestQueue.pop(0))
        t = readyQueue[0][2]
        while len(readyQueue) > 0:
            if len(readyQueue) > 1:
                quantam = math.ceil(math.sqrt(medianfind(readyQueue) * highest(readyQueue)))
            current = readyQueue.pop(0)
            if current[1] > quantam:
                t = t + quantam
                current[1] = current[1] - quantam
                if current[1] <= quantam // 2:
                    readyQueue.insert(0, current)
                if len(requestQueue) > 0:
                    n = len(requestQueue)
                    i = 0
                    while n > 0:
                        if t >= requestQueue[i][2]:
                            readyQueue.append(requestQueue.pop(i))
                            i -= 1
                        i += 1
                        n -= 1

                readyQueue.append(current)
                context.append(current[0])
                if len(context) >= 2:
                    if context[-1] == context[-2]:
                        context.pop()
                sequence = sequence + str(current[0]) + str([quantam]) + '->'
            else:
                t = t + current[1]
                wt[current[0]] = t - self.bt[current[0]] - self.ar[current[0]]
                sequence = sequence + str(current[0]) + str([current[1]]) + '->'
                context.append(current[0])
                if len(context) >= 2:
                    if context[-1] == context[-2]:
                        context.pop()
                current[1] = 0
                if len(requestQueue) > 0:
                    n = len(requestQueue)
                    i = 0
                    while n > 0:
                        if t >= requestQueue[i][2]:
                            readyQueue.append(requestQueue.pop(i))
                            i -= 1
                        i += 1
                        n -= 1

        print('sequence is')
        print(sequence)
        print('Number of context switches are:',len(context))

        return len(context)
