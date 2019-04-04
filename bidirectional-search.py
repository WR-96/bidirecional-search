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
    active_vertices_path_dict = {start: [start], goal: [goal]}
    # Vertices we have already examined.
    inactive_vertices = set()

    while len(active_vertices_path_dict) > 0:

        # Make a copy of active vertices so we can modify the original dictionary as we go.
        active_vertices = list(active_vertices_path_dict.keys())
        for vertex in active_vertices:
            # Get the path to where we are.
            current_path = active_vertices_path_dict[vertex]
            # Record whether we started at start or goal.
            origin = current_path[0]
            # Check for new neighbours.
            current_neighbours = set(graph[vertex]) - inactive_vertices
            # Check if our neighbours hit an active vertex
            if len(current_neighbours.intersection(active_vertices)) > 0:
                for meeting_vertex in current_neighbours.intersection(active_vertices):
                    # Check the two paths didn't start at same place. If not, then we've got a path from start to goal.
                    if origin != active_vertices_path_dict[meeting_vertex][0]:
                        # Reverse one of the paths.
                        active_vertices_path_dict[meeting_vertex].reverse()
                        # return the combined results
                        return active_vertices_path_dict[vertex] + active_vertices_path_dict[meeting_vertex]

            # No hits, so check for new neighbours to extend our paths.
            if len(set(current_neighbours) - inactive_vertices - set(active_vertices))  == 0:
                # If none, then remove the current path and record the endpoint as inactive.
                active_vertices_path_dict.pop(vertex, None)
                inactive_vertices.add(vertex)
            else:
                # Otherwise extend the paths, remove the previous one and update the inactive vertices.
                for neighbour_vertex in current_neighbours - inactive_vertices - set(active_vertices):
                    active_vertices_path_dict[neighbour_vertex] = current_path + [neighbour_vertex]
                    active_vertices.append(neighbour_vertex)
                active_vertices_path_dict.pop(vertex, None)
                inactive_vertices.add(vertex)

    return None

print (bi_directional_search(example_graph,0,16))
