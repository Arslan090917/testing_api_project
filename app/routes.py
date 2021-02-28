import datetime
import json
import random
import re
import string
import traceback

from app import app, db
from flask import request, jsonify
from xml.etree import ElementTree
from app.models import Books, Prices, Magazines

@app.before_request
def log_request_info():
    app.logger.info('Request: {} {}'.format(request.method, request.path))
    app.logger.info('Request headers: %s', request.headers)
    app.logger.info('Request body: %s', request.get_data().decode('utf8'))


@app.after_request
def log_response_info(response):
    app.logger.info('Response status: {}'.format(response.status))
    app.logger.info('Response body: %s', response.get_data().decode('utf8'))
    return response

@app.after_request
def apply_caching(response):
    response.headers['Content-Type'] = 'text/xml;charset=UTF-8'
    return response

@app.route('/book/new', methods=['POST'])
def add_new_book():
    json_data = json.loads(request.data.decode())
    answer = 'Книга была успешно добавлена на склад'
    book = Books()
    book.Name = json_data['name']
    book.Genre = json_data['gengre']
    book.Price = json_data['price']
    book.Count = json_data['count']
    book.Magazine = json_data['magazine']
    book.isAvailable = json_data['isAvailable']
    db.session.add(book)
    db.session.commit()
    return answer, 200

@app.route('/book', methods=['GET'])
def get_book():
    """
    Метод для просмотра книг
    """
    try:
        id = request.args.get('id')
        book = db.session.query(Books).filter_by(Id=id).one()
        json_data = {
            'name': book.Name,
            'gengre': book.Genre,
            'price': book.Price,
            'count': book.Count,
            'Magazine': book.Magazine,
            'is_available': book.isAvailable
        }
        return jsonify(json_data), 200
    except Exception:
        answer = traceback.format_exc()
        return answer, 500


@app.route('/book', methods=['DELETE'])
def delete_book():
    """
    Метод для просмотра книг
    """
    try:
        id = request.args.get('id')
        book = db.session.query(Books).filter_by(Id=id).one()
        db.session.delete(book)
        db.session.commit()
        answer = 'Кинга {} была успешно удаленна'.format(book.Name)
        return answer, 200
    except Exception:
        answer = traceback.format_exc()
        return answer, 500


@app.route('/book', methods=['PUT'])
def change_name_book():
    """
    Метод для просмотра книг
    """
    try:
        id = request.args.get('id')
        json_data = json.loads(request.data.decode())
        book = db.session.query(Books).filter_by(Id=id).one()
        book.Name = json_data['name']
        book.Genre = json_data['gengre']
        book.Price = json_data['price']
        book.Count = json_data['count']
        book.Magazine = json_data['magazine']
        book.isAvailable = json_data['isAvailable']
        db.session.commit()
        answer = 'Параметры книги были успешно изменены'
        return answer, 200
    except Exception:
        answer = traceback.format_exc()
        return answer, 500