# Screenshot Email Sender

This project captures a screenshot and sends it as an attachment via email using Python.

## Requirements

- Python 3.x
- `pyautogui` library
- A Gmail account with less secure app access enabled or an app password

## How to Use

1. Install the requirements by running the following command:
    ```bash
    pip install -r requirements.txt
    ```

2. Update the code with your Gmail account information:
    ```python
    conn.login("your-email@gmail.com", "your-password")
    conn.sendmail("your-email@gmail.com", "recipient-email@gmail.com", msg)
    ```

3. Run the script:
    ```bash
    python script.py
    ```

## Notes

- Make sure to enable less secure app access for your Gmail account or use an app password.
- The sent screenshot can be found in the recipient's email.
