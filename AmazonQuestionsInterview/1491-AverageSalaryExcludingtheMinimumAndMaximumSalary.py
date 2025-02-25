from typing import List

class Solution:
    def average(self, salary: List[int]) -> float:
        max_salary = float('-inf')  # Inicializa al menor valor posible
        min_salary = float('inf')   # Inicializa al mayor valor posible
        total_sum = 0

        for employee in salary:
            max_salary = max(max_salary, employee)  # Encuentra el máximo
            min_salary = min(min_salary, employee)  # Encuentra el mínimo
            total_sum += employee  # Suma todos los salarios

        return (total_sum - max_salary - min_salary) / (len(salary) - 2)
