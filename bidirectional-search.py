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

    search_path = {start: [start], goal: [goal]}
    visited_vertices = set()

    while len(search_path) > 0:
        unvisited_vertices = list(search_path.keys())

        for vertex in unvisited_vertices:

            current_path = search_path[vertex]
            origin_vertex = current_path[0]
            current_neighbours = set(graph[vertex]) - visited_vertices
            unvisited_neighbours = current_neighbours.intersection(unvisited_vertices) 

            # Check if our neighbours hit an active vertex
            if len(unvisited_neighbours) > 0:
                for meeting_vertex in unvisited_neighbours:
                    if origin_vertex != search_path[meeting_vertex][0]:
                        search_path[meeting_vertex].reverse()
                        return search_path[vertex] + search_path[meeting_vertex]

            # No hits, so check for new neighbours to extend our paths.
            if len(set(current_neighbours) - visited_vertices - set(unvisited_vertices))  == 0:
                search_path.pop(vertex, None)
                visited_vertices.add(vertex)
            else:
                # Otherwise extend the paths, remove the previous one and update the inactive vertices.
                for neighbour_vertex in current_neighbours - visited_vertices - set(unvisited_vertices):
                    search_path[neighbour_vertex] = current_path + [neighbour_vertex]
                    unvisited_vertices.append(neighbour_vertex)
                search_path.pop(vertex, None)
                visited_vertices.add(vertex)

    return None

print (bi_directional_search(example_graph,16,0))
