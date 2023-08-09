from flask import flash, redirect, render_template, url_for

from . import app, db
from yacut.forms import URLForm
from yacut.models import URLMap
from yacut.constants import SYMBOLS_FOR_URL, SHORT_MAX_SIZE
from yacut.utils import get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLForm()
    if not form.validate_on_submit():
        return render_template('yacut.html', form=form)
    short = form.custom_id.data
    if not short:
        short = get_unique_short_id()
    if URLMap.query.filter_by(short=short).first() is not None:
        flash(f'Имя {short} уже занято!')
        return render_template('yacut.html', form=form)
    if len(short) > SHORT_MAX_SIZE:
        flash('Максимальный длина ссылки 16 символов')
        return render_template('yacut.html', form=form)
    for char in short:
        if char not in SYMBOLS_FOR_URL:
            flash('Ссылка содержит недопустимые символы')
            return render_template('yacut.html', form=form)
    url_map = URLMap(original=form.original_link.data, short=short)
    db.session.add(url_map)
    db.session.commit()
    short_url = url_for('short_view', short=short, _external=True)
    flash('Ваша новая ссылка готова<br>' + '<a href="' + short_url + '">' + short_url + '</a>')
    return render_template('yacut.html', form=form)


@app.route('/<string:short>', methods=['GET'])
def short_view(short):
    url_map = URLMap.query.filter_by(short=short).first_or_404()
    return redirect(url_map.original)
