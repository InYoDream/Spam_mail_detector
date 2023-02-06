import numpy as np
import pickle
import streamlit as st
classifiers=pickle.load(open("spam.pkl","rb"))
words_dict=pickle.load(open("vectorizer.pkl","rb"))

def main():
    st.title("Spam Email Detector")
    sample_mail=st.text_input("Enter mail..")
    if st.button("Predict"):
        sample=[]
        for it in words_dict:
            sample.append(sample_mail.split(" ").count(it[0]))
        sample=np.array(sample)
        
        if((classifiers.predict(sample.reshape(1,3000)))==1):
            st.error('SPAM')
        else:
            st.success('HAM')
main()