__author__ = "Swapnik"
import uuid
from models.post import Post
import datetime
from database import Database

class Blog(object):
    def __init__(self, author, title, description, id = None):
        self.author = author
        self.title = title
        self.description = description
        self.id = uuid.uuid4().hex if id is None else id

    def new_post(self):
        title = input("Enter post title: ")
        content = input("Enter post Content: ")
        date = input("Enter post date, or leave blank for today (DDMMYYYY): ")
        post = Post(blog_id = self.id, \
            title = title, content = content, \
                date = datetime.datetime.utcnow() if "" else datetime.datetime.strptime(date, "%d%m%Y"))

        post.save_to_mongo()

    def get_posts(self):
        return Post.from_blog(self.id)

    def save_to_mongo(self):
        Database.insert(collection = 'blogs', data = self.json())

    def json(self):
        return{
            'author': self.author, 
            'title': self.title, 
            'description': self.description, 
            'id': self.id
        }

    @classmethod
    def get_from_mongo(cls, self):
        blog_data = Database.find_one(collection='blogs', query = {'id': id})

        return cls(author = blog_data['author'], title = blog_data['title'],
        description=blog_data['description'], id = blog_data['id'])