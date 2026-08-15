from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": [
        "customtkinter",
        "tkinter",
        "docxtpl",
        "docx",
        "pandas",
        "openpyxl"
    ],
    "include_files": [
        "modelo"
    ]
}

setup(
    name="Gerador de Comodatos",
    version="1.0",
    description="Gerador de contratos de comodato",
    options={
        "build_exe": build_exe_options
    },
    executables=[
        Executable(
            "app.py",
            base="gui",
            target_name="Gerador-de-Comodatos.exe"
        )
    ]
)