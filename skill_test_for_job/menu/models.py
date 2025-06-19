from django.db import models
from django.core.exceptions import ValidationError
import json


def validate_json(value):
    try:
        json.loads(value)
    except ValueError as e:
        raise ValidationError(f"Невалидный JSON: {e}")


class Menu(models.Model):
    name = models.CharField(max_length=20)
    fields = models.TextField(validators=[validate_json])
