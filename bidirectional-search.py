example_graph = {
        0:[2,3], 1:[4,5], 2:[0,6], 3:[0,6], 6:[2,3,8],
        4:[1,7], 5:[1,7], 7:[4,5,8], 8:[6,7,9, 10],
        9:[8,11,12], 11:[9,15], 12:[9,15],
        10:[8,13, 14], 13:[10,16], 14:[10,16], 
        15:[11,12], 16:[13,14]
        }

def bi_directional_search(graph, start, goal):

    if start == goal:
        return [start]

    paths_queue = { goal: [goal], start: [start]}
    visited_vertices = set()

    while len(paths_queue) > 0:
        known_vertices = list(paths_queue.keys())

        for vertex in known_vertices:

            current_path = paths_queue[vertex]
            origin_vertex = current_path[0]
            current_neighbours = set(graph[vertex]) - visited_vertices
            new_neighbours = current_neighbours - set(known_vertices)
            meeting_neighbours = current_neighbours.intersection(known_vertices) 

            # Check if our neighbours hit an active vertex
            if len(meeting_neighbours) > 0:
                for meeting_vertex in meeting_neighbours:
                    if origin_vertex != paths_queue[meeting_vertex][0]:
                        paths_queue[meeting_vertex].reverse()
                        return paths_queue[vertex] + paths_queue[meeting_vertex]

            # No hits, so check for new neighbours to extend our paths.
            if len(new_neighbours) >= 0:
                for neighbour_vertex in new_neighbours:
                    paths_queue[neighbour_vertex] = current_path + [neighbour_vertex]
                    known_vertices.append(neighbour_vertex)
            paths_queue.pop(vertex, None)
            visited_vertices.add(vertex)

    return None

print (bi_directional_search(example_graph,0,16))
