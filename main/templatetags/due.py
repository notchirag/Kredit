from django import template
from ..models import Entries
from datetime import date


register = template.Library()


@register.filter(name="due")
def due(entry):
    entry = Entries.objects.get(id=entry.id)

    due = str(entry.due_date - date.today())
    if due == '0:00:00':
        days = 0
    else:
        days  = int(due.split(" ")[0])

    if days <= 0 : isOverdue = True
    
    return isOverdue