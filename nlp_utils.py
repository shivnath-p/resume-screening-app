import spacy
import re

nlp = spacy.load("en_core_web_sm")

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text.lower())
    return text

def extract_skills(text, skill_list):
    doc = nlp(text)
    tokens = [token.text.lower() for token in doc if not token.is_stop]
    return list(set(tokens) & set(skill_list))
