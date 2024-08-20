def findBT(processes, btlist):
    btlist = [(pid, bt) for pid, bt in zip(processes, btlist)]
    return sorted(btlist, key = lambda x:x[1])

def findWT(btlist):
    n = len(btlist)

    wtlist = [0]*n
    for i in range(1, n):
        wtlist[i] = btlist[i-1][1] + wtlist[i-1]

    avg_wt = sum(wtlist) / n
    wtlist = [(btlist[i][0], wtlist[i]) for i in  range(n)]
    return wtlist, avg_wt

def findTAT(btlist, wtlist):
    n = len(wtlist)
    tatlist = [0]*n

    wtdict = dict(wtlist)

    for i in range(n):
        pid, bt = btlist[i]
        wt = wtdict[pid]
        tatlist[i] = bt+wt

    avg_tat = sum(tatlist) / n
    tatlist = [(btlist[i][0], tatlist[i]) for i in range(n)]
    return tatlist, avg_tat

def display(bt, wt, tat):
    print("Pid   BT   WT   TAT")
    wt, bt, tat = dict(wt), dict(bt), dict(tat)
    for pid in bt:
        print(f"{pid}   {bt[pid]}   {wt[pid]}   {tat[pid]}")

processes = list(range(1,11))
bt = [4,3,7,9,1,10,14,11,5,16]

bt = findBT(processes, bt)
wt, avg_wt = findWT(bt)
tat, avg_tat = findTAT(bt, wt)

display(bt, wt, tat)
print(f"Average Waiting Time = {avg_wt}")
print(f"Average Turnaround Time = {avg_tat}")



