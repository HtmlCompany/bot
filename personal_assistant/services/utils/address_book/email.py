from re import search

from personal_assistant.services.utils.field import Field


class Email(Field):
    @Field.value.setter
    def value(self, value):
        self._value: str = self._value_validation(value)

    @staticmethod
    def _value_validation(email: str) -> str:

        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        email = search(pattern, email)

        if not email:
            raise ValueError(f"Email {email} is not valid")

        return email.group()
        