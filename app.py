from flask import Flask, render_template

app = Flask(__name__)


# Create Index Page
@app.route('/')
def index():
	first_name = "Eric"
	favorite_pizza = ["Mushrooms", "Green Peppers", "Fresh Garlic", "Fresh Mozzarella"]
	return render_template('index.html',
		f_name = first_name,
		favorite_pizza = favorite_pizza)

# Create About Page
@app.route('/about')
def about():
		return render_template('about.html')

# Create Calendar Page
@app.route('/calendar')
def calendar():
		return render_template('calendar.html')