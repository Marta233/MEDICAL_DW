import os
import json
from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from dotenv import load_dotenv
import logging

# Load environment variables from .env file
load_dotenv()

# Set up logging
logging.basicConfig(
    filename='telegram_text_scraper.log',  # Log file name
    level=logging.INFO,  # Log level (you can change this to DEBUG for more details)
    format='%(asctime)s - %(levelname)s - %(message)s',  # Log format
    datefmt='%Y-%m-%d %H:%M:%S'  # Log date format
)
class TelegramChannelScraper:
    def __init__(self):
        # Load the API credentials and configuration from environment variables
        self.api_id = os.getenv('API_ID')
        self.api_hash = os.getenv('API_HASH')
        self.phone_number = os.getenv('PHONE_NUMBER')
        self.download_dir = os.getenv('DOWNLOAD_DIR', 'downloads')
        self.message_file = os.getenv('MESSAGE_FILE', 'telegram_messages.json')

        # Initialize the Telegram client
        self.client = TelegramClient('session_name', self.api_id, self.api_hash)

        # Ensure download directory exists
        self._create_directory(self.download_dir)

    def _create_directory(self, directory):
        """Create a directory if it doesn't exist."""
        if not os.path.exists(directory):
            os.makedirs(directory)

    def _save_message_to_file(self, file, message_data):
        """Save a message to the JSON file."""
        file.write(json.dumps(message_data, ensure_ascii=False) + "\n")



    async def fetch_messages_from_channel(self, channel):
        """Fetch messages from a single Telegram channel and save them to a file."""
        print(f"Joining and fetching messages from {channel}...")

        try:
            # Join the channel
            await self.client(JoinChannelRequest(channel))

            # Get the channel entity
            entity = await self.client.get_entity(channel)

            # Open the message file in append mode
            with open(self.message_file, 'a', encoding='utf-8') as file:
                # Fetch messages
                async for message in self.client.iter_messages(entity):
                    message_data = {
                        'channel': channel,
                        'message_id': message.id,
                        'date': message.date.isoformat(),
                        'sender': message.sender_id,
                        'text': message.text if message.text else '',
                    }

                    print(f"Saving message {message.id} from {channel}")
                    self._save_message_to_file(file, message_data)

        except Exception as e:
            print(f"Error fetching messages from {channel}: {str(e)}")

    async def connect(self):
        """Connect to the Telegram client."""
        await self.client.start(self.phone_number)

    async def disconnect(self):
        """Stop the Telegram client gracefully."""
        await self.client.disconnect()

    async def fetch_messages_from_channels(self, channels):
        """Fetch messages from a list of Telegram channels."""
        for channel in channels:
            await self.fetch_messages_from_channel(channel)