import customtkinter as ctk
from tkinter import messagebox


# Mesma paleta de vermelho usada no app principal
COR_DESTAQUE = "#E5484D"
COR_DESTAQUE_HOVER = "#C93E42"
COR_CANCELAR = "#7A2E31"
COR_CANCELAR_HOVER = "#5E2325"


class JanelaEquipamento(ctk.CTkToplevel):

    def __init__(self, master):

        super().__init__(master)

        self.master = master

        self.title("Cadastro de Equipamento")

        self.geometry("600x520")

        self.resizable(False, False)

        # Impede clicar na janela principal enquanto essa está aberta
        self.grab_set()

        self.criar_interface()


    # =====================================================
    # INTERFACE
    # =====================================================

    def criar_interface(self):

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)


        titulo = ctk.CTkLabel(
            self,
            text="Cadastro de Equipamento",
            font=("Segoe UI",22,"bold")
        )

        titulo.grid(
            row=0,
            column=0,
            columnspan=2,
            pady=(20,25)
        )


        # Tipo

        ctk.CTkLabel(
            self,
            text="Equipamento"
        ).grid(
            row=1,
            column=0,
            sticky="w",
            padx=20
        )


        self.tipo = ctk.CTkEntry(self)

        self.tipo.grid(
            row=2,
            column=0,
            padx=20,
            pady=(0,15),
            sticky="ew"
        )



        # Modelo

        ctk.CTkLabel(
            self,
            text="Marca / Modelo"
        ).grid(
            row=1,
            column=1,
            sticky="w",
            padx=20
        )


        self.modelo = ctk.CTkEntry(self)

        self.modelo.grid(
            row=2,
            column=1,
            padx=20,
            pady=(0,15),
            sticky="ew"
        )



        # Patrimônio

        ctk.CTkLabel(
            self,
            text="Patrimônio"
        ).grid(
            row=3,
            column=0,
            sticky="w",
            padx=20
        )


        self.patrimonio = ctk.CTkEntry(self)

        self.patrimonio.grid(
            row=4,
            column=0,
            padx=20,
            pady=(0,15),
            sticky="ew"
        )



        # Série

        ctk.CTkLabel(
            self,
            text="Número de Série"
        ).grid(
            row=3,
            column=1,
            sticky="w",
            padx=20
        )


        self.serial = ctk.CTkEntry(self)

        self.serial.grid(
            row=4,
            column=1,
            padx=20,
            pady=(0,15),
            sticky="ew"
        )



        # IMEI

        ctk.CTkLabel(
            self,
            text="IMEI"
        ).grid(
            row=5,
            column=0,
            sticky="w",
            padx=20
        )


        self.imei = ctk.CTkEntry(self)

        self.imei.grid(
            row=6,
            column=0,
            padx=20,
            pady=(0,15),
            sticky="ew"
        )



        # Linha

        ctk.CTkLabel(
            self,
            text="Linha"
        ).grid(
            row=5,
            column=1,
            sticky="w",
            padx=20
        )


        self.linha = ctk.CTkEntry(self)

        self.linha.grid(
            row=6,
            column=1,
            padx=20,
            pady=(0,15),
            sticky="ew"
        )



        # Observações

        ctk.CTkLabel(
            self,
            text="Observações"
        ).grid(
            row=7,
            column=0,
            columnspan=2,
            sticky="w",
            padx=20
        )


        self.obs = ctk.CTkTextbox(
            self,
            height=90
        )


        self.obs.grid(
            row=8,
            column=0,
            columnspan=2,
            padx=20,
            pady=(0,20),
            sticky="ew"
        )



        # Botões

        botoes = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )


        botoes.grid(
            row=9,
            column=0,
            columnspan=2,
            pady=10
        )


        salvar = ctk.CTkButton(
            botoes,
            text="Salvar",
            width=140,
            fg_color=COR_DESTAQUE,
            hover_color=COR_DESTAQUE_HOVER,
            command=self.salvar
        )


        salvar.pack(
            side="left",
            padx=10
        )



        cancelar = ctk.CTkButton(
            botoes,
            text="Cancelar",
            width=140,
            fg_color=COR_CANCELAR,
            hover_color=COR_CANCELAR_HOVER,
            command=self.destroy
        )


        cancelar.pack(
            side="left",
            padx=10
        )



    # =====================================================
    # SALVAR EQUIPAMENTO
    # =====================================================

    def salvar(self):

        if self.tipo.get().strip() == "":

            messagebox.showwarning(
                "Aviso",
                "Informe o tipo de equipamento."
            )

            return



        equipamento = {

            "tipo": self.tipo.get(),

            "modelo": self.modelo.get(),

            "patrimonio": self.patrimonio.get(),

            "serial": self.serial.get(),

            "imei": self.imei.get(),

            "linha": self.linha.get(),

            "obs": self.obs.get(
                "1.0",
                "end"
            ).strip()

        }



        # Adiciona na lista principal

        self.master.equipamentos.append(
            equipamento
        )


        # Atualiza a tela principal

        self.master.atualizar_lista()


        # Fecha janela

        self.destroy()