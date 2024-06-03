# from datetime import datetime
# import db
#
# class Post(db.Model):
#     __tablename__ = 'posts'
#     id = db.Column(db.Integer(), primary_key=True)
#     title = db.Column(db.String(255), nullable=False)
#     description = db.Column(db.Text, nullable=False)
#     created_on = db.Column(db.DateTime(), default=datetime.utcnow)
#     person = db.Column(db.String(255), nullable=False)
#
#     def __repr__(self):
#         return '<Post %r>' %self.id