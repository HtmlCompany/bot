from personal_assistant.services.utils.field import Field


class Text(Field):
    @Field.value.setter
    def value(self, value):
        self._value: str = self._value_validation(value)

    @staticmethod
    def _value_validation(value: str) -> str:
        if len(value) > 5000:
            raise ValueError(f"Text '{value}' is not valid.\n"
                             f"The length of the text must not exceed 5000 characters")

        return value
