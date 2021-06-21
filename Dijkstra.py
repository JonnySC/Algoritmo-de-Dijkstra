 def dijkstra(self):

        print('Ingresa el nodo inicial para Dijkstra: ')
        a = int(input())
        if a in self.vertices:
            self.vertices[a].distancia = 0
            actual = a
            noVisitados = []
            for v in self.vertices:
                if v != a:
                    self.vertices[v].distancias = float('inf')
                self.vertices[v].padre = None
                noVisitados.append(v)
            while len(noVisitados) > 0:
                for vecino in self.vertices[actual].vecinos:
                    if self.vertices[vecino[0]].visitado == False:
                        if self.vertices[actual].distancia + vecino[1] < self.vertices[vecino[0]].distancia:
                            self.vertices[vecino[0]].distancia = self.vertices[actual].distancia + vecino[1]
                            self.vertices[vecino[0]].padre = actual

                self.vertices[actual].visitado = True
                noVisitados.remove(actual)
                actual = self.minimo(noVisitados)
        else:
            return False
