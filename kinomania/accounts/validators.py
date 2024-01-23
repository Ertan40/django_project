from django.core.exceptions import ValidationError



def validate_only_letters(input):
    for char in input:
        if not char.isalpha():
            raise ValidationError("Name must be only letters.")