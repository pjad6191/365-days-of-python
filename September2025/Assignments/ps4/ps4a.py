# Problem Set 4A
# Name: Pamela Brown
# Time Spent: 1 hr

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    if len(sequence) == 1:
        return [sequence]
    
    base = sequence[0]
    rest = sequence[1:]
    perms_without_first = get_permutations(rest)
    
    
    results = []
    for perm in perms_without_first:        #Loop through each permutation in perms without first
        for i in range(len(perm) + 1):      # Insert base into every possible position
            new_perm = perm[:i] + base + perm[i:]
            results.append(new_perm)
            
    return results
'''
if __name__ == '__main__':
    '''

sequence = 'abcd'

print("Input:", sequence)
print("Output:", get_permutations(sequence))
    










    
    


