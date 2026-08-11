from flask import Flask
import threading

app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = threading.Thread(target=run)
    t.start()

keep_alive()
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
)

# Aapka Bot Token
BOT_TOKEN = "8732124533:AAEF5gJnNNo_eGIiP05YPhdNHraZrepZ5lQ"


# 1. /start Command - Main Menu
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
  keyboard = [
      [InlineKeyboardButton("🛒 Shop", callback_data="shop")],
      [
          InlineKeyboardButton("💰 Add Balance", callback_data="add_balance"),
          InlineKeyboardButton("📦 My Orders", callback_data="orders"),
      ],
      [
          InlineKeyboardButton("👤 Profile", callback_data="profile"),
          InlineKeyboardButton("🎁 Referral", callback_data="referral"),
      ],
      [
          InlineKeyboardButton("🔴 How To", callback_data="howto"),
          InlineKeyboardButton("🍀 Lucky", callback_data="lucky"),
      ],
      [
          InlineKeyboardButton("💶 Share", callback_data="share"),
          InlineKeyboardButton("💬 Support", callback_data="support"),
      ],
  ]
  reply_markup = InlineKeyboardMarkup(keyboard)

  welcome_text = (
      "🏪 **— GODCHEATS STORE —** 🏪\n\n"
      "🤖 *Hello, God!*\n\n"
      "🔑 Premium digital keys, instant delivery.\n\n"
      "— 🛒 Wide product catalog\n"
      "— ⚡ Instant key delivery\n"
      "— 💳 Multiple payment gateways\n"
      "— 📤 Referrals & spin-to-win\n"
      "— 🔒 24/7 admin support\n\n"
      "_Tap any button below to begin._"
  )

  if update.message:
    await update.message.reply_text(
        welcome_text, reply_markup=reply_markup, parse_mode="Markdown"
    )
  elif update.callback_query:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        welcome_text, reply_markup=reply_markup, parse_mode="Markdown"
    )


# 2. Shop Menu - Product Catalog
async def shop_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
  query = update.callback_query
  await query.answer()

  keyboard = [
      [InlineKeyboardButton("🔑 SILENT-CHEATS LITE", callback_data="item_21")],
[InlineKeyboardButton("🔑 SILENT-CHEATS BRUTAL", callback_data="item_22")],
[InlineKeyboardButton("🔑 SILENT-CHEATS APK MOD", callback_data="item_23")],
[InlineKeyboardButton("🔑 Rapid Core - Root Safe", callback_data="item_24")],
[InlineKeyboardButton("🔑 PRIME APKMOD", callback_data="item_25")],
[InlineKeyboardButton("🔑 PATOTEAM APKMOD", callback_data="item_26")],
[InlineKeyboardButton("🔑 IOS-MIGUL PRO", callback_data="item_27")],
[InlineKeyboardButton("🔑 Haxx Cker Pro", callback_data="item_28")],
[InlineKeyboardButton("🔑 HG CHEAT APKMOD", callback_data="item_29")],

      [InlineKeyboardButton("🔑 Drip Client - Non Root", callback_data="item_1")],
      [InlineKeyboardButton("🔑 Drip Client - Root", callback_data="item_2")],
      [InlineKeyboardButton("🔑 Fluorite FF iOS", callback_data="item_3")],
      [
          InlineKeyboardButton(
              "🔑 [ iOS ] Gbox Esign Certificate", callback_data="item_4"
          )
      ],
      [
          InlineKeyboardButton(
              "🔑 Hg ApkMod - Non Root + Root", callback_data="item_5"
          )
      ],
      [InlineKeyboardButton("🔑 Pato Blue Non Root", callback_data="item_6")],
      [InlineKeyboardButton("🔑 Pato Green Non Root", callback_data="item_7")],
      [InlineKeyboardButton("🔑 Pato Orange Non Root", callback_data="item_8")],
      [InlineKeyboardButton("🔑 Br Mode - Root", callback_data="item_9")],
      [
          InlineKeyboardButton(
              "🔑 Br Mode Silent Aim - PC", callback_data="item_10"
          )
      ],
      [
          InlineKeyboardButton(
              "🔑 [ iOS ] Gbox Official Certificate", callback_data="item_11"
          )
      ],
      [InlineKeyboardButton("🔑 Reaper X Pro - Root", callback_data="item_12")],
      [
          InlineKeyboardButton(
              "🔑 Reaper X Pro - Non Root", callback_data="item_13"
          )
      ],
      [
          InlineKeyboardButton(
              "✅ Prime Hook - Non Root", callback_data="item_14"
          )
      ],
      [InlineKeyboardButton("🔑 Alpha Regedit iOS", callback_data="item_15")],
      [InlineKeyboardButton("🔑 HAXXCKER PRO", callback_data="item_16")],
      [
          InlineKeyboardButton(
              "🔑 Haxx Cker Pro ApkMod [Non Root]", callback_data="item_17"
          )
      ],
      [
          InlineKeyboardButton(
              "🔑 70% Drag HS + Hologram [Non Root]", callback_data="item_18"
          )
      ],
      [
          InlineKeyboardButton(
              "✅ Haxx Cker Pro + Pc Logo Bypass", callback_data="item_19"
          )
      ],
      [
          InlineKeyboardButton(
              "🔑 Ghost Elite Steamer", callback_data="item_20"
          )
      ],
      [InlineKeyboardButton("🔙 Back to Main Menu", callback_data="main_menu")],
  ]
  reply_markup = InlineKeyboardMarkup(keyboard)

  await query.edit_message_text(
      "🛍️ **Pick a product from the catalog below:**",
      reply_markup=reply_markup,
      parse_mode="Markdown",
  )


# 3. Handle All Button Features & Actions
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
  query = update.callback_query
  data = query.data

  if data == "shop":
    await shop_menu(update, context)

  elif data == "main_menu":
    await start(update, context)

  elif data == "add_balance":
    await query.answer()
    await query.edit_message_text(
        "💰 **Add Balance:**\n\nTo top up your wallet, send payment to the"
        " admin or use UPI/Crypto gateway.\n\n📱 Send payment proof to Admin:"
        " `@godcheats`",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Back to Menu", callback_data="main_menu")]]
        ),
        parse_mode="Markdown",
    )

  elif data == "orders":
    await query.answer()
    await query.edit_message_text(
        "📦 **My Orders:**\n\nYou currently have no active or past key orders.",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Back to Menu", callback_data="main_menu")]]
        ),
        parse_mode="Markdown",
    )

  elif data == "profile":
    await query.answer()
    user = query.from_user
    await query.edit_message_text(
        f"👤 **User Profile:**\n\n👤 Name: {user.first_name}\n🆔 User ID:"
        f" `{user.id}`\n💰 Wallet Balance: $0.00\n🛒 Total Purchases: 0",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Back to Menu", callback_data="main_menu")]]
        ),
        parse_mode="Markdown",
    )

  elif data == "referral":
    await query.answer()
    user_id = query.from_user.id
    ref_link = f"https://t.me/{context.bot.username}?start=ref_{user_id}"
    await query.edit_message_text(
        "🎁 **Referral Program:**\n\nInvite your friends and earn bonus"
        f" balance!\n\n🔗 Your Referral Link:\n`{ref_link}`\n\n👥 Total Referrals:"
        " 0",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Back to Menu", callback_data="main_menu")]]
        ),
        parse_mode="Markdown",
    )

  elif data == "howto":
    await query.answer()
    await query.edit_message_text(
        "🔴 **How To Use Bot / Tutorials:**\n\n1️⃣ Click on **Shop** and select"
        " your desired product/key.\n2️⃣ Add balance or pay directly via"
        " available options.\n3️⃣ Receive your license key instantly!\n\n📺 Watch"
        " tutorial video: https://t.me/BotKeybuytutorial/9",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Back to Menu", callback_data="main_menu")]]
        ),
        parse_mode="Markdown",
    )

  elif data == "lucky":
    await query.answer()
    await query.edit_message_text(
        "🍀 **Lucky Spin / Reward:**\n\n🎁 Try your luck today! Spin the wheel"
        " to win free keys or wallet balance.\n\n*(Feature coming soon in next"
        " update!)*",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Back to Menu", callback_data="main_menu")]]
        ),
        parse_mode="Markdown",
    )

  elif data == "share":
    await query.answer()
    await query.edit_message_text(
        "💶 **Share Bot:**\n\nHelp support our store by sharing this bot with"
        f" your friends and gaming groups!\n\n👉 https://t.me/{context.bot.username}",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Back to Menu", callback_data="main_menu")]]
        ),
        parse_mode="Markdown",
    )

  elif data == "support":
    await query.answer()
    await query.edit_message_text(
        "💬 **Customer Support:**\n\nHaving issues with keys or payment? Contact"
        " our 24/7 admin support team directly.\n\n👤 Admin: `@godcheats`",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Back to Menu", callback_data="main_menu")]]
        ),
        parse_mode="Markdown",
    )

  elif data.startswith("item_"):
    await query.answer()
    
    products = {
        "item_21": {"name": "SILENT-CHEATS LITE", "prices": {"1 Day": 90, "3 Days": 180, "7 Days": 350, "14 Days": 600, "30 Days": 900}},
        "item_22": {"name": "SILENT-CHEATS BRUTAL", "prices": {"1 Day": 90, "3 Days": 180, "7 Days": 350, "14 Days": 600, "30 Days": 900}},
        "item_23": {"name": "SILENT-CHEATS APK MOD", "prices": {"1 Day": 90, "3 Days": 180, "7 Days": 350, "14 Days": 600, "30 Days": 900}},
        "item_24": {"name": "Rapid Core - Root Safe", "prices": {"1 Day": 90, "7 Days": 299, "30 Days": 1099}},
        "item_25": {"name": "PRIME APKMOD", "prices": {"1 Day": 90, "7 Days": 350}},
        "item_26": {"name": "PATOTEAM APKMOD", "prices": {"1 Day": 250, "3 Days": 400, "7 Days": 700, "30 Days": 1400}},
        "item_27": {"name": "IOS-MIGUL PRO", "prices": {"1 Day": 300, "7 Days": 1000, "30 Days": 2000}},
        "item_28": {"name": "Haxx Cker Pro", "prices": {"10 Days": 550, "20 Days": 1050, "30 Days": 1450}},
        "item_29": {"name": "HG CHEAT APKMOD", "prices": {"1 Day": 90, "3 Days": 180, "7 Days": 350, "30 Days": 900}},
    }
    
    item = products.get(data, {"name": "Product", "prices": {"1 Day": 100}})
    
    text = f"🎮 **{item['name']}**\n"
    text += "────────────────────\n\n"
    
    buttons = []
    
    for duration, price in item["prices"].items():
        if "1 Day" in duration:
            disc_price = price - 10
        elif "3 Day" in duration:
            disc_price = price - 20
        elif "7 Day" in duration:
            disc_price = price - 30
        elif "20 Day" in duration or "30 Day" in duration:
            disc_price = price - 40
        else:
            disc_price = price - 10
        
        text += f"⏱️ **{duration}**\n"
        text += f"💰 ~₹{price}~ **₹{disc_price}**\n"
        text += f"✅ In Stock\n\n"
        
        buttons.append([InlineKeyboardButton(f"📦 Buy {duration} - ₹{disc_price}", callback_data="add_balance")])
    
    text += "👇 **Select duration below:**"
    buttons.append([InlineKeyboardButton("🔙 Back to Shop", callback_data="shop")])
    
    reply_markup = InlineKeyboardMarkup(buttons)
    await query.edit_message_text
      
elif data == "add_balance":
    await query.answer()
    
    user = query.from_user
    username = f"@{user.username}" if user.username else user.first_name
    user_id = user.id
    
    text = "💳 **Payment & Balance Instructions:**\n\nTo purchase the key, please send payment to the admin and share a screenshot along with your User ID.\n\n👤 **Admin:** @Godmodesx"
    
    await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back to Shop", callback_data="shop")]]), parse_mode="Markdown")
    
    try:
        print(f"New purchase attempt by user: {username} (ID: {user_id})")
    except Exception as e:
        print(f"Error: {e}")
        (text, reply_markup=reply_markup, parse_mode="Markdown")

# 4. Main Application Setup
def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Bot is running...")
    app.run_polling()
    





if __name__ == "__main__":
  main()
  
