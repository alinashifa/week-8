import numpy as np
import pandas as pd
import streamlit as st


def main():
  st.title("Addition")
  number1 = st.number_input("Number 1")
  number2 = st.number_input("Number 2")
  sum = number1 + number2
  st.success('The output is {}'.format(sum))

if __name__=='__main__':
  main()
