import sys
import os
import re
import collections
#from collections import defaultdict
from collections import defaultdict
import ipdb;ipdb.set_trace();
dic = defaultdict(list)
l = []

with open('sed_callgraph.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        if not len(line) or line[0] == '#':
            continue
        t_line = line.split(' -- ')
        key = t_line[0]
        value = t_line[1][:-1]
        dic[key].append(value)

adj_list = [[0] * len(dic) for i in range(len(dic))]

for key,value in dic.items():
    l.append(key)

for key,value in dic.items():
    for item in value:
        adj_list[l.index(key)][l.index(item)] = 1

print('Adj_list top 5:\n{}'.format(adj_list[:5]))

with open('adj_table.txt', 'w') as f:
    for key, value in dic.items():
        f.write(str(key)+ ':' +str(value) +'\n')

os.system('cat adj_table.txt')

# Trans adj_table to adj_matrix



#求任意顶点开始的联通图 有且仅存在一个 且dfn[u] == low[u]
from collections import OrderedDict
matric = [[0,1,1,0,0,0],[0,0,0,1,0,0],[0,0,0,1,1,0],[1,0,0,0,0,1],[0,0,0,0,0,1],[0,0,0,0,0,0]]
dfn = OrderedDict()
low = OrderedDict()
flag = dict()
count = 0
n = 6
num = 0
class Stack(object):
    def __init__(self):
        self.items = list()
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def clear(self):
        del self.items[:]
    def empty(self):
        return self.size() == 0
    def size(self):
        return len(self.items)
    def top(self):
        return self.items[self.size() - 1]

s = Stack()
def tarjan(u):
    global s,num,n,count,flag,stack,dfn,low,matric
    count = count + 1
    dfn[u] = low[u] = count
    s.push(u)
    flag[u] = True
    #print("visiting {0} ...".format(str(u + 1)))
    for i in range(n):
        if matric[u][i] == 0:
            continue
        if flag.get(i, False) is True:
            if (dfn[i] < low[u]):
                low[u] = dfn[i]
        else:
            tarjan(i)
            low[u] = min(low[u], low[i])
    if (dfn[u] == low[u] and s.empty() is False):
       print("********连通图********")
       m = s.pop()
       flag[m] = False
       print(m + 1)
       while m != u and s.empty() is False:
           num = num + 1
           m = s.pop()
           flag[m] = False
           print(m+1)
       print("*********************")

if __name__  == "__main__":
    pass
    tarjan(3)
    print("连通图数量...")
    print(num)


