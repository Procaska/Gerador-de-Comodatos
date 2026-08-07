import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime

from equipamentos import JanelaEquipamento
from contrato import gerar_contrato


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


# =====================================================
# PALETA / CONSTANTES DE ESTILO
# =====================================================

COR_FUNDO_CARD = ("#F2F2F2", "#1E1E1E")
COR_FUNDO_ITEM = ("#E6E6E6", "#2A2A2A")
COR_BORDA = ("#D0D0D0", "#333333")
COR_DESTAQUE = "#800206"
COR_DESTAQUE_HOVER = "#4F0508"
COR_PERIGO = "#E5484D"
COR_PERIGO_HOVER = "#C93E42"
COR_TEXTO_SECUNDARIO = ("#6B6B6B", "#9A9A9A")

FONTE_TITULO = ("Segoe UI", 26, "bold")
FONTE_SUBTITULO = ("Segoe UI", 13)
FONTE_SECAO = ("Segoe UI", 16, "bold")
FONTE_LABEL = ("Segoe UI", 12)
FONTE_TEXTO = ("Segoe UI", 13)
FONTE_BOTAO = ("Segoe UI", 14, "bold")

RAIO = 12
PAD = 16


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Gerador de Termos de Comodato")
        self.geometry("1080x760")
        self.minsize(860, 640)

        self.equipamentos = []

        self.criar_interface()

    # =====================================================
    # INTERFACE
    # =====================================================

    def criar_interface(self):

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self._criar_cabecalho()

        # Área rolável principal — garante responsividade quando a janela
        # é redimensionada para algo menor que o conteúdo.
        container = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent"
        )
        container.grid(row=1, column=0, padx=24, pady=(0, 16), sticky="nsew")
        container.grid_columnconfigure(0, weight=1)

        self._criar_secao_dados(container)
        self._criar_secao_equipamentos(container)

        self._criar_rodape()

    # -----------------------------------------------------
    # CABEÇALHO
    # -----------------------------------------------------

    def _criar_cabecalho(self):

        cabecalho = ctk.CTkFrame(self, fg_color="transparent")
        cabecalho.grid(row=0, column=0, padx=24, pady=(24, 12), sticky="ew")
        cabecalho.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            cabecalho,
            text="Gerador de Termos de Comodato",
            font=FONTE_TITULO,
            anchor="w"
        ).grid(row=0, column=0, sticky="w")


    # DADOS DO COLABORADOR
    def _criar_secao_dados(self, parent):

        card = ctk.CTkFrame(parent, corner_radius=RAIO, fg_color=COR_FUNDO_CARD)
        card.grid(row=0, column=0, sticky="ew", pady=(0, 16))

        for i in range(4):
            card.grid_columnconfigure(i, weight=1)

        ctk.CTkLabel(
            card,
            text="👤  Dados do Colaborador",
            font=FONTE_SECAO,
            anchor="w"
        ).grid(row=0, column=0, columnspan=4, padx=PAD, pady=(PAD, 4), sticky="w")

        # Nome (linha inteira)
        ctk.CTkLabel(card, text="Nome", font=FONTE_LABEL, anchor="w").grid(
            row=1, column=0, columnspan=4, padx=PAD, pady=(12, 2), sticky="w"
        )
        self.nome = ctk.CTkEntry(
            card, placeholder_text="Nome completo", font=FONTE_TEXTO, height=36
        )
        self.nome.grid(row=2, column=0, columnspan=4, padx=PAD, pady=(0, 4), sticky="ew")

        # Campos em grade 2x2
        campos = [
            ("CPF", "cpf", "000.000.000-00"),
            ("RG", "rg", "00.000.000-0"),
            ("Cargo", "cargo", "Ex: Analista"),
            ("Setor", "setor", "Ex: TI"),
        ]

        for coluna, (texto, atributo, placeholder) in enumerate(campos):
            ctk.CTkLabel(card, text=texto, font=FONTE_LABEL, anchor="w").grid(
                row=3, column=coluna, padx=PAD, pady=(12, 2), sticky="w"
            )

            entrada = ctk.CTkEntry(
                card, placeholder_text=placeholder, font=FONTE_TEXTO, height=36
            )
            entrada.grid(row=4, column=coluna, padx=PAD, pady=(0, 4), sticky="ew")

            setattr(self, atributo, entrada)

        # Data
        ctk.CTkLabel(card, text="Data", font=FONTE_LABEL, anchor="w").grid(
            row=5, column=0, padx=PAD, pady=(12, 2), sticky="w"
        )
        self.data = ctk.CTkEntry(card, font=FONTE_TEXTO, height=36)
        self.data.insert(0, datetime.now().strftime("%d/%m/%Y"))
        self.data.grid(row=6, column=0, padx=PAD, pady=(0, PAD), sticky="ew")

    # -----------------------------------------------------
    # EQUIPAMENTOS
    # -----------------------------------------------------

    def _criar_secao_equipamentos(self, parent):

        card = ctk.CTkFrame(parent, corner_radius=RAIO, fg_color=COR_FUNDO_CARD)
        card.grid(row=1, column=0, sticky="ew", pady=(0, 16))
        card.grid_columnconfigure(0, weight=1)

        cabecalho = ctk.CTkFrame(card, fg_color="transparent")
        cabecalho.grid(row=0, column=0, padx=PAD, pady=(PAD, 8), sticky="ew")
        cabecalho.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            cabecalho,
            text="Equipamentos",
            font=FONTE_SECAO,
            anchor="w"
        ).grid(row=0, column=0, sticky="w")

        ctk.CTkButton(
            cabecalho,
            text="➕  Novo Equipamento",
            font=FONTE_BOTAO,
            height=34,
            corner_radius=8,
            fg_color=COR_DESTAQUE,
            hover_color=COR_DESTAQUE_HOVER,
            command=self.abrir_janela_equipamento
        ).grid(row=0, column=1, sticky="e")

        self.lista = ctk.CTkScrollableFrame(
            card,
            height=240,
            fg_color="transparent"
        )
        self.lista.grid(row=1, column=0, padx=PAD, pady=(0, PAD), sticky="nsew")
        self.lista.grid_columnconfigure(0, weight=1)

        self.atualizar_lista()

    # -----------------------------------------------------
    # RODAPÉ / AÇÃO PRINCIPAL
    # -----------------------------------------------------

    def _criar_rodape(self):

        rodape = ctk.CTkFrame(self, fg_color="transparent")
        rodape.grid(row=2, column=0, padx=24, pady=(0, 24), sticky="ew")
        rodape.grid_columnconfigure(0, weight=1)

        ctk.CTkButton(
            rodape,
            text="GERAR CONTRATO",
            width=240,
            height=44,
            corner_radius=10,
            font=FONTE_BOTAO,
            fg_color=COR_DESTAQUE,
            hover_color=COR_DESTAQUE_HOVER,
            command=self.gerar
        ).grid(row=0, column=0, pady=(0, 8))

        self.status_label = ctk.CTkLabel(
            rodape,
            text="",
            font=FONTE_LABEL,
            text_color=COR_TEXTO_SECUNDARIO,
            anchor="center"
        )
        self.status_label.grid(row=1, column=0)

    # =====================================================
    # ABRIR JANELA EQUIPAMENTO
    # =====================================================

    def abrir_janela_equipamento(self):
        JanelaEquipamento(self)

    # =====================================================
    # ATUALIZAR LISTA
    # =====================================================

    def atualizar_lista(self):

        for widget in self.lista.winfo_children():
            widget.destroy()

        if len(self.equipamentos) == 0:
            ctk.CTkLabel(
                self.lista,
                text="Nenhum equipamento cadastrado.",
                font=FONTE_TEXTO,
                text_color=COR_TEXTO_SECUNDARIO
            ).pack(pady=50)
            return

        for indice, equipamento in enumerate(self.equipamentos):

            linha = ctk.CTkFrame(
                self.lista,
                corner_radius=8,
                fg_color=COR_FUNDO_ITEM
            )
            linha.pack(fill="x", padx=2, pady=6)
            linha.grid_columnconfigure(0, weight=1)

            texto = (
                f"{equipamento.get('tipo', '')}  •  "
                f"{equipamento.get('modelo', '')}  •  "
                f"Patrimônio: {equipamento.get('patrimonio', '')}"
            )

            ctk.CTkLabel(
                linha,
                text=texto,
                font=FONTE_TEXTO,
                anchor="w",
                justify="left"
            ).grid(row=0, column=0, padx=14, pady=12, sticky="w")

            ctk.CTkButton(
                linha,
                text="🗑",
                width=32,
                height=28,
                corner_radius=6,
                font=FONTE_BOTAO,
                fg_color=COR_PERIGO,
                hover_color=COR_PERIGO_HOVER,
                command=lambda i=indice: self.remover_equipamento(i)
            ).grid(row=0, column=1, padx=(4, 14), pady=8, sticky="e")

    # =====================================================
    # REMOVER EQUIPAMENTO
    # =====================================================

    def remover_equipamento(self, indice):

        if 0 <= indice < len(self.equipamentos):
            del self.equipamentos[indice]
            self.atualizar_lista()

    # =====================================================
    # GERAR CONTRATO
    # =====================================================

    def gerar(self):

        dados = {
            "nome": self.nome.get(),
            "cpf": self.cpf.get(),
            "rg": self.rg.get(),
            "cargo": self.cargo.get(),
            "setor": self.setor.get(),
            "data": self.data.get(),
            "equipamentos": self.equipamentos
        }

        if dados["nome"].strip() == "":
            messagebox.showwarning("Aviso", "Informe o nome do colaborador.")
            return

        if len(self.equipamentos) == 0:
            messagebox.showwarning("Aviso", "Cadastre pelo menos um equipamento.")
            return

        try:
            self.status_label.configure(text="Gerando contrato...")
            self.update_idletasks()

            arquivo = gerar_contrato(dados)

            self.status_label.configure(text=f"Último contrato gerado: {arquivo}")
            messagebox.showinfo("Sucesso", f"Contrato gerado:\n\n{arquivo}")

        except Exception as erro:
            self.status_label.configure(text="")
            messagebox.showerror("Erro", f"Erro ao gerar contrato:\n\n{erro}")


# =====================================================
# EXECUÇÃO
# =====================================================

if __name__ == "__main__":
    app = App()
    app.mainloop()