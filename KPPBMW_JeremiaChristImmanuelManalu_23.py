'''
Author : Jemy
NN     : znt_sp_4

- Includes an upload option to visualize a new ECG data file for ".txt" extension.
- Includes a download button for downloading the ECG data (in text and image).
- Two ways to help visualize the given ECG data.
'''

# Import required libraries and modules
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import os
import tempfile
import base64 # For downloading ECG data image

# Define the Streamlit app title and header (KPP BMW)
st.title("KPP BMW")
st.header("Name  : Jeremia Christ Immanuel Manalu")
st.subheader("Batch : BME 23")

# Define a function to check if there is an appropiate path to the ECG data file. Else, it will raise an exception.
def load_ecg_data(file_path):
    try:
        ecg_data = np.loadtxt(file_path, dtype='float')
        return ecg_data
    except FileNotFoundError:
        st.error(f"File '{file_path}' Not found. Please upload your ECG data file.")
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

# Add a button to download the ECG data in raw text
st.sidebar.markdown("## Download ECG Data (Raw)")

# Save the ECG data to a temporary CSV file
temp_dir = tempfile.gettempdir()
temp_file_path = os.path.join(temp_dir, "ecg_data.csv")
np.savetxt(temp_file_path, ecg_data, delimiter=',', fmt='%f')

# Provide a download link to the temporary file (in text)
st.sidebar.download_button(
    label = "Click here to download ECG Data (in .csv)",
    data = temp_file_path,
    key = "ecg_data.csv",
    file_name = "ecg_data.csv"
)

# Add a button to download the ECG plot image file
st.sidebar.markdown("## Download ECG Plot Image (Full Visualization)")

# Save the ECG plot as a temporary image file (PNG)
temp_dir = tempfile.gettempdir()
temp_image_path = os.path.join(temp_dir, "ecg_plot.png")
plt.savefig(temp_image_path, format="png")

# Provide a download link for the image (encode as base64)
with open(temp_image_path, "rb") as img_file:
    img_bytes = img_file.read()
    img_b64 = base64.b64encode(img_bytes).decode()
# Use HTML anchor tag to provide the download link
st.sidebar.markdown(f'<a href="data:image/png;base64,{img_b64}" download="ecg_plot.png">Click here to download ECG Plot Image</a>', unsafe_allow_html=True)