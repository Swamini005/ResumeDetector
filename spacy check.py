import spacy

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# Example usage
doc = nlp("hello world")
for token in doc:
    print(token.text, token.pos_, token.dep_)


if __name__ == "__main__":
    app.run(debug=True)