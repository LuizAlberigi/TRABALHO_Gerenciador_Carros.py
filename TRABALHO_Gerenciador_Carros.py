
from shiny import App, ui, render, reactive

# Interface do usuário
app_ui = ui.page_fluid(
    ui.h2("Gerenciador de Carros"),

    ui.input_text("marca", "Marca do carro"),
    ui.input_text("modelo", "Modelo do carro"),
    ui.input_numeric("ano", "Ano do carro", value=2020, min=1900, max=2100),

    ui.input_action_button("btn_adicionar", "Adicionar Carro"),

    ui.h3("Carros cadastrados:"),
    ui.output_text_verbatim("lista_carros")
)

# Lógica do servidor
def server(input, output, session):
    # Lista reativa para armazenar carros
    carros = reactive.Val([])

    @reactive.Effect
    def _():
        # Ao clicar no botão, adiciona um carro
        input.btn_adicionar()
        marca = input.marca()
        modelo = input.modelo()
        ano = input.ano()

        # Só adiciona se tiver marca e modelo preenchidos
        if marca and modelo and ano:
            nova_lista = carros() + [f"{marca} {modelo} ({ano})"]
            carros.set(nova_lista)

    @output
    @render.text
    def lista_carros():
        lista = carros()
        if not lista:
            return "Nenhum carro cadastrado ainda."
        return "\n".join(lista)

# Criando a aplicação
app = App(app_ui, server)
