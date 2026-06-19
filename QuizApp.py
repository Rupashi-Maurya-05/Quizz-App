import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# ==========================================================
#  QUIZ DATA
# ==========================================================
QUIZ_DATA = {
    "General Knowledge": [
        ("What is the capital of France?", ["Paris", "Berlin", "Madrid", "London"], "Paris"),
        ("Which is the largest ocean in the world?", ["Atlantic", "Indian", "Arctic", "Pacific"], "Pacific"),
        ("Who painted the Mona Lisa?", ["Van Gogh", "Da Vinci", "Picasso", "Michelangelo"], "Da Vinci"),
        ("What is the currency of Japan?", ["Dollar", "Euro", "Yen", "Won"], "Yen"),
        ("Which country invented pizza?", ["France", "Italy", "USA", "Greece"], "Italy"),
        ("What is the tallest mountain?", ["K2", "Kangchenjunga", "Everest", "Lhotse"], "Everest"),
        ("How many continents are there?", ["5", "6", "7", "8"], "7"),
        ("Which language has the most native speakers?", ["English", "Hindi", "Mandarin", "Spanish"], "Mandarin"),
        ("What festival is known as the Festival of Lights?", ["Christmas", "Diwali", "Eid", "Holi"], "Diwali"),
        ("Who wrote 'Hamlet'?", ["Shakespeare", "Tolstoy", "Homer", "Dante"], "Shakespeare"),
    ],

    "Science": [
        ("What is H2O?", ["Hydrogen", "Water", "Oxygen", "Salt"], "Water"),
        ("What is the speed of light?", ["300,000 km/s", "150,000 km/s", "1,000 km/s", "50,000 km/s"], "300,000 km/s"),
        ("Earth is ___?", ["Square", "Flat", "Round", "Triangular"], "Round"),
        ("Sun is a ___?", ["Planet", "Star", "Comet", "Asteroid"], "Star"),
        ("Which vitamin is produced by sunlight?", ["A", "B12", "C", "D"], "D"),
        ("What gas do plants absorb?", ["Oxygen", "Carbon Dioxide", "Nitrogen", "Helium"], "Carbon Dioxide"),
        ("What part of the cell contains DNA?", ["Nucleus", "Cytoplasm", "Membrane", "Mitochondria"], "Nucleus"),
        ("Which planet has the strongest gravity?", ["Jupiter", "Earth", "Mars", "Venus"], "Jupiter"),
        ("What force keeps us on the ground?", ["Magnetism", "Friction", "Gravity", "Pressure"], "Gravity"),
        ("What is the powerhouse of the cell?", ["Nucleus", "Ribosome", "Chloroplast", "Mitochondria"], "Mitochondria"),
    ],

    "Technology": [
        ("What does CPU stand for?", ["Central Process Unit", "Central Processing Unit", "Computer Personal Unit", "Core Power Unit"], "Central Processing Unit"),
        ("Which company makes the iPhone?", ["Samsung", "Apple", "Google", "Nokia"], "Apple"),
        ("What does 'AI' stand for?", ["Automatic Input", "Artificial Intelligence", "Auto Interface", "Active Internet"], "Artificial Intelligence"),
        ("Which programming language is known for web styling?", ["Python", "CSS", "C++", "Java"], "CSS"),
        ("What is Wi-Fi used for?", ["Audio", "Cooking", "Wireless Internet", "Charging"], "Wireless Internet"),
        ("Who founded Microsoft?", ["Jobs", "Musk", "Gates", "Zuckerberg"], "Gates"),
        ("What is the brain of the computer?", ["Monitor", "Keyboard", "CPU", "Mouse"], "CPU"),
        ("HTML is used for?", ["Data Storage", "Web Pages", "Graphics", "Games"], "Web Pages"),
        ("What company owns Android?", ["Apple", "Google", "Microsoft", "Sony"], "Google"),
        ("Which device stores data permanently?", ["RAM", "SSD", "CPU", "Cache"], "SSD"),
    ],

    "Mathematics": [
        ("What is 15 + 17?", ["32", "30", "28", "34"], "32"),
        ("Square root of 81?", ["7", "8", "9", "10"], "9"),
        ("What is 12 × 12?", ["124", "144", "132", "112"], "144"),
        ("What is 100 ÷ 4?", ["20", "25", "50", "30"], "25"),
        ("Which is a prime number?", ["4", "9", "11", "21"], "11"),
        ("What is π approximately?", ["2.14", "3.14", "4.14", "5.14"], "3.14"),
        ("Solve: 45 – 18?", ["22", "27", "32", "29"], "27"),
        ("How many degrees in a right angle?", ["180", "90", "45", "360"], "90"),
        ("What is 7 × 8?", ["42", "48", "56", "64"], "56"),
        ("What is 1/2 + 1/4?", ["3/4", "2/4", "1/8", "1/3"], "3/4"),
    ],

    "Sports": [
        ("How many players in a football team?", ["9", "10", "11", "12"], "11"),
        ("Who is known as 'King of Football'?", ["Messi", "Pele", "Ronaldo", "Maradona"], "Pele"),
        ("Olympics are held every ___ years.", ["2", "3", "4", "6"], "4"),
        ("Cricket is played with how many innings?", ["1", "2", "3", "4"], "2"),
        ("Which country invented basketball?", ["USA", "Canada", "Spain", "Germany"], "USA"),
        ("How long is a marathon?", ["21 km", "42 km", "15 km", "50 km"], "42 km"),
        ("What sport uses a shuttlecock?", ["Tennis", "Badminton", "Squash", "Table Tennis"], "Badminton"),
        ("Which country won FIFA 2022?", ["Brazil", "Germany", "Argentina", "France"], "Argentina"),
        ("Which sport has a wicket?", ["Tennis", "Cricket", "Hockey", "Baseball"], "Cricket"),
        ("How many rings in the Olympic logo?", ["4", "5", "6", "7"], "5"),
    ],

    "History": [
        ("Who was the first President of the USA?", ["Lincoln", "Jefferson", "Washington", "Adams"], "Washington"),
        ("Who built the Pyramids?", ["Romans", "Egyptians", "Greeks", "Persians"], "Egyptians"),
        ("World War II ended in?", ["1942", "1945", "1948", "1950"], "1945"),
        ("Who discovered America?", ["Columbus", "Newton", "Galileo", "Da Vinci"], "Columbus"),
        ("Where was the Taj Mahal built?", ["Delhi", "Jaipur", "Agra", "Mumbai"], "Agra"),
        ("Who was known as Iron Man of India?", ["Gandhi", "Nehru", "Patel", "Bose"], "Patel"),
        ("The Great Wall is in which country?", ["India", "China", "Japan", "Russia"], "China"),
        ("Who invented the telephone?", ["Einstein", "Bell", "Edison", "Tesla"], "Bell"),
        ("In which year did India get Independence?", ["1947", "1950", "1945", "1937"], "1947"),
        ("Who was known as Napoleon of India?", ["Samudragupta", "Ashoka", "Akbar", "Shivaji"], "Samudragupta"),
    ],
}



# ==========================================================
#  MAIN APP
# ==========================================================
class QuizApp(tk.Tk):
    """Main application window and controller for all pages."""

    def __init__(self):
        super().__init__()

        # Window properties
        self.title("⚡ Ultimate Python Quiz Game")
        self.state("zoomed")
        self.configure(bg="#1e1e1e")

        # Global shared variables
        self.user_name = tk.StringVar()       # Player name
        self.selected_category = tk.StringVar()
        self.num_questions = tk.IntVar()
        self.questions_list = []              # List of selected questions
        self.current_index = 0
        self.score = 0
        self.user_answers = []               # Stores: (question, options, correct, chosen)

        # Create pages
        self.home_page = HomePage(self)
        self.quiz_page = QuizPage(self)
        self.results_page = ResultsPage(self)

        # Start on home screen
        self.home_page.pack(fill="both", expand=True)

    # ----------------------------------------------------------
    def start_quiz(self):
        """Validate inputs, generate questions, and start the quiz."""

        # Validate name
        if not self.user_name.get().strip():
            self.show_custom_dialog("Error", "Please enter your name.")
            return

        category = self.selected_category.get()
        total = self.num_questions.get()

        # Validate category
        if not category:
            self.show_custom_dialog("Error", "Please select a quiz category.")
            return

        # Validate number of questions
        if total <= 0:
            self.show_custom_dialog("Error", "Please enter a valid number of questions.")
            return

        if total > 10:
            self.show_custom_dialog("Oops!", "Max 10 questions allowed.", bg_color="#2b2b2b")
            return

        # Randomly pick questions from selected category
        available = QUIZ_DATA[category]
        self.questions_list = random.sample(available, min(total, len(available)))

        # Reset quiz state
        self.current_index = 0
        self.score = 0
        self.user_answers = []

        # Switch to quiz page
        self.home_page.pack_forget()
        self.quiz_page.load_question()
        self.quiz_page.pack(fill="both", expand=True)

    # ----------------------------------------------------------
    def show_results(self):
        """Switch to results page and display final summary."""
        self.quiz_page.pack_forget()

        self.results_page.display_results(
            self.user_name.get(),
            self.score,
            len(self.questions_list),
            self.user_answers
        )

        self.results_page.pack(fill="both", expand=True)

    # ----------------------------------------------------------
    def show_custom_dialog(self, title, message, bg_color="#1e1e1e", fg_color="white"):
        """Show a custom popup dialog with a message."""
        dialog = tk.Toplevel(self)
        dialog.title(title)
        dialog.configure(bg=bg_color)
        dialog.geometry("450x200")
        dialog.resizable(False, False)

        # Centering dialog
        dialog.update_idletasks()
        x = (dialog.winfo_screenwidth() // 2) - (dialog.winfo_width() // 2)
        y = (dialog.winfo_screenheight() // 2) - (dialog.winfo_height() // 2)
        dialog.geometry(f"+{x}+{y}")

        # Message text
        tk.Label(
            dialog, text=message,
            font=("Arial", 16, "bold"),
            bg=bg_color, fg=fg_color,
            wraplength=400, justify="center"
        ).pack(expand=True, pady=20)

        # OK Button
        tk.Button(
            dialog, text="OK",
            font=("Arial", 14, "bold"),
            bg="#00e676", fg="#000",
            width=12, command=dialog.destroy
        ).pack(pady=10)

        dialog.transient(self)
        dialog.grab_set()
        self.wait_window(dialog)



# ==========================================================
#  HOME PAGE UI
# ==========================================================
class HomePage(tk.Frame):
    """Landing page where user enters name, picks category, and selects number of questions."""

    def __init__(self, master):
        super().__init__(master, bg="#1e1e1e")

        # Title
        tk.Label(
            self,
            text="⚡ Welcome to the Ultimate Quiz Game!",
            font=("Arial", 36, "bold"),
            bg="#1e1e1e",
            fg="#00e676"
        ).pack(pady=40)

        # Name Input
        tk.Label(self, text="Enter Your Name:",
                 font=("Arial", 24), bg="#1e1e1e", fg="white").pack(pady=10)

        tk.Entry(
            self,
            textvariable=master.user_name,
            font=("Arial", 20),
            width=25
        ).pack(pady=10)

        # Category Selection
        tk.Label(self, text="Choose Category:",
                 font=("Arial", 24), bg="#1e1e1e", fg="white").pack(pady=20)

        self.category_box = ttk.Combobox(
            self,
            values=list(QUIZ_DATA.keys()),
            textvariable=master.selected_category,
            font=("Arial", 18),
            state="readonly",
            width=25
        )
        self.category_box.pack(pady=10)

        # Number of Questions Input
        tk.Label(
            self, text="Number of Questions (Max 10):",
            font=("Arial", 24),
            bg="#1e1e1e", fg="white"
        ).pack(pady=20)

        tk.Entry(
            self,
            textvariable=master.num_questions,
            font=("Arial", 18),
            width=10
        ).pack(pady=10)

        # Start Button
        tk.Button(
            self,
            text="🚀 Start Quiz",
            font=("Arial", 26, "bold"),
            bg="#00e676", fg="#000",
            padx=30, pady=15,
            command=master.start_quiz
        ).pack(pady=40)



# ==========================================================
#  QUIZ PAGE 
# ==========================================================
class QuizPage(tk.Frame):
    """Page that displays quiz questions, handles timer, and processes answers."""

    def __init__(self, master):
        super().__init__(master, bg="#121212")
        self.master = master

        # TIMER UI
        self.timer_seconds = 5  # countdown seconds

        self.timer_frame = tk.Frame(self, bg="#00e676", bd=3, relief="solid")
        self.timer_frame.place(relx=0.95, rely=0.05, anchor="ne")

        self.timer_label = tk.Label(
            self.timer_frame, text="5",
            font=("Arial", 36, "bold"),
            bg="#00e676", fg="black",
            padx=25, pady=10
        )
        self.timer_label.pack()

        self.current_timer = None  # Holds after() reference

        # ----------------------
        # QUESTION TEXT
        # ----------------------
        self.question_label = tk.Label(
            self, text="", font=("Arial", 30, "bold"),
            bg="#121212", fg="#ffffff", wraplength=1100
        )
        self.question_label.pack(pady=80)

        # ----------------------
        # ANSWER BUTTONS
        # ----------------------
        self.buttons = []
        for i in range(4):
            btn = tk.Button(
                self, text="", font=("Arial", 24),
                bg="#1f1f1f", fg="#ffffff",
                width=30, pady=12,
                command=lambda idx=i: self.select_answer(idx)
            )
            btn.pack(pady=20)
            self.buttons.append(btn)

    # ----------------------------------------------------------
    def update_timer_style(self):
        """Change timer color based on remaining seconds."""
        if self.timer_seconds >= 3:
            bg = "#00e676"  # green
            fg = "black"
        elif self.timer_seconds == 2:
            bg = "#ffea00"  # yellow
            fg = "black"
        else:
            bg = "#ff5252"  # red
            fg = "white"

        self.timer_frame.config(bg=bg)
        self.timer_label.config(bg=bg, fg=fg)

    # ----------------------------------------------------------
    def load_question(self):
        """Load the next question into the UI."""
        if self.current_timer:
            self.after_cancel(self.current_timer)

        # Reset timer
        self.timer_seconds = 5
        self.timer_label.config(text=str(self.timer_seconds))
        self.update_timer_style()

        # Load question data
        q, options, answer = self.master.questions_list[self.master.current_index]
        self.correct_answer = answer

        self.question_label.config(text=f"Q{self.master.current_index+1}: {q}")

        for i, btn in enumerate(self.buttons):
            btn.config(text=options[i])

        self.countdown()

    # ----------------------------------------------------------
    def countdown(self):
        """Timer countdown logic."""
        self.timer_label.config(text=str(self.timer_seconds))
        self.update_timer_style()

        # Time up
        if self.timer_seconds <= 0:
            self.skip_question()
            return

        # Continue counting
        self.timer_seconds -= 1
        self.current_timer = self.after(1000, self.countdown)

    # ----------------------------------------------------------
    def skip_question(self):
        """Auto-skip if timer expires."""
        q, options, correct = self.master.questions_list[self.master.current_index]
        self.master.user_answers.append((q, options, correct, "⏱ Skipped"))

        self.master.current_index += 1

        if self.master.current_index >= len(self.master.questions_list):
            self.finish_quiz()
        else:
            self.load_question()

    # ----------------------------------------------------------
    def select_answer(self, index):
        """Handle answer selection by user."""
        if self.current_timer:
            self.after_cancel(self.current_timer)

        chosen = self.buttons[index].cget("text")

        q, options, correct = self.master.questions_list[self.master.current_index]
        self.master.user_answers.append((q, options, correct, chosen))

        if chosen == correct:
            self.master.score += 1

        self.master.current_index += 1

        # Load next question or end quiz
        if self.master.current_index >= len(self.master.questions_list):
            self.finish_quiz()
        else:
            self.load_question()

    # ----------------------------------------------------------
    def finish_quiz(self):
        """Called when all questions have been answered."""
        if self.current_timer:
            self.after_cancel(self.current_timer)
        self.master.show_results()



# ==========================================================
#  RESULTS PAGE
# ==========================================================
class ResultsPage(tk.Frame):
    """Page showing final score, accuracy chart, and summary of all questions."""

    def __init__(self, master):
        super().__init__(master, bg="#101010")
        self.master = master

        self.title_label = tk.Label(
            self,
            text="Your Quiz Summary",
            font=("Arial", 40, "bold"),
            bg="#101010",
            fg="#00e676"
        )
        self.title_label.pack(pady=20)

        # Container for chart + summary
        self.container = tk.Frame(self, bg="#101010")
        self.container.pack(fill="both", expand=True, pady=10)

    # ----------------------------------------------------------
    def display_results(self, name, score, total, user_answers):
        """Render results UI after quiz is complete."""

        # Clear previous widgets
        for widget in self.container.winfo_children():
            widget.destroy()

        # Player score message
        if hasattr(self, "score_label"):
            self.score_label.destroy()

        self.score_label = tk.Label(
            self,
            text=f"{name}, you scored {score} out of {total}!",
            font=("Arial", 32, "bold"),
            bg="#101010",
            fg="#00e676"
        )
        self.score_label.pack(after=self.title_label, pady=(0, 20), anchor="center")

        # Determine available width
        self.container.update_idletasks()
        container_width = self.container.winfo_width() or 800

        # ---------------------------
        # LEFT: PIE CHART (35%)
        # ---------------------------
        chart_frame = tk.Frame(self.container, bg="#101010")
        chart_frame.pack(side="left", fill="both", expand=True)
        chart_frame.config(width=int(container_width * 0.35))

        # Create figure
        fig = plt.Figure(figsize=(4.5, 4.5), dpi=100)
        ax = fig.add_subplot(111)
        fig.patch.set_facecolor("#101010")
        ax.set_facecolor("#101010")

        sizes = [score, total - score]
        labels = ["Correct", "Wrong"]
        colors = ["#00c853", "#d32f2f"]

        wedges, texts, autotexts = ax.pie(
            sizes,
            labels=labels,
            autopct="%1.1f%%",
            colors=colors,
            textprops={"color": "white", "fontsize": 14}
        )

        for autotext in autotexts:
            autotext.set_color("white")
            autotext.set_fontsize(14)
            autotext.set_fontweight("bold")

        ax.set_title("Answer Accuracy", color="white", fontsize=22, pad=20)

        chart_canvas = FigureCanvasTkAgg(fig, master=chart_frame)
        chart_canvas.draw()
        chart_canvas.get_tk_widget().pack(expand=True)

        # ---------------------------
        # RIGHT: ANSWER SUMMARY (65%)
        # ---------------------------
        summary = tk.Frame(self.container, bg="#101010")
        summary.pack(side="right", fill="both", expand=True)
        summary.config(width=int(container_width * 0.65))

        # Scrollable area
        canvas = tk.Canvas(summary, bg="#101010", highlightthickness=0)
        scrollbar = tk.Scrollbar(summary, orient="vertical", command=canvas.yview)
        scroll_frame = tk.Frame(canvas, bg="#101010")

        scroll_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Create question summary cards
        for q, options, correct, chosen in user_answers:
            card = tk.Frame(scroll_frame, bg="#181818",
                            bd=1, relief="solid", padx=10, pady=8)
            card.pack(anchor="w", pady=10, fill="x")

            tk.Label(
                card, text=f"Q: {q}",
                font=("Arial", 15, "bold"),
                bg="#181818", fg="white", wraplength=650
            ).pack(anchor="w", pady=(0, 5))

            # Correct or wrong answer display
            if chosen == correct:
                tk.Label(
                    card, text=f"✅ Your Answer: {chosen}",
                    font=("Arial", 14),
                    bg="#181818", fg="#00e676"
                ).pack(anchor="w")
            else:
                tk.Label(
                    card, text=f"❌ Your Answer: {chosen}",
                    font=("Arial", 14),
                    bg="#181818", fg="#ff5252"
                ).pack(anchor="w")
                tk.Label(
                    card, text=f"Correct Answer: {correct}",
                    font=("Arial", 14, "bold"),
                    bg="#181818", fg="#00e5ff"
                ).pack(anchor="w")


# ==========================================================
# RUN APPLICATION
# ==========================================================
if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()
