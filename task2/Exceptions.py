class CustomException(Exception):
    def __str__(self):
        return self.__class__.__name__


class KillError(CustomException):
    pass


class DrunkError(CustomException):
    pass


class CarCrashError(CustomException):
    pass


class GluttonyError(CustomException):
    pass


class DepressionError(CustomException):
    pass