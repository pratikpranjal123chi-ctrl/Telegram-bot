from flask import Flask
import threading
import qrcode
import io 

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
        parse_mode="Markdown",)
    

  elif data == "lucky":
    await query.answer()
    await query.edit_message_text(
        "🍀 **Lucky Spin / Reward:**\n\n🎁 Try your luck today! Spin the wheel"
        " to win free keys or wallet balance.\n\n*(Feature coming soon in next"
        " update!)*",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Back to Menu", callback_data="main_menu")]]
        
        parse_mode="Markdown",
        )
    
    elif data.startswith("item_"):
    await query.answer()
    
    products = {
        "item_21": {"name": "SILENT-CHEATS LITE", "price": 90},
        "item_22": {"name": "SILENT-CHEATS BRUTAL", "price": 90},
        "item_23": {"name": "SILENT-CHEATS APK MOD", "price": 90},
        "item_24": {"name": "Rapid Core - Root Safe", "price": 90},
        "item_25": {"name": "PRIME APKMOD", "price": 90},
        "item_26": {"name": "PATOTEAM APKMOD", "price": 250},
        "item_27": {"name": "IOS-MIGUL PRO", "price": 300},
        "item_28": {"name": "Haxx Cker Pro", "price": 550},
        "item_29": {"name": "HG CHEAT APKMOD", "price": 90}
    }
    
    item_info = products.get(data, {"name": "Product", "price": 90})
    item_name = item_info["name"]
    price = item_info["price"]
    
    order_id = f"ORDE{abs(hash(str(query.from_user.id) + str(price) + item_name)) % 10000000000}EF11"
    upi_id = "mryashisbusy@fam"
    
    upi_url = f"upi://pay?pa={upi_id}&pn=Yash&am={price}.00&cu=INR&tn={order_id}"
    
    img = qrcode.make(upi_url)
    bio = io.BytesIO()
    bio.name = 'qr.png'
    img.save(bio, 'PNG')
    bio.seek(0)
    
    caption_text = (
        "📳 **UPI PAYMENT**\n"
        "────────────────────────\n"
        f"🎮 **Item:** {item_name}\n"
        f"💵 **Amount: ₹{price}.00 INR**\n"
        f"🔒 **Order:** `{order_id}`\n"
        f"🆔 **UPI ID:** `{upi_id}`\n"
        "⏱️ **Valid for:** 5:00 minutes\n\n"
        "📋 **How to pay**\n"
        "1️⃣ Scan the QR with any UPI app (GPay, PhonePe, Paytm)\n"
        "2️⃣ Or tap the UPI ID above to copy it\n"
        f"3️⃣ Pay **exactly ₹{price}.00 INR**\n"
        "4️⃣ Wait — keys auto-deliver in seconds\n\n"
        "⚠️ _Pay the EXACT amount or auto-verify will fail._\n"
        "_This QR is single-use and expires in 5 minutes._"
    )
    
    keyboard = [[InlineKeyboardButton("🔙 Back to Shop", callback_data="shop")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    try:
        await query.message.delete()
        await context.bot.send_photo(
            chat_id=query.message.chat_id,
            photo=bio,
            caption=caption_text,
            reply_markup=reply_markup,
            parse_mode="Markdown"
        )
    except Exception as e:
        print(f"Error: {e}")
        

# 4. Main Application Setup
def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Bot is running...")
    app.run_polling()
    





if __name__ == "__main__":
  main()
  
