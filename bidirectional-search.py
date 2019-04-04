example_graph = {
        0:[2,3], 1:[4,5], 2:[0,6], 3:[0,6], 6:[2,3,8],
        4:[1,7], 5:[1,7], 7:[4,5,8], 8:[6,7,9, 10],
        9:[8,11,12], 11:[9,15], 12:[9,15],
        10:[8,13, 14], 13:[10,16], 14:[10,16], 
        15:[11,12], 16:[13,14]
        }

def bi_directional_search(graph, start, goal):
    # Check if start and goal are equal.
    if start == goal:
        return [start]
    # Get dictionary of currently active vertices with their corresponding paths.
    search_path = {start: [start], goal: [goal]}
    # Vertices we have already examined.
    visited_vertices = set()

    while len(search_path) > 0:

        # Make a copy of active vertices so we can modify the original dictionary as we go.
        active_vertices = list(search_path.keys())
        for vertex in active_vertices:
            # Get the path to where we are.
            current_path = search_path[vertex]
            # Record whether we started at start or goal.
            origin = current_path[0]
            # Check for new neighbours.
            current_neighbours = set(graph[vertex]) - visited_vertices
            # Check if our neighbours hit an active vertex
            if len(current_neighbours.intersection(active_vertices)) > 0:
                for meeting_vertex in current_neighbours.intersection(active_vertices):
                    # Check the two paths didn't start at same place. If not, then we've got a path from start to goal.
                    if origin != search_path[meeting_vertex][0]:
                        # Reverse one of the paths.
                        search_path[meeting_vertex].reverse()
                        # return the combined results
                        return search_path[vertex] + search_path[meeting_vertex]

            # No hits, so check for new neighbours to extend our paths.
            if len(set(current_neighbours) - visited_vertices - set(active_vertices))  == 0:
                # If none, then remove the current path and record the endpoint as inactive.
                search_path.pop(vertex, None)
                visited_vertices.add(vertex)
            else:
                # Otherwise extend the paths, remove the previous one and update the inactive vertices.
                for neighbour_vertex in current_neighbours - visited_vertices - set(active_vertices):
                    search_path[neighbour_vertex] = current_path + [neighbour_vertex]
                    active_vertices.append(neighbour_vertex)
                search_path.pop(vertex, None)
                visited_vertices.add(vertex)

    return None

print (bi_directional_search(example_graph,16,0))
