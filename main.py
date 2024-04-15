import logging
import os
from telegram.ext import *
import string
from threading import *
from random import choice
from images_class import Filter
# from telegram.ext import Application, MessageHandler, filters
from requestsserver import Stoke_Market_chart
# from database import Database
from adminregistration import Admin_registration
from stoke_analysis import Moex_ta
from registration import Registration
from telegram import *
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
reply_keyboard_6 = [['/chart', '/analysis'],
                    ['/main_menu']]
reply_keyboard_7 = [['/work_music'], ['/main_menu']]
reply_keyboard_8 = [['/functions'], ['/main_menu']]

markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
markup_2 = ReplyKeyboardMarkup(reply_keyboard_2, one_time_keyboard=False)
markup_3 = ReplyKeyboardMarkup(reply_keyboard_3, one_time_keyboard=True)
markup_4 = ReplyKeyboardMarkup(reply_keyboard_4, one_time_keyboard=True)
markup_5 = ReplyKeyboardMarkup(reply_keyboard_5, one_time_keyboard=False)
markup_6 = ReplyKeyboardMarkup(reply_keyboard_6, one_time_keyboard=True)
markup_7 = ReplyKeyboardMarkup(reply_keyboard_7, one_time_keyboard=False)
markup_8 = ReplyKeyboardMarkup(reply_keyboard_8, one_time_keyboard=True)

PHOTO = 1


async def start(update, context):
    await update.message.reply_text("Здравствуйте! Для продолжение работы с ботом нажмите на кнопку ниже",
                                    reply_markup=markup_4)


async def admin_user(update, context):
    try:
        login_admin = context.args[0]
        password_admin = context.args[1]
        object_class = Admin_registration(login_admin, password_admin)
        if object_class.is_checking_for_admin():
            # a = Database()
            # a1 = a.read_database()
            # await update.message.reply_text(f"{a1}")
            await update.message.reply_text("📁")
            await update.message.reply_document('history_users.txt')
        else:
            await update.message.reply_text('Доступ запрещен')
    except IndexError:
        await update.message.reply_text("команда недоступна")



async def documentation(update, context):
    await update.message.reply_text('📁')
    await update.message.reply_document('документация.docx')


async def main_menu(update, context):
    user = update.effective_user
    text = 'Я бот, имеющий возможность работать с данными биржи, и имею дополнительные функции'
    await update.message.reply_html(
        rf"Привет {user.mention_html()}! {text}, о которых ты можешь прочитать в пункте настройки документация",
        reply_markup=markup
    )
    await update.message.reply_text("Выберите функцию")


async def admin_passwd(update, context):
    try:
        login_admin = context.args[0]
        password_admin = context.args[1]
        object_class = Admin_registration(login_admin, password_admin)
        if object_class.checking_for_admin():
            object_class.registration_admin()
            await update.message.reply_text("🔐")
            await update.message.reply_text("Регистрация прошла успешна!")
            await update.message.reply_text('Нажмите ниже', reply_markup=markup_3)
        else:
            await update.message.reply_text("❌")
            await update.message.reply_text("Логин или пароль занят. Повторите попытку или вернитесь на главную")
    except IndexError:
        await update.message.reply_text("команда недоступна!")


async def analysis(update, context):
    try:
        activ = context.args
        if len(activ) == 0:
            text = "Для того чтобы команда заработала нужно вести '/analysis {тикер акции} {таймфрейм}'"
            text_2 = 'Параметр тайфрейм необязательный, но если его не использовать то будет стоять дневной тайфрейм'
            await update.message.reply_text(
                f'{text} {text_2}. Списком где хранятся расшифровки таймфреймов отправлен ниже')
            await update.message.reply_document('timeframes.txt')
        else:
            if len(activ) == 1:
                object_class_Moex_one_argument = Moex_ta(activ[0])
                await update.message.reply_text(object_class_Moex_one_argument.technical_analysis())

            elif len(activ) == 2:
                object_class_Moex_two = Moex_ta(activ[0], activ[1])
                await update.message.reply_text(object_class_Moex_two.technical_analysis())

            else:
                await update.message.reply_text('Введены неверные данные')
                await update.message.reply_document('timeframes.txt')
    except BaseException:
        await update.message.reply_text("Введены некорректные данные")


async def work_music(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Прикрепите фото!")

    return PHOTO


async def photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    string_random = ''.join([choice([element for element in string.ascii_letters]) for _ in range(10)])
    photo_file = await update.message.photo[-1].get_file()
    name_file = f"user_photo{string_random}.jpg"
    await photo_file.download_to_drive(name_file)
    logger.info("Photo of %s: %s", user.first_name, name_file)
    object_class = Filter(name_file)
    file = object_class.script_1
    await update.message.reply_photo(file)
    object_class.delete()
    await update.message.reply_text('Выберите функцию', reply_markup=markup_8)
    return ConversationHandler.END


async def help(update, context):
    URL = 'https://disk.yandex.ru/i/NJ3zby3bwgm9lA'
    await update.message.reply_html(rf'Если документ не загружается можете перейти по ссылки <a href="{URL}">тут</a>')
    await update.message.reply_document(
        "документация.docx")


async def chart(update, context):
    try:
        active = context.args[0]
        initial_time = context.args[1]
        end_time = context.args[2]
        object_5 = Stoke_Market_chart(active, initial_time, end_time)
        active_write = Registration(active)
        active_write.request_write()
        file_name = object_5.chart()
        await update.message.reply_photo(file_name)
        await update.message.reply_text(f'{active} {initial_time} {end_time}')
        os.remove(file_name)
        # active_write_2 = Database()
        # active_write_2.write_database(active)
    except BaseException:
        await update.message.reply_text('Неверные данные')


async def information_admin(update, context):
    await update.message.reply_text(
        "Создатель проекта: Рязанов, Роман", reply_markup=markup_4)


async def stockmarket(update, context):
    await update.message.reply_text("Вам доступнен режим 'биржа' вибирайте функция", reply_markup=markup_6)


async def delete(update, context):
    await update.message.reply_text("")


async def functions(update, context):
    await update.message.reply_text('Выберите функцию', reply_markup=markup_7)


async def settings(update, context):
    await update.message.reply_text('💡', reply_markup=markup_5)


def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("chart", chart))
    application.add_handler(CommandHandler("analysis", analysis))
    application.add_handler(CommandHandler("admin_user", admin_user))
    application.add_handler(CommandHandler("documentation", documentation))
    application.add_handler(CommandHandler('main_menu', main_menu))
    application.add_handler(CommandHandler("info_admin", information_admin))
    application.add_handler(CommandHandler("stockmarket", stockmarket))
    application.add_handler(CommandHandler("functions", functions))
    application.add_handler(CommandHandler("settings", settings))
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("work_music", work_music)],
        states={
            PHOTO: [MessageHandler(filters.PHOTO, photo)]
        },
        fallbacks=[CommandHandler("photo", photo)],
    )

    application.add_handler(conv_handler)
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("admin_passwd", admin_passwd))
    application.run_polling()


if __name__ == '__main__':
    main()