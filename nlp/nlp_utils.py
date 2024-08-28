# Example of what might be in nlp_utils.py
import spacy

nlp = spacy.load("en_core_web_sm")

def process_text(text):
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]
