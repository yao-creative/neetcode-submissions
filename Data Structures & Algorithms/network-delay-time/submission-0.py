from collections import deque
from typing import List
import math
#kinda like djikstra but for all nodes. # use invariant that each iteration step given all the edges seen the node dist is minimal from k having looked all the edges having checked the edge then max(dist_nodes)
# exploration would just be a set of all side nodes
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #this seems breadth first search
        # perhaps dictionary + directed out edge {v: {e1,e2}} notation to track neighbors, 
        #add all k's neighbors:
        dist = [math.inf] * (n + 1)
        dist[k] = 0 #starting
        times_map = {} #unique since single iter loop and each edge has one source
        for time in times: 
            if time[0] not in times_map: 
                times_map[time[0]] = [(time[0],time[1], time[2])]
            else: 
                times_map[time[0]].append((time[0], time[1], time[2]))
        q = deque(times_map.get(k,[])) #should be all k's edges
        #basically iterate reachable and their distance otherwise -1 if one of them still inf, or max(dist) = inf then
        while len(q) > 0:
            e = q.popleft()
            print(f"e: {e}")
            # taking this edge to receiving is shorter then overide receiving node distance else 
            alt= dist[e[0]] + e[2]
            if dist[e[1]] > alt:
                dist[e[1]] = alt #new shortest, and propagate through 
                if e[1] in times_map: #not sink
                    for edge in times_map[e[1]]:
                        q.append(edge) #what if this is repeated if there's a loop or cycle? usually no since cycles are longer than direct reach. 
                        # no larger alt
                        #since there's always a shortest path there'll always be a propagation to the whole reachable graph.
                        # node added neighbor also will be unique if multiple ins to e[1], only one minimal
            #shortest between #current or if it went through e[0] first then go to e[1] using e[2]
            #can we gurantee that e[0] wouldn't be discounted later?
            # do we need to check the rest of the distances which went through e[1] --> v need to be discounted?
            # no since by the queue gurantee we find the min unweighed distance (num hops) in the number of edges from k,
            # so since edges appended here are strictly more hops increasing, we've not calculated e[1] forward to other edges.
        furthest = max(dist[1:]) 
        if furthest == math.inf:
            return -1
        else:
            return furthest
