import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._year = None

        self._graph = nx.Graph()
        self._drivers = DAO.getAllDrivers()
        self._idMapDrivers = {}
        for driver in self._drivers:
            self._idMapDrivers[driver.driverId] = driver
        self._nodes = None
        self._edges = None

    def buildGraph(self):
        self._graph.clear()
        self._nodes = DAO.getAllNodes(self._year)
        self._graph.add_nodes_from(self._nodes)
        self._edges = DAO.getAllEdges(self._year, self._idMapDrivers)
        # for edge in self._edges:
            # u = edge.d1
            # v = edge.d2
            # if self._graph.has_edge(u, v):
                # self._graph[u][v]['weight'] += 1
            # else:
                # self._graph.add_edge(u, v, weight=1)
        for edge in self._edges:
            self._graph.add_edge(edge.d1, edge.d2, weight=edge.peso)

    def getGraphDetails(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()

    def setYear(self, year):
        self._year = year

    def getYears(self):
        return DAO.getAllYears()
