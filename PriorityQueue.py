import heapq

class PriorityQueue:
    '''Priority class'''
    def __init__(self):
        '''initialize Priority class'''
        self.elements = []

    def empty(self):
        '''check if queue empty'''
        return len(self.elements) == 0

    def put(self, item, priority):
        '''put item with priority to the queue'''
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        '''get the element element in queue'''
        return heapq.heappop(self.elements)

    def update(self, item, priority):
        '''update new item to queue'''
        for index, (p, i) in enumerate(self.elements):
            if i == item:
                if p <= priority:
                    break
                del self.elements[index]
                self.elements.append((priority, item))
                heapq.heapify(self.elements)
                break
        else:
            self.put(item, priority)
