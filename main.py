#! /usr/bin/python3

import urwid


# ------------------------------------------
# Функции выхода
def exit_program(button):
    raise urwid.ExitMainLoop()


def exit_on_f10(key):
    if key == 'f10':
        raise urwid.ExitMainLoop()


# Функция для скрытия окна и запуска основного интерфейса
def start_app(button):
    loop.widget = screen  
    # Меняем виджет в главном цикле на основное окно


# ------------------------------------------
# Пример ('name','font','them')
palette = [
    ('phone_palitr', 'black', 'dark blue'),
    ('normal_palitr', 'black', 'light cyan'),
    ('button_palitr', 'black', 'light cyan'),
    ('warning_palitr', 'black', 'yellow'),
]

# ------------------------------------------
# Основное окно
body = urwid.AttrMap(urwid.Text("Тест интерфейса", align="center"), 'normal_palitr')
button = urwid.AttrMap(urwid.Button("Выход [F10]", exit_program), 'button_palitr')

# Создаём основной каркас интерфейса
frame = urwid.Frame(
    body=urwid.Filler(body),
    footer=urwid.Padding(button, align='center')
)

# Оборачиваем всё в AttrMap, чтобы применить общий фон
screen = urwid.AttrMap(frame, 'phone_palitr')

# ------------------------------------------
# Диалоговое окно
warning_text = urwid.Text(
    "Мы полагаем, что ваш системный администратор изложил вам основы\n"
    "безопасности. Как правило, всё сводится к трём следующим правилам:\n\n"
    "№1) Уважайте частную жизнь других.\n"
    " №2) Думайте, прежде что-то вводить.\n"
    "                      №3) С большой властью приходит большая ответственность.\n",
    align="center"
)
accept_button = urwid.Button("Принять", start_app)
cancel_button = urwid.Button("Отклонить", exit_program)

# Размещаем кнопки
button_row = urwid.Columns([
    urwid.Padding(urwid.AttrMap(accept_button, 'button_palitr'), align='center', width=13),
    urwid.Padding(urwid.AttrMap(cancel_button, 'button_palitr'), align='center', width=13)
])

# окно в рамке
warning_box = urwid.LineBox(
    urwid.Pile([warning_text, button_row]), title="⚠ Внимание!"
)

# наложение окна поверх основного интерфейса
overlay = urwid.Overlay(
    warning_box,  # palette
    screen,       # Основное приложение
    align='center', width=('relative', 50),   # Выравнивание и ширина окна
    valign='middle', height=('relative', 30)
)

# ------------------------------------------
# Run
loop = urwid.MainLoop(overlay, palette=palette, unhandled_input=exit_on_f10)
loop.run()