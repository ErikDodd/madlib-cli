def welcome_message():
    """
    Welcome message greeting user and explaining how to play
    """
    print("Welcome to my Madlib CLI Edition! To play, simply respond to the prompts. Enjoy!")


def enter_adjectives_and_noun():
    """
   Prompt user to enter an adjective 
   """
    # Make This More DRY later on
    print("Please enter an adjective")
    first_adjective = input("> ")
    print("Please enter an adjective")
    second_adjective = input("> ")
    print("Please enter a noun")
    noun = input("> ")


def read_template():
    """
    A function that reads a file in the asset folder, then returns a stripped string of the file contents
    """
    with open("assets/dark_and_stormy_night_template.txt") as file:
        contents = file.read()
        return contents


def parse_template():
    # Need to use * operator to strip the string
    pass


def merge():
    # Use format () to insert user inputs into the placeholders
    pass


welcome_message()
enter_adjectives_and_noun()
read_template()

