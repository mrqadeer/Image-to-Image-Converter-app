import requests
import os 
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
API_TOKEN=os.getenv("HUGGING_FACE_API_TOKEN")
def validate_name(name:str):
	API_URL = "https://api-inference.huggingface.co/models/dslim/bert-base-NER"
	headers = {"Authorization":API_TOKEN }

	def query(payload):
		response = requests.post(API_URL, headers=headers, json=payload)
		return response.json()
		
	output = query({
		"inputs": name,
	})
	try:
		result=output[0]['entity_group']=="PER"
	except Exception as e:
		st.warning(f"{name} is not valid name!")
	else:
		return result
