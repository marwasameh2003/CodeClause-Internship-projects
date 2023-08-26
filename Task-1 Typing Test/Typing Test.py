import tkinter as tk
import time
from random import random, choice

def calulate_wordPerMin(text, time_passed):
    words = text.split()
    num = len(words)
    minutes = time_passed/60
    WPM = num / minutes
    return WPM


def calAccuracy(ranpas, text):
    min_length = min(len(ranpas), len(text))
    if min_length == 0:
        return 'No text was Entered! 0'
    counter = 0
    for i in range(min_length):
        if text[i] != ranpas[i]:
            counter += 1

    correct = min_length - counter
    accuracy = (correct / min_length) * 100
    r_a_n = round(accuracy,2)
    return r_a_n
def calResults(tm, suppas , enteredpas):
    w = tk.Toplevel(bg="#F1C93B")
    # Set window size
    window_width = 600
    window_height = 300
    screen_width = w.winfo_screenwidth()
    screen_height = w.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    w.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
    w.title("RESULTS")
    et = time.time()
    res = et-tm
    text_widget2 = tk.Text(w, height=3, width=40,fg="#1A5D1A" , borderwidth=1, relief="solid")
    text_widget2.pack()
    text_widget2.insert(tk.END, "Total time = "+str(res) + " seconds\n")
    text_widget2.pack()
    en = enteredpas.get()
    acc = calAccuracy(suppas , en)
    text_widget = tk.Text(w, height=3, width=40, borderwidth=1, relief="solid",fg="#1A5D1A" )
    text_widget.pack()
    text_widget.insert(tk.END, "Accuracy = " + str(acc) + " %\n")
    text_widget.pack()
    text_widget3 = tk.Text(w, height=3, width=40, borderwidth=1, relief="solid",fg="#1A5D1A" )
    text_widget3.pack()
    WPM = calulate_wordPerMin(en,res)
    rn = round(WPM, 2)
    text_widget3.insert(tk.END, "Speed = "+ str(rn) + " WPM \n")
    text_widget3.pack()
    save_button = tk.Button(w, text="Back To Menu", command=practicing,fg="#1A5D1A")
    save_button.pack(pady=10)
    button = tk.Button(w, text="Exit Program", command=close,fg="#1A5D1A")
    button.pack(pady=10)


def easy():
    file_path = 'EasyPassages.txt'  # Replace with the correct file path

    passages = []

    try:
        with open(file_path, 'r') as file:
            passage = ""
            for line in file:
                if line.strip():  # Check if the line is not empty
                    passage += line
                elif passage:  # If the line is empty and we have accumulated text in passage
                    passages.append(passage.strip())
                    passage = ""  # Reset passage for the next one

            # Add the last passage (if any) after the loop
            if passage:
                passages.append(passage.strip())

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


    random_passage = choice(passages)
    win = tk.Toplevel(bg="#F1C93B")
    win.title("Easy Passage Test:")
    # Set window size
    window_width = 600
    window_height = 300
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    win.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
    text_label = tk.Label(win, text=random_passage,wraplength=450,bg="#FAE392")
    text_label.pack()
    t = "Enter the passage provided above:"
    txt = tk.Label(win, text=t,bg="#F1C93B",justify="left", anchor="w")
    txt.pack()
    entry = tk.Entry(win,width=100)
    st = time.time()
    entry.pack(padx=20, pady=10)
    save_button = tk.Button(win, text="Submit", command=lambda :calResults(st, random_passage ,entry),fg="#1A5D1A")
    save_button.pack()
    bt = tk.Button(win, text="Back To Menu", command=practicing, fg="#1A5D1A")
    bt.pack(pady=10)
    button = tk.Button(win, text="Exit Program", command=close,fg="#1A5D1A")
    button.pack()
def intermediate():
    file_path = 'IntermediatePassages.txt'  # Replace with the correct file path

    passages = []

    try:
        with open(file_path, 'r') as file:
            passage = ""
            for line in file:
                if line.strip():  # Check if the line is not empty
                    passage += line
                elif passage:  # If the line is empty and we have accumulated text in passage
                    passages.append(passage.strip())
                    passage = ""  # Reset passage for the next one

            # Add the last passage (if any) after the loop
            if passage:
                passages.append(passage.strip())

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    random_passage = choice(passages)
    win = tk.Toplevel(bg="#F1C93B")
    win.title("Intermediate Passage Test:")
    # Set window size
    window_width = 600
    window_height = 300
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    win.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
    text_label = tk.Label(win, text=random_passage, wraplength=450,bg="#FAE392")
    text_label.pack()
    txt = tk.Label(win, text="Enter the passage provided above:",bg="#F1C93B", anchor="w")
    txt.pack()
    entry = tk.Entry(win, width=100)
    st = time.time()
    entry.pack(padx=20, pady=10 )
    save_button = tk.Button(win, text="Submit", command=lambda: calResults(st, random_passage, entry),fg="#1A5D1A")
    save_button.pack(pady=10)
    bt = tk.Button(win, text="Back To Menu", command=practicing, fg="#1A5D1A")
    bt.pack(pady=10)
    button = tk.Button(win, text="Exit Program", command=close,fg="#1A5D1A")
    button.pack()
def hard():
    file_path = 'HardPassages.txt'  # Replace with the correct file path

    passages = []

    try:
        with open(file_path, 'r') as file:
            passage = ""
            for line in file:
                if line.strip():  # Check if the line is not empty
                    passage += line
                elif passage:  # If the line is empty and we have accumulated text in passage
                    passages.append(passage.strip())
                    passage = ""  # Reset passage for the next one

            # Add the last passage (if any) after the loop
            if passage:
                passages.append(passage.strip())

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    random_passage = choice(passages)
    win = tk.Toplevel(bg="#F1C93B")
    win.title("Hard Passage Test:")
    # Set window size
    window_width = 600
    window_height = 300
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    win.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
    text_label = tk.Label(win, text=random_passage, wraplength=450,bg="#FAE392")
    text_label.pack()
    txt = tk.Label(win, text="Enter the passage provided above:", bg="#F1C93B", anchor="w")
    txt.pack()
    entry = tk.Entry(win, width=100 )
    st = time.time()
    entry.pack(padx=20, pady=10)
    save_button = tk.Button(win, text="Submit", command=lambda: calResults(st, random_passage, entry),fg="#1A5D1A")
    save_button.pack(pady=10)
    bt = tk.Button(win, text="Back To Menu", command=practicing, fg="#1A5D1A")
    bt.pack(pady=10)
    button = tk.Button(win, text="Exit Program", command=close,fg="#1A5D1A")
    button.pack(pady=10)
def close():
    root.quit()

def practicing():
    win2dow = tk.Toplevel(bg="#F1C93B")
    win2dow.title("Practice Menu")
    # Set window size
    window_width = 600
    window_height = 300
    screen_width = win2dow.winfo_screenwidth()
    screen_height = win2dow.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    win2dow.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
    text = "Choose the level you want to practice:"
    text_label = tk.Label(win2dow, text=text , fg= "#1A5D1A",bg="#F1C93B")
    text_label.pack()

    button = tk.Button(win2dow, text="Easy", command=easy, fg= "#1A5D1A")
    button.pack(pady=5)

    button = tk.Button(win2dow, text="Intermediate", command=intermediate,fg= "#1A5D1A")
    button.pack(pady=5)

    button = tk.Button(win2dow, text="Hard", command=hard,fg= "#1A5D1A")
    button.pack(pady=5)
    button = tk.Button(win2dow, text="Exit Program", command=close ,fg= "#1A5D1A")
    button.pack(pady=5)

def menu():
    new_window = tk.Toplevel(bg="#F1C93B")
    new_window.title("MENU")
    # Set window size
    window_width = 600
    window_height = 300
    screen_width = new_window.winfo_screenwidth()
    screen_height = new_window.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    new_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    text = "Welcome To Speed Typing Test Program!"
    text_label = tk.Label( new_window, text=text, bg = "#F1C93B" )
    text_label.config(text=text)

    button = tk.Button(new_window, text="Practice  ", command=practicing , fg= "#1A5D1A")
    button.pack(pady=10)

    button = tk.Button(new_window, text="Exit Program", command=close, fg= "#1A5D1A")
    button.pack(pady=20)

def main():
    global root
    root = tk.Tk()
    # Set window size
    window_width = 600
    window_height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
    root.title("Speed Typing Test")
    background_color = "#F1C93B"  # Light gray
    root.configure(bg=background_color)
    text = "Welcome To Speed Typing Test Program!"
    text_label = tk.Label(root, text=text , fg="#1A5D1A" ,bg = "#F1C93B")
    text_label.pack(pady=20)


    button = tk.Button(root, text="Get Started", command=menu ,fg="#1A5D1A")
    button.pack()
    # background_color = "#1A5D1A"  # Light gray
    # button.configure(bg=background_color)


    root.mainloop()

main()
#Link Windows to each other
#change the passages colors
#1A5D1A green
#F1C93B  yellow

# اظبط اماكن الزراير
#هندلة حتة انه ميدخلش حاجه و يعمل سابمت
# هندلة التنقل بين الصفحات
#ديزاين النتيجه