import factory
from faker import Faker
import wagtail_factories
from wagtail.core.rich_text import RichText

from common.models import (
    PersonPage,
)


fake = Faker()


class PersonPageFactory(wagtail_factories.PageFactory):
    class Meta:
        model = PersonPage

    parent = factory.SubFactory(wagtail_factories.PageFactory, parent=None)
    bio = factory.LazyAttribute(lambda _: RichText(fake.paragraph()))
