
from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort
from urllib.parse import urlparse

#from hyprnews.auth import login_required
from hyprnews.db import get_db

bp = Blueprint('news', __name__)

@bp.route('/')
def index():
    return render_template('news/index.html')


@bp.route('/article/<id>')
def article(id):
    a = get_article(id)
    parsed = urlparse(a["url"])
    #return f"<h1>{a["title"]}</h1><p>{a["body"]}</p>"
    return render_template("news/article.html", title=a["title"], body=a["body"], url=a["url"], domain=parsed.hostname)

##
# TODO - move this somewhere sensible
##
def get_article(id, check_author=True):
    article = get_db().execute(
        'SELECT id, created, title, body, url '
        'FROM news '
        'WHERE id = ?',
        (id,)
    ).fetchone()

    if article is None:
        abort(404, f"Article id {id} doesn't exist.")

    return article

def add_article(title, body, url):
    db = get_db()
    db.execute(
        'INSERT INTO news (title, body, url) VALUES (?, ?, ?)',
        (title, body, url)
    )
    db.commit()


@bp.route("/new", methods=["GET", "POST"])
def new_article():
    if request.method == "POST":
        title   = request.form.get("title")
        content = request.form.get("content")
        url     = request.form.get("url")

        if title and content:
            add_article(title, content, url)
            return redirect(url_for("index"))

    return render_template("news/form.html")