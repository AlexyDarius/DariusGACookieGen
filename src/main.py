import tkinter as tk
from tkinter import filedialog
from tkinter import colorchooser
from generate_cookie_php import generate_cookie_php
from generate_cookie_js import generate_cookies_js
from generate_cookieConsentBar_js import generate_cookieConsentBar_js
from generate_gtagScript_js import generate_gtagScript_js
from generate_styles_css import generate_styles_css

def generate_files():
    main_domain = main_domain_entry.get()
    privacy_policy_url = privacy_policy_url_entry.get()
    main_message = main_message_entry.get("1.0", "end-1c")
    ga_message = ga_message_entry.get("1.0", "end-1c")
    gatag_id = gatag_id_entry.get()
    gtmtag_id = gtmtag_id_entry.get()
    cookie_expiration = cookie_expiration_entry.get()
    directory_path = directory_var.get()
    bg_color = color_entry1.get()
    primary_color = color_entry2.get()

    try:
        cookie_expiration = int(cookie_expiration)
        
    except ValueError:
        result_label.config(text="Cookie expiration must be an integer.")
        return

    if all([main_domain, privacy_policy_url, main_message, gatag_id, gtmtag_id, cookie_expiration, directory_path]):
        # Generate cookie.php
        generate_cookie_php(main_domain, directory_path)
        # Generate cookies.js
        generate_cookies_js(privacy_policy_url, main_message, gatag_id, cookie_expiration, directory_path)
        # Generate cookieConsentBar.js
        generate_cookieConsentBar_js(main_domain, ga_message, directory_path)
        # Generate gtagScript.js
        generate_gtagScript_js(gtmtag_id, directory_path)
        # Generate styles.css
        generate_styles_css(bg_color, primary_color, directory_path)
        
        result_label.config(text="Cookie files have been generated.")

        print("\nCookie files well generated, don't forget to minify !")
        print("Read readme.txt for implementation.\n")

        app.quit()
    else:
        result_label.config(text="Please provide all required fields.")

def select_directory():
    directory_path = filedialog.askdirectory()
    if directory_path:
        directory_var.set(directory_path)

def main_message_autofill():
    main_message_entry.delete("1.0", tk.END)
    main_message_entry.insert(tk.END, "Ce site utilise des cookies que vous pouvez paramétrer.")

def ga_message_autofill():
    ga_message_entry.delete("1.0", tk.END)
    ga_message_entry.insert(tk.END, "Google Analytics est utilisé pour capturer des informations générales anonymisées à propos de l'utilisation de cette page.")

def cookie_expiration_autofill():
    cookie_expiration_entry.delete(0, tk.END)
    cookie_expiration_entry.insert(0, "2678400")

def open_color_picker1():
    color = colorchooser.askcolor()[1]
    color_entry1.delete(0, tk.END)
    color_entry1.insert(0, color)

def open_color_picker2():
    color = colorchooser.askcolor()[1]
    color_entry2.delete(0, tk.END)
    color_entry2.insert(0, color)

app = tk.Tk()
app.title("Darius GA Cookie Generator")

directory_var = tk.StringVar()

directory_label = tk.Label(app, text="Select Directory:")
directory_label.pack()
directory_entry = tk.Entry(app, textvariable=directory_var, width = 50)
directory_entry.pack()

select_directory_button = tk.Button(app, text="Browse", command=select_directory)
select_directory_button.pack()

main_domain_label = tk.Label(app, text="Enter the main domain (e.g. dariusdev.fr, without www. !) :")
main_domain_label.pack()
main_domain_entry = tk.Entry(app)
main_domain_entry.pack()

privacy_policy_url_label = tk.Label(app, text="Privacy Policy URL (e.g. dariusdev.fr/privacy, without www. !) :")
privacy_policy_url_label.pack()
privacy_policy_url_entry = tk.Entry(app)
privacy_policy_url_entry.pack()

main_message_label = tk.Label(app, text="Main Message (e.g. Ce site utilise des cookies que vous pouvez paramétrer.) :")
main_message_label.pack()
main_message_entry = tk.Text(app, width=50, height=5)
main_message_autofill_button = tk.Button(app, text="Autofill", command=main_message_autofill)
main_message_autofill_button.pack()
main_message_entry.pack()

ga_message_label = tk.Label(app, text="Main Message (e.g. Google Analytics est utilisé pour capturer des informations\n générales anonymisées à propos de l'utilisation de cette page.) :")
ga_message_label.pack()
ga_message_autofill_button = tk.Button(app, text="Autofill", command=ga_message_autofill)
ga_message_autofill_button.pack()
ga_message_entry = tk.Text(app, width=50, height=5)
ga_message_entry.pack()

gatag_id_label = tk.Label(app, text="Google Analytics Tag ID (e.g. G-L0C0D6YQ9K) :")
gatag_id_label.pack()
gatag_id_entry = tk.Entry(app)
gatag_id_entry.pack()

gtmtag_id_label = tk.Label(app, text="Google Tag Manager Tag ID (e.g. GTM-L0C0D6YQ9K) :")
gtmtag_id_label.pack()
gtmtag_id_entry = tk.Entry(app)
gtmtag_id_entry.pack()

cookie_expiration_label = tk.Label(app, text="Cookie Expiration (seconds, 2678400 for 1 month):")
cookie_expiration_label.pack()
cookie_expiration_autofill_button = tk.Button(app, text="Autofill 1 month", command=cookie_expiration_autofill)
cookie_expiration_autofill_button.pack()
cookie_expiration_entry = tk.Entry(app)
cookie_expiration_entry.pack()

# Create an Entry widget for entering color in hex format
cookie_entry_label = tk.Label(app, text="Enter bg color of the cookie pop-up (#hex format) :")
cookie_entry_label.pack()
color_entry1 = tk.Entry(app)
color_entry1.pack()

# Create a Button to open the color picker
color_picker_button = tk.Button(app, text="Or use color picker", command=open_color_picker1)
color_picker_button.pack()

# Create an Entry widget for entering color in hex format
cookie_entry_label = tk.Label(app, text="Enter primary color of the cookie pop-up (#hex format) :")
cookie_entry_label.pack()
color_entry2 = tk.Entry(app)
color_entry2.pack()

# Create a Button to open the color picker
color_picker_button = tk.Button(app, text="Or use color picker", command=open_color_picker2)
color_picker_button.pack()

blank_label = tk.Label(app, text="")
blank_label.pack()

generate_button = tk.Button(app, text="Generate", command=generate_files)
generate_button.pack()

result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()
