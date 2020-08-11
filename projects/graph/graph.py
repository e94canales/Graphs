"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # init empty queue
        q = Queue()

        # set the starting vertex
        q.enqueue(starting_vertex)

        visited = set()

        while q.size() > 0:
            current = q.dequeue()

            if current not in visited:
                visited.add(current)
                print(current)

                # add all neighbors to the queue
                for neighbor in self.get_neighbors(current):
                    q.enqueue(neighbor)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # init stack
        s = Stack()

        # set start
        s.push(starting_vertex)
        visited = set()

        # while not empty
        while s.size() > 0:
            # set current
            current = s.pop()

            # if not in visited
            if current not in visited:
                # add to visited and print
                visited.add(current)
                print(current)

                # push current vertex neighbors to stack
                for neighbor in self.get_neighbors(current):
                    s.push(neighbor)


    def dft_recursive(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # init visited at start
        if visited is None:
            visited  = set()
        
        # if current vertex not in visited
        if starting_vertex not in visited:
            # add to visited and print
            visited.add(starting_vertex)
            print(starting_vertex)

            # get next vertex and recurse
            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)



    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()

        q.enqueue([starting_vertex])

        while q.size() > 0:
            # set path
            path = q.dequeue()
            # set vertex as last elem
            vertex = path[-1]

            # return path if vertex is destination
            if vertex == destination_vertex:
                return path

            for neighbor in self.get_neighbors(vertex):
                # set new path and queue it
                newPath = path.copy()
                newPath.append(neighbor)
                q.enqueue(newPath)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push(starting_vertex)
        path = []

        visited = set()

        # while not empty
        while s.size() > 0:
            vertex = s.pop()

            # if not in visited
            if vertex not in visited:
                # add to visited and path
                visited.add(vertex)
                path.append(vertex)

                # if current vertex is the destination return the path
                if vertex == destination_vertex:
                    return path

                # push each of currents neighbors
                for neighbor in self.get_neighbors(vertex):
                    s.push(neighbor)


    def dfs_recursive(self, starting_vertex, destination_vertex, path=[], visited=set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # if current vertex not in visited
        if starting_vertex not in visited:
            # add vertex to visited
            visited.add(starting_vertex)

            # if current vertex is destination, add to path and retrun
            if starting_vertex == destination_vertex:
                path.append(starting_vertex)
                return path
            else:

                for neighbor in self.get_neighbors(starting_vertex):

                    # recurse
                    self.dfs_recursive(neighbor, destination_vertex, path, visited)

                    # after recurssion if path is not empty insert current vortex at the beginning and return
                    if path != []:
                        path.insert(0, starting_vertex)
                        return path
                    
                    
        return path


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
