#from AviaxMusic.utils import get_name, increase_count, chatdb
#from AviaxMusic import app
#import uvloop
#from pyrogram import filters
#from datetime import date
#from pyrogram.types import (
#    Message,
#    CallbackQuery,
#    InlineKeyboardMarkup,
#    InlineKeyboardButton,
#)
#
#uvloop.install()
#
#@app.on_message(
#    ~filters.bot
#    & ~filters.forwarded
#    & filters.group
#    & ~filters.via_bot
#    & ~filters.service
#)
#
#async def inc_user(_, message: Message):
#    if message.text:
#        if (
#            message.text.strip() == "/top@AviaxBeatzBot"
#            or message.text.strip() == "/top"
#        ):
#            return await show_top_today(_, message)
#
#    chat = message.chat.id
#    user = message.from_user.id
#    increase_count(chat, user)
#    print(chat, user, "increased")
#
#
#async def show_top_today(_, message: Message):
#    print("today top in", message.chat.id)
#    chat = chatdb.find_one({"chat": message.chat.id})
#    today = str(date.today())
#
#    if not chat:
#        return await message.reply_text("no data available",
#        reply_markup=InlineKeyboardMarkup(
#            [[InlineKeyboardButton("Overall Ranking", callback_data="overall")]]
#        ),)
#
#    if not chat.get(today):
#        return await message.reply_text("no data available for today",
#        reply_markup=InlineKeyboardMarkup(
#            [[InlineKeyboardButton("Overall Ranking", callback_data="overall")]]
#        ),)
#    
#    t = "🔰 **Today's Top Users :**\n\n"
#
#    pos = 1
#    for i, k in sorted(chat[today].items(), key=lambda x: x[1], reverse=True)[:10]:
#        i = await get_name(app, i)
#
#        t += f"**{pos}.** {i} - {k}\n"
#        pos += 1
#
#    total = sum(chat[today].values())
#    t += f'\n✉️ Today messages: {total}'
#
#    await message.reply_text(
 #       t,
 #       reply_markup=InlineKeyboardMarkup(
#            [[InlineKeyboardButton("Overall Ranking", callback_data="overall")]]
#        ),
#    )
#
#
#@app.on_callback_query(filters.regex("overall"))
#async def show_top_overall_callback(_, query: CallbackQuery):
#    print("overall top in", query.message.chat.id)
#    chat = chatdb.find_one({"chat": query.message.chat.id})
#
#    if not chat:
#        return await query.answer("No data available", show_alert=True)
#
#    await query.answer("Processing... Please wait")
#
#    t = "🔰 **Overall Top Users :**\n\n"
#
#    overall_dict = {}
#    total =0
#    for i, k in chat.items():
#        if i == "chat" or i == "_id":
#            continue
#
#        for j, l in k.items():
#            if j not in overall_dict:
#                overall_dict[j] = l
#            else:
#                overall_dict[j] += l
#
#        total += sum(k.values())
#    
#
#    pos = 1
#    for i, k in sorted(overall_dict.items(), key=lambda x: x[1], reverse=True)[:10]:
#        i = await get_name(app, i)
#
#        t += f"**{pos}.** {i} - {k}\n"
#        pos += 1
#
#    t += f'\n✉️ Today messages: {total}'
#
#    await query.message.edit_text(
#        t,
#        reply_markup=InlineKeyboardMarkup(
#            [[InlineKeyboardButton("Today's Ranking", callback_data="today")]]
#        ),
#    )
#
#
#@app.on_callback_query(filters.regex("today"))
#async def show_top_today_callback(_, query: CallbackQuery):
#    print("today top in", query.message.chat.id)
#    chat = chatdb.find_one({"chat": query.message.chat.id})
#    today = str(date.today())
#
#    if not chat:
#        return await query.answer("No data available", show_alert=True)
#
#    if not chat.get(today):
#        return await query.answer("No data available for today", show_alert=True)
#
#    await query.answer("Processing... Please wait")
#
#    t = "🔰 **Today's Top Users :**\n\n"
#
#    pos = 1
#    for i, k in sorted(chat[today].items(), key=lambda x: x[1], reverse=True)[:10]:
#        i = await get_name(app, i)
#
#        t += f"**{pos}.** {i} - {k}\n"
#        pos += 1
#
#
#    total = sum(chat[today].values())
#    t += f'\n✉️ Today messages: {total}'
#
#
#    await query.message.edit_text(
#        t,
#        reply_markup=InlineKeyboardMarkup(
#            [[InlineKeyboardButton("Overall Ranking", callback_data="overall")]]
#        ),
#    )
#
