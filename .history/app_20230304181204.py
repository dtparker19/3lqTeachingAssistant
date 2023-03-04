#import exception packages
 mport streamlit as st
from streamlit_chat import message
from PIL import Image
import os
import openai 
import json

#retrive api key from json file
with open("openai_api_key.json") as f:
    api_key = json.load(f)
#
openai.api_key = api_key['API_KEY']

def ask(question):
    response = openai.Completion.create(
               model="text-davinci-003",
               prompt=question,
               temperature=0.7,
               max_tokens=1024,
               stop=["\\n"],
               top_p=1,
               frequency_penalty=0,
               presence_penalty=0
               )
    answer = response.choices[0].text
    return answer

#set the page title
st.set_page_config(page_title="3LQ Learning Bot", layout="centered")
# set the image caption
#st.image(Image, caption='Teaching Assitant Bot', use_column_width=True)
# page header
st.title(f"3LQ Learning Bot")
# store interaction history
#
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []
#

# We will get the user's input by calling the get_text function
def get_text():
    input_text = st.text_input("You: ","Hello, how are you?", key="input")
    return input_text
#
user_input = get_text()
#
if user_input:
    # write try catch block 
    try:
        response = ask(user_input)
        # store the output 
        st.session_state.past.append(user_input)
        st.session_state.generated.append(response)
    except Exception as e:
        st.session_state.generated.append("I am sorry, I did not understand your input")
    
#
if st.session_state['generated']:   
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')

