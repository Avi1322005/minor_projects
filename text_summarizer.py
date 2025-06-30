import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import heapq
import tkinter as tk
from tkinter import scrolledtext, messagebox

# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Summarization Function
def summarize_text():
    text = input_text.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Warning", "Please enter text to summarize.")
        return

    stop_words = set(stopwords.words("english"))
    word_freq = {}

    for word in word_tokenize(text.lower()):
        if word.isalnum() and word not in stop_words:
            word_freq[word] = word_freq.get(word, 0) + 1

    sentence_scores = {}
    sentences = sent_tokenize(text)
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_freq:
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + word_freq[word]

    # Change number of sentences here if needed
    summary_sentences = heapq.nlargest(3, sentence_scores, key=sentence_scores.get)
    summary = ' '.join(summary_sentences)

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, summary)

# Clear Function
def clear_all():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)

# GUI Setup
window = tk.Tk()
window.title("Text Summarizer")
window.geometry("800x600")
window.config(bg="#f0f0f0")

tk.Label(window, text="Enter Text to Summarize:", font=("Arial", 14), bg="#f0f0f0").pack(pady=10)
input_text = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=90, height=12, font=("Arial", 11))
input_text.pack(padx=10, pady=5)

# Buttons
button_frame = tk.Frame(window, bg="#f0f0f0")
button_frame.pack()

summarize_btn = tk.Button(button_frame, text="Summarize", command=summarize_text, font=("Arial", 12), bg="#4CAF50", fg="white", padx=10)
summarize_btn.grid(row=0, column=0, padx=10, pady=10)

clear_btn = tk.Button(button_frame, text="Clear", command=clear_all, font=("Arial", 12), bg="#f44336", fg="white", padx=10)
clear_btn.grid(row=0, column=1, padx=10, pady=10)

tk.Label(window, text="Summarized Text:", font=("Arial", 14), bg="#f0f0f0").pack(pady=10)
output_text = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=90, height=10, font=("Arial", 11))
output_text.pack(padx=10, pady=5)

window.mainloop()