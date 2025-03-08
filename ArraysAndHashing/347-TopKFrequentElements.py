class Solution(object):
    def topKFrequent(self, nums, k):
        # 1. Crear un diccionario para contar la frecuencia de cada número
        frequency_map = {}
        for num in nums:
            if num in frequency_map:
                frequency_map[num] += 1
            else:
                frequency_map[num] = 1
        
        # 2. Convertir el diccionario en una lista de tuplas (elemento, frecuencia)
        frequency_list = list(frequency_map.items())
        
        # 3. Ordenar la lista por la frecuencia en orden descendente
        frequency_list.sort(key=lambda x: x[1], reverse=True)
        
        result = [element[0] for element in frequency_list[:k]]
        print(result)
        return result

sol = Solution()
sol.topKFrequent([1,1,1,2,2,3], 2)