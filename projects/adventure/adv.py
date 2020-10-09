from room import Room
from player import Player
from world import World
from util import Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []


def opp_dir(direction):
    if direction == 'n':
        return 's'
    if direction == 's':
        return 'n'
    if direction == 'w':
        return 'e'
    if direction == 'e':
        return 'w'


def bfs(graph):
    print('\n\n\n--- BFS ---\n\n\n')
    q = Queue()

    moves = Queue()

    cur_room = player.current_room.id

    q.enqueue([cur_room])

    for move in player.current_room.get_exits():
        moves.enqueue(move)

    local_visited = list()
    path = list()

    while moves.size() > 0:
        move = moves.dequeue()
        cur_room = player.current_room.id
        print('\nnew loop\n')
        print('current room:', cur_room)
        print('local visited:', local_visited)
        print('paths:', path)
        print('moves:', move)

        # get directions
        directions = graph[cur_room]
        # check to see if the current room has any unexplored paths
        for k, v in directions.items():
            if v == '?':
                # if so, return resulting path
                cur_room = player.current_room.id
                local_visited.append(cur_room)
                print('BINGO', cur_room, 'directions:',
                      directions, 'local visited:', local_visited)

                return path, local_visited[1:]

        if cur_room not in local_visited:
            for k, v in directions.items():
                moves.enqueue(k)

        player.travel(move)
        path.append(move)
        local_visited.append(cur_room)


def dfs_paths(room=None, graph=None, path=None, visited=None):

    # initialize room, path, visitied
    if room is None:
        room = 0

    if path is None:
        path = []
    print("PATHS:", path)

    if visited is None:
        visited = []
    print("VISITED:", visited)

    # add to dictionary
    if graph is None:
        graph = {}
    if room not in visited:
        graph[room] = dict()
    print('Graph:', graph)

    # get id and directions for room
    room = player.current_room.id
    print('Room:', room)
    directions = player.current_room.get_exits()

    # populate possible directions for room if we've not been there before
    if room not in visited:
        for direction in directions:
            graph[room][direction] = '?'

    # add room to visited
    visited.append(room)

    # add previous room to current
    if len(path) > 0:
        last_move = path[-1]
        reverse_dir = opp_dir(last_move)
        graph[room][reverse_dir] = visited[-2]

    print('Graph Before Loop:', graph)

    # count unkowns
    unknown_count = 0
    for k, v in graph[room].items():
        if v == '?':
            unknown_count += 1

    # if unknown count is greater than zero
    if unknown_count > 0:
        for k, v in graph[room].items():
            # if direction is unknown, go that way
            if v == '?':
                cur_room = player.current_room.id
                player.travel(k)
                path.append(k)
                new_room = player.current_room.id
                print('From:', cur_room, 'Moving:', k, 'To:', new_room)
                graph[cur_room][k] = new_room
                dfs_paths(new_room, graph, path, visited)

    if unknown_count == 0:
        # navigate back an unknown room

        call = bfs(graph)

        if call is not None:
            new_path, local_visited = call
            path += new_path
            visited += local_visited
        print("BFS:", bfs(graph))

        # return path

    return graph, path, visited


print(dfs_paths())
world.print_rooms()

# TRAVERSAL TEST
# visited_rooms = set()
# player.current_room = world.starting_room
# visited_rooms.add(player.current_room)

# for move in traversal_path:
#     player.travel(move)
#     visited_rooms.add(player.current_room)

# if len(visited_rooms) == len(room_graph):
#     print(
#         f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
# else:
#     print("TESTS FAILED: INCOMPLETE TRAVERSAL")
#     print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
