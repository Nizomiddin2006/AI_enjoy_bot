from django.core.management.base import BaseCommand
from bot.handlers import bot

class Command(BaseCommand):
    help = "Telegram AI botni ishga tushiradi"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS(" AI bot ishga tushdi..."))
        bot.infinity_polling()
