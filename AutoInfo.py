from hikka.modules import loader
import time

class AutoInfoMod(loader.Module):
    """Авто-оновлення .info з реальним аптаймом"""
    
    strings = {"name": "AutoInfo"}

    def __init__(self):
        self.start_time = time.time()

    async def infocmd(self, message):
        """Показати кастомне .info з оновленням аптайму"""
        uptime = time.strftime("%H:%M:%S", time.gmtime(time.time() - self.start_time))
        owner = f"@{message.client.me.username}" if message.client.me.username else f"tg://user?id={message.client.me.id}"
        host = "🌟 Termux (Admin)"  # Можеш змінити на "Heroku" або зробити визначення автоматичним

        info_text = (
            "╭━─━📌 ІНФО МОДУЛЯ 📌━─━╮\n"
            f"┃ 🐱 Власник: {owner} \n"
            f"┃ ⌛️ Аптайм: {uptime} \n"
            f"┃ 🖥 Хост: {host} \n"
            "╰━─━─━─━─━─━─━─━─━─━─━╯"
        )

        await message.edit(info_text)￼Enter
