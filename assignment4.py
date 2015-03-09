#!/usr/bin/env python3
"""
ECE406: Winter 2015
Python file for assignment 4

we will use the queue module to implement a FIFO queue.
- you can create a queue with Q = queue.queue(max_size)
- you can inject v onto the queue with Q.put(v)
- you can eject from the queue with Q.get()
"""
import queue


def num_shortest_paths(adj, vertex_s):
    """
    Input:  1) A directed graph represented as an adjacency list adj:
                adj[1] is a list containing the neighbors of vertex 1
                (by default, vertices are numbered from 0 to |V| - 1)
            2) a vertex_s in 0,...,|V|-1

    Output: a matrix of distances, where M[i,j] gives the length of the shortest
            path from vertex i to vertex j passing through vertex_s
    """
    # < your code goes here.  feel free to change the name of the variables.
    # can represent pairwise distances as a list of lists,
    # where dist[i][j] gives distance from i to j
    result = []
    num_vertices = len(adj)
    vsToAll = dfs(adj, vertex_s)
    for vertex in range(num_vertices):
        row = dfs(adj, vertex)
        result.append([row[vertex_s]] * num_vertices)

    for col in range(num_vertices):
        for row in range(num_vertices):
            result[col][row] += vsToAll[row]
    return result


def dfs(adj, vertex_s):
    dist = [-1] * len(adj)
    Q = queue.Queue(len(adj))
    Q.put(vertex_s)
    dist[vertex_s] = 0
    while not Q.empty():
        vertex = Q.get()
        for child in adj[vertex]:
            if dist[child] == -1:
                Q.put(child)
                dist[child] = dist[vertex] + 1
    return dist


def main():
    """
    A simple test case for your algorithm with four vertices 0,1,2,3
    """
    adj = [[1, 2],
           [2, 3],
           [0],
           [2]]

    # test case:
    print(num_shortest_paths(adj, 2))
    # in this graph, the shortest path from 0 to 3 passing through 2 is
    # 0->2->0->1->3 having a length of 4


if __name__ == '__main__':
    main()
