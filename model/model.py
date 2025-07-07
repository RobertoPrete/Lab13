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

    def getGraphDetails(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()

    def setYear(self, year):
        self._year = year

    def getYears(self):
        return DAO.getAllYears()
