import tkinter as tk
from tkinter import messagebox
import random

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Quiz Generator")
        self.root.geometry("500x400")
        
        self.questions = [
            ("What is the capital of France?", "Paris"),
            ("What is 2 + 2?", "4"),
            ("What is the largest mammal?", "Blue whale"),
            ("What planet is known as the Red Planet?", "Mars"),
            ("Who wrote 'To Kill a Mockingbird'?", "Harper Lee")
        ]
        
        self.current_question = None
        
        self.title_label = tk.Label(root, text="Quiz Time!", font=("Helvetica", 20, "bold"))
        self.title_label.pack(pady=20)
        
        self.question_label = tk.Label(root, text="", font=("Helvetica", 16))
        self.question_label.pack(pady=20)
        
        self.answer_entry = tk.Entry(root, font=("Helvetica", 16))
        self.answer_entry.pack(pady=10)
        
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=20)
        
        self.next_button = tk.Button(self.button_frame, text="Next Question", command=self.next_question, font=("Helvetica", 12))
        self.next_button.pack(side=tk.LEFT, padx=10)
        
        self.submit_button = tk.Button(self.button_frame, text="Submit Answer", command=self.submit_answer, font=("Helvetica", 12))
        self.submit_button.pack(side=tk.LEFT, padx=10)
        
        self.result_label = tk.Label(root, text="", font=("Helvetica", 16))
        self.result_label.pack(pady=20)
        
        self.next_question()
    
    def next_question(self):
        self.result_label.config(text="")
        self.answer_entry.delete(0, tk.END)
        self.current_question = random.choice(self.questions)
        self.question_label.config(text=self.current_question[0])
    
    def submit_answer(self):
        answer = self.answer_entry.get()
        if answer.lower() == self.current_question[1].lower():
            self.result_label.config(text="Correct!", fg="green")
        else:
            self.result_label.config(text=f"Incorrect! The answer is {self.current_question[1]}.", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
