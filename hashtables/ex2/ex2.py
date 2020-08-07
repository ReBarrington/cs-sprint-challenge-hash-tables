#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def set_destination(self, new_destination):
        self.destination = new_destination

def reconstruct_trip(tickets, length):

    route = []
    connections = {}

    for i in range(length):

        if tickets[i].source not in connections.values():
            connections[tickets[i].source] = [tickets[i].destination]
        
        else:
            # this source/key is a value inside connections 
            connections[tickets[i].source].append(tickets[i].destination)

        if tickets[i].source == "NONE":
            # first flight
            route.append(connections.get(tickets[i].source))
            continue

    # # last destination will be NONE
    # route.pop()
    return route

