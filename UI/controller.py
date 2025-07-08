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
        self._year = e.control.value
        self._model.setYear(self._year)

    def handleCreaGrafo(self, e):
        year = self._year
        if year is None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Please select a year"))
            self._view.update_page()
            return
        self._model.buildGraph()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato: "))
        numNodi, numArchi = self._model.getGraphDetails()
        self._view.txt_result.controls.append(ft.Text(f"Numero di nodi: {numNodi}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di archi: {numArchi}"))
        bestDriver = self._model.getBestDriver()
        self._view.txt_result.controls.append(ft.Text(f"Best driver: {bestDriver[0]} , with score: {bestDriver[1]}"))
        self._view.update_page()

    def handleCerca(self, e):
        pass