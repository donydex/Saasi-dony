import os
import sys

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

def get_jar(folder):
    #folder = sys.argv[1]
    print('floder name:{}\n'.format(folder))
    #curl_path = os.getcwd()
    #jar_folder = 'get_jar'
    jar_path = os.path.join(os.getcwd(),'get_jar')
    if not os.path.exists(jar_path):
        os.makedirs(jar_path)
    try:
        files = os.popen('find {} -name \'*.jar\''.format(folder)).readlines()
    except:
        print("Don't find jar file!\n")
    if files == []:
        print("Don't find jar file in {}\n".format(folder))
    else:
        for file in files:
            os.system('cp {} {}'.format(file.strip(),jar_path))
        print('Get jar!\n')
    return jar_path

def analysis(jar_path, time):
    for file in os.listdir(jar_path):
        file_path = os.path.join(jar_path, file)
        os.system('java -jar javacg-0.1-SNAPSHOT-static.jar {0} \
                >> call-graph-{1}.txt'.format(file_path, time))
    print('Analysis have finished!\n')
    call_file_name = 'call-graph-{}'.format(time)
    return call_file_name

def get_time():
    import time
    now = int(round(time.time()*1000))
    re = time.strftime('%Y.%m.%d',time.localtime(now/1000))
    return re

def get_graph(call_file):
    os.system("sh 4.trans.sh " + call_file)
    print("Have got graph|\n")


def get_adj(call_file):
    import sys
    import os
    import re
    import collections
    #from collections import defaultdict
    from collections import defaultdict
    import ipdb;ipdb.set_trace();
    dic = defaultdict(list)
    l = []

    with open('sed_{}.txt'.format(call_file), 'r') as f:
        for line in f.readlines():
            line = line.strip()
            if not len(line) or line[0] == '#':
                continue
            t_line = line.split(' -> ')
            key = t_line[0]
            value = t_line[1][:-1]
            dic[key].append(value)


    for key,value in dic.items():
        if key not in l:
            l.append(key)
        if value not in l:
            l.append(value)

    adj_list = [[0] * len(l) for i in range(len(l))]
    for key,value in dic.items():
        for item in value:
            adj_list[l.index(key)][l.index(item)] = 1

    print('Adj_list top 2:\n{}'.format(adj_list[:2]))

    with open('adj_table_{}.txt'.format(call_file), 'w') as f:
        for key, value in dic.items():
            f.write(str(key)+ ':' +str(value) +'\n')

    os.system('cat adj_table_{}.txt'.format(call_file))
    print('Get adj!\n')
    return adj_list

#求任意顶点开始的联通图 有且仅存在一个 且dfn[u] == low[u]
def tarjan(u,matric):
    from collections import OrderedDict
    #matric = [[0,1,1,0,0,0],[0,0,0,1,0,0],[0,0,0,1,1,0],[1,0,0,0,0,1],[0,0,0,0,0,1],[0,0,0,0,0,0]]
    dfn = OrderedDict()
    low = OrderedDict()
    flag = dict()
    count = 0
    n = len(matric)
    num = 0
    s = Stack()
    #global s,num,n,count,flag,stack,dfn,low,matric
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
    return num

if __name__ == '__main__':
    folder = sys.argv[1]
    jar_path = get_jar(folder)
    now = get_time()
    call_file = analysis(jar_path, now)
    get_graph(call_file)
    matric = get_adj(call_file)
    #pass
    num = tarjan(3,matric)
    print("连通图数量...")
    print(num)
