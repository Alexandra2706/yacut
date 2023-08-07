from flask import jsonify, request
from http import HTTPStatus

from . import app, db
from yacut.consts import SYMBOLS_FOR_URL, SHORT_MAX_SIZE
from yacut.error_handlers import InvalidAPIUsage
from yacut.models import URLMap
from yacut.utils import get_unique_short_id


@app.route('/api/id/', methods=['POST'])
def create_short():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса',
                              HTTPStatus.BAD_REQUEST)
    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!',
                              HTTPStatus.BAD_REQUEST)
    if not data.get('custom_id'):
        data['custom_id'] = get_unique_short_id()
    if len(data['custom_id']) > SHORT_MAX_SIZE:
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки',
                              HTTPStatus.BAD_REQUEST)
    if (
            data.get('custom_id') and
            URLMap.query.filter_by(short=data['custom_id']).first() is not None
    ):
        raise InvalidAPIUsage(f'Имя "{data["custom_id"]}" уже занято.',
                              HTTPStatus.BAD_REQUEST)
    for char in data.get('custom_id'):
        if char not in SYMBOLS_FOR_URL:
            raise InvalidAPIUsage(
                'Указано недопустимое имя для короткой ссылки',
                HTTPStatus.BAD_REQUEST)

    url_map = URLMap()
    url_map.from_dict(data)
    db.session.add(url_map)
    db.session.commit()
    return jsonify(url_map.to_dict()), HTTPStatus.CREATED


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def view_url(short_id):
    url = URLMap.query.filter_by(short=short_id).first()
    if url is None:
        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify({'url': url.original}), HTTPStatus.OK
