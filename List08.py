def main(fruits):
    """
    A list called "fruits" is given and is five in length and contains at least one "apple". Remove the apples from the list and return the list.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    i=0
    n=len(fruits)
    while i<n:
        if fruits[i]=='apple':
            fruits.pop(i)
        n=len(fruits)
        i+=1
    return fruits
fruits=['apple','kivi','apple','banana','apple']
print(main(fruits))