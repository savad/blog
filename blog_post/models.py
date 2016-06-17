from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

from django_extensions.db.fields import AutoSlugField
from ckeditor.fields import RichTextField


class Tag(models.Model):
    name = models.CharField(max_length=128)
    slug = AutoSlugField(populate_from='name', unique=True)

    def __unicode__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', max_length=255, editable=True, unique=True)
    image = models.ImageField(null=True, blank=True)
    small_description = models.TextField(null=True, blank=True)
    description = RichTextField()
    tags = models.ManyToManyField(Tag)
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})
