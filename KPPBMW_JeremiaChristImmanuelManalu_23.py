'''
Author : Jemy
NN     : znt_sp_4

(+)
Includes an upload option to visualize a new ECG data file for ".txt" extension.
Includes a download button for downloading the ECG data.
Two ways to help visualize the given ECG data.

(-)
The downloaded ECG data is in temporary file (.csv extension)
'''

# Import required libraries and modules
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import os
import tempfile

# Define the Streamlit app title and header (KPP BMW)
st.title("KPP BMW")
st.subheader("Name  : Jeremia Christ Immanuel Manalu")
st.subheader("Batch : BME 23")

# Define a function to check if there is an appropiate path to the ECG data file. Else, it will raise an exception.
def load_ecg_data(file_path):
    try:
        ecg_data = np.loadtxt(file_path, dtype='float')
        return ecg_data
    except FileNotFoundError:
        st.error(f"File '{file_path}' not found. Please upload your ECG data file.")
        st.stop()

# Load the ECG data from the text(.txt) file
ecg_data_file = "Data_ECG.txt"
ecg_data = load_ecg_data(ecg_data_file)

# Create a Streamlit sidebar to upload a new ECG data file
uploaded_file = st.sidebar.file_uploader("Upload New ECG Data (in .txt format)")

# If a new file is uploaded, load and visualize it
if uploaded_file is not None:
    ecg_data = np.loadtxt(uploaded_file)
    st.success("ECG data file uploaded successfully!")

# Plot and display the ECG data (1)
st.write("## ECG Data Visualization with 10 : 500 ratio")

# ECG data (ratio 10 : 500) 
ecg_data2 = ecg_data[10 : 500]

# Configure the plot (1) and display it-> ECG Data with 10 : 500 ratio
plt.figure(figsize=(18, 8))
plt.plot(ecg_data2, color='red', label='ECG Signal')
plt.xlabel('Time') # x-axis label
plt.ylabel('Amplitude') #y-axis label
plt.title('ECG Signal')
plt.grid(True)
st.pyplot(plt)
 
# Plot and display the Full ECG data (2) and the 10 : 500 data ratio in (1)
st.write("## ECG Data Visualization Full")

# Configure the plot (2) and display it -> Full ECG Data
Ndata = len(ecg_data)
ECG_Full = np.arange(Ndata)
plt.plot(ECG_Full, ecg_data)
st.pyplot(plt) 

# Add a button to download the ECG data
st.sidebar.markdown("## Download ECG Data")

# Save the ECG data to a temporary CSV file
temp_dir = tempfile.gettempdir()
temp_file_path = os.path.join(temp_dir, "ecg_data.csv")
np.savetxt(temp_file_path, ecg_data, delimiter=',', fmt='%f')

# Provide a download link to the temporary file
st.sidebar.download_button(
    label="Click here to download ECG Data (in .csv)",
    data=temp_file_path,
    key="ecg_data.csv",
    file_name="ecg_data.csv"
)
