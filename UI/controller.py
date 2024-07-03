import flet as ft
from model.model import Model
from UI.view import View


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listShape = []

    def fillDD(self):
        pass

    def fill_dd_year(self):
        years = self._model.get_years()
        for year in years:
            self._view.ddyear.options.append(ft.dropdown.Option(year))
        self._view.update_page()

    def fill_dd_shape(self):
        self._view.ddshape.options.clear()
        shapes = self._model.get_shapes(self._view.ddyear.value)
        for shape in shapes:
            self._view.ddshape.options.append(ft.dropdown.Option(shape))
        self._view.update_page()

    def year_selected(self, e):
        self._model.selected_year = self._view.ddyear.value
        self.fill_dd_shape()

    def shape_selected(self, e):
        self._model.selected_shape = self._view.ddshape.value

    def handle_graph(self, e):
        print("Handle graph called")
        self._model.build_graph()
        self._model.print_graph()
    def handle_path(self, e):
        pass