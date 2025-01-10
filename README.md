# backup_com_python
fazer backup de forma simples com Python
README
Backup Automático de Arquivos
Este projeto é um script Python que automatiza o processo de criação de backups de arquivos e pastas em um diretório selecionado pelo usuário. Através de uma interface simples, o script permite selecionar uma pasta e criar um backup com marcação de data e hora.

Descrição
O script realiza as seguintes tarefas:

Permite ao usuário selecionar uma pasta no computador usando uma janela de diálogo.
Cria uma subpasta chamada backup dentro da pasta selecionada.
Organiza os backups com base na data e hora do momento da execução.
Copia todos os arquivos e subpastas (exceto a própria pasta de backup) para a nova pasta de backup.
Recursos
Uso de Tkinter para interface gráfica de seleção de pastas.
Criação automatizada de pastas para backups com base na data e hora.
Suporte à cópia de arquivos e pastas:
Arquivos são copiados diretamente.
Subpastas são copiadas recursivamente, mantendo a estrutura original.
Evita duplicação ao ignorar a própria pasta de backup no processo.
Requisitos
Python 3.x
Módulos padrão:
os
shutil
datetime
tkinter


Copyright (c) 2025 Manoel Farias da Silva
e-mail: manoelfariasdasilvasantos@gmail.com

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
