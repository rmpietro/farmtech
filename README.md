# FIAP - Trabalho Fase 1  - Graduação Inteligência Artificial
## Farm Tech

Projeto em grupo com a implementação da proposta solicitada em material de estudo da Faculdade.

### Integrantes do Grupo

- [Rodrigo Mastropietro](https://github.com/rmpietro)
- [Tiago de Andrade Bastos](https://github.com/tiagobastos87)
- [Pedro Scofield](https://github.com/Shyproust)
- [Gustavo Valtrick](https://github.com/gustavo-valtrick)
- [Iago Cotta](https://github.com/Iago-Cotta)
  - *Por uma troca de nome de usuário o Iago não está aparecendo como colaborador porque o Github não fez o link entre o comitador e o usuário adicionado, no entanto ele é um dos integrantes do grupo e seus commits podem ser verificados no histórico do projeto.*

### Pontos de Observação do Projeto
- Toda a lógica realizada em R encontra-se em arquivos específicos dentro da pasta "R";
- As execuções de scripts R foram realizadas a partir de chamada no Python, usando sua interface subprocess para executar comandos de prompt;
- A comunicação entre Python e R foi realizada através de arquivos CSV, onde o Python escreve e o R lê, e vice-versa, dependendo da funcionalidade presente no item de menu;
- O arquivo "main.py" é o arquivo principal do projeto, onde é possível executar o programa e navegar entre as funcionalidades propostas;
- Maiores detalhes serão explicados no vídeo de explicação do projeto, parte integrande do entregável à Faculdade.

### Dependência de Bibliotecas no Projeto
- Python:
  - pandas 
  - subprocess 
  - os
- R:
  - tidyverse
  - httr
  - glue