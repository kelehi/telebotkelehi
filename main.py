import logging
# from telegram.ext import Application, MessageHandler, filters
from adminregistration import Admin_registration
from telegram.ext import *
from telegram import *
from telegram import ReplyKeyboardMarkup
from token_bot import TOKEN
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

reply_keyboard_2 = [['/functions', '/stockmarket'],
                    ['/settings', '/info_admin']]

reply_keyboard = [['/stockmarket', '/functions'],
                  ['/settings', '/info_admin']]

markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
markup_2 = ReplyKeyboardMarkup(reply_keyboard_2, one_time_keyboard=False)


async def v2(update, context):
    await update.message.reply_text(
        "Информация об админе.")


async def admin_passwd(update, context):
    login_admin = context.args[0]
    password_admin = context.args[1]
    object_class = Admin_registration(login_admin, password_admin)
    if object_class.checking_for_admin():
        object_class.registration_admin()
        await update.message.reply_text("Зарегистрировался! Нажмите на кнопку ниже")
        await update.message.reply_text('/start')
    else:
        await update.message.reply_text("Логин и пароль занят занят")


async def v1(update, context):
    await update.message.reply_text(
        "")


async def start(update, context):
    user = update.effective_user
    await update.message.reply_html(
        rf"Привет {user.mention_html()}! Я бот, имеющий возможность работать с данными биржи, и имею дополнительные\n функции, о которых ты можешь прочитать в пункте настройки документация",
        reply_markup=markup
    )
    await update.message.reply_text("Выберите функцию")



async def help(update, context):
    await update.message.reply_text(
        "Я бот справочник.")


async def information_admin(update, context):
    await update.message.reply_text(
        "Создатель проекта: Рязанов, Роман")


async def stockmarket(update, context):
    await update.message.reply_text("")


async def functions(update, context):
    await update.message.reply_text("")


async def settings(update, context):
    await update.message.reply_text(
        "",
        reply_markup=markup_2)


def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("info_admin", information_admin))
    application.add_handler(CommandHandler("stockmarket", stockmarket))
    application.add_handler(CommandHandler("functions", functions))
    application.add_handler(CommandHandler("settings", settings))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("admin_passwd", admin_passwd))
    application.run_polling()


if __name__ == '__main__':
    main()