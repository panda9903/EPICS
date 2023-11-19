import requests
import streamlit as st

def main():

    st.header("Predictive Maintenance")

    input1 = st.text_input("Input 1")
    input2 = st.text_input("Input 2")
    input3 = st.text_input("Input 3")
    input4 = st.text_input("Input 4")
    input5 = st.text_input("Input 5")
    input6 = st.text_input("Input 6")

    if st.button("Calculate"):
        output = calculate_output(input1, input2, input3, input4, input5, input6)
        output = output[1]


        if(output == '0'):
            result = "No Failure"
        else:
            result = "Failure"


        st.text_area("Output", value=result, height=10, max_chars=None, key=None)

def calculate_output(input1, input2, input3, input4, input5, input6):

    url = "http://127.0.0.1:5000"
    payload = {
        "data": [input1, input2, input3, input4, input5, input6]
    }
    response = requests.post(url + "/predict", json=payload)
    output = response.text
    return output

if __name__ == "__main__":
    main()
