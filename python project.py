import tkinter as tk
from tkinter import messagebox
import pyshorteners #type:ignore

def shorten_url():
    long_url = url_entry.get()
    if not long_url:
        messagebox.showerror("Error", "Please enter a URL")
        return

    shortener = pyshorteners.Shortener()
    try:
        short_url = shortener.tinyurl.short(long_url)
        result_label.config(text=f"Conversion results: {short_url}")
        copy_button.config(state=tk.NORMAL)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to shorten URL: {str(e)}")

def clear_entry():
    url_entry.delete(0, tk.END)
    result_label.config(text="")
    copy_button.config(state=tk.DISABLED)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(result_label.cget("text").split(" ")[-1])
    messagebox.showinfo("Copied", "Shortened URL copied to clipboard")
    
root = tk.Tk()
root.title("URL Shortener")
root.geometry("1920x1820")
root.configure(bg="#2c3e50")

font_name = "Times New Roman"
font_bold = "Times New Roman Bold"
times = "Times New Roman"

top_label1 = tk.Label(root, text="M KUMARASAMY COLLEGE OF ENGINEERING - KARUR", font=(font_bold, 18), bg="#2c3e50", fg="white")
top_label1.pack(pady=5)

top_label2 = tk.Label(root, text="PYTHON END SEMESTER PROJECT", font=(font_bold, 17), bg="#2c3e50", fg="white")
top_label2.pack(pady=5)

top_label3 = tk.Label(root, text="G PRAVIN RAJ", font=(font_name, 16), bg="#2c3e50", fg="white")
top_label3.pack(pady=5)

reg_label = tk.Label(root, text="Reg No: 927623BCS079", font=(font_name, 16), bg="#2c3e50", fg="white")
reg_label.pack(pady=5)

title_label = tk.Label(root, text="URL Shortener", font=(font_bold, 20), bg="#2980b9", fg="white")
title_label.pack(pady=10, fill=tk.X)

url_label = tk.Label(root, text="Enter long URL:", bg="#2c3e50", fg="white", font=(font_name, 14))
url_label.pack(pady=5)

url_entry = tk.Entry(root, font=(times, 14), width=40)
url_entry.pack(pady=5)

shorten_button = tk.Button(root, text="Shorten", command=shorten_url, font=(font_bold, 14), bg="#27ae60", fg="white", width=10)
shorten_button.pack(pady=10)

result_label = tk.Label(root, text="", fg="white", bg="#2c3e50", font=(font_name, 12))
result_label.pack(pady=5)

clear_button = tk.Button(root, text="Clear", command=clear_entry, font=(font_bold, 12), bg="#e74c3c", fg="white", width=10)
clear_button.pack(pady=10)

copy_button = tk.Button(root, text="Copy", state=tk.DISABLED, command=copy_to_clipboard, font=(font_bold, 12), bg="#3498db", fg="white", width=10)
copy_button.pack(pady=10)

root.mainloop()