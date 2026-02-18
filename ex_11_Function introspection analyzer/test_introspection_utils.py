from introspection_utils import analyze_function


def greet(name):
    """Returns greeting message."""
    return "Hello " + name


print("----- Testing with Custom Function -----")
analyze_function(greet)

print("\n\n----- Testing with Built-in Function (str.upper) -----")
analyze_function(str.upper)
