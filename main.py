class Node:
    id: int
    neighbours: list[Node]
    isPh: bool

    def __int__(self):
        self.id = 0
        self.neighbours = []
        self.isPh = False


class Graph:
    nodes: list[Node]

    def __int__(self):
        self.nodes: list[Node] = None

    def load(self):
        noNodes, noPhs = map(int, input().split(' '))
        phRestaurants = map(int, input().split(' '))
        self.nodes = Node[Node() * noNodes]

        # initialization
        for i in range(noNodes):
            self.nodes[i].id = i
            if i in phRestaurants:
                self.nodes[i].isPh = True

        # read in paths.
        for i in range(noNodes - 1):
            start, end = map(int, input().split(' '))
            self.nodes[start].neighbours.append(self.nodes[end])
            self.nodes[end].neighbouts.append(self.nodes[start])

    def collectLeaves(self) -> list[Node]:
        leaves = []
        for node in self.nodes:
            if len(node.neighbours) == 1 and not node.isPh:
                leaves.append(node)
        return leaves

    def cutLeaves(self, leaves: list[Node]) -> list[Node]:
        returnLeaves = []
        for leave in leaves:
            neighbour = leave.neighbours[0]
            neighbour.neighbours.remove(leave)
            self.nodes.remove(leave)
            if len(neighbour.neighbours) == 1 and not neighbour.isPh:
                returnLeaves.append(neighbour)
        return returnLeaves

    def cut(self):
        leaves = self.collectLeaves()
        while leaves:
            leaves = self.cutLeaves(leaves)

    def getFurthestNode(self, parent: Node, current: Node) -> tuple[Node, int]:
        distance = 0
        furthestNode = None

        if len(current.neighbours) == 1:
            return current, 0

        for child in current.neighbours:
            if child != parent:
                fNode, dist = self.getFurthestNode(current, child)
                if distance < dist:
                    distance = dist
                    furthestNode = fNode
        return furthestNode, distance+1

    def getFurthestNode(self, start: Node) -> tuple[Node, int]:
        distance = 0
        furthestNode = None

        for node in start.neighbours:
            fNode, dis = self.getFurthestNode(start, node)
            if dis > distance:
                distance = dis
                furthestNode = fNode
        return furthestNode, distance+1

    def getDiameter(self) -> int:
        node = self.nodes[0]
        node, distance = self.getFurthestNode(node)
        node, distance = self.getFurthestNode(node)
        return distance

    def getNoPaths(self) -> int:
        return len(self.nodes)-1


graph: Graph = Graph()
graph.load()
graph.cut()
diameter = graph.getDiameter()
print(diameter + (graph.getNoPaths() - diameter) * 2)
