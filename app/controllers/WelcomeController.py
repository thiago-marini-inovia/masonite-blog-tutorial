"""A WelcomeController Module."""
from masonite.views import View
from masonite.controllers import Controller
from masonite.inertia import Inertia


class WelcomeController(Controller):
    """WelcomeController Controller Class."""

    def show(self, view: Inertia):
        return view.render('Index')
