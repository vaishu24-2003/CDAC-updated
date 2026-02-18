batch_bangalore = {"Amit", "Ravi", "Sneha", "Priya"}
batch_pune = {"Ravi", "Karan", "Sneha", "Meena"}
#Get All Students (Union)
def get_all_students(batch1: set, batch2: set) -> set:
    """
    Returns union of both batches.
    """

    if not isinstance(batch1, set) or not isinstance(batch2, set):
        raise ValueError("Both inputs must be sets")

    return batch1 | batch2
#Get Common Students (Intersection)
def get_common_students(batch1: set, batch2: set) -> set:
    """
    Returns intersection of both batches.
    """

    if not isinstance(batch1, set) or not isinstance(batch2, set):
        raise ValueError("Both inputs must be sets")

    return batch1 & batch2
#Get Exclusive Students (Only in Batch1)
def get_exclusive_students(batch1: set, batch2: set) -> set:
    """
    Returns students who are only in batch1.
    """

    if not isinstance(batch1, set) or not isinstance(batch2, set):
        raise ValueError("Both inputs must be sets")

    return batch1 - batch2
#Demonstration
if __name__ == "__main__":

    batch_bangalore = {"Amit", "Ravi", "Sneha", "Priya"}
    batch_pune = {"Ravi", "Karan", "Sneha", "Meena"}

    print("All Students:", get_all_students(batch_bangalore, batch_pune))
    print("Common Students:", get_common_students(batch_bangalore, batch_pune))
    print("Exclusive to Bangalore:",
          get_exclusive_students(batch_bangalore, batch_pune))
