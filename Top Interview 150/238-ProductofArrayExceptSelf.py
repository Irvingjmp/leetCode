def productExceptSelf(nums):
    n = len(nums)
    answer = [1] * n

    # Calcular productos prefix
    prefix_product = 1
    for i in range(n):
        answer[i] = prefix_product
        print(answer)
        prefix_product *= nums[i]
        print(prefix_product)

    # Calcular productos suffix
    suffix_product = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix_product
        print("suffix_product",suffix_product)
        suffix_product *= nums[i]

    return answer

nums = [1,2,3,4]
productExceptSelf(nums)