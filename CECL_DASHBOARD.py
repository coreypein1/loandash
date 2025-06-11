{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "d4a41d59-8944-480e-b0e4-80ca29d164ed",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "\n",
    "df = pd.read_csv('DLDC.csv')\n",
    "\n",
    "st.title(\"Loan Dashboard\")\n",
    "\n",
    "st.write(\"Data Preview:\")\n",
    "\n",
    "st.dataframe(df)\n",
    "\n",
    "st.subheader(\"Loan Balance Histogram\")\n",
    "st.bar_chart(df['loan_amount'])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "99d02773-b3c3-4677-92ad-96b3ddef4804",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
