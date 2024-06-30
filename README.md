
# Domain Availability Checker

This Python project checks the availability of domains and sends notifications via Pushover if a domain is available.

## Prerequisites

- Python 3.x
- `whois` library
- `requests` library
- Pushover account with API token and user key

## Setup

1. **Install required libraries**:

    ```
    pip install python-whois requests
    ```
   or
    ```
    pip install -r requirements.txt
    ```

2. **Pushover Credentials**:

    Create a `pushover_credentials.json` file in the same directory as the script with the following content:

    ```json
    {
        "user_key": "YOUR_USER_KEY",
        "api_token": "YOUR_API_TOKEN"
    }
    ```

3. **Domains File**:

    Create a `domains.txt` file in the same directory as the script and list the domains you want to check, one per line.

    Example `domains.txt`:

    ```
    example.com
    google.com
    youtube.de
    ```

## Usage

Run the script:

```
python domain_checker.py
```

The script will read the domains from `domains.txt` and check their availability. If a domain is available, a Pushover notification will be sent.

## Project Files

- `check.py`: The main script to check domain availability and send notifications.
- `domains.txt`: A file containing the list of domains to check.
- `pushover_credentials.json`: A file containing Pushover API credentials.

## Example Output

```
Checking domain example.com
Domain example.com is already registered.
Checking domain google.com
Domain google.com is already registered.
Checking domain youtube.de
Domain youtube.de is already registered.
```

If a domain is available:

```
Checking domain availabledomain.com
Domain availabledomain.com is available!
Pushover notification sent successfully.
```

## Author

Sebastian Espei
