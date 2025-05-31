class RecipeExporter:
    def __init__(self, strategy=None):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def export(self, recipes):
        if not self.strategy:
            raise ValueError("Export strategy not set.")
        return self.strategy.export(recipes)
