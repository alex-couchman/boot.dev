from queue import Queue


def matchmake(queue, user):
    name, action = user[0], user[1]
    if action == "leave":
        queue.search_and_remove(name)

if __name__ == "__main__":
    queue = Queue()
    queue.push

