import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._year = None

        self._graph = nx.DiGraph()
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
        self.getAllEdgesV1()

    def getAllEdgesV1(self):
        """Raccoglie gli archi senza i pesi, i pesi li mette in seguito quando aggiunge gli archi al grafo"""
        self._edges = DAO.getAllEdgesV1(self._year, self._idMapDrivers)
        for edge in self._edges:
            u = edge.d1
            v = edge.d2
            if self._graph.has_edge(u, v):
                self._graph[u][v]['weight'] += 1
            else:
                self._graph.add_edge(u, v, weight=1)

    def getAllEdgesV2(self):
        """Raccoglie gli archi con i pesi associati in modo da aggiungerli direttamente al grafo"""
        self._edges = DAO.getAllEdgesV2(self._year, self._idMapDrivers)
        for edge in self._edges:
            self._graph.add_edge(edge.d1, edge.d2, weight=edge.peso)

    def getGraphDetails(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()

    def getBestDriver(self):
        risultati = []
        for driver in self._graph.nodes():
            driverScore = 0
            vittorie = 0
            sconfitte = 0
            for e in self._graph.out_edges(driver, data=True):
                vittorie = vittorie + e[2]["weight"]
            for e in self._graph.in_edges(driver, data=True):
                sconfitte = sconfitte + e[2]["weight"]
            driverScore = vittorie - sconfitte
            risultati.append((driver, driverScore))
        vittorieOrdinate = sorted(risultati, key=lambda x: x[1], reverse=True)
        return vittorieOrdinate[0]


    def setYear(self, year):
        self._year = year

    def getYears(self):
        return DAO.getAllYears()
