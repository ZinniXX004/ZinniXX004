'''
Jeremia Christ Immanuel Manalu
5023231017

Probability and Statistics
'''

# Import required libraries and modules
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import os
import tempfile
import base64 # For downloading ECG data image

# Define the Streamlit app title and header (KPP BMW)
st.title("Probability and Statistics")
st.header("Name  : Jeremia Christ Immanuel Manalu")
st.subheader("NRP : 5023231017")

# Define a function to check if there is an appropiate path to the ECG data file. Else, it will raise an exception.
def load_data(file_path):
    try:
        data = np.loadtxt(file_path, dtype='float')
        return data
    except FileNotFoundError:
        st.error(f"File '{file_path}' Not found. Please upload your data file.")
        st.stop()

# Load the ECG data from the text(.txt) file
data_file_sebelum = "Heart Rate_Rainhard_Sebelum.txt"
data_before = load_data(data_file_sebelum)

data_file_sesudah = "Heart Rate_Rainhard_Sesudah.txt"
data_after = load_data(data_file_sesudah)

# Create a Streamlit sidebar to upload a new data file
uploaded_file = st.sidebar.file_uploader("Upload New Data (in .txt format)")

# If a new file is uploaded, load and visualize it
if uploaded_file is not None:
    new_data = np.loadtxt(uploaded_file)
    st.success("Data file uploaded successfully!")

# Plot and display the data (1)
st.write("## Health Rate Data Visualization")

# Data 1 (Before) 
data1 = data_before[10 : 500]

# Data 2 (After)
data2 = data_after[10 : 500]

# Configure the plot (1) and display it-> Data 1 with 10 : 500 ratio
plt.figure(figsize=(18, 8))
plt.plot(data1, color='red', label='Health Rate Plot (Before)')
plt.xlabel('Time') # x-axis label
plt.ylabel('Heart Rate') #y-axis label
plt.title('Before')
plt.grid(True)
st.pyplot(plt)

# Configure the plot (1) and display it-> Data 2 with 10 : 500 ratio
plt.figure(figsize=(18, 8))
plt.plot(data2, color='red', label='Health Rate Plot (After)')
plt.xlabel('Time') # x-axis label
plt.ylabel('Heart rate') #y-axis label
plt.title('After')
plt.grid(True)
st.pyplot(plt)
 
# Plot and display the data (2)
st.write("## Health Rate Data Full Visualization")

# Configure the plot (2) and display it -> Full Health Rate Data (Before)
Ndata1 = len(data_before)
Before_Full = np.arange(Ndata1)
plt.plot(Before_Full, data_before)
st.pyplot(plt) 

# Plot and display the data (2)
st.write("## Health Rate Data Full Visualization")

# Configure the plot (2) and display it -> Full Health Rate Data (After)
Ndata2 = len(data_after)
After_Full = np.arange(Ndata2)
plt.plot(After_Full, data_after)
st.pyplot(plt) 
