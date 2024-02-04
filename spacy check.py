import spacy

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# Example usage
doc = nlp("This is a sample sentence.")
for token in doc:
    print(token.text, token.pos_, token.dep_)
