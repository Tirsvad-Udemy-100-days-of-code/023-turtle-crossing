# Installation

🌐 [English](Install) · **Dansk** · [Bahasa Malaysia](Install-ms)

## Krav

- Python 3.13 eller nyere med `tkinter`.
- `git`.
- Valgfrit: Doxygen til kildedokumentationen.

## Windows PowerShell

```powershell
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/023-turtle-crossing.git
cd 023-turtle-crossing
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install --group dev
```

## Linux Debian

```bash
sudo apt update && sudo apt install -y git python3.13 python3.13-venv python3-tk
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/023-turtle-crossing.git
cd 023-turtle-crossing
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install --group dev
```

## macOS

```bash
brew install python@3.13 python-tk@3.13 git
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/023-turtle-crossing.git
cd 023-turtle-crossing
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install --group dev
```

## Kør og test

```bash
python src/main.py
python -m pytest
```

Næste: [Spil](Play-da).
