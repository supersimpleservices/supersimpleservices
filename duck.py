import discord
import openai
from openai import AsyncOpenAI

# Define intents
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

# Initialize the Discord client with intents
client = discord.Client(intents=intents)

# Set your OpenAI API key
openai.api_key = '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'

async_client = AsyncOpenAI(api_key='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')

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def ask_openai(prompt):
#    response = await openai.ChatCompletion.create(
#    response = await async_client.ChatCompletion.create(
    response = await async_client.chat.completions.create(
        model="gpt-3.5-turbo",  # or another model name depending on your requirement
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
#    return response['choices'][0]['message']['content']
#    return response.choices[0].message['content']
    return response.choices[0].message.content


#   except Exception as e:
#       print(f"Error: {e}")
#       return "Sorry, I couldn't process that request."


# Example usage in your Discord bot
@client.event
async def on_message(message):
    # Don't respond to messages sent by the bot
    if message.author == client.user:
        return

    if message.content.startswith('!ask'):
        # Extracting the message to send to the OpenAI API
        user_message = message.content[len('!ask'):].strip()
        # Calling the OpenAI API
        response_message = await ask_openai(user_message)
        # Sending the response back to Discord
        await message.channel.send(response_message)

# Run the bot
client.run('MTE4NzE3MjkxOTY4ODgyNjkzMA.GF2ryR.fDQ2156vogDlt-BHTH3Q7Zl6pVcfLCztly6st8')
