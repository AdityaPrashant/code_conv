# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 11:40:12 2023

@author: p_adi
"""

# main.py

# Execute the important_libraries.py file to import necessary libraries
try:
    exec(open("important_libraries.py").read())
except FileNotFoundError:
    print("important_libraries.py not found. Make sure the file exists.")

# Function to translate Python code
def translate_code():
    python_code = code_input.get("1.0", tk.END)  # Get Python code from the text widget
    
    # Define the target programming languages
    languages = ["java", "r", "c", "cpp"]
    
    translations = {}
    for lang in languages:
        response = openai.Completion.create(
            engine="davinci-002",  # Use the "davinci-002" model
            prompt=f"Translate the following Python code into {lang}:\n{python_code}",
            max_tokens=50,         # Adjust this value as needed
            n=1,                    # Generate a single translation
            temperature=0.5,        # Adjust the temperature (higher values make output more random)
            top_p=0.85,              # Adjust the top_p (higher values make output more focused)
            stop=None,              # You can specify a stop string to control the length of the output
        )
        translations[lang] = response.choices[0].text
    
    # Clear the previous translations
    result_text.delete("1.0", tk.END)
    
    # Display the translations
    for lang, translation in translations.items():
        result_text.insert(tk.END, f"\n{lang.capitalize()} Code:\n{translation}\n")

# The rest of your code remains unchanged
# Create the main window
window = tk.Tk()
window.title("Python Code Translator")

# Open the window in fullscreen mode
window.attributes('-fullscreen', True)

# Create a custom window control frame
window_control_frame = tk.Frame(window, bg="lightgray")
window_control_frame.pack(fill=tk.X)

# Create minimize, maximize, and close buttons
minimize_button = tk.Button(window_control_frame, text="-", command=lambda: window.iconify())
maximize_button = tk.Button(window_control_frame, text="□", command=lambda: window.state('zoomed'))
close_button = tk.Button(window_control_frame, text="✕", command=window.quit)

minimize_button.pack(side=tk.LEFT)
maximize_button.pack(side=tk.LEFT)
close_button.pack(side=tk.RIGHT)

# Add padding to the UI
padding_frame = tk.Frame(window, padx=20, pady=20)
padding_frame.pack(fill=tk.BOTH, expand=True)

# Create a text input widget for Python code with a colorful background
code_label = tk.Label(padding_frame, text="Enter Python Code:")
code_label.pack()
code_input = scrolledtext.ScrolledText(padding_frame, width=50, height=10)
code_input.pack()
code_input.configure(bg="lightgray", fg="black")  # Set background to light gray and text color to black

# Create a button to trigger translation
translate_button = tk.Button(padding_frame, text="Translate", command=translate_code)
translate_button.pack()

# Create a text widget to display translations with a colorful background
result_label = tk.Label(padding_frame, text="Translations:")
result_label.pack()
result_text = scrolledtext.ScrolledText(padding_frame, width=50, height=20)
result_text.pack()
result_text.configure(bg="lightblue", fg="black")  # Set background to light blue and text color to black

# Start the Tkinter main loop
window.mainloop()
