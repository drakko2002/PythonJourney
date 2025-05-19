import tkinter as tk
from PythonStudy_01.AulaSaulo.SauloTKinter.mvc.MVC.Model.model import AFDModel
from PythonStudy_01.AulaSaulo.SauloTKinter.mvc.MVC.View.view import AFDView
from PythonStudy_01.AulaSaulo.SauloTKinter.mvc.MVC.Control.controller import AFDController

if __name__ == "__main__":
    root = tk.Tk()
    model = AFDModel()
    view = AFDView(root)
    controller = AFDController(model, view)
    root.mainloop()
