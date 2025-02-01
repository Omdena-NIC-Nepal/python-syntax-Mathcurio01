def format_string(name, age):
    """
    Create a formatted string using f-strings.
    Args:
        name (str): Person's name
        age (int): Person's age
    Returns:
    """
    return f"My name is {name} and I am {age} years old"

def conditional_check(number):
    """
    Check if a number is greater, lesser, or equal to 10.
    Args:
        number (int): Number to check
    Returns:
    if (number>10):
       print("number is greater than 10")
    elif(number=10):
      print("number is equal to 10 ")
    else:
    print("less than 10")
        str: "Greater", "Lesser", or "Equal"
    """
    if (number>10):
        return "Greater"
    elif(number==10):
        return "Equal"
    elif(number<10):
        return "Lesser"

def loop_sum(n):
    """
    Calculate sum of numbers from 1 to n using a loop.
    Args:
        n (int): Upper limit
    Returns:
        
    """
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
    return sum


def list_operations(numbers):
    """
    Perform operations on a list of numbers.
    Args:
        numbers (list): List of numbers
       
    Returns:

        tuple: (sum, max, min)
    """
    return(sum(numbers),max(numbers), min(numbers))

def dict_operations(students_dict):
    """
    Find students with scores above 80.
    Args:
        students_dict (dict): Dictionary of student names and scores
      
    Returns:
        list: Names of students with scores > 80
        
    """
    lists = []
    for student in students_dict.keys():
        if(students_dict[student] >= 80):
            lists.append(student)
    return lists

def set_operations(list1, list2):
    """
    Find common elements between two lists.
    Args:
        list1 (list): First list
        list2 (list): Second list
    Returns:
        set: Common elements
    """
    common = set(list1).intersection(set(list2))
    return common
            

def arithmetic_ops(a, b):
    """
    Perform arithmetic operations.
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        dict: Results of arithmetic operations
    """
    return {
        "sum": a+b,
        "difference": a-b,
        "product":a*b,
        "quotient":a/b

    }
    


def logical_ops(x, y):
    """
    Perform logical operations.
    Args:
        x (bool): First boolean
        y (bool): Second boolean
    Returns:
        dict: Results of logical operations
    """
    return {
        'and' : x and y,
        'or': x or y,
        'not_x' : not x

    }

def bitwise_ops(a, b):
    """
    Perform bitwise operations.
    Args:
        a (int): First integer
        b (int): Second integer
    Returns:
        dict: Results of bitwise operations
    """
    return {
        'and':a & b,
        'or':a | b,
        'xor':a^b
    }

    pass