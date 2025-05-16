import controllers.controller
import models
import models.model
import views
import controllers
import views.view

if __name__ == '__main__':
    modelo = models.model.ProdutorConsumidorModel(tamanho_fila=3)
    visao = views.view.ProdutorConsumidorView()
    ctrl = controllers.controller.ProdutorConsumidorController(modelo, visao)
    visao.mainloop()
