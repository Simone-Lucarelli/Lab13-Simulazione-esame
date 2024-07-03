def handlepath(self):
    self.maxdistance = 0
    self.bestpath = []

    for nodo in self.graph.nodes():
        last_node = nodo
        self.recursive(last_node, [], 0, [last_node])

    printable_path = self.printablepath(self.bestpath)

    return self.maxdistance, printable_path


def recursive(self, last_node, partial, last_weight, visited):
    # uscita preventiva dalla ricorsione (es cerca cammino di tot archi e noi abbiamo un parziale più lungo di tot
    archiammissibili = self.getArchiAmmissibili(last_node, last_weight, visited)

    if not archiammissibili:  # per cammini chiusi invece la condizione è last_node == first_node
        distTot = self.calcolaDistTot(partial)
        if distTot > self.maxdistance:  # aggiungere altre condizioni su cammini chiusi di almeno tot passi o esattamente tot passi
            self.maxdistance = distTot
            self.bestpath = copy.deepcopy(partial)
    else:
        for edge in archiammissibili:
            partial.append(edge)
            visited.append(edge[1])
            self.recursive(edge[1], partial, edge[2]["weight"], visited)
            partial.pop()
            visited.pop()


def getArchiAmmissibili(self, last_node, last_weight, visited):
    output = []
    archivicini = self.graph.edges(last_node, data=True)
    for edge in archivicini:
        if edge[2]["weight"] > last_weight and edge[1] not in visited:
            output.append(edge)
    return output


def calcolaDistTot(self, partial):
    distTot = 0
    for edge in partial:
        dist = geodesic((edge[0].Lat, edge[0].Lng), (edge[1].Lat, edge[1].Lng)).kilometers
        distTot += dist
    return distTot


def printablepath(self, path):
    result = []
    for edge in path:
        result.append(
            f"{edge[0].id}->{edge[1].id}, peso: {edge[2]['weight']}, distanza: {geodesic((edge[0].Lat, edge[0].Lng), (edge[1].Lat, edge[1].Lng)).kilometers}")
    return result