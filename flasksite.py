from flask import Flask, render_template, request
from main import hhapi

app = Flask(__name__)


@app.route("/")
def index():
    #
    context = {
        'name': 'Bobovich Dmitry',
        'create_date': "08.11.2023"
    }

    return render_template('index_flask.html', **context)
    # return render_template('index.html', main_data=main_data, name='Leo', age=99)


@app.route('/contacts/')
def contacts():
    # где то взяли данные
    context = {
        'name': 'Bobovich Dmitry',
        'create_date': "08.11.2023"
    }
    # Контекст name=developer_name - те данные, которые мы передаем из view в шаблон
    # context = {'name': developer_name}
    # Словарь контекста context
    # return render_template('contacts.html', context=context)
    return render_template('contacts_flask.html', **context)


@app.route('/results/', methods=['GET'] )
def results():
    with open('output.txt', 'r', encoding="UTF-8") as f:
        text = f.read()
    #print(text)
    return render_template('results_flask.html', text=text)


@app.route('/run/', methods=['GET'])
def run_get():
    #with open('output.txt', 'r', encoding="UTF-8") as f:
        #text = f.read()
    return render_template('form_flask.html')
    # with open('main.txt', 'a') as f:
    #     f.write('hello')


@app.route('/run/', methods=['POST'])
def run_post():
    # Как получть данные формы
    text = request.form['input_text']
    hhapi(text)
    with open('output.txt', 'a') as f:
        f.write(f'{text}\n')
    with open('output.txt', 'r', encoding="UTF-8") as f:
        text = f.read()
    #print(text)

    return render_template('results_flask.html', text=text)
    #return render_template('results_flask.html')


if __name__ == "__main__":
    app.run(debug=True)