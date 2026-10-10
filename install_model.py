"""Installa il modello wake-word "alis" nella cartella dei modelli openWakeWord."""
from __future__ import annotations

import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
MODEL = "alis.onnx"


def models_dir() -> Path:
    import openwakeword
    return Path(openwakeword.__file__).resolve().parent / "resources" / "models"


def main() -> None:
    src = HERE / MODEL
    if not src.is_file():
        raise SystemExit(f"Manca {src}")
    try:
        import openwakeword  # noqa: F401
    except ImportError:
        print("Installo openwakeword…")
        import subprocess
        subprocess.run([sys.executable, "-m", "pip", "install", "openwakeword"],
                       check=True)
    dest = models_dir() / MODEL
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.is_file():
        print(f"Già installato: {dest}")
    else:
        shutil.copyfile(src, dest)
        print(f"Installato: {dest}")
    print("Prova: di' «Alis» vicino al microfono con l'esempio in README.")


if __name__ == "__main__":
    main()
