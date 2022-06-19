from django.db import models


# Create your models here.
class Accounts(models.Model):
    account_name = models.CharField(max_length=50)    #the name of the account owner
    pub_key = models.CharField(max_length=100)         #public key of this account
    acc_add = models.CharField(max_length=100)         #private key of this account

    def __str__(self) -> str:
        """
        return the dictionary in which the key is the name of the account and the values is a tuple of public key and private key of the specified address
        """
        return self.pub_key