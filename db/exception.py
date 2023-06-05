
class DatabaseException(Exception):
    """Exception raised when there is an issue with the db"""
    def __init__(self, error):
        self.message = "Database Error"
        self.error = error

    def __str__(self):
        return str(f'{self.message}: {self.error}')
