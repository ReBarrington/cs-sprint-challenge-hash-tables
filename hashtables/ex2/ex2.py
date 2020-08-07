#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

def reconstruct_trip(tickets, length):

    route = [None] * length
    connections = {}

    for ticket in tickets:

        connections[ticket.source] = ticket.destination

    # reset the initial destination
    destination = connections['NONE']
    # iterate over the length
    
    for i in range(length):
        # set the route i to destination
        route[i] = destination
        # set the destination to the next ticket's destination
        destination = connections[destination]

    return route