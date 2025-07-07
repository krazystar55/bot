from telegram.ext import ApplicationBuilder, CommandHandler
from config import 7835794353:AAEvGDPagNHEbc1rk59_92OuyNLUjwLgDUI
from modules.scan_osint import scan
from modules.reverse import reverse

app = ApplicationBuilder().token(7835794353:AAEvGDPagNHEbc1rk59_92OuyNLUjwLgDUI).build()

app.add_handler(CommandHandler("start", lambda u, c: u.message.reply_text(
    "🕵️ OSINT Bot Ready.\nCommands:\n/scan <email|user|number>\n/reverse <binary_path>"
)))
app.add_handler(CommandHandler("scan", scan))
app.add_handler(CommandHandler("reverse", reverse))

print("🤖 SecureIndia OSINT Bot [LEVEL 1] Running...")
app.run_polling()
