from flask import Flask, request, render_template
from pybadges import badge
from data import get_cf,get_cc,get_at
app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route("/")
def home():
	return "This API is working."

@app.route("/codeforces.svg")
def codeforces():
	user=request.args.get('user')
	logo='https://lh3.googleusercontent.com/WsR_f03nbqW3qZjCZeXUYmnmhSWXo3hQhLX9hgl9QHydCgbXQi_VJeAwnmtuIgTHKdQ'
	x = get_cf(user)
	rating,colour = x[0], x[1]
	s = badge(left_text='Codeforces', right_text=rating, right_color=colour,logo=logo)
	return s

@app.route("/codechef.svg")
def codechef():
	user=request.args.get('user')
	logo='https://i.pinimg.com/originals/c5/d9/fc/c5d9fc1e18bcf039f464c2ab6cfb3eb6.jpg'
	x = get_cc(user)
	rating,colour = x[0], x[1]
	s = badge(left_text='Codechef', right_text=rating, right_color=colour,logo=logo)
	return s

@app.route("/atcoder.svg")
def atcoder():
	user=request.args.get('user')
	logo='https://img.atcoder.jp/assets/atcoder.png'
	x = get_at(user)
	rating,colour = x[0], x[1]
	s = badge(left_text='Atcoder', right_text=rating, right_color=colour,logo=logo)
	return s


@app.errorhandler(404)
def page_not_found(error):
   return "This user doesn't exists."


if __name__ == "__main__":
    app.debug = True
    app.run()
