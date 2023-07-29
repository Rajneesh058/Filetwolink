#Adarsh goel
from Adarsh.bot import StreamBot
from Adarsh.vars import Var
import logging
logger = logging.getLogger(__name__)
from Adarsh.bot.plugins.stream import MY_PASS
from Adarsh.utils.human_readable import humanbytes
from Adarsh.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from Adarsh.utils.file_properties import get_name, get_hash, get_media_file_size
db = Database(Var.DATABASE_URL, Var.name)
from pyrogram.types import ReplyKeyboardMarkup

START_TEXT = """
<i>👋 Hᴇʏ,</i>{}\n
<i>I'ᴍ Tᴇʟᴇɢʀᴀᴍ Fɪʟᴇs Sᴛʀᴇᴀᴍɪɴɢ Bᴏᴛ ᴀs ᴡᴇʟʟ Dɪʀᴇᴄᴛ Lɪɴᴋs Gᴇɴᴇʀᴀᴛᴇ</i>\n
<i>Cʟɪᴄᴋ ᴏɴ Hᴇʟᴘ ᴛᴏ ɢᴇᴛ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ</i>\n
<i><u>𝗪𝗔𝗥𝗡𝗜𝗡𝗚 🚸</u></i>
<b>🔞 Pʀᴏɴ ᴄᴏɴᴛᴇɴᴛꜱ ʟᴇᴀᴅꜱ ᴛᴏ ᴘᴇʀᴍᴀɴᴇɴᴛ ʙᴀɴ ʏᴏᴜ.</b>\n\n
<i><b>🍃 Bᴏᴛ Mᴀɪɴᴛᴀɪɴᴇᴅ Bʏ :</b>@Epic_creation_bots</i>"""

HELP_TEXT = """
<i>- Sᴇɴᴅ ᴍᴇ ᴀɴʏ ꜰɪʟᴇ (ᴏʀ) ᴍᴇᴅɪᴀ ꜰʀᴏᴍ ᴛᴇʟᴇɢʀᴀᴍ.</i>
<i>- I ᴡɪʟʟ ᴘʀᴏᴠɪᴅᴇ ᴇxᴛᴇʀɴᴀʟ ᴅɪʀᴇᴄᴛ ᴅᴏᴡɴʟᴏᴀᴅ/Stream ʟɪɴᴋ !.</i>
<i>- Aᴅᴅ Mᴇ ɪɴ ʏᴏᴜʀ Cʜᴀɴɴᴇʟ Fᴏʀ Dɪʀᴇᴄᴛ Dᴏᴡɴʟᴏᴀᴅ Lɪɴᴋs Bᴜᴛᴛᴏɴ</i>
<i>- Tʜɪs Pᴇʀᴍᴇᴀɴᴛ Lɪɴᴋ Wɪᴛʜ Fᴀsᴛᴇsᴛ Sᴘᴇᴇᴅ</i>\n
<u>🔸 𝗪𝗔𝗥𝗡𝗜𝗡𝗚 🚸</u>\n
<b>🔞 Pʀᴏɴ ᴄᴏɴᴛᴇɴᴛꜱ ʟᴇᴀᴅꜱ ᴛᴏ ᴘᴇʀᴍᴀɴᴇɴᴛ ʙᴀɴ ʏᴏᴜ.</b>\n
<i>Cᴏɴᴛᴀᴄᴛ ᴅᴇᴠᴇʟᴏᴘᴇʀ (ᴏʀ) ʀᴇᴘᴏʀᴛ ʙᴜɢꜱ</i> <b>: <a href='https://t.me/Rajneesh_Singh_Tomar'>[ ᴄʟɪᴄᴋ ʜᴇʀᴇ ]</a></b>"""

ABOUT_TEXT = """
<b>⚜ Mʏ ɴᴀᴍᴇ : FileStreamX</b>\n
<b>🔸Vᴇʀꜱɪᴏɴ : <a href='https://t.me/direct_link_generator'>3.0.1</a></b>\n
<b>🔹Sᴏᴜʀᴄᴇ : <a href='https://github.com/Moviesindna/FileStreamBot?organization=Moviesindna&organization=Moviesindna'>Cʟɪᴄᴋ Hᴇʀᴇ</a></b>\n
<b>🔸GitHub : <a href='https://GitHub.com/avipatilpro'>Fᴏʟʟᴏᴡ</a></b>\n
<b>🔹Dᴇᴠᴇʟᴏᴘᴇʀ : <a href='https://telegram.me/Rajneesh_Singh_Tomar'>Rajneesh_Singh_Tomar</a></b>\n
<b>🔸Lᴀꜱᴛ ᴜᴘᴅᴀᴛᴇᴅ : <a href='https://t.me/direct_link_generator'>[ 26-oct-22 ] 03:55 PM</a></b>"""
                      
@StreamBot.on_message(filters.command('start') & filters.private)
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{m.from_user.first_name}](tg://user?id={m.from_user.id}) Started !!"
        )
    usr_cmd = m.text.split("_")[-1]
    if usr_cmd == "/start":
        await m.reply_photo(
            photo="https://graph.org/file/8e67ae4a3803f69a28218.jpg",
            caption="**ʜᴇʟʟᴏ...⚡\n\nɪᴀᴍ ᴀ sɪᴍᴘʟᴇ ᴛᴇʟᴇɢʀᴀᴍ ғɪʟᴇ/ᴠɪᴅᴇᴏ ᴛᴏ ᴘᴇʀᴍᴀɴᴇɴᴛ ʟɪɴᴋ ᴀɴᴅ sᴛʀᴇᴀᴍ ʟɪɴᴋ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ.**\n\n**ᴜsᴇ /help ғᴏʀ ᴍᴏʀᴇ ᴅᴇᴛsɪʟs\n\nsᴇɴᴅ ᴍᴇ ᴀɴʏ ᴠɪᴅᴇᴏ / ғɪʟᴇ ᴛᴏ sᴇᴇ ᴍʏ ᴘᴏᴡᴇʀᴢ...**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("⚡ UPDATES ⚡", url="https://t.me/beta_botz"), 
                     InlineKeyboardButton("⚡ SUPPORT ⚡", url="https://t.me/beta_support")],
                    [InlineKeyboardButton("OWNER", url="https://t.me/jeol_tg"), 
                     InlineKeyboardButton("About", callback_data='about')],
                    [InlineKeyboardButton("Help", callback_data='help')]
                ]
            ),
            
        )
    else:

        get_msg = await b.get_messages(chat_id=Var.BIN_CHANNEL, ids=int(usr_cmd))

        file_size = None
        if get_msg.video:
            file_size = f"{humanbytes(get_msg.video.file_size)}"
        elif get_msg.document:
            file_size = f"{humanbytes(get_msg.document.file_size)}"
        elif get_msg.audio:
            file_size = f"{humanbytes(get_msg.audio.file_size)}"

        file_name = None
        if get_msg.video:
            file_name = f"{get_msg.video.file_name}"
        elif get_msg.document:
            file_name = f"{get_msg.document.file_name}"
        elif get_msg.audio:
            file_name = f"{get_msg.audio.file_name}"

        stream_link = "https://{}/{}".format(Var.FQDN, get_msg.id) if Var.ON_HEROKU or Var.NO_PORT else \
            "http://{}:{}/{}".format(Var.FQDN,
                                     Var.PORT,
                                     get_msg.id)

        msg_text = "**ᴛᴏᴜʀ ʟɪɴᴋ ɪs ɢᴇɴᴇʀᴀᴛᴇᴅ...⚡\n\n📧 ғɪʟᴇ ɴᴀᴍᴇ :-\n{}\n {}\n\n💌 ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ :- {}\n\n♻️ ᴛʜɪs ʟɪɴᴋ ɪs ᴘᴇʀᴍᴀɴᴇɴᴛ ᴀɴᴅ ᴡᴏɴ'ᴛ ɢᴇᴛ ᴇxᴘɪʀᴇᴅ ♻️\n\n<b>❖ YouTube.com/@itzjeol</b>**"
        await m.reply_text(            
            text=msg_text.format(file_name, file_size, stream_link),
            
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⚡ ᴅᴏᴡɴʟᴏᴀᴅ ɴᴏᴡ ⚡", url=stream_link)]])
        )


@StreamBot.on_message(filters.command('help') & filters.private)
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) Started !!"
        )
              
    await message.reply_photo(
            photo="https://graph.org/file/8e67ae4a3803f69a28218.jpg",
            caption="**┣⪼ sᴇɴᴅ ᴍᴇ ᴀɴʏ ғɪʟᴇ/ᴠɪᴅᴇᴏ ᴛʜᴇɴ ɪ ᴡɪʟʟ ʏᴏᴜ ᴘᴇʀᴍᴀɴᴇɴᴛ sʜᴀʀᴇᴀʙʟᴇ ʟɪɴᴋ ᴏғ ɪᴛ...\n\n┣⪼ ᴛʜɪs ʟɪɴᴋ ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴏʀ ᴛᴏ sᴛʀᴇᴀᴍ ᴜsɪɴɢ ᴇxᴛᴇʀɴᴀʟ ᴠɪᴅᴇᴏ ᴘʟᴀʏᴇʀs ᴛʜʀᴏᴜɢʜ ᴍʏ sᴇʀᴠᴇʀs.\n\n┣⪼ ғᴏʀ sᴛʀᴇᴀᴍɪɴɢ ᴊᴜsᴛ ᴄᴏᴘʏ ᴛʜᴇ ʟɪɴᴋ ᴀɴᴅ ᴘᴀsᴛᴇ ɪᴛ ɪɴ ʏᴏᴜʀ ᴠɪᴅᴇᴏ ᴘʟᴀʏᴇʀ ᴛᴏ sᴛᴀʀᴛ sᴛʀᴇᴀᴍɪɴɢ.\n\n┣⪼ ᴛʜɪs ʙᴏᴛ ɪs ᴀʟsᴏ sᴜᴘᴘᴏʀᴛ ɪɴ ᴄʜᴀɴɴᴇʟ. ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴀs ᴀᴅᴍɪɴ ᴛᴏ ɢᴇᴛ ʀᴇᴀʟᴛɪᴍᴇ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ ғᴏʀ ᴇᴠᴇʀʏ ғɪʟᴇs/ᴠɪᴅᴇᴏs ᴘᴏsʏ../\n\n┣⪼ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ :- /about\n\n\nᴘʟᴇᴀsᴇ sʜᴀʀᴇ ᴀɴᴅ sᴜʙsᴄʀɪʙᴇ**", 
  
        
        reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("⚡ UPDATES ⚡", url="https://t.me/beta_botz"), 
                     InlineKeyboardButton("⚡ SUPPORT ⚡", url="https://t.me/beta_support")],
                    [InlineKeyboardButton("OWNER", url="https://t.me/jeol_tg"), 
                     InlineKeyboardButton("About", callback_data='about')],
                    [InlineKeyboardButton("Help", callback_data='help')]
                ]
            ),
            
        )

@StreamBot.on_message(filters.command('about') & filters.private)
async def about_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) Started !!"
        )
    await message.reply_photo(
            photo="https://graph.org/file/8e67ae4a3803f69a28218.jpg",
            caption="""<b>sᴏᴍᴇ ʜɪᴅᴅᴇɴ ᴅᴇᴛᴀɪʟs😜</b>

<b>╭━━━━━━━〔ғɪʟᴇ ᴛᴏ ʟɪɴᴋ ʙᴏᴛ〕</b>
┃
┣⪼<b>ʙᴏᴛ ɴᴀᴍᴇ : ғɪʟᴇ ᴛᴏ ʟɪɴᴋ
┣⪼<b>ᴜᴘᴅᴀᴛᴇᴢ : <a href='https://t.me/beta_botz'>jeol botz</a></b>
┣⪼<b>sᴜᴘᴘᴏʀᴛ : <a href='https://t.me/beta_support'>jeol support</a></b>
┣⪼<b>sᴇʀᴠᴇʀ : ʜᴇʀᴜᴋᴏ</b>
┣⪼<b>ʟɪʙʀᴀʀʏ : ᴘʏʀᴏɢʀᴀᴍ</b>
┣⪼<b>ʟᴀɴɢᴜᴀɢᴇ: ᴘʏᴛʜᴏɴ 3</b>
┣⪼<b>ʏᴏᴜᴛᴜʙᴇ : <a href='https://youtube.com/@itzjeol'>Jeol botz</a></b>
┃
<b>╰━━━━━━━〔ᴘʟᴇᴀsʀ sᴜᴘᴘᴏʀᴛ〕</b>""",
  
        
        reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("⚡ UPDATES ⚡", url="https://t.me/beta_botz"), InlineKeyboardButton("⚡ SUPPORT ⚡", url="https://t.me/beta_support")],
                    [InlineKeyboardButton("OWNER", url="https://t.me/jeol_tg"), InlineKeyboardButton("💠 DEVELOPER", url="https://github.com/Adarsh-Goel")],
                    [InlineKeyboardButton("💌 SUBSCRIBE 💌", url="https://youtube.com/@itzjeol")]
                ]
            ),
            
        )

START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Hᴇʟᴘ', callback_data='help'),
        InlineKeyboardButton('Aʙᴏᴜᴛ', callback_data='about'),
        InlineKeyboardButton('Cʟᴏsᴇ', callback_data='close')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Hᴏᴍᴇ', callback_data='home'),
        InlineKeyboardButton('Aʙᴏᴜᴛ', callback_data='about'),
        InlineKeyboardButton('Cʟᴏsᴇ', callback_data='close')
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Hᴏᴍᴇ', callback_data='home'),
        InlineKeyboardButton('Hᴇʟᴘ', callback_data='help'),
        InlineKeyboardButton('Cʟᴏsᴇ', callback_data='close')
        ]]
      )

@StreamBot.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=ABOUT_BUTTONS
        )
    else:
        await update.message.delete()

def get_media_file_size(m):
    media = m.video or m.audio or m.document
    if media and media.file_size:
        return media.file_size
    else:
        return None


def get_media_file_name(m):
    media = m.video or m.document or m.audio
    if media and media.file_name:
        return urllib.parse.quote_plus(media.file_name)
    else:
        return None
