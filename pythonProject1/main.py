# Импортируем необходимые классы.
import logging
from telegram.ext import Application, MessageHandler, filters, CommandHandler
from config import BOT_TOKEN

# Запускаем логгирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)



async def start(update, context):
    await update.message.reply_text('Привет! Это бот для оповещения какой-либо новости в твоем ВК сообществе и '
                                    'дискорд канале!')
    await update.message.reply_text('Если хотите отправить оповещение, отправьте /notificate')


async def notificate(update, context):
    pass


def main():
    application = Application.builder().token(BOT_TOKEN).build()

    start_bot = CommandHandler("start", start)
    push_notificate = CommandHandler('notificate', )

    # Регистрируем обработчик в приложении.
    application.add_handler(start_bot)

    # Запускаем приложение.
    application.run_polling()

if __name__ == '__main__':
    main()