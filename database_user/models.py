from utility.database_utility import *

# extend user model for extra information
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now, editable=False)

    about = models.CharField(max_length=255, null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    address = models.ForeignKey(to="database_general.Address", on_delete=models.SET_NULL, null=True, blank=True, related_name="user_address")

    college = models.ForeignKey(to="database_main.College", on_delete=models.SET_NULL, null=True, blank=True, related_name="user_college")
    identifier = models.CharField(max_length=255, null=True, blank=True)

    user_role = models.ForeignKey(to="database_general.Tag", on_delete=models.SET_NULL, null=True, blank=True, related_name="user_role")

    def __str__(self) -> str:
        return self.get_full_name()