import requests
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from HotspotRobot import pbot


@pbot.on_message(filters.command("imdb"))
async def imdb(client, message):
    if len(message.command) < 2:
        return await message.reply_text("» ɢɪᴠᴇ ᴍᴇ ꜱᴏᴍᴇ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ.\n   ᴇx. /imdb Avengers")
    text = (
        message.text.split(None, 1)[1]
        if len(message.command) < 3
        else message.text.split(None, 1)[1].replace(" ", "%20")
    )
    url = requests.get(f"https://api.safone.tech/tmdb?query={text}").json()["results"][
        0
    ]
    poster = url["poster"]
    imdb_link = url["imdbLink"]
    title = url["title"]
    rating = url["rating"]
    releasedate = url["releaseDate"]
    description = url["overview"]
    popularity = url["popularity"]
    runtime = url["runtime"]
    status = url["status"]
    await client.send_photo(
        message.chat.id,
        poster,
        caption=f"""**» IMDB Movie Details:**

‣ **Title** = `{title}`
‣ **Description** = `{description}`
‣ **Rating** = `{rating}`
‣ **Release-Date** = `{releasedate}`
‣ **Popularity** = `{popularity}`
‣ **Runtime** = `{runtime}`
‣ **Status** = `{status}`
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="• ɪᴍᴅʙ ʟɪɴᴋ •",
                        url=imdb_link,
                    ),
                ],
            ],
        ),
    )


__help__ = """
  ➲ /imdb <ᴍᴏᴠɪᴇ ɴᴀᴍᴇ>: ɢᴇᴛ ꜰᴜʟʟ ɪɴꜰᴏ ᴀʙᴏᴜᴛ ᴀ ᴍᴏᴠɪᴇ ꜰʀᴏᴍ [imdb.com](https://m.imdb.com)
"""
__mod_name__ = "Iᴍᴅʙ"