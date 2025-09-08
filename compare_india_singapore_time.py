import tkinter as tk
from tkinter import font as tkfont
from datetime import datetime
import pytz

def update_time():
    """
    Updates the time and date for Singapore and India in the GUI.
    """
    # Get current time
    now_utc = datetime.now(pytz.utc)
    
    # Get time for Singapore (Asia/Singapore)
    singapore_tz = pytz.timezone('Asia/Singapore')
    singapore_time = now_utc.astimezone(singapore_tz)
    
    # Get time for India (Asia/Kolkata)
    india_tz = pytz.timezone('Asia/Kolkata')
    india_time = now_utc.astimezone(india_tz)
    
    # Format the time and date strings
    singapore_time_str = singapore_time.strftime('%H:%M:%S')
    singapore_date_str = singapore_time.strftime('%A, %B %d, %Y')
    
    india_time_str = india_time.strftime('%H:%M:%S')
    india_date_str = india_time.strftime('%A, %B %d, %Y')
    
    # Update the labels in the GUI
    singapore_time_label.config(text=singapore_time_str)
    singapore_date_label.config(text=singapore_date_str)
    
    india_time_label.config(text=india_time_str)
    india_date_label.config(text=india_date_str)
    
    # Schedule the next update in 1000 milliseconds (1 second)
    root.after(1000, update_time)

# --- GUI Setup ---
root = tk.Tk()
root.title("Global Time App")
root.geometry("600x300")
root.resizable(False, False)
root.configure(bg='#f0f4f8')

# Custom fonts
title_font = tkfont.Font(family="Inter", size=24, weight="bold")
time_font = tkfont.Font(family="Inter", size=48, weight="bold")
date_font = tkfont.Font(family="Inter", size=12, weight="normal")
location_font = tkfont.Font(family="Inter", size=18, weight="normal")

# Create a main frame to center content
main_frame = tk.Frame(root, bg='#f0f4f8')
main_frame.pack(expand=True, fill='both', padx=20, pady=20)

# Main title
title_label = tk.Label(main_frame, text="Global Time", font=title_font, bg='#f0f4f8', fg='#2d3748')
title_label.pack(pady=(0, 20))

# Time card frames
clocks_frame = tk.Frame(main_frame, bg='#f0f4f8')
clocks_frame.pack(fill='both', expand=True)

# Singapore frame
singapore_frame = tk.Frame(clocks_frame, bg='#4c51bf', padx=20, pady=20, relief=tk.RAISED, bd=2)
singapore_frame.pack(side='left', fill='both', expand=True, padx=(0, 10))

singapore_title_label = tk.Label(singapore_frame, text="Singapore", font=location_font, bg='#4c51bf', fg='white')
singapore_title_label.pack(pady=(0, 10))

singapore_time_label = tk.Label(singapore_frame, font=time_font, bg='#4c51bf', fg='white')
singapore_time_label.pack()

singapore_date_label = tk.Label(singapore_frame, font=date_font, bg='#4c51bf', fg='white')
singapore_date_label.pack()

# India frame
india_frame = tk.Frame(clocks_frame, bg='#38a169', padx=20, pady=20, relief=tk.RAISED, bd=2)
india_frame.pack(side='right', fill='both', expand=True, padx=(10, 0))

india_title_label = tk.Label(india_frame, text="India", font=location_font, bg='#38a169', fg='white')
india_title_label.pack(pady=(0, 10))

india_time_label = tk.Label(india_frame, font=time_font, bg='#38a169', fg='white')
india_time_label.pack()

india_date_label = tk.Label(india_frame, font=date_font, bg='#38a169', fg='white')
india_date_label.pack()

# Initial call to update time and start the loop
update_time()

# Start the Tkinter event loop
root.mainloop()
