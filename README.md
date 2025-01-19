# Backup Automático de Arquivos e Pastas

Este script em Python cria backups de arquivos e pastas dentro de um diretório selecionado pelo usuário. Ele organiza os backups em subpastas com timestamps para fácil identificação.

## Funcionalidades

- Seleção interativa de uma pasta no computador.
- Criação automática de uma pasta de backup no diretório selecionado.
- Organização dos backups em subpastas com a data e hora da execução do script.
- Cópia de arquivos e pastas, excluindo a própria pasta de backup.

## Requisitos

Certifique-se de que você tenha os seguintes requisitos antes de executar o script:

- Python 3.6 ou superior.
- Módulos nativos do Python: `os`, `shutil`, `datetime`.
- Biblioteca `tkinter` para a interface de seleção de pastas (instalada por padrão na maioria das distribuições do Python).
