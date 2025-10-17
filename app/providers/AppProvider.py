from masonite.providers import Provider


class AppProvider(Provider):
    def __init__(self, application):
        self.application = application

    def register(self):
        pass

    wsgi = False

    def boot(self):
        pass
        # add shared data
        # def get_auth():
        #     user = auth.user()
        #     if user:
        #         return {
        #             'user': {
        #                 'id': user.id,
        #                 'first_name': user.first_name,
        #                 'last_name': user.last_name,
        #                 'email': user.email,
        #                 'role': user.role,
        #                 'account': {
        #                     'id': user.account.id,
        #                     'name': user.account.name
        #                 }
        #             }
        #         }
        #     else:
        #         return {'user': None}

        # self.app.make('Inertia').share({
        #     'auth': get_auth
        # })
