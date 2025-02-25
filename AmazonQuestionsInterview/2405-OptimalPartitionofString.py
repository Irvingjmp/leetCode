def partitionString(s):
    
    seen = set()  
    partitions = 1  

    # Iterate through each character in the string
    for char in s:

        if char in seen:
            # Start a new partition
            partitions += 1
            seen.clear()  # Reset the set for the new substring
        seen.add(char)

    return partitions
s = "abacaba"
print(partitionString(s))
