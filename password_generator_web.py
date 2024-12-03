import streamlit as st
from password_generator_cli import generate_password
from file_operations import write_passwords_to_file, read_passwords_from_file

st.title("Password Generator App")
st.write("This app generates a random password for you.")
st.write("You can also save the password to a file")

n_letters = st.number_input("Enter number of letters", min_value=0, value=4, key="letters") 
n_symbols = st.number_input("Enter number of symbols", min_value=0, value=4, key="symbols")
n_numbers = st.number_input("Enter number of letters", min_value=0, value=4, key="numbers")

if st.button("Generate Password"):
    passwords = generate_password(n_letters, n_symbols, n_numbers)
    st.success(f"Generated Password: , {passwords}")
    write_passwords_to_file(passwords)
    st.info("Password saved to file")

if st.checkbox("Show password"):
    passwords = read_passwords_from_file()
    st.write("Saved passwords:")
    for password in passwords:
        st.write(password)  # Display the password
    
else:
    st.warning("No passwords saved yet!")