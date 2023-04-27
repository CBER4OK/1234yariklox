from flask import Flask, render_template, request, redirect
import re
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    # Получаем данные из формы
    username = request.form['username']
    password = request.form['password']
    # Проверяем, что данные корректны
    f = open('info.txt', 'r')
    a = f.read()
    a1 = re.split(':|\n', a)
    for i in range((len(a1) // 2) - 1):
        if a1[i + 1] == username and a1[i + (len(a1) // 2) + 1] == password:
            return redirect('/redirect')
        else:
            return 'Неправильное имя пользователя или пароль'


@app.route('/redirect')
def redirect_to_yandex_disk():
    return redirect('https://disk.yandex.ru/d/aT-pSfiNNtjUrQ')


if __name__ == '__main__':
    app.run(debug=True)
