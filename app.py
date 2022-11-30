import numpy as np
import pandas as pd
import streamlit as st


def main():
  st.title("Addition")
  st.markdown(html_temp,unsafe_allow_html=True)
  number1 = st.number_input("Number 1")
  number2 = st.number_input("Number 2")
  result = number1 + number2
  st.success('The output is {}'.format(result))
  if st.button("Made By"):
      st.text("Syeda Ahmedi Fatima")

if __name__=='__main__':
  main()
