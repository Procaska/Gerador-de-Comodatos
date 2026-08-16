````markdown
# 📄 Gerador de Contratos de Comodato
Aplicação desenvolvida em Python para facilitar e agilizar a geração de contratos de comodato.

## 👌Tecnologias

- Python
- CustomTkinter
- docxtpl
- Jinja2
- CX_Freeze

## 📁 Estrutura do projeto
```
Gerador-de-Comodatos/
├── main.py
├── setup.py
├── modelo/
│   └── comodato.docx
└── contratos/
````
## ▶️ Executando o projeto
Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o programa:
```bash
python main.py
```

## Criando o executável
O projeto utiliza o **CX_Freeze** para gerar uma versão executável do sistema.

### 1. Instale o CX_Freeze
```bash
pip install cx-Freeze
```

### 2. Gere a build
```bash
python setup.py build
```

Após o processo, a pasta `build` será criada contendo o executável e os arquivos necessários para o funcionamento do programa.

> ⚠️ Para distribuir o programa, copie a pasta completa gerada pelo CX_Freeze e não somente o arquivo `.exe`.


Desenvolvido por **Arthur Procaska**.

