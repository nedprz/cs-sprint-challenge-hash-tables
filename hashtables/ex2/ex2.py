#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
cache = {}
def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    route = [None] * length
        
    for ticket in tickets:
        cache[ticket.source] = ticket.destination

    destination = cache["NONE"]
    
    for i in range(length):
        route[i] = destination
        destination = cache[destination]

    return route