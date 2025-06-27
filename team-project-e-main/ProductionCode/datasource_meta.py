'''This is for the singleton pattern implementation in Python. 
This code is based on refactoring guru's python singleton example.
https://refactoring.guru/design-patterns/singleton/python/example'''

class DataSourceMeta(type):
    """
    Using metaclass to implement the Singleton pattern.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Create an instance of the DataSource class if it does not already exist.
        Otherwise, return the existing instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
