from django.db import models
from django.http import HttpResponse
import logging


logger = logging.getLogger(__name__)


class Poem(models.Model):
    title = models.CharField(max_length=200)
    dynasty = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    content = models.TextField()


#
def poem_list(request):
    logger.info('poem_list')
    return "poem_list"
