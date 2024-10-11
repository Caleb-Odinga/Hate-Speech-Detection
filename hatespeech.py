import tkinter as tk
from tkinter import messagebox
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Example dataset
dataset = [
    ("Wewe ni mjinga kabisa", "Hate"),
    ("Habari yako rafiki?", "Non-Hate"),
    ("Lazima tuwaondoe wale watu", "Hate"),
    ("Elimu ni muhimu kwa kila mtu", "Non-Hate")
]

# Preprocess the dataset
texts, labels = zip(*dataset)
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# Train the classifier
classifier = MultinomialNB()
classifier.fit(X, labels)

# Function to classify input
def classify_input():
    input_text = text_entry.get()
    input_vector = vectorizer.transform([input_text])
    prediction = classifier.predict(input_vector)[0]
    messagebox.showinfo("Classification Result", f"The text is classified as: {prediction}")

# Create the Tkinter GUI
root = tk.Tk()
root.title("Kiswahili Hate Speech Classifier")

# Input Field
text_label = tk.Label(root, text="Enter Kiswahili Text:")
text_label.pack()
text_entry = tk.Entry(root, width=50)
text_entry.pack()

# Classify Button
classify_button = tk.Button(root, text="Classify", command=classify_input)
classify_button.pack()

root.mainloop()
