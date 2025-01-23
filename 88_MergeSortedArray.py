def merge(nums1, m, nums2, n):
    i = m - 1  # Puntero al último elemento válido de nums1
    j = n - 1  # Puntero al último elemento de nums2
    k = m + n - 1  # Puntero al último índice total en nums1
    
    # Comparar y llenar desde el final
    while i >= 0 and j >= 0:
        print(i,j)
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1  # Mueve el puntero de nums1
        else:
            nums1[k] = nums2[j]
            j -= 1  # Mueve el puntero de nums2
        k -= 1  # Mueve el puntero en nums1
    print(k)
    # Si quedan elementos en nums2, cópialos a nums1
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
    print(nums1)

nums1 = [4, 5, 6, 0, 0, 0]
m = 3
nums2 = [1, 2, 3]
n = 3

merge(nums1,m,nums2,n)