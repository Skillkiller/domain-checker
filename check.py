import whois
import requests
import json

with open("pushover_credentials.json", "r") as file:
    pushover_credentials = json.load(file)


def send_pushover_notification(message):
    payload = {
        "token": pushover_credentials["api_token"],
        "user": pushover_credentials["user_key"],
        "message": message
    }
    response = requests.post("https://api.pushover.net/1/messages.json", data=payload)
    if response.status_code == 200:
        print("Pushover notification sent successfully.")
    else:
        print(f"Failed to send Pushover notification: {response.text}")


def load_domains(file_path):
    with open(file_path, "r") as file:
        domains = [line.strip() for line in file.readlines()]
    return domains


def check_domains(domains):
    for domain in domains:
        print(f"Checking domain {domain}")
        try:
            domain_info = whois.whois(domain)
            if domain_info.status is None or domain_info.status == "free":
                domain_free(domain)
            else:
                domain_registered(domain)
        except whois.parser.PywhoisError as e:
            if len(e.args) > 0 and "Status: free" in e.args[0]:
                domain_free(domain)
            else:
                print(f"Could not check {domain}: {e}")
        except Exception as e:
            print(f"Could not check {domain}: {e}")


def domain_free(domain):
    message = f"Domain {domain} is available!"
    print(message)
    send_pushover_notification(message)


def domain_registered(domain):
    print(f"Domain {domain} is already registered.")


domains = load_domains("domains.txt")
check_domains(domains)
