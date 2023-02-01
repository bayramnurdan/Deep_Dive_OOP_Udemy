class BaseValidator:
    """ Base Descriptor class """
    def __init__(self, minimum=None, maximum=None):   # Setting min and max  is not a must
        self.minimum = minimum
        self.maximum = maximum

    def __set_name__(self, owner, name):
        self.property_name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.property_name, None)

    def __set__(self, instance, value):
        self.validate(value)  # if everything is okay exception will not be raised. and each subclass will have its own method.
        instance.__dict__[self.property_name] = value


class IntegerField(BaseValidator):  # integer value is validated   # type is specified in class level

    def validate(self, value):
        if not isinstance(value, int):
            raise ValueError(f"{self.property_name} must be {self._type.__name__} type")
        if self.minimum is not None and value < self.minimum:
            raise ValueError(f"{self.property_name} must be greater than {self.minimum}")
        if self.maximum is not None and value > self.maximum:
            raise ValueError(f"{self.property_name} must be smaller than {self.maximum}")


class CharField(BaseValidator):  # length of string is validated

    def validate(self, value):
        if not isinstance(value, str):
            raise ValueError(f"{self.property_name} must be {self._type.__name__} type")
        if self.minimum is not None and len(value) < self.minimum:
            raise ValueError(f"{self.property_name} must be longer than {self.minimum} characters ")
        if self.maximum is not None and len(value) > self.maximum:
            raise ValueError(f"{self.property_name} must be shorter than {self.maximum} characters")


class Person:
    name = CharField(5, 10)
    age = IntegerField(0, 100)

    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person("Nurdan", -10)
print(p.__dict__)
