import hikari
import lightbulb

import extensions

with open("token.txt") as f:
    _token = f.read().strip()

bot = hikari.GatewayBot(_token)
client = lightbulb.client_from_app(bot)

bot.subscribe(hikari.StartingEvent, client.start)


@bot.listen(hikari.StartingEvent)
async def on_starting(_: hikari.StartingEvent) -> None:
    await client.load_extensions_from_package(extensions)


bot.run()
