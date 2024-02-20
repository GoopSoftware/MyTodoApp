FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    todo items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


    # Does not need to return any values it just needs to write. Doesnt need a variable
    # Because it returns NONE
def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the todo items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


# __name__ is == __main__ when running functions.py because it is the main file ran
# __name__ is == __functions__ when running cli.py
if __name__ == "__main__":
    print(get_todos())
