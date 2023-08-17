import os
import openai  # pip install openai
import customtkinter as ctk  # pip install customtkinter


# Functions
def generate():
    prompt = "Please generate 10 ideas for coding projects. "

    language = language_dropdown.get()
    prompt += f"The programming language is {language}. "
    # --------------------------
    difficulty = difficulty_value.get()
    prompt += f"The difficulty is {difficulty}. "
    # --------------------------
    if checkbox1.get():
        prompt += "The project should include a database. "
    if checkbox2.get():
        prompt += "The project should include a API. "

    # openai.api_key = "YOUR_OPENAI_API_KEY" # Add your api key
    openai.api_key = os.getenv(key="OPENAI_API_KEY")  # Add key to your system environment variable
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])

    answer = response.choices[0].message.content
    result.insert(index="0.0", text=answer)


# App Theme Set & Main UI Codes
root = ctk.CTk()
root.geometry("750x550")
root.title("ChatGPT Project Idea Generator")
ctk.set_appearance_mode("dark")  # default use your system setting

title_lable = ctk.CTkLabel(
    master=root, text="Project Idea Generator ©2023", font=ctk.CTkFont(size=30, weight="bold")
)
title_lable.pack(padx=10, pady=(40, 20))  # pad y is 40 top and 20 bottem

frame = ctk.CTkFrame(master=root)
frame.pack(fill="x", padx=100)

language_frame = ctk.CTkFrame(master=frame)
language_frame.pack(padx=100, pady=(20, 5), fill="both")
# ------------------------
language_lable = ctk.CTkLabel(master=language_frame, text="Programming Language", font=ctk.CTkFont(weight="bold"))
language_lable.pack()
# ------------------------
language_dropdown = ctk.CTkComboBox(master=language_frame, values=["Python", "Java", "C++", "GoLang", "JavaScript", "C#"])
language_dropdown.pack(pady=10)

difficulty_frame = ctk.CTkFrame(master=frame)
difficulty_frame.pack(padx=100, pady=5, fill="both")
# ------------------------
difficulty_lable = ctk.CTkLabel(master=difficulty_frame, text="Project Difficulty", font=ctk.CTkFont(weight="bold"))
difficulty_lable.pack()
# ------------------------
difficulty_value = ctk.StringVar(value="Easy")
radiobutton1 = ctk.CTkRadioButton(master=difficulty_frame, text="Easy", variable=difficulty_value, value="Easy")
radiobutton1.pack(side="left", padx=(20, 10), pady=10)
radiobutton2 = ctk.CTkRadioButton(master=difficulty_frame, text="Medium", variable=difficulty_value, value="Medium")
radiobutton2.pack(side="left", padx=10, pady=10)
radiobutton3 = ctk.CTkRadioButton(master=difficulty_frame, text="Hard", variable=difficulty_value, value="Hard")
radiobutton3.pack(side="left", padx=10, pady=10)

features_frame = ctk.CTkFrame(master=frame)
features_frame.pack(padx=100, pady=5, fill="both")
# ------------------------
features_labe = ctk.CTkLabel(master=features_frame, text="Features", font=ctk.CTkFont(weight="bold"))
features_labe.pack()
# ------------------------
checkbox1 = ctk.CTkCheckBox(master=features_frame, text="Database")
checkbox1.pack(side="left", padx=50, pady=10)
checkbox2 = ctk.CTkCheckBox(master=features_frame, text="API")
checkbox2.pack(side="left", padx=50, pady=10)

button = ctk.CTkButton(master=frame, text="Generate Ideas", command=generate)
button.pack(fill="x", padx=100, pady=(5, 20))


result = ctk.CTkTextbox(master=root, font=ctk.CTkFont(size=15))
result.pack(pady=10, fill="x", padx=100)

# End Main Codes

# Run Main Window
root.mainloop()
