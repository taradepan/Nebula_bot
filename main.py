import io
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from chat import gchat, gimg
from img import img
from rag import embed, pdfchat, query_search
import os
import dotenv
dotenv.load_dotenv()
TOKEN = os.environ.get('TOKEN')

Access= False

def start(update: Update, context: CallbackContext) -> None:
  update.message.reply_text('Please Enter the Access Code using /access <code>')

def handle_message(update: Update, context: CallbackContext) -> None:
  global Access
  if Access:
    response = gchat(update.message.text)
    update.message.reply_text(response)
  else:
    update.message.reply_text('Access Denied')

def handle_files(update:Update, context:CallbackContext) -> None:
    file = update.message.document
    if file and file.file_name.endswith('.pdf'):
        file_id = file.file_id
        file_name = file.file_name
        update.message.reply_text('Processing the PDF file')
        file_path = context.bot.get_file(file_id).download()
        embed(file_path, file_name)
        print(f"{file_name} is loaded")
        os.remove(file_path)
        update.message.reply_text('PDF file processed successfully.\nYou can now ask questions based on pdf using /pdf <question>')
        
def pdf(update: Update, context: CallbackContext) -> None:
  global Access
  if Access:
    prompt = update.message.text
    response = query_search(prompt)
    update.message.reply_text(pdfchat(prompt, response))
  else:
    update.message.reply_text('Access Denied')

def access(update: Update, context: CallbackContext) -> None:
	global Access
	if context.args[0] == "password@1234":
		update.message.reply_text('Access Granted')
		Access = True
	else:
		update.message.reply_text('Access Denied')
      
def handle_image(update: Update, context: CallbackContext) -> None:
  global Access
  if Access:
    photo = update.message.photo[-1]
    file = photo.get_file()
    response = gimg(update.message.caption, file)
    update.message.reply_text(response)
  else:
    update.message.reply_text('Access Denied')

def image(update: Update, context: CallbackContext) -> None:
  global Access
  if Access:
    prompt = update.message.text
    response = img(prompt)
    bio = io.BytesIO()
    response.save(bio, 'JPEG')
    bio.seek(0)
    update.message.reply_photo(photo=bio)
    
  else:
    update.message.reply_text('Access Denied')

def help(update: Update, context: CallbackContext) -> None:
  update.message.reply_text('/access <code> : to use the bot\n/image <prompt> : to generate an image\n Image with caption: to chat based on the image')

def main() -> None:
    updater = Updater(TOKEN, use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(CommandHandler("access", access))
    dispatcher.add_handler(CommandHandler("help", start))
    dispatcher.add_handler(CommandHandler("image", image))
    dispatcher.add_handler(CommandHandler("pdf", pdf))
    dispatcher.add_handler(MessageHandler(Filters.document, handle_files))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    dispatcher.add_handler(MessageHandler(Filters.photo, handle_image))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
  main()