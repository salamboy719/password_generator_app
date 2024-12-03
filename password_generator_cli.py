import random
letters = [ "a", "b", "c"]
numbers = ["0", "1", "2"]
symbols = ["@", "#", "$"]


def generate_password(n_letters, n_numbers, n_symbols):

    letter_choices = [random.choice(letters) for i in range(n_letters)] 
    number_choices = [random.choice(numbers) for i in range(n_numbers)] 
    symbols_choices = [random.choice(symbols) for i in range(n_symbols)] 

    password_list = letter_choices + number_choices + symbols_choices + symbols_choices

    random.shuffle(password_list)
    
    return "".join(password_list)
