import heapq # Importar biblioteca heapq

def heap_comandos(): # Definir função
    heap = [] # Lista vazia
    comandos = int(input("Entre com o número de comandos: ")) # Receber entrada do usuário 

    for _ in range(comandos): # Loop para receber entrada do usuário 
        comando = input("Número: ").split() # Receber entrada do usuario e dividir em lista
        if comando[0] == '1': # Caso o comando seja 1
            value = int(comando[1]) # Receber valor
            heapq.heappush(heap, value) # Adicionar valor na lista
        elif comando[0] == '2': # Caso o comando seja 2
            value = int(comando[1]) # Receber valor 
            heap.remove(value) # Remover valor da lista
            heapq.heapify(heap) # Organizar lista
        elif comando[0] == '3': # Caso o comando seja 3
            if heap: # Caso a lista não esteja vazia 
                print(heap[0]) # Imprimir o primeiro valor da lista 
            else: # Caso a lista esteja vazia
                print("Heap está vazio") # Imprimir o aviso

if __name__ == "__main__": # Caso o arquivo seja chamado diretamente
    heap_comandos() # Chamar função