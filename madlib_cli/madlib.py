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
    pass


def read_template(path):
    """
    A function that reads a file in the asset folder, then returns a stripped string of the file contents
    """
    print("path", path)
    with open(path) as file:
        contents = file.read()
        print("TEST 1", type(contents))
        return contents


def parse_template(template):
    actual_stripped = ""
    actual_adjective = []
    cut_out_word = False
    word = ""
    stripped_template = template.strip()
    for char in stripped_template:
        if cut_out_word == True:
            if char == "}":
                actual_adjective.append(word)
                actual_stripped += char
                word = ""
                cut_out_word = False
            #if char != "}":
            else:
                word += char
        else:
            actual_stripped += char
            if char == "{":
                cut_out_word = True
    return actual_stripped, tuple(actual_adjective)







def merge(actual_stripped, actual_adjective):
    result = actual_stripped.format(*actual_adjective)
    return result

if __name__ == "__main__":
    welcome_message()
    enter_adjectives_and_noun()
    path = "assets/dark_and_stormy_night_template.txt"
    read_template(path)

