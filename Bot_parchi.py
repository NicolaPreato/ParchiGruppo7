from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import sqlite3
from math import radians, cos, sin, asin, sqrt

conn = sqlite3.connect("./Parchi.db")
print("Opened database successfully");
"""
def Parchi_valeggio(): 
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM [Parchi e giardini_Valeggio]')
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as sqlerror:
        print("Error while connecting to sqlite", sqlerror)
"""
def execute_query(query):
    conn = sqlite3.connect("Parchi.db")
    cursor = conn.execute(query)
    results = cursor.fetchall
    conn.close()
    return results

def format_results(results):
    formatted = ''
    for row in results(results):
        formatted += "Nomeidentificativo: {}, Indirizzo: {}, Mq: {}, Attrezzato: {}, Note: {}, Parcogiochi: {}, Campisportivi: {}, Zoneriposo: {}\n" .format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
    return formatted

def printparco(update,context):
    query= "SELECT * FROM [Parchi e girdini_Sona]"
    results = execute_query(query)
    formatted_results = format_results(results)
    response = "Elenco parchi Sona:\n" + formatted_results
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)

with open("token.txt", "r") as f:
    TOKEN = f.read()
    print("Il tuo token è ", TOKEN)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when /hello is issued."""
    await update.message.reply_text("Benvenuti nel servizio di ricerca parchi Verona\nPer scegliere la località digitare /localita")

async def localita(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when /hello is issued."""
    await update.message.reply_text("Scegli tra queste località:\n/Valeggio\n/Sommacampagna\n/Sona\n/Palazzolo_di_sona\n/Lugangano_di_sona\n/San_giorgio_in_salici\n/Pescantina\n/Mozzecane\n/Pastrengo\n/Villafranca\n/Castelnuovo")
    

async def Valeggio(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when /hello is issued."""
    await update.message.reply_text("PARCO ICHENHAUSEN\nFANTE\nCOMBONI\nFASCINELLI\nDELLA RIMEMBRANZA\nVERDE PALAZZETTO\nBELLUNO\nBRENTA\nTAGLIAMENTO\nMAZZINI\nRICCI\nPOETI\nTRIESTE\nPONTIERI\nFALCONE\nFINCATO\nFALLACI\nFANTE\nPARTIGIANI\nBERSAGLIERE\nSAN PIETRO\nVERONA\nVENEZIA\nISONZO\nICHENHAUSEN\nFINCATO\nSCUOLA DELL'INFANZIA IL MELOGRANO\nPO\nMORO\n\nMATTEOTTI\nBORSELLINO\nFANTE\nSCUOLA PRIMARIA CARLO COLLODI\nGIARDINI DI BORGHETTO\nPUNTA BORGHETTO\nSANZIO\nSCUOLA DELLINFANZIA CA PRATO\nMONTE COCOLO\nNIKOLAJEWKA\nTEODORICO\nATTILA\nUNNi\nALPI\nBENACO\nPASTRENGO\nTEODORICO\nPACINOTTI\nARMONIA\nCONCORDIA\nFERMI\nIMPRENDITORI\nPIGOZZI\nASILO NIDO GLI GNOMI")

async def Sommacampagna(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when /hello is issued."""
    await update.message.reply_text("Parco pubblico Villa Venier\nParco Baleno\nParco della Bissara\nParco Caprioli\nParco Giochi Monte Molin
Giardini di Piazza della Repubblica
Parco pubblico")

async def Sona(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when /hello is issued."""
    await update.message.reply_text("Hello!")

async def Palazzolo_di_sona(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when /hello is issued."""
    await update.message.reply_text("Hello!")

async def Lugagnano_di_sona(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when /hello is issued."""
    await update.message.reply_text("Hello!")

async def San_giorgio_in_salici(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when /hello is issued."""
    await update.message.reply_text("Hello!")

async def Pescantina(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when /hello is issued."""
    await update.message.reply_text("Hello!")

async def Mozzecane(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when /hello is issued."""
    await update.message.reply_text("Hello!")
   
async def Pastrengo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when /hello is issued."""
    await update.message.reply_text("Hello!")

async def Villafranca(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when /hello is issued."""
    await update.message.reply_text("Hello!")

async def Castelnuovo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when /hello is issued."""
    await update.message.reply_text("Hello!")


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")

def main() -> None:
    #echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("localita", localita))
    app.add_handler(CommandHandler("Valeggio", Valeggio))
    app.add_handler(CommandHandler("Sommacampagna", Sommacampagna))
    app.add_handler(CommandHandler("Sona", Sona))
    app.add_handler(CommandHandler("Palazzolo_di_sona", Palazzolo_di_sona))
    app.add_handler(CommandHandler("Lugagnano_di_sona", Lugagnano_di_sona))
    app.add_handler(CommandHandler("San_giorgio_in_salici", San_giorgio_in_salici))
    app.add_handler(CommandHandler("Pescantina", Pescantina))
    app.add_handler(CommandHandler("Mozzecane", Mozzecane))
    app.add_handler(CommandHandler("Pastengo", Pastrengo))
    app.add_handler(CommandHandler("Villafranca", Villafranca))
    app.add_handler(CommandHandler("Castelnuovo", Castelnuovo))
    app.run_polling()

if __name__=='__main__':
   main()


