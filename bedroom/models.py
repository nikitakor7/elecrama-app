from django.db import models
from django.utils import timezone
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class bedroom(models.Model):
    created = models.DateTimeField(default=lambda: timezone.localtime(timezone.now()))
    switch = models.CharField(max_length=100, blank=True, default='Switch1')
    status = models.BooleanField('ON', default=True)
    current_value = models.CharField(max_length=100, blank=True, default='128')

    class Meta:
        ordering = ('created',)
        


    
