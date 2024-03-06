import requests

def send_discord_message(webhook_url, content):
    """
    Sends a message to a Discord webhook.

    Parameters:
    - webhook_url (str): The URL of the Discord webhook.
    - content (str): The content of the message.

    Returns:
    - bool: True if the message was sent successfully, False otherwise.
    """
    try:
        data = {"content": content}
        response = requests.post(webhook_url, json=data)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            print("Message sent successfully!")
            return True
        else:
            print(f"Failed to send message. Status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False

# Replace 'YOUR_WEBHOOK_URL' with the actual webhook URL
webhook_url = 'YOUR_WEBHOOK_URL'

# Example message content
message_content = "replace me with a message"

# Send the message
send_discord_message(webhook_url, message_content)
