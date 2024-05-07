from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator
import re

class CustomPasswordValidator(BaseValidator):
    def __init__(self, *args, **kwargs):
        super().__init__(limit_value=object,*args, **kwargs)
        self.regex = re.compile(r'\d')  # Regular expression to check for numeric characters

    def __call__(self, value):
        if len(value) < 8:
            raise ValidationError(
                'رمز عبور باید حداقل شامل ۸ کاراکتر باشد.',
                code=self.code,
            )

        if value.isdigit():
            raise ValidationError(
                'رمز عبور نباید فقط شامل اعداد باشد',
                code=self.code,
            )
