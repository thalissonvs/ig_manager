# Como configurar o ambiente do *IG Manager*

Abaixo está um tutorial completo de como instalar as dependências e executar com sucesso o projeto.
Basta seguir o passo a passo que tudo funcionará conforme esperado (Windows).

## Download de dependências

1.  O primeiro passo para executar com sucesso o projeto é utilizar o gerenciador de versões do python `pyenv` que você pode
encontrar para download [aqui](https://github.com/pyenv-win/pyenv-win).
2. Após baixar e se certificar que consegue rodar o comando `pyenv` no seu terminal, navegue até o diretório raiz do projeto,
   abra o terminal, e digite o comando:

   ```bash
   pyenv install 3.12.1
   ```
3. Com o python correto instalado, está tudo configurado. Ao tentar rodar o comando `python` em um terminal aberto nessa pasta,
   o `pyenv` se certificará de ler o arquivo `.python-version` e o utilizar como a versão oficial do projeto.

4. Com o python correto instalado, agora vamos instalar o gerenciador de dependências. Minha escolha foi o `poetry`, que além
   de instalar todas as dependências e resolver conflitos de versão, cria um ambiente virtual automaticamente, assim não instalando
   bibliotecas no seu python global. A forma mais eficiente de instalar o `poetry` segundo a [documentação oficial](https://python-poetry.org/docs/)
   é utilizando o `pipx`, que nada mais é que uma forma de instalar uma ferramenta de linha de comando de maneira descentralizada, que irá funcionar
   independentemente da versão do python instalada. O `pipx` instala cada aplicativo em seu próprio ambiente virtual, garantindo que não haja conflitos
   de dependência entre diferentes ferramentas que você pode usar. Isso é especialmente útil para ferramentas de linha de comando como o `poetry`,
   que têm suas próprias dependências que podem não ser compatíveis com as de outros pacotes python instalados globalmente.  Uma vez instalado com `pipx`,
   o `poetry` pode ser usado globalmente em qualquer terminal, independentemente do ambiente python ativo. Para instalar o `pipx` é simples, basta executar:

   ```bash
   python -m pip install pipx
   pipx ensurepath
   ```

   Com esses dois comandos executados com sucesso, basta instalar o `poetry` utilizando:

   ```bash
   pipx install poetry
   ```

   E pronto! o gerenciador de dependências está instalado.

6. Com o `poetry` instalado, agora basta instalar todas as dependências com o comando:

   ```bash
   poetry install
   ```

   Esse comando deve ser executado dentro do **diretório raiz do projeto**. O `poetry` irá procurar pelo arquivo
   `pyproject.toml`, e instalar tudo automaticamente, além de criar um ambiente virtual isolado para o projeto!
   Além de instalar as dependências do projeto, irá instalar as dependências de desenvolvimento, como formatadores de
   código, `weditor` para inspecionar widgets de dispositivos androids, biblioteca para execução de testes, etc. Com
   tudo isso configurado, estamos prontos para executar o projeto.

## Inicialização do *IG Manager*

Com tudo configurado corretamente, fica simples, sempre que for executar o projeto, basta rodar:

```bash
python .\main.py
```

Certifique-se de que, antes de executar, o ambiente virtual criado pelo poetry esteja habilitado no terminal.
Geralmente isso aparece como algo assim:

```bash
(ig-manager-py3.12) C:\Users\Thalisson Vinicius\Documents\Programacao\python\ig_manager>
```

Caso não esteja, basta executar o comando:

```bash
poetry shell
```

Esse comando se certificará de habilitar o ambiente virtual no seu terminal atual.
