#exercise 1

words = ['this' , 'is', 'a', 'sentence', '.']


def reverse(words, index1, index2, index3, index4, index5):
    words[index1], words[index2], words[index3], words[index4], words[index5] = words[index5], words[index4], words[index3], words[index2], words[index1]
    
    return words
    
reverse(words, 0, 1, 2, 3, 4)
    

#exercise 3

def binary_search(lst, target):
    lst = [10,23,70,45,11,15]
    low = 0 
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == lst[mid]:
            return f"The index for {target} is {mid}"
        elif target < lst[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

binary_search(lst,70)

