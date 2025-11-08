from queue import Queue


def matchmake(queue, user):
    name, action = user[0], user[1]
    if action == "leave":
        queue.search_and_remove(name)
    if action == "join":
        queue.push(name)
    if queue.size() >= 4:
        user1 = queue.pop()
        user2 = queue.pop()
        return f"{user1} matched {user2}!"
    else:
        return "No match found"
    





if __name__ == "__main__":
    pass
