class Grafo: # Clase Grafo
    def __init__(self, vertices): # Construtor
        self.V = vertices # Número de Vértices 
        self.grafo = [] # Lista de listas de adjacências 

    def adicionar_aresta(self, u, v, w): # Adicionar aresta
        self.grafo.append([u, v, w]) # Adicionar vertices e peso

    def busca(self, pai, i): # Buscar vértices
        if pai[i] == i: # Se o pai for o próprio vértice
            return i # Retornar o vértice
        return self.busca(pai, pai[i]) # Chamar recursivamente

    def uniao_das_vertices(self, pai, rank, x, y): # Unir vértices
        raiz_x = self.busca(pai, x) # Buscar vértice x
        raiz_y = self.busca(pai, y) # Buscar vértice y

        if rank[raiz_x] < rank[raiz_y]: # Se o rank de x for menor que o rank de y 
            pai[raiz_x] = raiz_y # pai de x recebe y
        elif rank[raiz_x] > rank[raiz_y]: # Se o rank de x for maior que o rank de y
            pai[raiz_y] = raiz_x # pai de y recebe x
        else: # Se o rank de x for igual ao rank de y
            pai[raiz_y] = raiz_x # pai de y recebe x
            rank[raiz_x] += 1 # Incrementar rank de x

    def algoritmo_kruskal(self): # Algoritmo de Kruskal
        resultado = [] # Lista de resultados
        i, e = 0, 0 # Indice e quantidade de arestas
        self.grafo = sorted(self.grafo, key=lambda item: item[2]) # Ordenar lista de adjacências por peso
        pai = [] # Lista de pais
        rank = [] # Lista de ranks

        for nodulo in range(self.V): # Criar lista de pais e ranks
            pai.append(nodulo) # Criar lista de pais
            rank.append(0) # Criar lista de ranks

        while e < self.V - 1: # Enquanto quantidade de arestas for menor que o número de vezes 
            u, v, w = self.grafo[i] # U, V e peso da aresta
            i = i + 1 # Incrementar indice
            x = self.busca(pai, u) # Buscar vértice x
            y = self.busca(pai, v) # Buscar vértice y

            if x != y: # Se x for diferente de y 
                e = e + 1 # Incrementar quantidade de arestas
                resultado.append([u, v, w]) # Adicionar aresta ao resultado
                self.uniao_das_vertices(pai, rank, x, y) # Unir vértices

        total_peso = 0 # Variável para o peso total
        for u, v, w in resultado: # Para cada aresta no resultado
            total_peso += w # Adicionar peso da aresta ao peso total

        return total_peso # Retornar peso total


if __name__ == "__main__": # Caso o arquivo seja chamado diretamente
    N, M = map(int, input("Adicionar o número N, M separada por um espaço: ").split()) # Ler N e M
    entrada = [] # Lista de entradas
    for _ in range(M): # Para cada 
        x, y, r = map(int, input("Adicionar x, y, r separados por um espaço: ").split()) # Ler x, y e r
        entrada.append([x, y, r]) # Adicionar entradas a lista

    grafo = Grafo(N) # Criar grafo

    for x, y, r in entrada: # Para cada entrada
        grafo.adicionar_aresta(x - 1, y - 1, r) # Adicionar aresta ao grafo

    resultado = grafo.algoritmo_kruskal() # Chamar algoritmo de Kruskal
    print("Resultado: ", + resultado) # Imprimir resultado
