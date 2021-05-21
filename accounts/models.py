from django.db import models
from address.models import AddressField
from django.db.models.deletion import CASCADE
# from phonenumber_field.modelfields import PhoneNumberField


class Account(models.Model):
    user_creation_date = models.DateTimeField(auto_now_add=True)
    form_signed_date = models.DateTimeField()
    is_client = models.BooleanField()
    is_patient = models.BooleanField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    initials = models.CharField(max_length=3)
    full_name = models.CharField(max_length=300)
    date_of_birth = models.DateTimeField()
    email = models.EmailField()
    username = models.CharField(max_length=50)
    home_address = AddressField(related_name='+', blank=True, null=True)
    # home_phone = PhoneNumberField()
    # cell_phone = PhoneNumberField()

class AccountOptions(models.Model):
    account = models.ForeignKey(Account, on_delete=CASCADE)
    sex = models.CharField(max_length=100)

class AccountChoices(models.Model):
    accountoptions = models.ForeignKey(AccountOptions, on_delete=models.CASCADE)
    male = models.CharField(max_length=4)
    female = models.CharField(max_length=6)  




    
    