from aiogram import executor
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Message
from config import dp
from aiogram.dispatcher.filters import Text
from pytube import YouTube


@dp.message_handler(CommandStart())
async def bot_start(message: Message):
    text = ("Menu: ", "/start-Botni ishga tushirish", "/help-Settings knopkasi")
    await message.answer("\n".join(text))


@dp.message_handler(Text(startswith="http"))
async def music_download(msg: Message):
    link = msg.text
    from io import BytesIO
    buffer = BytesIO()
    url = YouTube(link)
    if url.check_availability() is None:
        audio = url.streams.get_audio_only()
        audio.stream_to_buffer(buffer=buffer)
        buffer.seek(0)
        filename = url.title
        await msg.answer_audio(audio=buffer, caption=filename)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)