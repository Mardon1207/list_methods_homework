def main(numbers,i):
    """
    You are given a list of numbers. i Delete and return the number in the index.
    Args:
        numbers(list): parameter
        i(int): parameter
    Returns:
        list: return answer
    """
    fruits.pop(i)
    return fruits
fruits=[1,2,3,4,5,6,7,8]
i=int(input())
print(main(fruits,i))