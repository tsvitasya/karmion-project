from flask import Flask, request, render_template_string
import кара  # Мы импортируем твой кара.ру как модуль

app = Flask(name)

@app.route('/')
def home():
    return "<h1>Кармион калькулятор работает!</h1>"

if name == 'main':
    app.run()
