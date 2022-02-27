from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from UserAccountsApp.models import CustomUser, UserProfile


@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user = instance)
        print("sender", sender)


@receiver(post_save, sender = User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
    print('instance: ', instance)


# @receiver(user_logged_in, sender=User)
# def login_success(sender, request, user, **kwargs):
#     print("User logged in")
#     ip=request.META.get['REMOTE_ADDR']
#     print('Login cliend IP address: ',ip)
#     request.session['ip'] = ip

