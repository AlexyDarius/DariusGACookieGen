def generate_cookie_php(main_domain, directory_path):
    php_code = f'''<link rel="stylesheet" href="https://www.{main_domain}/cookies/styles.css">
<script src="https://www.{main_domain}/cookies/cookie.js"></script>
<script src="https://www.{main_domain}/cookies/cookieConsentBar.js"></script>'''

    with open(f"{directory_path}/cookie.php", "w") as php_file:
        php_file.write(php_code)
