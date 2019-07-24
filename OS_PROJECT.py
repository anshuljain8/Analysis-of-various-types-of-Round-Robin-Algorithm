#import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import time
from RoundRobin import Processes
from multilevelfeedback import Multi_Processes
from VariableQuanta import Existing_Processes
from LowBT import LowBT_Processes
#from HighBT import HighBT_Processes

pltWt=[]
pltTat=[]
pltContext=[]

def FindTurnAroundTime(p, wt, tat):
    n = len(wt)
    for i in range(n):
        tat[i] = wt[i] + p.bt[i]

def FindAvgTime(p, quantam):
    n = len(p.bt)
    wt = [0 for i in range(n)]
    tat = [0 for i in range(n)]
    total_wt = 0
    total_tat = 0
    context=p.FindWaitingTime(wt, quantam)
    FindTurnAroundTime(p,wt, tat)
    print('Process', end="    ")
    print('Arrivaltime', end="    ")
    print('BurstTime', end="   ")
    print('WaitingTime', end="    ")
    print('TurnAroundTime', end="     ")
    print()
    for i in range(n):
        print(p.id[i] + 1, end="              ")
        print(p.ar[i], end="              ")

        print(p.bt[i], end="              ")
        print(wt[i], end="              ")
        print(tat[i], end="              ")
        print()

    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
    print('Avg Waiting time is : ', total_wt / n)
    print('Avg TurnAroundTime time is : ', total_tat / n)

    return total_wt/n,total_tat/n,context


def add_results(avgwt,avgtat,context):
    pltWt.append(avgwt)
    pltTat.append(avgtat)
    pltContext.append(context)


def main():
    global pltWt,pltTat,pltContext
    p1 = Processes()                          # NORMAL ROUND ROBIN
    p2=LowBT_Processes()                      # VARIATION OF QUANTAM TIME
    p3=Existing_Processes()                  # EXISTING MODEL
    p4=Multi_Processes()                     # MULTILEVEL FEEDBACK
    print('enter the number of processes: ')
    n=int(input())
    print('enter the burst time and arival time of processes:(Bursttime Arivaltime) ')
    for i in range(n):
        x=input().split()
        bt=int(x[0])
        ar=int(x[1])
        p1.set_id_bt_ar(i,bt,ar)
        p2.set_id_bt_ar(i,bt,ar)
        p3.set_id_bt_ar(i,bt,ar)
        p4.set_id_bt_ar(i,bt,ar)


    print('enter the quantam time:')
    quantam=int(input())
    print()

    # BASIC ROUND ROBIN............................
    print('################################################################################################')
    print()
    print('Basic Round Robin Results are:')
    avgwt,avgtat,context=FindAvgTime(p1,quantam)
    add_results(avgwt,avgtat,context)



    # EXISTING MODEL.....................
    print('##################################################################################################')
    print()
    print(' Variation Quantam time algorithm results are :')

    avgwt, avgtat, context = FindAvgTime(p2, quantam)
    add_results(avgwt, avgtat, context)

    # MULTIEVEL FEEDBACK.................
    print('##################################################################################################')
    print()
    print('Existing algorithm results are: ')

    avgwt, avgtat, context = FindAvgTime(p3, quantam)
    add_results(avgwt, avgtat, context)

    # VARIATION OF RR(MEDIAN).....................
    print('###################################################################################################')
    print()
    print('Multi Level feedback Results are:')

    avgwt, avgtat, context = FindAvgTime(p4, quantam)
    add_results(avgwt, avgtat, context)
    fig=plt.figure()

    plt1=fig.add_subplot(131)
    plt2=fig.add_subplot(132)
    plt3=fig.add_subplot(133)

    plt1.bar(0,pltWt[0],label='Basic RR-->'+str([pltWt[0]]),color='r')
    plt1.bar(1,pltWt[1],label='Variant quanta algorithm-->'+str([pltWt[1]]),color='g')
    plt1.bar(2,pltWt[2],label='Existing implementaion-->'+str([pltWt[2]]),color='b')
    plt1.bar(3,pltWt[3],label='Multievel feeedback-->'+str([pltWt[3]]),color='c')
    plt1.set_ylabel('time (seconds)')
    plt1.set_title('Comparision of Av. Waiting Times')

    plt1.legend()
    plt2.bar(0,pltTat[0], label='Basic RR-->'+str([pltTat[0]]), color='r')
    plt2.bar(1, pltTat[1], label='Variant quanta algorithm-->'+str([pltTat[1]]), color='g')
    plt2.bar(2, pltTat[2], label='Existing implementaion-->'+str([pltTat[2]]), color='b')
    plt2.bar(3, pltTat[3], label='Multievel feeedback-->'+str([pltTat[3]]), color='c')
    plt2.set_ylabel('time (seconds)')
    plt2.set_title('Comparision of Av. TurnAround Times')
    plt2.legend()

    plt3.bar(0, pltContext[0], label='Basic RR-->'+str([pltContext[0]]), color='r')
    plt3.bar(1, pltContext[1], label='Variant quanta algorithm-->'+str([pltContext[1]]), color='g')
    plt3.bar(2, pltContext[2], label='Existing implementaion-->'+str([pltContext[2]]), color='b')
    plt3.bar(3, pltContext[3], label='Multievel feeedback-->'+str([pltContext[3]]), color='c')
    plt3.set_ylabel('Number of context switches')
    plt3.set_title('Comparision of number of context switches')
    plt.legend()
    plt.grid(True, color='k')
    plt.show()
if __name__=='__main__':
    main()
