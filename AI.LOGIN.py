# This program will prompt the user to opt in or out of basic encryption standards. If the user opts in, the program will use the SHA3-384 hashing algorithm to store the key tags. The program also includes user interaction for adding symbol-value pairs to a session and retrieving the value of a symbol. The getpass function is used to hide the user’s input when they enter their user ID, symbol, and value.

import random
import string
import hashlib
from getpass import getpass

# Function to generate a random session ID
def generate_session_id(length=10):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

# Function to hash a key tag using SHA3-384
def hash_key_tag(key_tag):
    return hashlib.sha3_384(key_tag.encode()).hexdigest()

# Dictionary to store symbol-value pairs
symbol_value_dict = {}

# Dictionary to store session storage matrix
session_storage_matrix = {}

# Function to add a symbol-value pair
def add_symbol_value_pair(symbol, value, use_encryption):
    if use_encryption:
        symbol = hash_key_tag(symbol)
    symbol_value_dict[symbol] = value

# Function to get value of a symbol
def get_symbol_value(symbol, use_encryption):
    if use_encryption:
        symbol = hash_key_tag(symbol)
    return symbol_value_dict.get(symbol, None)

# Function to add a session
def add_session(user_id):
    session_id = generate_session_id()
    session_storage_matrix[session_id] = {'user_id': user_id, 'symbol_value_dict': {}}
    return session_id

# Function to get session info
def get_session_info(session_id):
    return session_storage_matrix.get(session_id, None)

# Function to add a symbol-value pair to a session
def add_symbol_value_pair_to_session(session_id, symbol, value, use_encryption):
    session_info = get_session_info(session_id)
    if session_info is not None:
        if use_encryption:
            symbol = hash_key_tag(symbol)
        session_info['symbol_value_dict'][symbol] = value

# User interaction
def user_interaction():
    use_encryption = input("Do you want to use basic encryption standards (yes/no)? ")
    use_encryption = use_encryption.lower() == 'yes'
    user_id = getpass("Enter your user ID: ")
    session_id = add_session(user_id)
    print(f"Created a new session with ID: {session_id}")
    while True:
        action = input("Enter 'add' to add a symbol-value pair, 'get' to get a value, or 'quit' to quit: ")
        if action.lower() == 'add':
            symbol = getpass("Enter the symbol: ")
            value = getpass("Enter the value: ")
            add_symbol_value_pair_to_session(session_id, symbol, value, use_encryption)
            print("Added symbol-value pair to session.")
        elif action.lower() == 'get':
            symbol = getpass("Enter the symbol: ")
            value = get_symbol_value(symbol, use_encryption)
            print(f"The value of the symbol is: {value}")
        elif action.lower() == 'quit':
            break
        else:
            print("Invalid action. Please enter 'add', 'get', or 'quit'.")

if __name__ == "__main__":
    user_interaction()
