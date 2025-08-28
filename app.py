import tkinter as tk
from tkinter import messagebox
import time
import random
import csv
import os
from datetime import datetime

# --- Constants ---
APP_TITLE = "Typing Speed Test"
WINDOW_GEOMETRY = "800x500"
BG_COLOR = "#f0f0f0"
FONT_NAME = "Helvetica"
FONT_SIZE_NORMAL = 14
FONT_SIZE_LARGE = 18
FONT_SIZE_STATS = 12

CORRECT_COLOR = "#2E8B57"  # SeaGreen
INCORRECT_COLOR = "#DC143C" # Crimson
DEFAULT_TEXT_COLOR = "#333333"

# --- Sample Sentences for the Test ---
SAMPLE_TEXTS = [
    "The quick brown fox jumps over the lazy dog.",
    "Never underestimate the power of a good book.",
    "The journey of a thousand miles begins with a single step.",
    "To be or not to be, that is the question.",
    "The sun always shines brightest after the rain.",
    "Creativity is intelligence having fun.",
    "In the middle of difficulty lies opportunity.",
    "Actions speak louder than words.",
    "A picture is worth a thousand words.",
    "The early bird catches the worm.",
    "You can't judge a book by its cover.",
    "Honesty is the best policy.",
    "Laughter is the best medicine.",
    "An apple a day keeps the doctor away.",
    "The cat is sleeping on the rug.",
    "He walked to the store to buy some milk.",
    "She read the book in a single afternoon.",
    "The children are playing in the park.",
    "My favorite color is blue.",
    "The bus was late this morning.",
    "It is a beautiful day outside.",
    "He likes to listen to music while he works.",
    "She baked a cake for her friend's birthday.",
    "They went to the beach last weekend.",
    "The small puppy wagged its tail happily.",
    "Please close the door when you leave.",
    "The moon is very bright tonight.",
    "He planted a new tree in the garden.",
    "Water is essential for all living things.",
    "The train will arrive at the station soon.",
    "She always drinks coffee in the morning.",
    "My computer is running very slowly today.",
    "The birds are singing in the trees.",
    "He forgot to set his alarm clock.",
    "They watched a funny movie last night.",
    "I need to finish my homework before dinner.",
    "The flowers in the garden are very colorful.",
    "He is learning how to play the guitar.",
    "She sent an email to her boss.",
    "The library is a quiet place to study.",
    "The dog barked at the mailman.",
    "It started to rain just as we left.",
    "He fixed the broken chair with some glue.",
    "She wore a beautiful dress to the party.",
    "The stars are shining brightly in the sky.",
    "We should plan our vacation for next summer.",
    "The best way to predict the future is to create it.",
    "Success is not final, failure is not fatal.",
    "Believe you can and you are halfway there.",
    "The only way to do great work is to love what you do.",
    "The wind is blowing the leaves off the trees.",
    "He found his lost keys under the sofa.",
    "She enjoys going for a long walk in the evening.",
    "The baby is sleeping peacefully in his crib.",
    "I have a meeting at ten o'clock tomorrow.",
    "The mountain peak was covered in snow.",
    "He wrote a thank you note to his aunt.",
    "The soup is too hot to eat right now.",
    "She helped the old man cross the street.",
    "The world is full of amazing places to visit.",
    "He solved the difficult puzzle in just a few minutes.",
    "The sun sets in the west.",
    "The Earth revolves around the sun.",
    "A gentle breeze rustled the leaves of the trees.",
    "The old house stood on top of a hill.",
    "He told a joke that made everyone laugh.",
    "She is an excellent student and works very hard.",
    "The museum was filled with interesting artifacts.",
    "They decided to go for a bike ride.",
    "He built a small boat with his own hands.",
    "The phone rang, but nobody answered it.",
    "I prefer tea over coffee.",
    "The winter season can be very cold.",
    "She found a beautiful seashell on the shore.",
    "The clock on the wall struck midnight.",
    "He has a great sense of humor.",
    "The bridge crosses over the wide river.",
    "She painted a beautiful landscape.",
    "The city looks beautiful at night from here.",
    "He loves to explore new and exciting places.",
    "The new restaurant downtown is very popular.",
    "She is saving money to buy a new car.",
    "The forest is home to many kinds of animals.",
    "He carefully followed the recipe instructions.",
    "The concert was absolutely amazing.",
    "I need to buy some groceries on my way home.",
    "The quiet hum of the refrigerator was the only sound.",
    "She has a wonderful collection of old stamps.",
    "The airplane flew high above the clouds.",
    "He is always willing to help his neighbors.",
    "The park is a great place for a picnic.",
    "She is very good at playing chess.",
    "The smell of freshly baked bread filled the air.",
    "He took a deep breath and dived into the water.",
    "The old map led them to a hidden treasure.",
    "The little girl was chasing butterflies.",
    "Hard work and dedication lead to success.",
    "The storm passed quickly, leaving a rainbow.",
    "He likes to read mystery novels in his free time.",
    "She has a very positive outlook on life.",
    "The team celebrated their victory after the game.",
    "The test was easier than I had expected.",
    "He is known for his kindness and generosity.",
    "The secret to getting ahead is getting started.",
    "Every moment is a fresh beginning.",
    "Change your thoughts and you change your world.",
    "Strive for progress, not perfection.",
    "What we think, we become.",
    "The old clock in the hall ticked loudly.",
    "She tied a yellow ribbon around the oak tree.",
    "He hit the baseball out of the park.",
    "The garden was full of red and yellow roses.",
    "I have to wake up early tomorrow for my flight.",
    "He solved the math problem on the blackboard.",
    "The quiet lake reflected the morning sun.",
    "She has a talent for making people feel welcome.",
    "The story was passed down through generations.",
    "He packed his suitcase for the long trip.",
    "The little boat sailed smoothly across the water.",
    "She listened to the sound of the ocean waves.",
    "The chef prepared a delicious meal for the guests.",
    "He enjoys the simple pleasures of life.",
    "The road was long and wound through the hills.",
    "She wrote her name on the first page of the book.",
    "The new software is much faster than the old one.",
    "He was surprised to see his friend at the door.",
    "The old man told stories of his youth.",
    "She learned to speak three different languages.",
    "The night was clear and full of stars.",
    "He made a promise that he intended to keep.",
    "The small village was quiet and peaceful.",
    "She watched the snowflakes fall outside her window.",
    "The key to the mystery was hidden in the letter.",
    "He is a very reliable and trustworthy person.",
    "The first step is always the hardest.",
    "She made a wish and blew out the candles.",
    "The river flowed gently towards the sea.",
    "He found a four-leaf clover in the field.",
    "The painting was a masterpiece of modern art.",
    "She always tries to see the good in people.",
    "The new highway bypasses the town center.",
    "He built a sturdy fence around his property.",
    "The puppy chewed on his new toy.",
    "She decided to take a different route to work.",
    "The old tree provided shade from the hot sun.",
    "He is training for a marathon next month.",
    "The aroma of coffee filled the entire house.",
    "She carefully arranged the flowers in a vase.",
    "The detective searched for clues at the crime scene.",
    "He enjoys the challenge of a difficult task.",
    "The sound of distant thunder was heard.",
    "She wore a warm scarf on the cold day.",
    "The company announced its new product today.",
    "He gave a brilliant speech at the conference.",
    "The cat watched the bird from the window.",
    "She took a photograph of the beautiful sunset.",
    "The path through the woods was narrow and winding.",
    "He always keeps his desk neat and organized.",
    "The child's laughter was infectious.",
    "She found comfort in the words of a good book.",
    "The farmer worked in his fields from dawn to dusk.",
    "He wrote a song about his hometown.",
    "The boat's sail caught the wind perfectly.",
    "She has a remarkable memory for names and faces.",
    "The ice on the pond was thick enough for skating.",
    "He carefully planned every detail of the event.",
    "The echo of his voice returned from the canyon.",
    "She felt a great sense of accomplishment.",
    "The old photograph brought back many memories.",
    "He always double checks his work for errors.",
    "The mountain air was fresh and clean.",
    "She packed a healthy lunch for her son.",
    "The new policy will be effective next week.",
    "He was a pioneer in the field of science.",
    "The candle flickered in the gentle breeze.",
    "She is passionate about environmental protection.",
    "The two friends had a long conversation.",
    "He is an advocate for social justice.",
    "The soft blanket was warm and cozy.",
    "She has a deep appreciation for classical music.",
    "The historic building was restored to its former glory.",
    "He learned a valuable lesson from his mistake.",
    "The garden was a peaceful oasis in the city.",
    "She has an amazing ability to solve problems.",
    "The desert landscape was vast and empty.",
    "He felt a surge of excitement and anticipation.",
    "The old sailor had many tales of the sea.",
    "She showed great courage in a difficult situation.",
    "The small town had a strong sense of community.",
    "He worked with precision and great attention to detail.",
    "The view from the top of the hill was breathtaking.",
    "She has a natural talent for drawing and painting.",
    "The calm water of the lake was like a mirror.",
    "He took a moment to appreciate the beauty around him.",
    "The author's new book is a bestseller.",
    "She has a very cheerful and optimistic personality.",
]

# --- CSV File for Progress Tracking ---
PROGRESS_FILE = "typing_progress.csv"

class TypingSpeedApp:
    def __init__(self, root):
        self.root = root
        self.root.title(APP_TITLE)
        self.root.geometry(WINDOW_GEOMETRY)
        self.root.config(bg=BG_COLOR, padx=20, pady=20)

        # State variables
        self.sample_text = ""
        self.test_running = False
        self.start_time = 0
        self.elapsed_time = 0

        # Create and layout widgets
        self.setup_ui()

        # Load the first test
        self.reset_test()
        
        # Check for CSV file and create if it doesn't exist
        self.init_progress_file()

    def setup_ui(self):
        # --- Title ---
        title_label = tk.Label(
            self.root,
            text="Typing Speed Test",
            font=(FONT_NAME, 24, "bold"),
            bg=BG_COLOR,
            fg=DEFAULT_TEXT_COLOR
        )
        title_label.pack(pady=(0, 20))

        # --- Sample Text Display ---
        self.sample_text_widget = tk.Text(
            self.root,
            font=(FONT_NAME, FONT_SIZE_LARGE),
            wrap=tk.WORD,
            height=3,
            padx=10,
            pady=10,
            bd=2,
            relief="groove"
        )
        self.sample_text_widget.pack(fill=tk.X)
        # Prevent user from editing the sample text
        self.sample_text_widget.config(state=tk.DISABLED)

        # --- User Input Text Box ---
        self.input_text = tk.Text(
            self.root,
            font=(FONT_NAME, FONT_SIZE_LARGE),
            wrap=tk.WORD,
            height=3,
            padx=10,
            pady=10,
            bd=2,
            relief="groove"
        )
        self.input_text.pack(fill=tk.X, pady=(10, 0))
        self.input_text.focus() # Start with the cursor here
        # Bind key release event to check input
        self.input_text.bind("<KeyRelease>", self.check_input)

        # --- Stats Frame ---
        stats_frame = tk.Frame(self.root, bg=BG_COLOR)
        stats_frame.pack(fill=tk.X, pady=20)
        
        self.time_label = tk.Label(stats_frame, text="Time: 0s", font=(FONT_NAME, FONT_SIZE_STATS), bg=BG_COLOR)
        self.time_label.pack(side=tk.LEFT, expand=True)

        self.wpm_label = tk.Label(stats_frame, text="WPM: 0", font=(FONT_NAME, FONT_SIZE_STATS), bg=BG_COLOR)
        self.wpm_label.pack(side=tk.LEFT, expand=True)

        self.accuracy_label = tk.Label(stats_frame, text="Accuracy: 100%", font=(FONT_NAME, FONT_SIZE_STATS), bg=BG_COLOR)
        self.accuracy_label.pack(side=tk.LEFT, expand=True)

        # --- Reset Button ---
        self.reset_button = tk.Button(
            self.root,
            text="New Test",
            font=(FONT_NAME, FONT_SIZE_NORMAL),
            command=self.reset_test
        )
        self.reset_button.pack(pady=10)

    def init_progress_file(self):
        """Creates the CSV file with a header if it doesn't exist."""
        if not os.path.exists(PROGRESS_FILE):
            with open(PROGRESS_FILE, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Timestamp", "WPM", "Accuracy (%)"])

    def save_progress(self, wpm, accuracy):
        """Appends the result of a completed test to the CSV file."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            with open(PROGRESS_FILE, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([timestamp, wpm, accuracy])
        except IOError as e:
            messagebox.showerror("Save Error", f"Could not save progress: {e}")

    def start_test(self):
        """Starts the timer and the test."""
        if not self.test_running:
            self.test_running = True
            self.start_time = time.time()
            self.update_timer()

    def update_timer(self):
        """Updates the elapsed time label every second."""
        if self.test_running:
            self.elapsed_time = time.time() - self.start_time
            self.time_label.config(text=f"Time: {self.elapsed_time:.1f}s")
            # Schedule the next update
            self.root.after(100, self.update_timer)

    def check_input(self, event):
        """Called on every key release in the input box."""
        # Start the test on the first key press
        if not self.test_running:
            self.start_test()

        # Get current typed text
        typed_text = self.input_text.get("1.0", "end-1c")
        typed_len = len(typed_text)

        # Re-enable the widget to modify tags
        self.sample_text_widget.config(state=tk.NORMAL)
        # Clear previous formatting
        self.sample_text_widget.tag_remove("correct", "1.0", tk.END)
        self.sample_text_widget.tag_remove("incorrect", "1.0", tk.END)

        correct_chars = 0
        # Compare typed text with sample text and apply highlighting
        for i, char in enumerate(typed_text):
            if i < len(self.sample_text):
                if char == self.sample_text[i]:
                    correct_chars += 1
                    self.sample_text_widget.tag_add("correct", f"1.{i}", f"1.{i+1}")
                else:
                    self.sample_text_widget.tag_add("incorrect", f"1.{i}", f"1.{i+1}")
        
        # Disable the widget again
        self.sample_text_widget.config(state=tk.DISABLED)

        # --- Calculate and Update Stats ---
        # Accuracy
        accuracy = (correct_chars / typed_len) * 100 if typed_len > 0 else 100
        self.accuracy_label.config(text=f"Accuracy: {accuracy:.1f}%")

        # WPM (Words Per Minute)
        if self.elapsed_time > 0:
            # A "word" is standardized as 5 characters for WPM calculation
            wpm = (correct_chars / 5) / (self.elapsed_time / 60)
            self.wpm_label.config(text=f"WPM: {wpm:.2f}")

        # --- Check for test completion ---
        if typed_len == len(self.sample_text):
            self.test_running = False
            self.input_text.config(state=tk.DISABLED)
            
            final_wpm = float(f"{wpm:.2f}")
            final_accuracy = float(f"{accuracy:.1f}")
            
            # Save the progress
            self.save_progress(final_wpm, final_accuracy)
            
            messagebox.showinfo(
                "Test Complete!",
                f"Your final score:\n\nWPM: {final_wpm}\nAccuracy: {final_accuracy}%\n\nProgress has been saved."
            )

    def reset_test(self):
        """Resets the application for a new test."""
        self.test_running = False
        self.start_time = 0
        self.elapsed_time = 0

        # Choose a new random sentence
        self.sample_text = random.choice(SAMPLE_TEXTS)

        # Reset UI elements
        self.time_label.config(text="Time: 0s")
        self.wpm_label.config(text="WPM: 0")
        self.accuracy_label.config(text="Accuracy: 100%")

        self.sample_text_widget.config(state=tk.NORMAL)
        self.sample_text_widget.delete("1.0", tk.END)
        self.sample_text_widget.insert("1.0", self.sample_text)
        self.sample_text_widget.config(state=tk.DISABLED)
        # Configure tags for highlighting
        self.sample_text_widget.tag_config("correct", foreground=CORRECT_COLOR)
        self.sample_text_widget.tag_config("incorrect", foreground=INCORRECT_COLOR, underline=True)

        self.input_text.config(state=tk.NORMAL)
        self.input_text.delete("1.0", tk.END)
        self.input_text.focus()

# --- Main Execution ---
if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedApp(root)
    root.mainloop()