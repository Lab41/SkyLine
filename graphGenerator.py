from stinger import *
from os import system
from time import clock
from heapq import heappush, heappop
from random import randint as r, seed as s, random as P, sample

s(0xcafebabe)

rSeeds = (3,20)
rTypes = (5,100)
rValues = (100,1000)
rBranchesMin = (1,3)
rBranchesMax = (4,5)
rDepth = (2,8)
rExtraAncestors = (2,15)
rJoinsPerTree = (10,200)
pMoreAncestors = 0.09
rCycles = (128,512)
pCloseCycle = 0.04
pJumpInCycle = 0.02

nSeeds = r(*rSeeds)
nTypes = r(*rTypes)
nValues = r(*rValues)
nBranches = [(r(*rBranchesMin), r(*rBranchesMax)) for x in xrange(0,nTypes+1)]
nJoins = r(*rJoinsPerTree) * nSeeds

graph = []
seeds = []
vID = 0
eID = 0

for i in xrange(0,nSeeds):
    print "seed", i, "of", nSeeds
    seeds.append(vID)
    graph.append((r(0, nTypes), r(0, nValues), []))
    current = [len(graph)-1]
    vID = len(graph)
    for L in xrange(0,r(*rDepth)):
        print "\tlevel", L
        parents = current
        current = []
        for parent in parents:
            for kid in xrange(0,r(*nBranches[graph[parent][0]])):
                current.append(vID)
                graph.append((r(0, nTypes), r(0, nValues), []))
                graph[parent][2].append(vID)
                if P() < pMoreAncestors:
                    for ancestor in sample(xrange(seeds[-1], parent), min(parent-seeds[-1], r(*rExtraAncestors))):
                        graph[ancestor][2].append(vID)
                vID = len(graph)
print vID

print "Adding edges between trees...",
for edge in zip(sample(xrange(vID), nJoins), sample(xrange(vID), nJoins)):
    graph[edge[0]][2].append(edge[1])
print "done!"

print "Adding cycles:"
cycleStarts = sample(xrange(vID), r(*rCycles))
for start in cycleStarts:
    trail = {start: True}
    current = start
    print "\t", start, "->",
    while True:
        if len(graph[current][2]) == 0:
            if current != start and  P() < pCloseCycle:
                    graph[current][2].append(start)
                    break
            else:
                new = sample(xrange(vID), 1)[0]
                graph[current][2].append(new)
                current = new
                if current in trail: break
                trail[current] = True
                print "*"+str(current), "->",
        elif P() < pCloseCycle:
            graph[current][2].append(start)
            break
        elif P() < pJumpInCycle:
            new = sample(xrange(vID), 1)[0]
            graph[current][2].append(new)
            current = new
            if current in trail: break
            trail[current] = True
            print "*"+str(current), "->",
        else:             
            current = sample(graph[current][2], 1)[0]
            if current in trail: break
            trail[current] = True
            print current, "->",
    print "."
print "Done!"

walk = []
ec = 0

def addV(v):
    walk.append((1,v))

def addE(e):
    global ec
    ec += 1
    walk.append((2,e[0],e[1]))

print vID
print "Traversing"

frontier = []
visited = {}
for v in seeds:
    addV(v)
    visited[v] = True
    edgesSeen={}
    for e in graph[v][2]:
        if e not in edgesSeen:
            heappush(frontier, (sample(xrange(vID), 1)[0], (v, e)))
            edgesSeen[e] = True

while frontier != []:
    next = heappop(frontier)[1]
    if next[1] not in visited:
        addV(next[1])
        visited[next[1]] = True
        edgeSeen={}
        for e in graph[next[1]][2]:
            if e not in edgesSeen:
                heappush(frontier, (sample(xrange(vID), 1)[0], (next[1], e)))    
                edgeSeen[e] = True
    addE(next)

print ec, "edges and", vID, "vertices!"

print " === Titan Benchmark === "
system("rm -rf /tmp/titan-benchmark && mkdir /tmp/titan-benchmark")
open("/tmp/titan-benchmark/da_graph.txt", "wb").write("\n".join([",".join(map(str,step)) for step in walk])+"\n")
system("cp bench.gremlin /tmp/titan-benchmark")
system("cp titan-0.5.3-hadoop2.zip /tmp/titan-benchmark")
system("cd /tmp/titan-benchmark && " +
       "unzip titan-0.5.3-hadoop2.zip >/dev/null 2>&1 && " +
       "titan-0.5.3-hadoop2/bin/gremlin.sh < bench.gremlin | grep 'Time taken' | grep -v println")

print " === Stinger Benchmark === "

walk_f = filter(lambda x: x[0] == 2, walk)
start = clock()

stinger = stinger_new()

for step in walk_f:    
    stinger_insert_edge(stinger, 0, step[1], step[2], 1, 1)

stop = clock()
print "Total time taken:", stop-start        

results = {0: {0: 0, 1: 0}, 1: {0: 0, 1: 0}}

print ec, "edges and", vID, "vertices!"
