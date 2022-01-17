from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.crypto import get_random_string
import uuid

class FakeUser(models.Model):
    username = models.CharField(max_length= 40, null= False, blank= False)
    email = models.EmailField(max_length= 50, null= False, blank= True)
    password = models.CharField(max_length= 8, default= uuid.uuid4().hex[:8])

    def __str__(self):
        return self.username

class PersonalInformation(models.Model):
    user = models.OneToOneField(FakeUser, on_delete= models.CASCADE, related_name= 'personal_information')
    name = models.CharField(max_length= 20)
    lastname = models.CharField(max_length= 20)
    phone = models.CharField(max_length=9)

    def __str__(self):
        return f'{self.name} {self.lastname}'

class Address(models.Model):
    user = models.OneToOneField(FakeUser, on_delete= models.CASCADE, related_name= 'address')
    city = models.CharField(max_length= 30)
    street = models.CharField(max_length=50)
    zip_code = models.CharField(max_length= 10)

    def __str__(self):
        return f'{self.city} {self.street}'

class FakeToken(models.Model):
    key = models.CharField(max_length= 32)
    user = models.OneToOneField(FakeUser, on_delete= models.CASCADE, related_name= 'token')

    def __str__(self):
        return self.key

    # https://stackoverflow.com/questions/25943850/django-package-to-generate-random-alphanumeric-string/25949808


# signals

@receiver(post_save, sender = FakeUser)
def create_fake_token(sender, instance, created, **kwargs):
    if created:
        # esto al parecer solo se activa cuando la instancia se crea solo en ese caso
        string = get_random_string(length= 32)
        FakeToken.objects.create(key = string, user = instance)
        # print('exito token')
    
    #lo que esta aqui deberia ejecutarse cada vez que se guarda o seo supongo, esso podriamos ponerlo en un else
    # print('error token')