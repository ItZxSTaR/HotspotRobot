import os
import subprocess
import sys

from contextlib import suppress
from time import sleep

from telegram import TelegramError, Update
from telegram.error import Unauthorized
from telegram.ext import CallbackContext, CommandHandler, run_async

from HotspotRobot import dispatcher, OWNER_ID, ALLOW_CHATS
from  HotspotRobot.modules.sql import users_sql
from HotspotRobot.modules.helper_funcs.chat_status import dev_plus


@run_async
@dev_plus
def allow_groups(update: Update, context: CallbackContext):
    args = context.args
    if not args:
        update.effective_message.reply_text(f"Current state: {ALLOW_CHATS}")
        return
    if args[0].lower() in ["off", "no"]:
        ALLOW_CHATS = True
    elif args[0].lower() in ["yes", "on"]:
        ALLOW_CHATS = False
    else:
        update.effective_message.reply_text("Format: /lockdown Yes/No or Off/On")
        return
    update.effective_message.reply_text("Done! Lockdown value toggled.")


@run_async
def leave(update: Update, context: CallbackContext):
    bot = context.bot
    user_id = update.effective_user.id
    args = context.args
    if user_id == OWNER_ID:
        if args:
            chat_id = str(args[0])
            try:
                bot.leave_chat(int(chat_id))
                users_sql.rem_chat(chat_id)
            except TelegramError:
                update.effective_message.reply_text("I could not leave that group.")
                return
            with suppress(Unauthorized):
                update.effective_message.reply_text("» ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ʟᴇꜰᴛᴇᴅ ᴛʜᴀᴛ ᴄʜᴀᴛ.")
        else:
            update.effective_message.reply_text("Send a valid Chat ID")


@run_async
@dev_plus
def gitpull(update: Update, context: CallbackContext):
    sent_msg = update.effective_message.reply_text(
        "Pulling all changes from remote and then attempting to restart."
    )
    subprocess.Popen("git pull", stdout=subprocess.PIPE, shell=True)

    sent_msg_text = sent_msg.text + "\n\nChanges pulled...I guess.. Restarting in "

    for i in reversed(range(5)):
        sent_msg.edit_text(sent_msg_text + str(i + 1))
        sleep(1)

    sent_msg.edit_text("» ʀᴇꜱᴛᴀʀᴛᴇᴅ.")

    os.system("restart.bat")
    os.execv("start.bat", sys.argv)


@run_async
@dev_plus
def reboot(update: Update, context: CallbackContext):
    update.effective_message.reply_text("Starting a new instance and shutting down this one")

    os.system("restart.bat")
    os.execv("start.bat", sys.argv)


LEAVE_HANDLER = CommandHandler("leave", leave)
GITPULL_HANDLER = CommandHandler("gitpull", gitpull)
REBOOT_HANDLER = CommandHandler("reboot", reboot)
ALLOWGROUPS_HANDLER = CommandHandler("lockdown", allow_groups)

dispatcher.add_handler(ALLOWGROUPS_HANDLER)
dispatcher.add_handler(LEAVE_HANDLER)
dispatcher.add_handler(GITPULL_HANDLER)
dispatcher.add_handler(REBOOT_HANDLER)

__mod_name__ = "Dev"
__handlers__ = [LEAVE_HANDLER, GITPULL_HANDLER, REBOOT_HANDLER, ALLOWGROUPS_HANDLER]
