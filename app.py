from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///shopp.db"
db = SQLAlchemy(app)


################ создание БД ###############

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    isActive = db.Column(db.Boolean, default=True)
    img = db.Column(db.Text, nullable=False)



    def __repr__(self):
        return self.title

################ ДОБАВЛЕНИЕ ДАННЫХ В БД  ###############
@app.route("/create", methods=["POST","GET"])
def create():
    if request.method == "POST":
        title = request.form['title']
        price = request.form['price']
        img = request.form['img']

        item=Item(title=title,price=price,img=img)
        try:
            db.session.add(item)
            db.session.commit()
            return redirect("/")
        except:
            "что то пошло не так"
    return render_template('create.html')

################ УДАЛЕНИЕ ДАННЫХ В БД  ###############

@app.route("/index/<int:id>/delete")
def delete(id):
    item=Item.query.get_or_404(id)

    try:
        db.session.delete(item)
        db.session.commit()
        return redirect("/")
    except:
        "что то пошло не так"






@app.route("/")
@app.route("/index")
def index():
    items=Item.query.order_by(Item.title).all()
    return render_template('index.html',data=items)


@app.route("/about")
def about():
    return render_template('about.html')





if __name__ in "__main__":
    app.run(debug=True)