
# Telegram Group Messenger

This project is a Telegram bot that uses the Telethon library to send messages to multiple Telegram groups. It automates the process of posting a predefined message in specified groups, making it useful for announcements, promotions, or information dissemination.

## Features

- Connects to Telegram using a user account.
- Sends messages to multiple predefined Telegram groups.
- Implements a simple error handling mechanism.
- Utilizes a session to maintain the user's login state.

## Prerequisites

- Python 3.6 or higher
- [Telethon](https://github.com/LonamiWebs/Telethon) library

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/nouredinekn/aws-cloud-boto3.git
   cd aws-cloud-boto3
   ```

2. Install the required packages:

   ```bash
   pip install telethon
   ```

## Configuration

Before running the bot, update the following variables in the script:

- `api_id`: Your Telegram API ID. You can obtain this from the [Telegram API](https://my.telegram.org/apps).
- `api_hash`: Your Telegram API Hash. This is also available from the [Telegram API](https://my.telegram.org/apps).
- `phone`: Your Telegram phone number in international format.
- `groups`: A list of Telegram group usernames where you want to send the message.
- `msg`: The message you want to send.

## Usage

1. Open your terminal.
2. Run the script:

   ```bash
   python your_script_name.py
   ```

3. The bot will connect to Telegram and send the message to the specified groups.

## Example Script

Here's a sample script for sending messages:

```python
from telethon import TelegramClient
import time

api_id = 7357692
api_hash = 'b113123d7856fda37b8a23726cbd6ba7'
phone = '+212666666666'  # Your Telegram number

groups = [
    'ebay_seller_plus',
    'ebaymethod',
    # Add more groups here
]

msg = '''Your message here'''

client = TelegramClient('session_name', api_id, api_hash)
client.start()

while True:
    print('Sending messages...')
    for group in groups:
        try:
            entity = client.get_entity(group)
            client.send_message(entity=entity, message=msg)
            print(f"Message sent to {group}")
        except Exception as e:
            print(f"Failed to send message to {group}: {e}")
    print('Waiting for 10 minutes before trying again...')
    time.sleep(600)  # Wait for 10 minutes before sending messages again
```

## Notes

- Ensure you comply with Telegram's terms of service regarding spamming and messaging.
- Consider implementing more advanced error handling and logging for production use.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or suggestions, feel free to reach out on Telegram: [@nouredine_kn](https://t.me/nouredine_kn).

