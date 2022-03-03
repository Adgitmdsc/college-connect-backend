from utility.database_utility import *

class Address(models.Model):
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now, editable=False)

    address_line_1 = models.CharField(max_length=255, null=True, blank=True)
    address_line_1 = models.CharField(max_length=255, null=True, blank=True)
    address_line_1 = models.CharField(max_length=255, null=True, blank=True)

    address_city = models.CharField(max_length=255, null=True, blank=True)
    address_state = models.CharField(max_length=255, null=True, blank=True)

    address_state = models.CharField(max_length=255, null=True, blank=True)

class Tag(models.Model):
    tag_name = models.CharField(max_length=25, unique=True)
    tag_type = models.CharField(max_length=25, unique=True)

    def __str__(self) -> str:
        return self.tag_name