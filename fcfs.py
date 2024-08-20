def findWT(processes, n, bt):
    wt = [0]*n

    for i in range(1, n):
        wt[i] = bt[i-1] + wt[i-1]
    return wt

def findTAT(processes, n, bt, wt):
    tat = [0]*n

    for i in range(n):
        tat[i] = bt[i] + wt[i]
    return tat

def findavgTime(processes, n, bt):
    total_wt, total_tat = 0, 0

    wt = findWT(processes, n, bt)
    tat = findTAT(processes, n, bt, wt)

    print("  Pid---BT---WT---TAT")

    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        print(f" {str(i+1)}   {str(bt[i])}   {str(wt[i])}  {str(tat[i])}")

    print(f"Average WT = {str(total_wt/n)}")
    print(f"Average TAT = {str(total_tat/n)}")


processes = [1,2,3]
n = len(processes)
bt = [10, 5, 8]

findavgTime(processes, n, bt)

