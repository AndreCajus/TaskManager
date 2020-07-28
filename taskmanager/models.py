#Instead of referring to User directly, you should reference the user model using django.contrib.auth.get_user_model()
#When you define a foreign key or many-to-many relations to the user model, you should specify the custom model using the AUTH_USER_MODEL setting.
from django.conf import settings
from django.db import models
from django.contrib.gis.db import models

# to create postgis extension
from django.contrib.postgres.operations import CreateExtension
from django.db import migrations

class Migration(migrations.Migration):
    operations = [ CreateExtension('postgis') ]


class Task(models.Model):

    class Categories(models.TextChoices):
        CONSTRUCTION        = 'CN', 'Consruction'
        SPECIAL_EVENT       = 'SE', 'Special Event'
        INCIDENT            = 'IC', 'Incident'
        WEATHER_CONDITION   = 'WC', 'Weather Condition'
        ROAD_CONDITION      = 'RC', 'Road Condition'

    class States(models.TextChoices):
        TO_VALIDATE         = 'TV', 'To Validate'
        VALIDATED           = 'VT', 'Validated'
        RESOLVED            = 'RV', 'Resolved'

    description         = models.CharField(verbose_name = 'Description', max_length=200, unique=True) #description unique to be used as url paramRV
    loc_geo             = models.PointField(verbose_name = 'Geographic Localization', null=True, blank=True)
    author              = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    creation_date       = models.DateTimeField(verbose_name = 'Creation Date', auto_now_add=True)
    update_date         = models.DateTimeField(verbose_name = 'Update Date', auto_now=True)
    states              = models.CharField(
        verbose_name = 'States',
        max_length=2,
        choices=States.choices,
        default=States.TO_VALIDATE,
    )
    category            = models.CharField(
        verbose_name = 'Category',
        max_length=2,
        choices=Categories.choices,
        default=Categories.CONSTRUCTION,
    )

    def __str__(self):
        return self.description
