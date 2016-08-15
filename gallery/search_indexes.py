import datetime
from haystack import indexes
from .models import Portfolio


class PortfolioIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    writer = indexes.CharField(model_attr='writer')
    created_date = indexes.DateTimeField(model_attr='created_date')

    def get_model(self):
        return Portfolio

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(created_date__lte=datetime.datetime.now())