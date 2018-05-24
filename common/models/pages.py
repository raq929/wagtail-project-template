from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField

from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index


class PersonPage(Page):
    photo = models.ForeignKey(
        'common.CustomImage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    bio = RichTextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('bio'),
        FieldPanel('website'),
        ImageChooserPanel('photo'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('bio'),
    ]
