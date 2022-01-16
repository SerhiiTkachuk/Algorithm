graph = {"start": {"a": 5, "b": 2}, "a": {"d": 2, "с": 4}, "b": {"a": 8, "d": 7}, "c": {"d": 6, "fin": 3},
         "d": {"fin": 1}, "fin": {}}  # таблица графика зависимостей

infinity = float("inf")
costs = {"a": 5, "b": 2, "c": infinity, "d": infinity, "fin": infinity}  # таблица стоимостей

parents = {"a": "start", "b": "start", "c": None, "d": None, "fin": None}  # таблица родителей

processed = []  # массив для отслеживания уже обработанных узлов


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)  # находим узел с наименьшей стоимостью
while node is not None:  # если обработаны все узлы, цикл завершен
    print(node)
    cost = costs[node]
    neighbors = graph[node]
    print(neighbors)
    for n in neighbors.keys():
        print("n: " + n)
        new_cost = cost + neighbors[n]
        print(new_cost)
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
            print(costs)
    processed.append(node)
    node = find_lowest_cost_node(costs)

print(costs)
print(parents)
