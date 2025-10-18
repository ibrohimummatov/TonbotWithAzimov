UMMATOV🎧 )), [18/10/2025 15:10]
import os
import logging
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Web App URL - GitHub Pages yoki Netlify manzili
WEB_APP_URL = "https://sizning-web-app-manzilingiz.uz"

users_db = {}

class User:
    def init(self, user_id):
        self.user_id = user_id
        self.balance = 1146.33
        self.daily_rate = 1.1
        self.respect = 7
        self.referrals = []
        self.completed_tasks = []

def get_user(user_id):
    if user_id not in users_db:
        users_db[user_id] = User(user_id)
    return users_db[user_id]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = get_user(update.effective_user.id)
    
    # Asosiy menyu - sizning skrinshotdagi tartibda
    keyboard = [
        [InlineKeyboardButton("🎯 Vazifalar", callback_data="tasks")],
        [InlineKeyboardButton("👥 Do'stlar", callback_data="friends")], 
        [InlineKeyboardButton("🏆 Reyting", callback_data="top")],
        [InlineKeyboardButton("🆘 Yordam", callback_data="support")],
        [InlineKeyboardButton("🚀 Web App da ochish", web_app=WebAppInfo(url=WEB_APP_URL))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    message = (
        f"💎 *{user.balance:.2f} SO'M*\n\n"
        f"Balans o'sishi\n"
        f"+{user.daily_rate}% kuniga\n\n"
        f"📈 Sizning kunlik daromadingiz:\n"
        f"0.0001261 SO'M\n"
        f"{'─' * 30}\n"
    )
    
    await update.message.reply_text(
        message,
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def show_tasks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    user = get_user(query.from_user.id)
    
    # Sizning skrinshotdagi vazifalar
    tasks_text = (
        "🎯 *Vazifalar*\n\n"
        "⚠️ *Ogohlantirish: Kanallardan chiqib ketish uchun jarima 0.02 SO'M*\n\n"
        "🔹 *Kanalga obuna bo'lish*\n"
        "+0.010 SO'M\n"
        "✅ Obuna bo'lish   Tekshirish\n\n"
        "🔹 *Botni ishga tushirish*\n"  
        "+0.010 SO'M\n"
        "🚀 O'tish   Tekshirish\n\n"
        "🔹 *Botni ishga tushirish*\n"
        "+0.010 SO'M\n"
        "🚀 O'tish   Tekshirish\n\n"
        "🔹 *Kanalga obuna bo'lish*\n"
        "+0.001 SO'M\n"
        "✅ Obuna bo'lish   Tekshirish\n"
    )
    
    keyboard = [
        [InlineKeyboardButton("🔙 Asosiy menyu", callback_data="main_menu")],
        [InlineKeyboardButton("🚀 Web App da ochish", web_app=WebAppInfo(url=f"{WEB_APP_URL}/index.html"))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(tasks_text, reply_markup=reply_markup, parse_mode='Markdown')

async def show_friends(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    user = get_user(query.from_user.id)
    
    friends_text = (
        "👥 *Mening do'stlarim*\n\n"
        "+0.1% stavkaga har bir do'st\n"
        "Maksimum 2%\n\n"
        "20% daromaddan har bir do'st\n"
        "Doimiy\n\n"
        f"{'─' * 30}\n"
        "💫 Do'stlardan daromad har kuni\n\n"
        "20% barcha do'stlarning kunlik daromadidan\n\n"
        "Sizda hali referallar yo'q\n"
        f"{'─' * 30}\n"
    )
    
    keyboard = [
        [InlineKeyboardButton("📌 Mening referal havolam", callback_data="referral_link")],
        [InlineKeyboardButton("📎 Havolani ulashish", callback_data="share_link")],
        [InlineKeyboardButton("🎁 Bonus kodi", callback_data="bonus_code")],
        [InlineKeyboardButton("💎 PROMOKOD KIRITING", callback_data="enter_promo")],

UMMATOV🎧 )), [18/10/2025 15:10]
[InlineKeyboardButton("👍 Bizning Telegram kanal", callback_data="our_channel")],
        [InlineKeyboardButton("🔍 TONBANK", callback_data="tonbank_channel")],
        [InlineKeyboardButton("🔄 Respectlarni SO'M ga almashtirish", callback_data="swap")],
        [InlineKeyboardButton("🔙 Asosiy menyu", callback_data="main_menu")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(friends_text, reply_markup=reply_markup, parse_mode='Markdown')

async def show_swap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    user = get_user(query.from_user.id)
    
    swap_text = (
        "🔄 *Respectlarni SO'M ga almashtirish*\n\n"
        "*Almashinish kursi*\n"
        "1 respect = 0.001 SO'M\n\n"
        "0\n"
        "7\n" 
        "0.000 SO'M\n\n"
        "🔄 Hammasini almashtirish\n"
        f"{'─' * 30}\n"
        "🎯 Vazifalar    👥 Do'stlar    🏆 Reyting    🆘 Yordam"
    )
    
    keyboard = [
        [InlineKeyboardButton("🔄 Hammasini almashtirish", callback_data="swap_all")],
        [InlineKeyboardButton("❓ Respect qanday olish kerak", callback_data="how_to_get")],
        [InlineKeyboardButton("🔙 Asosiy menyu", callback_data="main_menu")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(swap_text, reply_markup=reply_markup, parse_mode='Markdown')

async def show_support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    support_text = (
        "💬 *Qo'llab-quvvatlash chati*\n\n"
        "*Yordam*\n"
        "Muammoingizni iloji boricha aniqroq tasvirlab bering va mutaxassis javobini kuting.\n\n"
        "🕐 Hozirgina"
    )
    
    keyboard = [[InlineKeyboardButton("🔙 Asosiy menyu", callback_data="main_menu")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(support_text, reply_markup=reply_markup, parse_mode='Markdown')

async def show_top(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    top_text = (
        "🏆 *Reyting*\n\n"
        "1. 👤 User1 - 2500.50 SO'M\n"
        "2. 👤 User2 - 1800.25 SO'M\n" 
        "3. 👤 User3 - 1500.75 SO'M\n"
        "4. 👤 Siz - 1146.33 SO'M\n"
        "5. 👤 User4 - 800.30 SO'M\n"
    )
    
    keyboard = [[InlineKeyboardButton("🔙 Asosiy menyu", callback_data="main_menu")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(top_text, reply_markup=reply_markup, parse_mode='Markdown')

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user = get_user(query.from_user.id)
    
    if query.data == "main_menu":
        await start(update, context)
    elif query.data == "tasks":
        await show_tasks(update, context)
    elif query.data == "friends":
        await show_friends(update, context)
    elif query.data == "swap":
        await show_swap(update, context)
    elif query.data == "top":
        await show_top(update, context)
    elif query.data == "support":
        await show_support(update, context)
    elif query.data == "swap_all":
        await query.answer("✅ 0.007 SO'M qo'shildi!")
    elif query.data == "referral_link":
        await query.answer("📎 https://t.me/my_tonbank_bot/app?startapp=03")
    elif query.data in ["bonus_code", "enter_promo", "our_channel", "tonbank_channel"]:
        await query.answer("🚀 Tez orada ishga tushadi!")

def main():
    BOT_TOKEN = "8304176773:AAFBMeUV2KWYJvrD0_ekO0P1Ek-nvG98Ko0"
    
    application = Application.builder().token(BOT_TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))
    
    print("Bot ishga tushdi...")
    application.run_polling()

if name == "main":
    main()
