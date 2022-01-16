from collections import deque


# Реализация графа(схема о стрелками) с помощью хеш-таблици(словаря)
graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = ['']
graph['peggy'] = ['']
graph['thom'] = ['']
graph['jonny'] = ['']

def search(name):
    search_queue = deque()  # создаем очередь
    #search_queue = []
    search_queue += graph[name] # добавляем список имен первой линии
    searched = [] # создаем список проверенных
    while search_queue:
        person = search_queue.popleft()
        #person = search_queue.pop(0)
        if not person in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False            

def person_is_seller(name):
    return name[-1] == 'm'

search('you')
