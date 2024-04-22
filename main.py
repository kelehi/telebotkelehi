import os
import string
from random import choice

import logging
from telegram.ext import *
from telegram import *

from token_bot import TOKEN
from images_class import Filter
from database import Database
from requestsserver import Stoсke_Market_chart
from adminregistration import Admin_registration
from stoke_analysis import Moex_ta, Crypto
from write_text import Write


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
reply_keyboard_6 = [['/start_chart', '/analysis'],
                    ['/main_menu']]
reply_keyboard_7 = [['/work_photo'], ['/send_music'],
                    ['/main_menu']]
reply_keyboard_8 = [['/functions'], ['/main_menu']]
reply_keyboard_9 = [['/start_analysis_stocks'], ['/start_crypto'],
                    ['/main_menu']]
reply_keyboard_10 = [['/main_menu']]
reply_keyboard_11 = [['/stockmarket'], ['/analysis'],
                     ['/main_menu']]

markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
markup_2 = ReplyKeyboardMarkup(reply_keyboard_2, one_time_keyboard=False)
markup_3 = ReplyKeyboardMarkup(reply_keyboard_3, one_time_keyboard=True)
markup_4 = ReplyKeyboardMarkup(reply_keyboard_4, one_time_keyboard=True)
markup_5 = ReplyKeyboardMarkup(reply_keyboard_5, one_time_keyboard=False)
markup_6 = ReplyKeyboardMarkup(reply_keyboard_6, one_time_keyboard=True)
markup_7 = ReplyKeyboardMarkup(reply_keyboard_7, one_time_keyboard=False)
markup_8 = ReplyKeyboardMarkup(reply_keyboard_8, one_time_keyboard=True)
markup_9 = ReplyKeyboardMarkup(reply_keyboard_9, one_time_keyboard=False)
markup_10 = ReplyKeyboardMarkup(reply_keyboard_10, one_time_keyboard=False)
markup_11 = ReplyKeyboardMarkup(reply_keyboard_11, one_time_keyboard=False)

PHOTO = 1
MUSIC = 2
CHART = 3
CRYPTOCURRENCY = 4
STOCK_MARKET = 5

database = Database()


async def start(update, context):  # Старт бота
    user = update.effective_user
    await update.message.reply_html(
        rf"Привет {user.mention_html()}! Для продолжение работы с ботом нажмите на кнопку ниже", reply_markup=markup_4)


async def main_menu(update, context):  # Главное меню
    text = 'Я бот, имеющий возможность работать с данными биржи, и имею дополнительные функции'
    await update.message.reply_text(
        f"{text}, о которых ты можешь прочитать в пункте 'settings' 'documentation'", reply_markup=markup)

    await update.message.reply_text("Выберите функцию")


async def stockmarket(update, context):  # функция для перехода в раздел 'биржа'
    await update.message.reply_text("Вам доступнен режим 'биржа' вибирайте функцию", reply_markup=markup_6)


async def functions(update, context):  # функция для перехода в раздел 'дополнительные функции'
    await update.message.reply_text('Выберите функцию', reply_markup=markup_7)


async def settings(update, context):  # функция для перехода в раздел 'настройки'
    await update.message.reply_text('💡', reply_markup=markup_5)


async def information_admin(update, context):  # функция для получения информации о создателе
    await update.message.reply_text(
        "Создатель проекта: Рязанов, Роман", reply_markup=markup_4)


async def analysis(update, context):  # функция для перехода в раздел 'технческий анализ'
    await update.message.reply_text('Выберите функцию', reply_markup=markup_9)


async def start_chart(update, context):  # Запуск графика
    await update.message.reply_text(
        'Введите данные: тикер акции начальная дата конечная дата. Пример: YNDX 23-11-01 24-04-15')

    return CHART


async def chart(update, context):  # Рисование и отправка графика
    try:
        active = str(update.message.text).split()[0]
        initial_time = str(update.message.text).split()[1]
        end_time = str(update.message.text).split()[2]
        base = Stoсke_Market_chart(active, initial_time, end_time)
        database.write_database(active, initial_time, end_time)
        active_write = Write(active)
        active_write.request_write()
        file_name = base.chart()
        await update.message.reply_photo(file_name)
        await update.message.reply_text(f'{active} {initial_time} {end_time}')
        os.remove(file_name)

    except BaseException:
        await update.message.reply_text(f'Ошибка к доступа к серверу или неправильный формат ввода')

    return ConversationHandler.END


async def start_analysis_stocks(update, context):  # старт анализа (Акции)
    await update.message.reply_text(
        "Введите тикер акции и таймфрейм. Пример запроса: ASTR 1w. Файл с таймфреймеми отправлен ниже")
    await update.message.reply_document('timeframes.txt')

    return STOCK_MARKET


async def analysis_stocks(update, context):  # технический анализ (Акции)
    try:
        activ = str(update.message.text).split()
        if len(activ) == 1:
            active_write = Write(activ[0])
            active_write.request_write()
            activ_1 = Moex_ta(activ[0])
            await update.message.reply_text(activ_1.technical_analysis(),
                                            reply_markup=markup_11)

        elif len(activ) == 2:
            active_write = Write(activ[0])
            active_write.request_write()
            activ_2 = Moex_ta(activ[0], activ[1])
            await update.message.reply_text(activ_2.technical_analysis(), reply_markup=markup_11)

    except BaseException:
        text = "Для того чтобы команда заработала нужно вести {тикер акции} {таймфрейм}'"
        text_2 = 'Параметр тайфрейм необязательный, но если его не использовать то будет стоять дневной тайфрейм'
        await update.message.reply_text(
            f'{text} {text_2}. Списком где хранятся расшифровки таймфреймов отправлен ниже')
        await update.message.reply_text(f"Введены некорректные данные", reply_markup=markup_11)
        await update.message.reply_document('timeframes.txt')

    return ConversationHandler.END


async def start_crypto(update, context):  # старт анализа (Криптовалюта)
    text = 'Файл с таймфреймеми отправлен ниже'
    await update.message.reply_text(
        f"Введите тикер криптовалюты и таймфрейм. Пример запроса для биткоина: BTCUSD 1w. {text}")
    await update.message.reply_document('timeframes.txt')

    return CRYPTOCURRENCY


async def cryptocurrency(update, context):  # технический анализ (Криптовалюта)
    try:
        activ = str(update.message.text).split()

        if len(activ) == 1:
            active_write = Write(activ[0])
            active_write.request_write()
            activ_1 = Crypto(activ[0])
            await update.message.reply_text(activ_1.technical_analysis())

        elif len(activ) == 2:
            active_write = Write(activ[0])
            active_write.request_write()
            active_2 = Crypto(activ[0], activ[1])
            await update.message.reply_text(active_2.technical_analysis(), reply_markup=markup_11)

    except BaseException:
        text = "Для того чтобы команда заработала нужно вести {тикер криптовалюты} {таймфрейм}'"
        text_2 = 'Параметр тайфрейм необязательный, но если его не использовать то будет стоять дневной тайфрейм'
        await update.message.reply_text(
            f'{text} {text_2}. Списком где хранятся расшифровки таймфреймов отправлен ниже')
        await update.message.reply_text('Введены неверные данные или проблема с сервером.', reply_markup=markup_11)
        await update.message.reply_document('timeframes.txt')

    return ConversationHandler.END


async def documentation(update, context):  # Отправляем документацию
    await update.message.reply_text('📁')
    await update.message.reply_document('документация.docx')


async def admin_user(update, context):
    # Проверяем является ли пользователь админом, если да, отправляем админскую информацию
    try:
        login_admin = context.args[0]
        password_admin = context.args[1]
        object_class = Admin_registration(login_admin, password_admin)
        if object_class.is_checking_for_admin():
            await update.message.reply_text("📁")
            await update.message.reply_document('history_users.txt')
            await update.message.reply_text(f'{database.read_database()}')
        else:
            await update.message.reply_text('Доступ запрещен')

    except IndexError:
        await update.message.reply_text("команда недоступна")


async def send_music(update, context):  # Отправляем аудиофайл
    await update.message.reply_audio('file_audio.mp3')


async def work_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):  # Старт наложения фильтра на фото
    await update.message.reply_text("Прикрепите фото!")

    return PHOTO


async def photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # сохраняем накладываем фильтер отправлем новое фото
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


async def admin_passwd(update, context):  # Регистрируем админа
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
            await update.message.reply_text("Логин или пароль занят. Повторите попытку или вернитесь на главную",
                                            reply_markup=markup_10)
    except IndexError:
        await update.message.reply_text("команда недоступна!")


async def help(update, context):  # Отправка документации
    URL = 'https://disk.yandex.ru/i/NJ3zby3bwgm9lA'
    await update.message.reply_html(rf'Если документ не загружается можете перейти по ссылки <a href="{URL}">тут</a>')
    await update.message.reply_document(
        "документация.docx")


def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("admin_user", admin_user))
    application.add_handler(CommandHandler("documentation", documentation))
    application.add_handler(CommandHandler("send_music", send_music))
    application.add_handler(CommandHandler('main_menu', main_menu))
    application.add_handler(CommandHandler("info_admin", information_admin))
    application.add_handler(CommandHandler("stockmarket", stockmarket))
    application.add_handler(CommandHandler("functions", functions))
    application.add_handler(CommandHandler("settings", settings))
    application.add_handler(CommandHandler('analysis', analysis))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("admin_passwd", admin_passwd))

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("work_photo", work_photo)],
        states={
            PHOTO: [MessageHandler(filters.PHOTO, photo)]
        },
        fallbacks=[CommandHandler("photo", photo)],
    )

    conv_handler_2 = ConversationHandler(
        entry_points=[CommandHandler("start_chart", start_chart)],
        states={
            CHART: [MessageHandler(filters.TEXT, chart)]
        },
        fallbacks=[CommandHandler("chart", chart)]
    )

    conv_handler_3 = ConversationHandler(
        entry_points=[CommandHandler("start_analysis_stocks", start_analysis_stocks)],
        states={
            STOCK_MARKET: [MessageHandler(filters.TEXT, analysis_stocks)]
        },
        fallbacks=[CommandHandler("analysis_stocks", analysis_stocks)],
    )

    conv_handler_4 = ConversationHandler(
        entry_points=[CommandHandler("start_crypto", start_crypto)],
        states={
            CRYPTOCURRENCY: [MessageHandler(filters.TEXT, cryptocurrency)]
        },
        fallbacks=[CommandHandler("cryptocurrency", cryptocurrency)],
    )

    application.add_handler(conv_handler)
    application.add_handler(conv_handler_2)
    application.add_handler(conv_handler_3)
    application.add_handler(conv_handler_4)
    application.run_polling()


if __name__ == '__main__':
    main()
