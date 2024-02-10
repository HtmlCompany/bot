from personal_assistant.services.utils.field import Field


class Tag(Field):
    @Field.value.setter
    def value(self, value):
        self._value: str = self._value_validation(value)

    @staticmethod
    def _value_validation(value: str) -> str:
        if len(value) > 30:
            raise ValueError(f"Tag '{value}' is not valid.\n"
                             f"Tag length must be up to 30 characters.")

        return value
