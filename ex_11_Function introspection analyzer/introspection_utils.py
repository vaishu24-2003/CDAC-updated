def analyze_function(func):
    """
    Analyzes a function using introspection tools.

    It will:
    - Print type(func)
    - Print first 10 results of dir(func)
    - Display help(func)
    """

    print("Type of function:")
    print(type(func))

    print("\nFirst 10 attributes from dir():")
    attributes = dir(func)
    print(attributes[:10])

    print("\nHelp documentation:")
    help(func)
