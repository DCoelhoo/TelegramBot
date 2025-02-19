from key import Key
from telegram import Bot
from telegram.ext import Application
import asyncio
from messages import Messages

#Define Bot Token
BOT_TOKEN = Key.return_token()

#Define Chat ID
CHAT_ID = Key.return_chatId()


async def send_messages():
    """A function to send Messages"""

    # Create an instance of Messages class
    message_bot = Messages()

    # Call the chooseMessage method on the instance
    bot_message = message_bot.chooseMessage()

    #Create Bot
    bot = Bot(token = BOT_TOKEN)

    #Send message
    await bot.send_message(chat_id = CHAT_ID, text= bot_message)

async def main():
    """ Calls functions """
    await send_messages()

if __name__ == "__main__":
    asyncio.run(main()) 



