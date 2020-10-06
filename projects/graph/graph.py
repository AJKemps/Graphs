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
        else:
            raise IndexError("nonexistent vertex")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """

        if len(self.vertices[vertex_id]) > 0:
            return self.vertices[vertex_id]
        else:
            return None

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()

        q.enqueue(starting_vertex)

        visited = set()

        while q.size() > 0:

            v = q.dequeue()

            if v not in visited:
                visited.add(v)
                print(v)

                for neighor in self.get_neighbors(v):
                    q.enqueue(neighor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = []

        stack.append(starting_vertex)

        visited = set()

        while len(stack) > 0:

            v = stack.pop()

            if v not in visited:
                visited.add(v)
                print(v)

                for neighor in self.get_neighbors(v):
                    stack.append(neighor)

    def dft_recursive(self, starting_vertex, path=[]):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        path += [starting_vertex]
        print(starting_vertex)

        for neighor in self.get_neighbors(starting_vertex):
            if neighor not in path:
                self.dft_recursive(neighor, path)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()

        q.enqueue([starting_vertex])

        visited = set()

        while q.size() > 0:

            v = q.dequeue()

            last_element = v[-1]

            if last_element == destination_vertex:
                return v

            if last_element not in visited:
                visited.add(last_element)

                for neighor in self.get_neighbors(last_element):
                    q.enqueue([*v, neighor])

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = []

        stack.append([starting_vertex])

        visited = set()

        while len(stack) > 0:

            v = stack.pop()
            last_element = v[-1]

            if last_element == destination_vertex:
                return v

            if last_element not in visited:
                visited.add(last_element)
                print(last_element)

                for neighor in self.get_neighbors(last_element):
                    stack.append([*v, neighor])

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """

        if visited is None:
            visited = set()
        visited.add(starting_vertex)

        if path is None:
            path = [starting_vertex]

        for neighbor in self.get_neighbors(starting_vertex):

            if neighbor not in visited:

                new_path = path + [neighbor]

                if neighbor == destination_vertex:
                    return new_path

                new_node = self.dfs_recursive(
                    neighbor, destination_vertex, visited, new_path)
                if new_node is not None:
                    return new_node

        return None


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
    print('-------')
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
    print('-------')
    print(graph.dfs_recursive(1, 6))
