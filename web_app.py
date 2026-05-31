from flask import Flask, request, session, redirect, url_for
import kara

app = Flask(name)
app.secret_key = 'karmion_secret_key_2026'

USERNAME = 'admin'
PASSWORD = 'Karmion2026'

# Страница с формой для ввода даты
home_html = """
<html>
    <body style="font-family: sans-serif; text-align: center; margin-top: 50px;">
        <h2>Система Karmion: Расчет</h2>
        <form method="post" action="/calculate">
            <input type="number" name="day" placeholder="День" required><br><br>
            <input type="number" name="month" placeholder="Месяц" required><br><br>
            <input type="number" name="year" placeholder="Год" required><br><br>
            <button type="submit">Рассчитать</button>
        </form>
    </body>
</html>
"""

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form.get('username') == USERNAME and request.form.get('password') == PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('home'))
        return "Неверный логин или пароль! <a href='/login'>Назад</a>"
    return '<form method="post">Логин: <input type="text" name="username"><br>Пароль: <input type="password" name="password"><br><button type="submit">Войти</button></form>'

@app.route('/')
def home():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return home_html

@app.route('/calculate', methods=['POST'])
def calculate():
    import kara
    import sys
    import io
    
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    day = request.form.get('day')
    month = request.form.get('month')
    year = request.form.get('year')

    buffer = io.StringIO()
    sys.stdout = buffer
    
    try:
        kara.user_day = int(day)
        kara.user_month = int(month)
        kara.user_year = int(year)
    except Exception as e:
        sys.stdout = sys.stdout
        return f"Ошибка данных: {str(e)}"
    
    sys.stdout = sys.stdout
    return f"<pre>{buffer.getvalue()}</pre>"

if name == 'main':
    app.run()
