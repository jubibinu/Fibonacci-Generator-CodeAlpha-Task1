import tkinter as tk

def generate_fibonacci_numbers():
    n = int(entry.get())
    fibonacci_sequence = [0, 1]

    while len(fibonacci_sequence) < n:
        next_fib = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_fib)

    result_label.config(text=f"Fibonacci Sequence: {', '.join(map(str, fibonacci_sequence))}")

app = tk.Tk()
app.title("Fibonacci Number Generator")

app.configure(bg='#FFB6C1')

# Use a custom font
custom_font = ("Arial", 16)

label = tk.Label(app, text="Enter the number of Fibonacci numbers to generate:", font=custom_font, bg='#FFB6C1')
label.grid(row=0, column=0, padx=20, pady=20)

entry = tk.Entry(app, font=custom_font, bg='#ffffff', fg='#000000')
entry.grid(row=0, column=1, padx=20, pady=20)

generate_button = tk.Button(app, text="Generate", command=generate_fibonacci_numbers, font=custom_font, bg='#007bff', fg='#ffffff')
generate_button.grid(row=1, column=0, columnspan=2, pady=20)

result_label = tk.Label(app, text="", font=custom_font, bg='#FFB6C1')
result_label.grid(row=2, column=0, columnspan=2, pady=20)

app.mainloop()