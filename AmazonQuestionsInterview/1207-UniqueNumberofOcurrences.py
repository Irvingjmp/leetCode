def uniqueOccurrences(arr):
    # Contar las frecuencias
    frecuencia = {}
    for num in arr:
        frecuencia[num] = frecuencia.get(num, 0) + 1

    # Verificar si las frecuencias son únicas
    return len(frecuencia.values()) == len(set(frecuencia.values()))

arr = [10,2,2,10,10,3]
print(uniqueOccurrences(arr))
