import logging
from telegram.ext import *
# from telegram.ext import Application, MessageHandler, filters
from adminregistration import Admin_registration
# from stoke_analysis import Moex_ta
import telegram
from telegram import ReplyKeyboardMarkup
from token_bot import TOKEN
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


reply_keyboard = [['/stockmarket', '/functions'],
                  ['/settings', '/info_admin']]
reply_keyboard_2 = [['/send_document']]
reply_keyboard_3 = [['/start']]
reply_keyboard_4 = [['/main_menu']]
reply_keyboard_5 = [['/documentation', '/admin_user'],
                    ['/main_menu']]


markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
markup_2 = ReplyKeyboardMarkup(reply_keyboard_2, one_time_keyboard=False)
markup_3 = ReplyKeyboardMarkup(reply_keyboard_3, one_time_keyboard=True)
markup_4 = ReplyKeyboardMarkup(reply_keyboard_4, one_time_keyboard=True)
markup_5 = ReplyKeyboardMarkup(reply_keyboard_5, one_time_keyboard=False)


async def start(update, context):
    await update.message.reply_text("Здравствуйте! Для продолжение работы с ботом нажмите на кнопку ниже",
                                    reply_markup=markup_4)


async def admin_user(update, context):
    login_admin = context.args[0]
    password_admin = context.args[1]
    object_class = Admin_registration(login_admin, password_admin)
    if object_class.is_checking_for_admin():
        await update.message.reply_text("📁")
        await update.message.reply_document('admin_registration.json')
    else:
        await update.message.reply_text('Доступ запрещен')


# async def to_the_main_menu(update, context):
#     await update.message.command('/main_menu')


async def back(update, context):
    await update.message.command('/main_menu')


async def documentation(update, context):
    await update.message.reply_text('📁')
    await update.message.reply_document('документация.docx')


async def main_menu(update, context):
    user = update.effective_user
    await update.message.reply_html(
        rf"Привет {user.mention_html()}! Я бот, имеющий возможность работать с данными биржи, и имею дополнительные функции, о которых ты можешь прочитать в пункте настройки документация",
        reply_markup=markup
    )
    await update.message.reply_text("Выберите функцию")


async def admin_passwd(update, context):
    login_admin = context.args[0]
    password_admin = context.args[1]
    object_class = Admin_registration(login_admin, password_admin)
    if object_class.checking_for_admin():
        object_class.registration_admin()
        await update.message.reply_text("🔐")
        await update.message.reply_text("Зарегистрировались! Нажмите на кнопку ниже")
        await update.message.reply_text('Нажмите ниже', reply_markup=markup_3)
    else:
        await update.message.reply_text("❌")
        await update.message.reply_text("Логин или пароль занят")


async def help(update, context):
    await update.message.reply_document(
        "документация.docx")


async def information_admin(update, context):
    await update.message.reply_text(
        "Создатель проекта: Рязанов, Роман", reply_markup=markup_4)


async def stockmarket(update, context):
    await update.message.reply_text("1")


async def functions(update, context):
    await update.message.reply_text("2")


async def settings(update, context):
    await update.message.reply_text('💡', reply_markup=markup_5)


def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("back", back))
    application.add_handler(CommandHandler("admin_user", admin_user))
    application.add_handler(CommandHandler("documentation", documentation))
    # application.add_handler(CommandHandler("to_the_main_menu", to_the_main_menu))
    application.add_handler(CommandHandler('main_menu', main_menu))
    application.add_handler(CommandHandler("info_admin", information_admin))
    application.add_handler(CommandHandler("stockmarket", stockmarket))
    application.add_handler(CommandHandler("functions", functions))
    application.add_handler(CommandHandler("settings", settings))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("admin_passwd", admin_passwd))
    application.run_polling()


if __name__ == '__main__':
    main()
