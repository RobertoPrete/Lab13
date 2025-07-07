import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._year = None

    def fillDDYear(self):
        years = self._model.getYears()
        for year in years:
            self._view._ddAnno.options.append(ft.dropdown.Option(year))
        self._view.update_page()

    def handleDDYearSelection(self, e):
        pass

    def handleCreaGrafo(self,e):
        pass

    def handleCerca(self, e):
        pass