from flask import Flask, render_template
import flask_alchemy_orm
app = Flask(__name__, template_folder='templates')

@app.route('/')
def startpage():
    title = 'каталог магазина'
    names = flask_alchemy_orm.text_names.split('\n')
    prices = flask_alchemy_orm.text_prices.split('\n')
    images = flask_alchemy_orm.text_images.split('\n')
    data = zip(names, prices, images)

    return render_template("catalog_alchemy_orm.html", title=title, data=data)

@app.route('/contacts.html')
def contacts():
    return render_template('contacts.html')

if __name__ == '__main__':
    app.run('0.0.0.0')
