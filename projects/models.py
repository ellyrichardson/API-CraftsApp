# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

# model for posting projects
class Posts(models.Model):
    id = models.AutoField(primary_key=True)
    #user = models.ForeignKey('Users', models.DO_NOTHING)
    post_title = models.CharField(max_length=255)
    post_content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    post_media = models.TextField(blank=True, null=True)
    post_user = models.IntegerField(blank=True, null=True)

    def __str__(self):
        # A string representation of the model.
        return self.post_title
