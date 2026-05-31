from flask import Flask, request, render_template_string
import sys
import builtins

# Создаем "заглушку" для input, которая не будет спрашивать, а просто вернет пустоту или число
def fake_input(prompt=None):
    return "1"  # Это значение будет подставляться везде, где программа просит ввод

builtins.input = fake_input

# Теперь импортируем твой файл
import kara
import кара  # Мы импортируем твой кара.py как модуль

app = Flask(name)

@app.route('/')
def home():
    return "<h1>Кармион калькулятор работает!</h1>"

if name == 'main':
    app.run()
