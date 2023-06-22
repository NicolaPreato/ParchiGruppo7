from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
# import sqlite3
from math import radians, cos, sin, asin, sqrt

italiano = "Italiano  🇮🇹"
fontanella_vicina_it = "Indicazioni per la fontanella più vicina  ➤"
fontanelle_Verona_it = "Mappa delle fontanelle di Verona  🗺"
cambia_lingua_it="Cambia lingua / Change language\n⇦ 🇮🇹 / 🇬🇧 / 🇺🇸"
tutorial_it="Come inviare la posizione 🔧"
indietro_it="Torna indietro ⇦"
tutorial_ios_it=" iOS "
tutorial_android_it="🤖  Android  🤖"
tutorial_indietro_it="Torna indietro  ⇦"
quiz_it="Quiz 📝"

with open("token.txt", "r") as f:
    TOKEN = f.read()
    print("Il tuo token è ", TOKEN)


"""
async def startCommand(update: Update, context: CallbackContext) -> None:
    diz(update, context)
    aggiungi_dizionario(update, context, dizionario)
    buttons = [[KeyboardButton(italiano)]]
    testo = "Benvenuto nel nostro bot\nScegli la lingua 🇮🇹"
    context.bot.send_message(chat_id=update.effective_chat.id, text=testo, reply_markup=ReplyKeyboardMarkup(buttons))
    testo = "Welcome to our bot\nChose the language 🇬🇧 / 🇺🇸"
    context.bot.send_message(chat_id=update.effective_chat.id, text=testo, reply_markup=ReplyKeyboardMarkup(buttons))
"""
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when /hello is issued."""
    await update.message.reply_text("Benvenuto nel Servizio di ricerca dei parchi e giardini di Verona\nPer scegliere i filtri di riceca digita /Filtri")


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when /hello is issued."""
    await update.message.reply_text("Hello!")


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")

def main() -> None:
    #echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("hello", hello))
    app.add_handler(CommandHandler('help', help))
    app.run_polling()

if __name__=='__main__':
   main()


