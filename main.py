"""
class ADBUtils: responsável por executar comandos adb
class IAutomator: interface que deve ser implementada por qualquer classe que deseje automatizar uma aplicação. Deve conter os métodos .click() .send_keys() e .wait()
class AutomatorFactory: fábrica de classes concretas que implementam IAutomator. Deve conter um método get_automator que recebe um parâmetro do tipo str.
class AndroidAutomator: classe que implementa a interface IAutomator e é responsável por automatizar aplicativos Android. Deve receber como parâmetro um objeto da classe ADBUtils.
class IGAuth: responsável por autenticar o usuário no Instagram. Deve receber AutomatorFactory como parâmetro.
class IGInteractor: responsável por ações de seguir e curtir no instagram. Deve receber AutomatorFactory como parâmetro.
class IGFacade: padrão facade para coordenar as ações de autenticação e interação no Instagram. Instancia IGAuth e IGInteractor e as utiliza para realizar as ações.

class WeezuAPI: responsável por retornar as ações de seguir/curtir de acordo com o usuário fornecido.
class ConfigHandler: responsável por ler e gerenciar o arquivo de configuração.


Exemplo do uso de arquitetura MVC com QtDesigner para uma tela de configurações:

-view: herda a classe gerada pelo pyuic5, não contém lógica de negócio. Possui métodos para obter e setar os valores dos campos.
-model: é basicamente a classe que armazena o estado da aplicação. Pode possuir por exemplo o estado dos widgets, se estão selecionados ou não, etc.
também possui os signals, que serão emitidos quando houver alguma alteração no estado da aplicação. O model não deve ter referência à view nem ao controller.
-controller: conecta a view com o model. Ou seja, ele conecta os signals da view com os métodos do model e vice-versa, além de conter a lógica de negócio da aplicação.


Exemplo de implementação:

class ConfigView: herda a classe gerada pelo pyuic5, contém os métodos para obter e setar os valores dos campos.
class ConfigModel: armazena o estado da aplicação e os signals.
class ConfigController: conecta a view com o model e contém a lógica de negócio da aplicação.
"""
import sys

from PyQt5.QtWidgets import QApplication

from ig_manager.gui.views.main_view import MainView

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_view = MainView()
    main_view.show()
    sys.exit(app.exec_())
