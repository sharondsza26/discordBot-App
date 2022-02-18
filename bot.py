import discord 
import requests
import json
import asyncio

client = discord.Client()


def get_question():
    qs = ''
    id = 1
    answer = 0
    # collecting the question
    response = requests.get("https://shielded-sierra-27313.herokuapp.com/api/random/")
    # formatting the data into a dictionary, for easy access 
    json_data = json.loads(response.text)
    qs += "Question: \n"
    qs += json_data[0]['title'] + "\n"

    # numbering the ans for display
    for item in json_data[0]['answer']:
        qs += str(id) + ". " + item['answer'] + "\n"

        # if the option is correct, update answer id (1. correct option, answer == 1)
        if item['is_correct']:
            answer = id
        # next
        id += 1 
    
    return(qs, answer)


# async method
@client.event
async def on_message(message):
    # if message is from the bot, ignore
    if message.author == client.user:
        return
    
    # if user wants a question
    if message.content.startswith('$question'):
    
        qs, answer = get_question()
        await message.channel.send(qs)


        # settig up a web socket to listen for answer
        def check(m):
            return m.author == message.author and m.content.isdigit() 

        try:
            # waiting to chack if there is user input
            guess = await client.wait_for('message', check=check, timeout=10.0)
        except asyncio.TimeoutError:
            return await message.channel.send('Sorry, you took too long')

        if int(guess.content) == answer:
            await message.channel.send('You are right!')
        else:
            await message.channel.send('Oops. That is not right')

        
# Bot Token
client.run('OTQzODU5MDYzNjcyOTQ2NzM5.Yg5LQA.w-3Xy4FoJNhhl4O5slbG9NeHOiY')
