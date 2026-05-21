import requests
from bs4 import BeautifulSoup
from datetime import datetime
from colorama import Fore, init

init()
def valid_url(url):

    parsed = urlparse(url)

    return bool(parsed.scheme and parsed.netloc)
while True:
    print(Fore.CYAN + """
==== MINI SECURITY TOOLKIT ====

1. Website Status Check
2. Title Grabber
3. Header Check
4. Save Website Report
5. Multi Website Scan
6. Response Time Check
7. Exit
""")

    choice = input(Fore.YELLOW + "Choose option: ")

    if choice == "1":
        url = input("Enter URL: ")
        try:
            response = requests.get(url, timeout=5)
            print(Fore.GREEN + "Status Code:", response.status_code)
            print("Server:", response.headers.get("Server"))
        except Exception as e:
            print(Fore.RED + "Error:", e)

    elif choice == "2":
        url = input("Enter URL: ")
        try:
            response = requests.get(url, timeout=5)
            soup = BeautifulSoup(response.text, "html.parser")
            print(Fore.GREEN + "Title:", soup.title.string if soup.title else "No title")
        except Exception as e:
            print(Fore.RED + "Error:", e)

    elif choice == "3":
        url = input("Enter URL: ")
        try:
            response = requests.get(url, timeout=5)
            print(Fore.GREEN + "\nHeaders:\n")
            for key, value in response.headers.items():
                print(Fore.WHITE + f"{key}: {value}")
        except Exception as e:
            print(Fore.RED + "Error:", e)

    elif choice == "4":
        url = input("Enter URL: ")
        try:
            response = requests.get(url, timeout=5)
            report = f"""
Website Report
Date: {datetime.now()}

URL: {url}
Status Code: {response.status_code}
Server: {response.headers.get("Server")}
Content Type: {response.headers.get("Content-Type")}
Response Time: {response.elapsed.total_seconds()} seconds
"""
            with open("report.txt", "a") as file:
                file.write(report)

            print(Fore.GREEN + "Report saved in report.txt")
        except Exception as e:
            print(Fore.RED + "Error:", e)

    elif choice == "5":
        sites_input = input("Enter websites separated by comma: ")
        websites = sites_input.split(",")

        print(Fore.CYAN + "\nStarting Multi Website Scan...\n")

        for site in websites:
            site = site.strip()

            try:
                response = requests.get(site, timeout=5)
                print(Fore.GREEN + f"\nWebsite: {site}")
                print(Fore.YELLOW + f"Status: {response.status_code}")
                print(Fore.WHITE + f"Server: {response.headers.get('Server')}")
                print(Fore.WHITE + f"Response Time: {response.elapsed.total_seconds()} seconds")
                print("----------------------")
            except Exception as e:
                print(Fore.RED + f"Error scanning {site}: {e}")

    elif choice == "6":
        url = input("Enter URL: ")
        try:
            response = requests.get(url, timeout=5)
            print(Fore.GREEN + f"Status: {response.status_code}")
            print(Fore.YELLOW + f"Response Time: {response.elapsed.total_seconds()} seconds")
        except Exception as e:
            print(Fore.RED + f"Error: {e}")

    elif choice == "7":
        print(Fore.MAGENTA + "Goodbye bhai 🙂")
        break

    else:
        print(Fore.RED + "Invalid option")
