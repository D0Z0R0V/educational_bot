from button import *
import os

if __name__ == '__main__':
    application = ApplicationBuilder().token(os.environ.get('API_KEY')).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    button_handler = CallbackQueryHandler(button)
    application.add_handler(button_handler)

    application.add_handler(CallbackQueryHandler(button_7_class, pattern='^gravity_7_class$'))
    application.add_handler(CallbackQueryHandler(button_9_class, pattern='^gravity_9_class$'))
    application.add_handler(CallbackQueryHandler(button_10_class, pattern='^gravity_10_class$'))
    application.add_handler(CallbackQueryHandler(button_apps, pattern='^gravity_apps$'))

    try:
        application.run_polling()
    except Exception as e:
        print(f"An error occurred: {e}")
