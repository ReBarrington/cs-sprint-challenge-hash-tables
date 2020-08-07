#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):

    route = []
    location = "NONE"

    for i in range(length):

        if tickets[i].source == location:
            if tickets[i].destination != "NONE":
                route.append(tickets[i].destination)
            location = tickets[i].destination
            continue
    return route