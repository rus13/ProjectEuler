__author__ = 'ruslan'
from queue import PriorityQueue

max_value = 100000000


def floyd_warshall(m):
    dist = [[0] * len(m)] * len(m)
    for k in range(len(m)):
        for i in range(len(m)):
            for j in range(len(m)):
                if m[i][k] + m[k][j] < m[i][j]:
                    m[i][j] = min(m[i][k] + m[k][j], m[i][j])


def bellman_ford(edges, n, s):
    dist = [max_value] * n
    dist[s] = 0
    prev = [-1] * n
    for i in range(n - 1):
        for e in edges:
            if dist[e[0]] + e[2] < dist[e[1]]:
                dist[e[1]] = dist[e[0]] + e[2]
                prev[e[1]] = e[0]


# edge_list[s] contain tuples of the form (t, w) such that there is an edge (s, t) with weight w
def dijkstra(edge_list, s):
    n = len(edge_list)
    dist = [max_value] * n
    dist[s] = 0
    prev = [-1] * n
    q = PriorityQueue()
    q.put(s, 0)
    #for i in range(1,n):
    #    q.put(max_value,i)
    for i in range(n):
        cur = q.get()
        for next in edge_list[cur]:
            if dist[cur] + next[1] < dist[next[0]]:
                dist[next[0]] = dist[cur] + next[1]
                prev[next[0]] = cur
                q.put(next[0], dist[next[0]])
    return dist, prev


edge_list = [
    [(1, 5), (2, 6)],
    [(2, 5)],
    [(1, 5)]
]
dist, prev = dijkstra(edge_list, 0)
print("hallo")

q = PriorityQueue()
q.put("fuenf",5)
q.put("eins",1)
t = q.get()
print("test")