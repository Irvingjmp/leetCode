def getMaxThroughput(host_throughput):
    # Si hay menos de 3, no se forma ninguna tripleta
    if len(host_throughput) < 3:
        return 0
    
    # 1. Ordenar
    host_throughput.sort()
    print(host_throughput)
    n = len(host_throughput)
    
    # 2. Cantidad de tripletas
    k = n // 3
    
    # 3. Inicializar el total
    total = 0
    
    # 4. Sumamos los 'k' valores en posiciones n-2, n-4, n-6, ...
    for i in range(k):
        
        total += host_throughput[n - 2*(i+1) ]
        print(host_throughput[n - 2*(i+1) ])
    return total

# host_throughput = [1, 3, 2, 6, 5, 4]
# host_throughput = [10, 8, 7, 5, 2, 1]
# host_throughput = [3, 4, 4, 5, 6, 6, 8]
host_throughput = [1,2,3,4,5,6]
print(getMaxThroughput(host_throughput))