import discord
import giphypop
import requests

nigger = [
    'https://media.giphy.com/media/l0ExcmTLOCZyecYaA/giphy.gif',
    'https://media.giphy.com/media/26gsjUq73y6M2VTSU/giphy.gif',
    'https://media.giphy.com/media/l0Ex8HiCGD8BnsVvG/giphy.gif',
    'https://media.giphy.com/media/26xBJJEETvqGHxVIc/giphy.gif',
    'https://media.giphy.com/media/l0Ex9w7OHj6M3ieK4/giphy.gif',
]

btc_message = ('The current price of Bitcoin in USD is $')
client = discord.Client()
g = giphypop.Giphy('FvsIzLSKfDRhFwANJVYzMKiEAl8Ss7uL')

helpdoc = [
    'These are the hot commands for ur memes',

    '```!rapeme will get you raped```',

    '```!erection will give you some hot and steamy stuff```',

    '```!cat will give u some adorable pussy```',

    '```!doge will give u them puppers',

    '```!BTC will give u the price of that good good crypto```',

    '```!nigga will give u that good good```',

]


@client.event
async def on_message(message):
    msg = 'Congratulations, i am raping you now your my little anal slut! {0.author.mention}'.format(message)

    if message.author == client.user:
        return

    if message.content.startswith('!doge'):

        await client.send_message(message.channel, g.screensaver('doge'))
    if message.content.startswith('!cat'):

        await client.send_message(message.channel, g.screensaver('cat'))
    if message.content.startswith('!erection'):

        await client.send_message(message.channel, g.screensaver('pron'))

    if message.content.startswith('!BTC'):

        await client.send_message(message.channel, (btc_message + (
        requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()['bpi']['USD']['rate'])))

    if message.content.startswith('!nigga'):

        await  client.send_message(message.channel, nigger)

    if message.content.startswith('!rapeme'):

        await client.send_message(message.channel, msg)

    if message.content.startswith('!helpme'):

        await  client.send_message(message.channel, helpdoc)



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run('NDY1MDM1ODk1MjEzNjU0MDI3.DiQsQQ.gH0zJBfbmzO920ibpfoWi1R9phE')


