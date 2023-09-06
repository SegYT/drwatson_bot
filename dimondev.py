from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

patterns = [
    [ ['помо', 'не работает', 'не робит'], ['бот', 'апи', 'api', 'гб', 'глаз бога', 'глаза', 'бога'], ''.join(open('fix_api.txt', 'r', encoding='utf-8').read())],
    [ ['начать', 'как'], ['уязвимо', 'bug', 'баг', 'bounty', 'баунти', 'баунтить', 'баги', 'пентест', 'pentest', 'пентестинг', 'pentesting'], ''.join(open('bugbounty.txt', 'r', encoding='utf-8').read())]
]

TOKEN = 'TOKEN_GOES_HERE'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def chat_message(msg: types.Message):
    print(msg.text)
    for pattern in patterns:
        stop = False
        for start_word in pattern[0]:
            for key_word in pattern[1]:
                if start_word in msg.text.lower() and key_word in msg.text.lower():
                    await msg.reply(pattern[2], parse_mode="MarkdownV2")
                    stop = True
                    break

            if stop: break

    if check_banWord(msg.text):
        await msg.reply(f'Без мата {msg.from_user.mention}, больше не повторяю.')
        await bot.delete_message(msg.chat.id, message_id=msg.message_id)

def check_banWord(msg):
    banwords = ''
    with open('block_words.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            banwords += line

    banwords = banwords.replace('\n', '').replace(' ', '').split(',')
    
    for banword in banwords:
        if banword.lower() in msg.lower():
            return True
    
    return False

executor.start_polling(dp)
