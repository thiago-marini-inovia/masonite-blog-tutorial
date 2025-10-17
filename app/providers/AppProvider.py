from masonite.providers import Provider
import os


class AppProvider(Provider):
    def __init__(self, application):
        self.application = application

    def register(self):
        pass

    wsgi = False

    def boot(self):
        # Share hot reloading status with all views (checked dynamically)
        from masonite.views import View
        view = self.application.make(View)
        
        def check_hot_reload():
            hot_file = os.path.join(os.getcwd(), 'storage/compiled/hot')
            return os.path.exists(hot_file)
        
        view.share({'hot': check_hot_reload})
        
        # Also share with Inertia (for the root template)
        try:
            inertia = self.application.make('Inertia')
            inertia.share({'hot': check_hot_reload})
        except:
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
