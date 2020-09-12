import flask
import pybadges
from data import get_cf, get_cc, get_at, get_yuki

app = flask.Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def home():
    return "This API is working."


@app.route("/codeforces/<user>")
def codeforces(user):
    # logo='https://lh3.googleusercontent.com/WsR_f03nbqW3qZjCZeXUYmnmhSWXo3hQhLX9hgl9QHydCgbXQi_VJeAwnmtuIgTHKdQ'
    x = get_cf(user)
    rating, colour = x[0], x[1]
    badge = pybadges.badge(left_text='Codeforces', right_text=rating, right_color=colour)
    response = flask.make_response(badge)
    response.content_type = 'image/svg+xml'
    return response


@app.route("/codechef/<user>")
def codechef(user):
    # logo='https://i.pinimg.com/originals/c5/d9/fc/c5d9fc1e18bcf039f464c2ab6cfb3eb6.jpg'
    x = get_cc(user)
    rating, colour = x[0], x[1]
    badge = pybadges.badge(left_text='Codechef', right_text=rating, right_color=colour)
    response = flask.make_response(badge)
    response.content_type = 'image/svg+xml'
    return response


@app.route("/atcoder/<user>")
def atcoder(user):
    # logo='https://img.atcoder.jp/assets/atcoder.png'
    x = get_at(user)
    rating, colour = x[0], x[1]
    badge = pybadges.badge(left_text='Atcoder', right_text=rating, right_color=colour)
    response = flask.make_response(badge)
    response.content_type = 'image/svg+xml'
    return response


@app.route("/yukicoder/<user>")
def yukicoder(user):
    x = get_yuki(user)
    level, colour = x[0], x[1]
    badge = pybadges.badge(left_text='YukiCoder', right_text=level, right_color=colour)
    response = flask.make_response(badge)
    response.content_type = 'image/svg+xml'
    return response


@app.errorhandler(404)
def page_not_found(error):
    return "This user doesn't exists."


if __name__ == "__main__":
    # app.debug = True
    app.run()
