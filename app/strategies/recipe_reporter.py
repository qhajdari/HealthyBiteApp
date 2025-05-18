class RecipeExporter:
    def __init__(self, strategy: ExportStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: ExportStrategy):
        self.strategy = strategy

    def export(self, recipe):
        return self.strategy.export(recipe)
