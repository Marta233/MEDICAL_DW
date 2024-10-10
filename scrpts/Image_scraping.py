import os
import json
from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.types import MessageMediaPhoto
from dotenv import load_dotenv
import logging

# Load environment variables from .env file
load_dotenv()

# Set up logging
logging.basicConfig(
    filename='telegram_image_scraper.log',  # Log file name for images
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

class TelegramImageScraper:
    def __init__(self):
        self.api_id = os.getenv('API_ID')
        self.api_hash = os.getenv('API_HASH')
        self.phone_number = os.getenv('PHONE_NUMBER')
        self.download_dir = os.getenv('DOWNLOAD_DIR', 'downloads')  # Directory for downloaded images

        self.client = TelegramClient('session_name', self.api_id, self.api_hash)

        self._create_directory(self.download_dir)

    def _create_directory(self, directory):
        """Create a directory if it doesn't exist."""
        if not os.path.exists(directory):
            os.makedirs(directory)

    async def _download_media(self, message):
        """Download media from a message if it contains a photo."""
        if message.media and isinstance(message.media, MessageMediaPhoto):
            photo_path = await message.download_media(file=self.download_dir)
            return photo_path
        return None

    async def fetch_images_from_channel(self, channel):
        """Fetch images from a single Telegram channel and save them to the specified download directory."""
        print(f"Joining and fetching images from {channel}...")

        try:
            # Join the channel
            await self.client(JoinChannelRequest(channel))

            # Get the channel entity
            entity = await self.client.get_entity(channel)

            # Fetch messages
            async for message in self.client.iter_messages(entity):
                # Download media if present
                media_path = await self._download_media(message)
                if media_path:
                    print(f"Downloaded image to {media_path}")

        except Exception as e:
            print(f"Error fetching images from {channel}: {str(e)}")

    async def connect(self):
        """Connect to the Telegram client."""
        await self.client.start(self.phone_number)

    async def disconnect(self):
        """Stop the Telegram client gracefully."""
        await self.client.disconnect()

    async def fetch_images_from_channels(self, channels):
        """Fetch images from a list of Telegram channels."""
        for channel in channels:
            await self.fetch_images_from_channel(channel)
