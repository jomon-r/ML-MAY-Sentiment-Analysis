import streamlit as st
import joblib
st.title('Sentiment Analysis Deployment')
test_model = joblib.load('Sentiment-Analysis')
ip = st.text_input('Enter your message')
op = test_model.predict([ip])
if op[0] == '1':
  result = 'POSITIVE COMMENT'
elif op[0] == '0':
  result = 'NEUTRAL COMMENT'
else:
  result = 'NEGATIVE COMMENT'
if st.button('Predict'):
  st.title(result)

  
  
