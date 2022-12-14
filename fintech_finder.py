# Cryptocurrency Wallet
################################################################################
# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3
from crypto_wallet import generate_account, get_balance, send_transaction

w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))

################################################################################
# Fintech Finder Candidate Information

# Database of Fintech Finder candidates including their name, digital address, rating and hourly cost per Ether.
# A single Ether is currently valued at $1,500
candidate_database = {
    "Lane": ["Lane", "0xaC8eB8B2ed5C4a0fC41a84Ee4950F417f67029F0", "4.3", .20, "Images/lane.jpeg"],
    "Ash": ["Ash", "0x2422858F9C4480c2724A309D58Ffd7Ac8bF65396", "5.0", .33, "Images/ash.jpeg"],
    "Jo": ["Jo", "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", "4.7", .19, "Images/jo.jpeg"],
    "Kendall": ["Kendall", "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", "4.1", .16, "Images/kendall.jpeg"]
}

# A list of the FinTech Finder candidates first names
people = ["Lane", "Ash", "Jo", "Kendall"]


def get_people(w3):
    """Display the database of Fintech Finders candidate information."""
    db_list = list(candidate_database.values())

    for number in range(len(people)):
        st.image(db_list[number][4], width=200)
        st.write("Name: ", db_list[number][0])
        st.write("Ethereum Account Address: ", db_list[number][1])
        st.write("FinTech Finder Rating: ", db_list[number][2])
        st.write("Hourly Rate per Ether: ", db_list[number][3], "eth")
        st.text(" \n")

################################################################################
# Streamlit Code

# Function that displays the etherium balance of the customer’s account.
def write_etherium_balance(address):
    # Write the returned ether balance to the sidebar
    ether_balance = get_balance(w3, address)
    st.sidebar.write(f"Account Balance: {ether_balance:.2f}")

# Function that calculates total_wage
def calculate_wage(hourly_rate, number_of_hours):
    return hourly_rate * number_of_hours
    
################################################################################
# Streamlit application headings
st.markdown("# Fintech Finder!")
st.markdown("## Hire A Fintech Professional!")
st.text(" \n")

################################################################################
# Streamlit Sidebar Code - Start
st.sidebar.markdown("## Client Account Address and Ethernet Balance in Ether")

##########################################
# Generate account
account = generate_account()

##########################################
# Write the client's Ethereum account address to the sidebar
st.sidebar.write(account.address)

##########################################
# Write the returned ether balance to the sidebar
write_etherium_balance(account.address)   
    
##########################################
# Create a select box to chose a FinTech Hire candidate
person = st.sidebar.selectbox('Select a Person', people)

# Create a input field to record the number of hours the candidate worked
hours = st.sidebar.number_input("Number of Hours")

st.sidebar.markdown("## Candidate Name, Hourly Rate, and Ethereum Address")

# Identify the FinTech Hire candidate
candidate = candidate_database[person][0]

# Write the Fintech Finder candidate's name to the sidebar
st.sidebar.write(candidate)

# Identify the FinTech Finder candidate's hourly rate
hourly_rate = candidate_database[person][3]

# Write the inTech Finder candidate's hourly rate to the sidebar
st.sidebar.write(hourly_rate)

# Identify the FinTech Finder candidate's Ethereum Address
candidate_address = candidate_database[person][1]

# Write the FinTech Finder candidate's Ethereum Address to the sidebar
st.sidebar.write(candidate_address)

st.sidebar.markdown("## Total Wage in Ether")

################################################################################
# Call wage calculation and write on the sidebar
total_wage = calculate_wage(hourly_rate, hours)

# Write the `wage` calculation to the Streamlit sidebar
st.sidebar.write(total_wage)

##########################################
if st.sidebar.button("Send Transaction"):

    # Call the `send_transaction` function and pass it 3 parameters:
    # `account`, the `candidate_address`, and the `wage` as parameters
    transaction_hash = send_transaction(w3, account, candidate_address, total_wage)

    # Markdown for the transaction hash
    st.sidebar.markdown("#### Validated Transaction Hash")

    # Write the returned transaction hash to the screen
    st.sidebar.write(transaction_hash)

    # Celebrate your successful payment
    st.balloons()

# The function that starts the Streamlit application
# Writes FinTech Finder candidates to the Streamlit page
get_people(w3)
