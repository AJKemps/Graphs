# paths = []


def get_ancestors(graph, starting_node):

    ancestors = []

    for pair in graph:
        if pair[1] == starting_node:
            ancestors.append(pair[0])

    print('ancestors:', ancestors)

    if len(ancestors) > 0:
        return ancestors
    else:
        return None


def dfs_recursive_ancestors(ancestors, starting_node, path=None, visited=None, paths=None):

    if paths is None:
        paths = []

    if visited is None:
        visited = set()
    visited.add(starting_node)
    print('VISITED:', visited)

    if path is None:
        path = [starting_node]

    print('path:', path)

    parents = get_ancestors(ancestors, starting_node)

    if parents is None:
        paths.append(path)

    if parents is not None:

        for ancestor in get_ancestors(ancestors, starting_node):

            if ancestor not in visited:
                new_path = path + [ancestor]
                print('new_path:', new_path)

                next_ancestor = dfs_recursive_ancestors(
                    ancestors, ancestor, new_path, visited, paths)

                if next_ancestor is not None:
                    return next_ancestor
                # if next_ancestor is None:
                #     paths.append(new_path)

    print('DONE', paths)
    return paths


def earliest_ancestor(ancestors, starting_node):

    paths = dfs_recursive_ancestors(ancestors, starting_node)

    print('ENDING paths:', paths)
    print(len(paths))

    if len(paths) < 1:
        return -1

    results = []
    longest = paths[0]

    for path in paths:
        if len(path) > len(longest):
            longest = path

    for path in paths:
        if len(path) == len(longest):
            results.append(path)
            longest = path

    print('results:', results)

    if len(results) > 1:
        cur = results[0]
        for result in results:
            print(result[-1], cur[-1])
            if result[-1] < cur[-1]:
                cur = result[-1]
        results = cur

    oldest_relative = results[-1][-1]

    if oldest_relative == starting_node:
        return -1
    else:
        return oldest_relative


if __name__ == '__main__':
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                      (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    print(earliest_ancestor(test_ancestors, 1))
    print(earliest_ancestor(test_ancestors, 6))
