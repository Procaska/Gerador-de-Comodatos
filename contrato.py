from docxtpl import DocxTemplate
from datetime import datetime
import os


def gerar_contrato(dados):

    # Caminho do modelo

    caminho_modelo = "modelo/comodato.docx"


    # Pasta de saída

    pasta_saida = "contratos"


    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)



    # Abre o documento

    doc = DocxTemplate(caminho_modelo)



    # Dados enviados pelo app

    contexto = {

        "nome": dados["nome"],

        "cpf": dados["cpf"],

        "rg": dados["rg"],

        "cargo": dados["cargo"],

        "setor": dados["setor"],

        "data": dados["data"],


        "equipamentos": dados["equipamentos"]

    }



    # Renderiza o documento

    doc.render(contexto)



    # Nome do arquivo

    nome_arquivo = (
        f"Comodato_{dados['nome'].replace(' ', '_')}.docx"
    )


    caminho_final = os.path.join(
        pasta_saida,
        nome_arquivo
    )



    # Salva

    doc.save(caminho_final)



    return caminho_final