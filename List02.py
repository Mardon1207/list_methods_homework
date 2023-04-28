def main(fruits,x,i):
    """
    You will be given a list of fruits. Add the x fruit to the i index and return it.
    Args:
        fruits(list): parameter 
        x(str): parameter
        i(int): parameter
    Returns:
        list: return answer
    """
    fruits.insert(i,x)
    return fruits
fruits=['apple','banana']
i=int(input())
x=str(input())
print(main(fruits,x,i))