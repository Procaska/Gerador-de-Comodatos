from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": [
        "customtkinter",
        "docxtpl",
        "docx",
        "jinja2",
    ],
    "include_files": [
        ("modelo", "modelo"),
    ],
}

setup(
    name="Gerador de Comodatos",
    version="1.0",
    description="Gerador de Contratos de Comodato",
    options={"build_exe": build_exe_options},
    executables=[
        Executable(
            "main.py",
            target_name="GeradorComodatos.exe",
            base="gui"
        )
    ]
)