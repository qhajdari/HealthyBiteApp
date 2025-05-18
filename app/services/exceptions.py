class InvalidRecipeException(Exception):
    def __init__(self, message="The recipe is invalid. Please fill in all fields."):
        self.message = message
        super().__init__(self.message)
