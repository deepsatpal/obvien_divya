from django.db import models

# Create your models here.
class UserTag(models.Model):
    id = models.AutoField(primary_key=True)
    #contact = models.ForeignKey('Contact', related_name="user_tags", on_delete=models.CASCADE,)
    contact_id = models.IntegerField(max_length=11)
    user_id = models.IntegerField(max_length=11)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "user_tags"