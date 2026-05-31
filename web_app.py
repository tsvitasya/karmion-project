from flask import Flask, request, render_template_string, session, redirect, url_for
import kara

app = Flask(name)
# Это секретный ключ для защиты сессии
app.secret_key = 'karmion_secret_key_2026'

# Данные для входа
USERNAME = 'admin'
PASSWORD = 'Karmion2026'

# Страница входа
login_html = """
<html>
    <body style="font-family: sans-serif; text-align: center; margin-top: 50px;">
        <h2>Вход в Karmion</h2>
        <form method="post" action="/login">
            <input type="text" name="username" placeholder="Логин" required><br><br>
            <input type="password" name="password" placeholder="Пароль" required><br><br>
            <button type="submit">Войти</button>
        </form>
    </body>
</html>
"""

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == USERNAME and request.form['password'] == PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('home'))
        return "Неверный логин или пароль! <a href='/login'>Попробовать еще раз</a>"
    return login_html

@app.route('/')
def home():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    # Сюда мы добавим вызов функции из kara.py, когда ты будешь готова
    return "Доступ разрешен! Система Karmion готова к работе."

if name == 'main':
    app.run()
