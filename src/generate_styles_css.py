def generate_styles_css(bg_color, primary_color, directory_path):
    js_code = f'''#cookie-msg {{
    max-width: 100%;
    color: #0c3028;
    background-color: {bg_color};
    text-align: center;
    padding: 12px;
    margin-bottom: 12px;
    margin-left: 12px;
    margin-right: 12px;
    border-style: solid;
    border-color: {primary_color};
}}
.button_v7h {{
    color: {bg_color};
    background-color: {primary_color};
}}
'''

    with open(f"{directory_path}/styles.css", "w") as js_file:
        js_file.write(js_code)
