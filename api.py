# from flask import jsonify, request
# from models import Post
# from flask_restful import abort
# from pytz import unicode

# @app.route('/tasks', methods=['GET'])
# def get_tasks():
#     lis = []
#     items = Post.query.all()
#     for d in items:
#         lis.append({"id": d.id, "title": d.title, "description": d.description, "created_on": d.created_on, "person": d.person})
#     return jsonify({'tasks': lis})
#
# @app.route('/tasks/<int:task_id>', methods=['GET'])
# def get_task(task_id):
#     lis = []
#     vor = {}
#     items = Post.query.get(task_id)
#     vor.update(id=items.id, title=items.title, description=items.description, created_on=items.created_on, person=items.person)
#     lis.append(vor)
#     return jsonify({'tasks': vor})
#

# def create_task():
#     title = request.json.get('title')
#     description = request.json.get('description')
#     existing_person = Post.query \
#         .filter(Post.title == title) \
#         .filter(Post.description == description) \
#         .one_or_none()
#     if existing_person is None:
#         p = Post(title=request.json['title'], description=request.json['description'], person=request.json['person'])
#         db.session.add(p)
#         db.session.commit()
#         return 'Успешно!'
#     else:
#         return "Дубль!", 409
#

# def update_task(task_id):
#     vor = {}
#     if task_id == 0:
#         abort(404)
#     if not request.json:
#         abort(400)
#     if 'title' in request.json and type(request.json['title']) != unicode:
#         abort(400)
#     if 'description' in request.json and type(request.json['description']) is not unicode:
#         abort(400)
#     if 'done' in request.json and type(request.json['done']) is not bool:
#         abort(400)
#     p = Post.query.get(task_id)
#     p.title = request.json['title']
#     p.description = request.json['description']
#     p.person = request.json['person']
#     db.session.commit()
#     f = Post.query.get(task_id)
#     vor.update(id=f.id, title=f.title, description=f.description, created_on=f.created_on,
#                person=f.person)
#     return jsonify({'task': vor})
#

# def delete_task(task_id):
#     x = Post.query.get(task_id)
#     db.session.delete(x)
#     db.session.commit()
#     return 'Успешно!'
#
# app.ru()
