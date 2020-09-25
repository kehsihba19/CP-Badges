import flask
import pybadges
from data import get_info
from flask import request

app = flask.Flask(__name__)
app.url_map.strict_slashes = False

logos = {
    'codeforces': 'https://lh3.googleusercontent.com/WsR_f03nbqW3qZjCZeXUYmnmhSWXo3hQhLX9hgl9QHydCgbXQi_VJeAwnmtuIgTHKdQ',
    'codechef': 'https://i.pinimg.com/originals/c5/d9/fc/c5d9fc1e18bcf039f464c2ab6cfb3eb6.jpg',
    'atcoder': 'https://img.atcoder.jp/assets/atcoder.png',
    'topcoder': 'https://raw.githubusercontent.com/donnemartin/interactive-coding-challenges/master/images/logo_topcoder.png',
    'yukicoder': 'https://pbs.twimg.com/profile_images/875757061669232640/T1_mPQuO_400x400.jpg'
}

website_text = {
    'atcoder': 'AtCoder',
    'codechef': 'Codechef',
    'codeforces': 'Codeforces',
    'topcoder': 'TopCoder',
    'yukicoder': 'YukiCoder'
}


@app.route("/<website>/<handle>")
def get_badge(handle, website):
    q = None or request.args.get('logo')
    display_logo = True if (q and q.lower() == 'true') else False
    logo = logos[website]
    x = get_info(handle, website)
    rating, color = str(x[0]), str(x[1])
    text = website_text[website.lower()]
    if display_logo:
        badge = pybadges.badge(left_text=text, right_text=rating, right_color=color, logo=logo, embed_logo=True)
    else:
        badge = pybadges.badge(left_text=text, right_text=rating, right_color=color)
    response = flask.make_response(badge)
    response.content_type = 'image/svg+xml'
    return response


@app.route("/")
def home():
    return "This API is working."


@app.errorhandler(404)
def page_not_found(error):
    return "This user doesn't exists."


if __name__ == "__main__":
    # app.debug = True
    app.run()
