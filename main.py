from collections import OrderedDict

graph = {
    'A': {'B': 5, 'D': 5, 'E': 7},
    'B': {'C': 4},
    'C': {'D': 8, 'E': 2},
    'D': {'C': 8, 'E': 6},
    'E': {'B': 3},
}


def distance_between_stops(rail_line):
    node_line = rail_line.split('-')
    distance = 0
    try:
        for i in range(len(node_line) - 1):
            distance += graph[node_line[i]][node_line[i+1]]
    except:
        return 'NO SUCH ROUTE'
    return distance

def all_routes_util(starting, current, ending, routes, visited):
    nodes = graph[current].keys()
    visited.append(current)
    for node in nodes:
        if node != ending and node not in visited:
            routes.append("{}{}{}".format(starting, current, node))
            all_routes_util(starting, node, ending, routes, visited)
        else:
            routes.append("{}-".format(ending))
    return routes

def all_routes(start_stop, end_stop):
    routes = all_routes_util(start_stop, start_stop, end_stop, [], [])
    lines = []
    routes_string = "".join(routes)
    for item in  routes_string.split("-"):
        if item != "":
            lines.append("".join(OrderedDict.fromkeys(item)))
    return lines[:]


def number_of_stops(start_stop, end_stop, max_stops):
    routes = all_routes(start_stop, end_stop)
    lines = []
    print(routes)
    for route in routes:
        if len(route) <= max_stops:
            lines.append(route)
    return len(lines)
