import os
from datetime import datetime
import customtkinter as ctk
from tkinter import messagebox
from docxtpl import DocxTemplate

# CONFIGURAÇÕES
MODELO_DOCX = "modelo/comodato.docx"
PASTA_SAIDA = "contratos"

os.makedirs(PASTA_SAIDA, exist_ok=True)

# CONFIGURAÇÃO DA INTERFACE
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class GeradorComodato(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("ComodaTech")
        largura = 1000
        altura = 750

        # Verifica a resolução da tela
        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()

        # Ajusta a janela caso a tela seja menor
        largura = min(largura, largura_tela - 80)
        altura = min(altura, altura_tela - 100)
        self.geometry(f"{largura}x{altura}")

        # Tamanho mínimo permitido
        self.minsize(800, 600)
        self.equipamentos = []
        self.criar_interface()

    # INTERFACE PRINCIPAL
    def criar_interface(self):
        # Título
        titulo = ctk.CTkLabel(
            self,
            text="Gerador de Comodatos",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        titulo.pack(pady=(20, 5))

        # FRAME DO COLABORADOR
        frame_colaborador = ctk.CTkFrame(self)
        frame_colaborador.pack(fill="x", padx=20, pady=10)

        label_colaborador = ctk.CTkLabel(
            frame_colaborador,
            text="Dados do Comodatário",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        label_colaborador.grid(
            row=0,
            column=0,
            columnspan=4,
            padx=15,
            pady=(15, 10),
            sticky="w"
        )

        # Nome
        ctk.CTkLabel(
            frame_colaborador,
            text="Nome:"
        ).grid(row=1, column=0, padx=10, pady=8, sticky="e")

        self.entry_nome = ctk.CTkEntry(
            frame_colaborador,
            placeholder_text="Nome completo"
        )
        self.entry_nome.grid(
            row=1,
            column=1,
            padx=10,
            pady=8,
            sticky="ew"
        )

        # CPF
        ctk.CTkLabel(
            frame_colaborador,
            text="CPF:"
        ).grid(row=1, column=2, padx=10, pady=8, sticky="e")

        self.entry_cpf = ctk.CTkEntry(
            frame_colaborador,
            placeholder_text="000.000.000-00"
        )

        self.entry_cpf.grid(
            row=1,
            column=3,
            padx=10,
            pady=8,
            sticky="ew"
        )
        
        # RG
        ctk.CTkLabel(
            frame_colaborador,
            text="RG:"
        ).grid(row=2, column=0, padx=10, pady=8, sticky="e")

        self.entry_rg = ctk.CTkEntry(
            frame_colaborador,
            placeholder_text="Número do RG"
        )
        self.entry_rg.grid(
            row=2,
            column=1,
            padx=10,
            pady=8,
            sticky="ew"
        )

        # Cargo
        ctk.CTkLabel(
            frame_colaborador,
            text="Cargo:"
        ).grid(row=2, column=2, padx=10, pady=8, sticky="e")

        self.entry_cargo = ctk.CTkEntry(
            frame_colaborador,
            placeholder_text="Cargo"
        )
        self.entry_cargo.grid(
            row=2,
            column=3,
            padx=10,
            pady=8,
            sticky="ew"
        )

        # Setor
        ctk.CTkLabel(
            frame_colaborador,
            text="Setor:"
        ).grid(row=3, column=0, padx=10, pady=8, sticky="e")

        self.entry_setor = ctk.CTkEntry(
            frame_colaborador,
            placeholder_text="Setor"
        )
        self.entry_setor.grid(
            row=3,
            column=1,
            padx=10,
            pady=8,
            sticky="ew"
        )

        # Data
        ctk.CTkLabel(
            frame_colaborador,
            text="Data:"
        ).grid(row=3, column=2, padx=10, pady=8, sticky="e")

        self.entry_data = ctk.CTkEntry(
            frame_colaborador
        )
        self.entry_data.insert(
            0,
            datetime.now().strftime("%d/%m/%Y")
        )
        self.entry_data.grid(
            row=3,
            column=3,
            padx=10,
            pady=8,
            sticky="ew"
        )

        # Configuração das colunas
        frame_colaborador.grid_columnconfigure(1, weight=1)
        frame_colaborador.grid_columnconfigure(3, weight=1)

        # EQUIPAMENTOS
        frame_equipamentos = ctk.CTkFrame(self)
        frame_equipamentos.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        titulo_equipamentos = ctk.CTkLabel(
            frame_equipamentos,
            text="Equipamentos",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        titulo_equipamentos.pack(
            anchor="w",
            padx=15,
            pady=(15, 5)
        )

        # Botão adicionar
        self.btn_adicionar = ctk.CTkButton(
            frame_equipamentos,
            text="+ Adicionar equipamento",
            command=self.adicionar_equipamento
        )
        self.btn_adicionar.pack(
            anchor="w",
            padx=15,
            pady=5
        )

        # Área com scroll
        self.scroll_equipamentos = ctk.CTkScrollableFrame(
            frame_equipamentos,
            height=280
        )
        self.scroll_equipamentos.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=10
        )

        # Primeiro equipamento
        self.adicionar_equipamento()

       
        # BOTÃO GERAR
        self.btn_gerar = ctk.CTkButton(
            self,
            text="GERAR CONTRATO",
            height=45,
            font=ctk.CTkFont(size=16, weight="bold"),
            command=self.gerar_contrato
        )
        self.btn_gerar.pack(
            fill="x",
            padx=20,
            pady=(5, 20)
        )


    # MASCARA DE CPF
        self.entry_cpf.bind("<KeyRelease>", self.formatar_cpf)
    def formatar_cpf(self, event=None):
        valor = self.entry_cpf.get()

        # Mantém somente números
        numeros = ''.join(filter(str.isdigit, valor))

        # Limita a 11 dígitos
        numeros = numeros[:11]

        if len(numeros) <= 3:
         formatado = numeros
        elif len(numeros) <= 6:
         formatado = f"{numeros[:3]}.{numeros[3:]}"
        elif len(numeros) <= 9:
         formatado = f"{numeros[:3]}.{numeros[3:6]}.{numeros[6:]}"
        else:
         formatado = (
            f"{numeros[:3]}."
            f"{numeros[3:6]}."
            f"{numeros[6:9]}-"
            f"{numeros[9:]}"
                )
        self.entry_cpf.delete(0, "end")
        self.entry_cpf.insert(0, formatado)


    # ADICIONAR EQUIPAMENTO
    def adicionar_equipamento(self):

        numero = len(self.equipamentos) + 1

        frame = ctk.CTkFrame(
            self.scroll_equipamentos
        )
        frame.pack(
            fill="x",
            padx=5,
            pady=8
        )

        titulo = ctk.CTkLabel(
            frame,
            text=f"Equipamento {numero}",
            font=ctk.CTkFont(size=15, weight="bold")
        )
        titulo.grid(
            row=0,
            column=0,
            columnspan=4,
            padx=10,
            pady=(10, 5),
            sticky="w"
        )

        # Tipo
        entry_tipo = ctk.CTkComboBox(
            frame,
            values=[
                "Notebook",
                "Monitor",
                "Celular",
                "Tablet",
                "Teclado",
                "Mouse",
                "Outro"         ])
        
        entry_tipo.set("Selecione o tipo")
        entry_tipo.grid(
            row=1,
            column=1,
            padx=8,
            pady=5,
            sticky="ew"
        )

        # Modelo
        ctk.CTkLabel(
            frame,
            text="Modelo:"
        ).grid(row=1, column=2, padx=8, pady=5, sticky="e")

        entry_modelo = ctk.CTkEntry(
            frame,
            placeholder_text="Modelo do equipamento"
        )
        entry_modelo.grid(
            row=1,
            column=3,
            padx=8,
            pady=5,
            sticky="ew"
        )

        # Patrimônio
        ctk.CTkLabel(
            frame,
            text="Patrimônio:"
        ).grid(row=2, column=0, padx=8, pady=5, sticky="e")

        entry_patrimonio = ctk.CTkEntry(
            frame,
            placeholder_text="Número do patrimônio"
        )
        entry_patrimonio.grid(
            row=2,
            column=1,
            padx=8,
            pady=5,
            sticky="ew"
        )

        # Serial
        ctk.CTkLabel(
            frame,
            text="Serial:"
        ).grid(row=2, column=2, padx=8, pady=5, sticky="e")

        entry_serial = ctk.CTkEntry(
            frame,
            placeholder_text="Número de série"
        )
        entry_serial.grid(
            row=2,
            column=3,
            padx=8,
            pady=5,
            sticky="ew"
        )

        # IMEI
        ctk.CTkLabel(
            frame,
            text="IMEI:"
        ).grid(row=3, column=0, padx=8, pady=5, sticky="e")

        entry_imei = ctk.CTkEntry(
            frame,
            placeholder_text="IMEI (se aplicável)"
        )
        entry_imei.grid(
            row=3,
            column=1,
            padx=8,
            pady=5,
            sticky="ew"
        )

        # Linha
        ctk.CTkLabel(
            frame,
            text="Linha:"
        ).grid(row=3, column=2, padx=8, pady=5, sticky="e")

        entry_linha = ctk.CTkEntry(
            frame,
            placeholder_text="Número da linha (se aplicável)"
        )
        entry_linha.grid(
            row=3,
            column=3,
            padx=8,
            pady=5,
            sticky="ew"
        )

        # Observações
        ctk.CTkLabel(
            frame,
            text="Observações:"
        ).grid(row=4, column=0, padx=8, pady=5, sticky="e")

        entry_obs = ctk.CTkEntry(
            frame,
            placeholder_text="Observações"
        )
        entry_obs.grid(
            row=4,
            column=1,
            columnspan=3,
            padx=8,
            pady=5,
            sticky="ew"
        )

        # Botão remover
        btn_remover = ctk.CTkButton(
            frame,
            text="Remover",
            width=80,
            fg_color="#c0392b",
            hover_color="#922b21",
            command=lambda f=frame: self.remover_equipamento(f)
        )
        btn_remover.grid(
            row=5,
            column=3,
            padx=8,
            pady=(5, 10),
            sticky="e"
        )

        # Configuração das colunas
        frame.grid_columnconfigure(1, weight=1)
        frame.grid_columnconfigure(3, weight=1)

        # Guarda referências dos campos
        equipamento = {
            "frame": frame,
            "tipo": entry_tipo,
            "modelo": entry_modelo,
            "patrimonio": entry_patrimonio,
            "serial": entry_serial,
            "imei": entry_imei,
            "linha": entry_linha,
            "obs": entry_obs
        }

        self.equipamentos.append(equipamento)


    # REMOVER EQUIPAMENTO
    def remover_equipamento(self, frame):

        if len(self.equipamentos) <= 1:
            messagebox.showwarning(
                "Atenção",
                "O comodato precisa ter pelo menos um equipamento."
            )
            return

        for equipamento in self.equipamentos:
            if equipamento["frame"] == frame:
                equipamento["frame"].destroy()
                self.equipamentos.remove(equipamento)
                break

        self.atualizar_numeracao()


    # ATUALIZAR NUMERAÇÃO
    def atualizar_numeracao(self):

        for i, equipamento in enumerate(self.equipamentos, start=1):

            # Procura o primeiro CTkLabel dentro do frame
            widgets = equipamento["frame"].winfo_children()

            for widget in widgets:
                if isinstance(widget, ctk.CTkLabel):
                    texto = widget.cget("text")

                    if texto.startswith("Equipamento"):
                        widget.configure(
                            text=f"Equipamento {i}"
                        )
                        break


    # PEGAR VALOR DOS CAMPOS
    def obter_valor(self, entry):
        return entry.get().strip()

    # VALIDAR DADOS
    def validar(self):

        nome = self.obter_valor(self.entry_nome)
        cpf = self.obter_valor(self.entry_cpf)
        rg = self.obter_valor(self.entry_rg)
        cargo = self.obter_valor(self.entry_cargo)
        setor = self.obter_valor(self.entry_setor)

        if not nome:
            messagebox.showwarning(
                "Campo obrigatório",
                "Informe o nome do comodatário."
            )
            self.entry_nome.focus()
            return False

        if not cpf:
            messagebox.showwarning(
                "Campo obrigatório",
                "Informe o CPF."
            )
            self.entry_cpf.focus()
            return False

        if not rg:
            messagebox.showwarning(
                "Campo obrigatório",
                "Informe o RG."
            )
            self.entry_rg.focus()
            return False

        if not cargo:
            messagebox.showwarning(
                "Campo obrigatório",
                "Informe o cargo."
            )
            self.entry_cargo.focus()
            return False

        if not setor:
            messagebox.showwarning(
                "Campo obrigatório",
                "Informe o setor."
            )
            self.entry_setor.focus()
            return False

        return True


    # GERAR CONTRATO
    def gerar_contrato(self):

        if not self.validar():
            return

        if not os.path.exists(MODELO_DOCX):

            messagebox.showerror(
                "Erro",
                f"O arquivo '{MODELO_DOCX}' não foi encontrado."
            )

            return

        try:
            # Dados do colaborador
            nome = self.obter_valor(self.entry_nome)
            cpf = self.obter_valor(self.entry_cpf)
            rg = self.obter_valor(self.entry_rg)
            cargo = self.obter_valor(self.entry_cargo)
            setor = self.obter_valor(self.entry_setor)

            data = self.obter_valor(self.entry_data)


            # Dados dos equipamentos
            equipamentos = []

            for equipamento in self.equipamentos:

                dados = {
                    "eq_tipo": self.obter_valor(equipamento["tipo"]),
                    "eq_modelo": self.obter_valor(equipamento["modelo"]),
                    "eq_patrimonio": self.obter_valor(
                        equipamento["patrimonio"]
                    ),
                    "eq_serial": self.obter_valor(
                        equipamento["serial"]
                    ),
                    "eq_imei": self.obter_valor(
                        equipamento["imei"]
                    ),
                    "eq_linha": self.obter_valor(
                        equipamento["linha"]
                    ),
                    "eq_obs": self.obter_valor(
                        equipamento["obs"]
                    )
                }
                equipamentos.append(dados)


            # Carregar modelo
            doc = DocxTemplate(MODELO_DOCX)

            # Contexto
            contexto = {
                "nome": nome,
                "cpf": cpf,
                "rg": rg,
                "cargo": cargo,
                "setor": setor,
                "data": data,
                "equipamentos": equipamentos
            }

            # Renderizar documento
            doc.render(contexto)

            # Nome do arquivo
            nome_arquivo = self.limpar_nome_arquivo(nome)

            nome_arquivo = (f"Comodato_{nome_arquivo}.docx" )

            caminho_saida = os.path.join(
                PASTA_SAIDA,
                nome_arquivo )

            # Salvar
            doc.save(caminho_saida)

            messagebox.showinfo(
                "Sucesso",
                f"Contrato gerado com sucesso!\n\n"
                f"Arquivo:\n{caminho_saida}" )

        except Exception as erro:

            messagebox.showerror(
                "Erro ao gerar contrato",
                f"Ocorreu um erro:\n\n{erro}" )

    # LIMPAR NOME DO ARQUIVO
    @staticmethod
    def limpar_nome_arquivo(nome):

        caracteres_invalidos = '<>:"/\\|?*'

        for caractere in caracteres_invalidos:
            nome = nome.replace(caractere, "")

        return nome.strip()


# EXECUÇÃO
if __name__ == "__main__":
    app = GeradorComodato()
    app.mainloop()