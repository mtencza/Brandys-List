#models.py
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import CharField
from django.db.models import UUIDField
from django_extensions.db.fields import AutoSlugField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields
import uuid

class Category(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)


    class Meta:
        ordering = ('-pk',)
        verbose_name_plural = "categories"

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('home_category_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('home_category_update', args=(self.slug,))

    def __str__(self):
        return self.name


class ServiceProvider(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)

    # Relationship Fields
    services = models.ManyToManyField(
        'home.Service',
        related_name="serviceproviders", 
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('home_serviceprovider_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('home_serviceprovider_update', args=(self.slug,))

    def __str__(self):
        return self.name


class Service(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)

    # Relationship Fields
    Category = models.ForeignKey(
        'home.Category',
        on_delete=models.CASCADE, related_name="services", 
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('home_service_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('home_service_update', args=(self.slug,))

    def __str__(self):
        return self.name


