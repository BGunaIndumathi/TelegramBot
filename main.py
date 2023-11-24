# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
bot = Bot(token='5811877381:AAEoaae6Zj_NzJRmL9XSAAk1jaUWBrc851o')
dp = Dispatcher()

# Menu kb1.
b1 = KeyboardButton("/pl")
b2 = KeyboardButton("/Btech")
b3 = KeyboardButton("Inter")
b4 = KeyboardButton("/Degree")
b1a = KeyboardButton("Diploma")
b5 = KeyboardButton("/help")

# Programming Languages kb2
b6 = KeyboardButton("C")
b7 = KeyboardButton("Cpp")
b8 = KeyboardButton("Java")
b9 = KeyboardButton("Python")

# Btech courses kb3
b10 = KeyboardButton("/CSE")
b11 = KeyboardButton("/EEE")
b12 = KeyboardButton("/ECE")
b13 = KeyboardButton("/CIVIL")
b14 = KeyboardButton("/MECH")

# CSE subjects kb4
b15 = KeyboardButton("OS")
b16 = KeyboardButton("CN")
b17 = KeyboardButton("COA")
b18 = KeyboardButton("DS")
b19 = KeyboardButton("DLD")

# ECE subjects kb7
b20 = KeyboardButton("EDC")
b21 = KeyboardButton("NA")
b22 = KeyboardButton("S&S")
b23 = KeyboardButton("P&DS")
b24 = KeyboardButton("BEE")
b25 = KeyboardButton("ECA")
b26 = KeyboardButton("CS")
b27 = KeyboardButton("DP")
b28 = KeyboardButton("AWP")

# EEE subjects kb6
b29 = KeyboardButton("EDC")
b30 = KeyboardButton("CS")
b31 = KeyboardButton("PS")
b32 = KeyboardButton("DE")
b33 = KeyboardButton("EM")
b34 = KeyboardButton("PE")
b35 = KeyboardButton("S&S")


# MECH subjects kb8

b36 = KeyboardButton("ED")
b37 = KeyboardButton("EM")
b38 = KeyboardButton("MOS")
b39 = KeyboardButton("MD")
b40 = KeyboardButton("ET")
b41 = KeyboardButton("COM")
b42 = KeyboardButton("MSE")

# CIVIL subjects kb9

b43 = KeyboardButton("MOS")
b44 = KeyboardButton("FM&HM")
b45 = KeyboardButton("BM&C")
b46 = KeyboardButton("SS")
b47 = KeyboardButton("SA")
b48 = KeyboardButton("EM")
b49 = KeyboardButton("DOCS")

# DEGREE
b50 = KeyboardButton("MPC")
b51 = KeyboardButton("MPCs")
b52 = KeyboardButton("MCCs")
b53 = KeyboardButton("BSc")
b54 = KeyboardButton("Communication Skills")


# BUTTONS
kb1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False).add(b3, b1a, b2, b4, b1, b5)
kb2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False).add(b6, b7, b8, b9, b5)
kb3 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False).add(b10, b11, b12, b13, b14, b5)
kb4 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False).add(b15, b16, b17, b18, b19, b5)
kb5 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False).add(b20, b21, b22, b23, b24, b25, b26, b27,
                                                                             b28, b5)
kb6 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False).add(b29, b30, b31, b32, b33, b34, b35, b5)
kb7 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False).add(b36, b37, b38, b39, b40, b41, b42, b5)
kb8 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False).add(b43, b44, b45, b46, b47, b48, b49, b5)
kb9 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False).add(b50, b51, b52, b53, b54, b5)


# triggered when a new message is received, you can handle specific types of messages-
@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.message):
    await message.reply("Hello buddy...click on the course that you want", reply_markup=kb1)


@dp.message_handler(commands=['pl'])
async def welcome(message: types.message):
    await message.reply("Click on the language that you want", reply_markup=kb2)


@dp.message_handler(commands=['CSE'])
async def welcome(message: types.message):
    await message.reply("Click on the subject that you want", reply_markup=kb4)


@dp.message_handler(commands=['Btech'])
async def welcome(message: types.message):
    await message.reply("Click on the Branch that you want", reply_markup=kb3)


@dp.message_handler(commands=['EEE'])
async def welcome(message: types.message):
    await message.reply("Click on the subject that you want", reply_markup=kb6)


@dp.message_handler(commands=['ECE'])
async def welcome(message: types.message):
    await message.reply("Click on the subject that you want", reply_markup=kb5)


@dp.message_handler(commands=['MECH'])
async def welcome(message: types.message):
    await message.reply("Click on the subject that you want", reply_markup=kb7)


@dp.message_handler(commands=['CIVIL'])
async def welcome(message: types.message):
    await message.reply("Click on the subject that you want", reply_markup=kb8)


@dp.message_handler(commands=['Degree'])
async def welcome(message: types.message):
    await message.reply("Click on the subject that you want", reply_markup=kb9)


@dp.message_handler()
async def kb_answer(message: types.Message):
    if message.text == "Inter":
        await message.answer("We are researching on this.")
    elif message.text == "Diploma":
        await message.answer("We are researching on this.")
    elif message.text == "MPC":
        await message.answer("We are researching on this.")
    elif message.text == "MPCs":
        await message.answer("We are researching on this.")
    elif message.text == "MCCs":
        await message.answer("We are researching on this.")
    elif message.text == "BSc":
        await message.answer("We are researching on this.")
    elif message.text == "Communication Skills":
        await message.answer("We are researching on this.")

    # ..........CSE.............
    elif message.text == "C":
        await message.answer("https://youtube.com/playlist?list=PLBlnK6fEyqRhX6r2uhhlubuF5QextdCSM")
    elif message.text == "Cpp":
        await message.answer("https://youtube.com/playlist?list=PLBlnK6fEyqRh6isJ01MBnbNpV3ZsktSyS")
    elif message.text == "Java":
        await message.answer("https://youtube.com/playlist?list=PLBlnK6fEyqRjKA_NuK9mHmlk0dZzuP1P5")
    elif message.text == "Python":
        await message.answer("https://youtube.com/playlist?list=PLBlnK6fEyqRiueC_HzwFallNO76hfXBB7")
    elif message.text == "OS":
        await message.answer("https://youtube.com/playlist?list=PLBlnK6fEyqRiVhbXDGLXDk_OQAeuVcp2O")
    elif message.text == "CN":
        await message.answer("https://youtube.com/playlist?list=PLBlnK6fEyqRgMCUAG0XRw78UA8qnv6jEx")
    elif message.text == "DS":
        await message.answer("https://youtube.com/playlist?list=PLBlnK6fEyqRj9lld8sWIUNwlKfdUoPd1Y")
    elif message.text == "COA":
        await message.answer("youtube.com/playlist?list=PLBlnK6fEyqRgLLlzdgiTUKULKJPYc0A4q")
    elif message.text == "DLD":
        await message.answer("https://youtube.com/playlist?list=PLBlnK6fEyqRjMH3mWf6kwqiTbT798eAOm")

    # .......ECE.........
    elif message.text == "EDC":
        await message.answer("https://youtube.com/playlist?list=PLZycBso7-qO3cIqZJraJOnjvjLp0MhWHD")
    elif message.text == "NA":
        await message.answer("https://youtube.com/playlist?list=PLBlnK6fEyqRhG6s3jYIU48CqsT5cyiDTO")
    elif message.text == "S&S":
        await message.answer("https://youtube.com/playlist?list=PLBlnK6fEyqRgLR-hMp7wem-bdVN1iEhs")
    elif message.text == "P&DS":
        await message.answer("https://youtube.com/playlist?list=PL9zyqBvEBmDZEeBRubH8IO3H2i7K7UtEq")
    elif message.text == "BEE":
        await message.answer("https://youtube.com/playlist?list=PL8T_f_7Y4chYRUJZSdtgPp57YX4RgWONj")
    elif message.text == "ECA":
        await message.answer(
            "https://youtube.com/playlist?list=PLROvODCYkEM-6AQKkgvQbT5MvR5yR5_Ua "
            " https://youtube.com/playlist?list=PLtmB4Xi1QiUDDsuEI0p2lO7tDuYGBS6rt")
    elif message.text == "CS":
        await message.answer("https://youtube.com/playlist?list=PLBlnK6fEyqRhqzJT87LsdQKYZBC93ezDo")
    elif message.text == "DC":
        await message.answer("https://youtube.com/playlist?list=PLXOYj6DUOGrr-O76Jv2JVc7PsjM80RkeS")
    elif message.text == "AWP":
        await message.answer(
            "https://youtube.com/playlist?list=PLMpCSwrw7iRG_UJgF7aUV4QhHwT0TVDRi"
            " https://youtube.com/playlist?list=PLlzcioi3jRIR8f6wtY5StBS5fkg4gZ")

    # ..........MECH..............

    elif message.text == "ED":
        await message.answer("https://youtu.be/WG6H2pISUzQ")
    elif message.text == "EM":
        await message.answer("https://youtube.com/playlist?list=PLDN15nk5uLiAyM7MbRBF1eIFC8y5vMRxI")
    elif message.text == "MOS":
        await message.answer("https://youtube.com/playlist?list=PLIhUrsYr8yHzft7ygw5THZo4aDcsxEadP")
    elif message.text == "MD":
        await message.answer("https://youtube.com/playlist?list=PLJu6FW_RN3r5adM4phY-DtkFPQIQ06XR7")
    elif message.text == "ET":
        await message.answer("https://youtube.com/playlist?list=PL9RcWoqXmzaK6AHCCyL_J6gqc02RN-w-D")
    elif message.text == "KOM":
        await message.answer("https://youtube.com/playlist?list=PLBEA57F7E7560C8E8")
    elif message.text == "MSE":
        await message.answer("https://youtube.com/playlist?list=PLyAZSyX8Qy5Am_2StOOQ5vCUE3VIcAenE")

    # .................EEE...................

    elif message.text == "EDC":
        await message.answer("https://youtube.com/playlist?list=PLm_MSClsnwm8EdADExAUnwdEM51R3Yhfc")
    elif message.text == "CS":
        await message.answer("https://youtube.com/playlist?list=PLBlnK6fEyqRhqzJT87LsdQKYZBC93ezD")
    elif message.text == "PS":
        await message.answer("https://youtube.com/playlist?list=PLBlnK6fEyqRi17rO6B3_XHtMqAKXQ0Tp4")
    elif message.text == "DE":
        await message.answer("https://youtube.com/playlist?list=PLBlnK6fEyqRjMH3mWf6kwqiTbT798eAOm")
    elif message.text == "EM":
        await message.answer("https://youtube.com/playlist?list=PLp6ek2hDcoNCANsWM2mw3qi0387BhfLyV")
    elif message.text == "PE":
        await message.answer("https://youtube.com/playlist?list=PLgwJf8NK-2e5Hnu82T1CYLZ8kbZs4Jx8x")
    elif message.text == "S&S":
        await message.answer("https://youtube.com/playlist?list=PLBlnK6fEyqRhG6s3jYIU48CqsT5cyiDTO")

    # .............CIVIL...................

    elif message.text == "MOS":
        await message.answer("https://youtube.com/playlist?list=PLACnzDzyaitaL0OQgPn3w0ZM6bIFzPSsA")
    elif message.text == "FM&HM":
        await message.answer("https://youtube.com/playlist?list=PLACnzDzyaitZGIic1K_y8OMu-WLvTfmiu")
    elif message.text == "BM&C":
        await message.answer("https://youtube.com/playlist?list=PLk7ptZcI9vmhBh7evUtxAbHe3Ojs_099H")
    elif message.text == "SS":
        await message.answer("https://youtube.com/playlist?list=PLm_MSClsnwm9zs1zCObw4xd57v77mYA1z")
    elif message.text == "SA":
        await message.answer("https://youtube.com/playlist?list=PLDN15nk5uLiAyM7MbRBF1eIFC8y5vMRxI")
    elif message.text == "EM":
        await message.answer("https://youtube.com/playlist?list=PLDN15nk5uLiAyM7MbRBF1eIFC8y5vMRxI")
    elif message.text == "DOCS":
        await message.answer("https://youtube.com/playlist?list=PLlwCCCn9O0b2FXG10IAHpULgMR3f4mkFr")
    elif message.text == "Bye":
        await message.answer("keep learning...bye")
    elif message.text == "bye":
        await message.answer("keep learning...bye")
    else:
        await message.answer(f'invalid command : {message.text} -please enter a valid command')
dp.start_polling()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
