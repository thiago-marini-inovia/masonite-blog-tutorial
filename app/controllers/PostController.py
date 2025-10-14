from masonite.controllers import Controller
from masonite.views import View
from app.models.Post import Post
from masonite.request import Request


class PostController(Controller):
    def show(self, view: View):
        posts = Post.all()

        return view.render('posts', {'posts': posts})

    def single(self, view: View, request: Request):
        post = Post.find(request.param('id'))

        return view.render('single', {'post': post})

    def store(self, request: Request):
        post = Post.find(request.param('id'))

        post.title = request.input('title')
        post.body = request.input('body')

        post.save()

        return 'post updated'

    def update(self, view: View, request: Request):
        post = Post.find(request.param('id'))

        return view.render('update', {'post': post})

    def delete(self, request: Request):
        post = Post.find(request.param('id'))

        post.delete()

        return 'post deleted'
