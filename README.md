# Snake - Hra pro dva hráče

Snake hra vytvořená v pygame pro dva hráče. Hráči ovládají hady pomocí kláves a snaží se získat co nejvíce bodů sbíráním jídla, aniž by narazili do sebe nebo do vlastního ocasu.

## Instalace

### Požadavky
- Python 3.8 nebo vyšší
- [uv](https://github.com/astral-sh/uv) - moderní Python package manager

### Linux

1. Nainstalujte `uv`:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Spusťte hru:
```bash
uv run main.py
```

### Windows

1. Nainstalujte `uv` pomocí PowerShell:
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

2. Spusťte hru:
```powershell
uv run main.py
```

## Ovládání

- **Hráč 1**: Šipky (↑ ↓ ← →)
- **Hráč 2**: W, A, S, D

## Spuštění

Hra se automaticky spustí po spuštění `main.py`. Pro ukončení stiskněte křížek v okně hry.