import numpy as np
import pandas as pd
import streamlit as st


def main():
  st.title("Addition")
  html_temp = """
  <div style="background-color:pink;padding:10px">
  <h2>Addition of 2 numbers</h2>
  </div>
  """
  st.markdown(html_temp,unsafe_allow_html=True)
  number1 = st.number_input("Number 1")
  number2 = st.number_input("Number 2")
  result = number1 + number2
  st.success('The output is {}'.format(result))
  if st.button("Made By"):
      st.text("Syeda Ahmedi Fatima")

if __name__=='__main__':
  main()
