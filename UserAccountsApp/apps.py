from django.apps import AppConfig


class UseraccountsappConfig(AppConfig):
    name = 'UserAccountsApp'
    
    def ready(self):
        import UserAccountsApp.signals
