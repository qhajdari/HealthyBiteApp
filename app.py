from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///healthybite.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# We will temporarily insert the models here
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50))
    ingredients = db.Column(db.Text)
    instructions = db.Column(db.Text)
    prep_time = db.Column(db.Integer)

@app.route('/')
def index():
    recipes = Recipe.query.all()
    return render_template('index.html', recipes=recipes)

@app.route('/add', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        name = request.form['name']
        category = request.form['category']
        ingredients = request.form['ingredients']
        instructions = request.form['instructions']
        prep_time = int(request.form['prep_time'])

        recipe = Recipe(
            name=name,
            category=category,
            ingredients=ingredients,
            instructions=instructions,
            prep_time=prep_time
        )
        db.session.add(recipe)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_recipe.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
