from flask import *
from item import *
app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def home_page():
    return render_template("home.html")
@app.route('/shop', methods=['POST','GET'])
def shop():
    necklace=Item("Necklace",12.5)
    keychain=Item("Keychain",5)
    hat=Item("Hat",20.67)
    hoodie=Item("Hoodie",30.55)
    items=[necklace,keychain,hat,hoodie]
    return render_template("shop.html",items=items)

if __name__ == '__main__':
   app.run(debug = True)