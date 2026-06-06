from pathlib import Path

# Diretório raiz onde a busca começará
raiz = Path(".")

for arquivo in raiz.rglob("*complete*.txt"):
    if arquivo.is_file():
        try:
            arquivo.unlink()
            print(f"Removido: {arquivo}")
        except Exception as e:
            print(f"Erro ao remover {arquivo}: {e}")