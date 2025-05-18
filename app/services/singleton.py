class SingletonMeta(type):
    """
    This is a metaclass that ensures that any class that uses it
    will have only one instance (singleton).
    """
   
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
