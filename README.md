# GBDD - Gerenciador de Banco de Dados Docente

Este projeto, feito com apoio do professor Marcos Amaral, busca criar um programa capaz de gerenciar e operar sobre o banco de dados do DECOM (Departamento de Computação do CEFET-MG).


## Rodando localmente

Para rodar esse projeto, você vai precisar do interpretador de Python na versão 3.10 para cima. Seguem os passos:

Clone o projeto

```bash
  git clone https://github.com/MatheusViniciusV/GBDD.git
```

Entre no diretório do projeto 

```bash
  cd GBDD
```

Execute o arquivo _main_

```bash
  python src/main.py
```


## Documentação

#### Arquivo: main
```http
  /src/BancoDeDados.py
```
    Quando executado, inicia o fluxo de execução do programa.

#### Classe: BancoDeDados

```http
  /src/BancoDeDados.py
```

| Parâmetros de Inicialização  | Descrição |
| :---------- | :--------- | 
| Nenhum | Iterador com o banco de dados |

#### Classe: GUIAdicionarLinha

```http
  /src/GUIAdicionarLinha.py
```

| Parâmetros de Inicialização  | Descrição |
| :---------- | :--------- | 
| Iterador com o banco de dados, janela da tabela e o nome da tabela | Janela para adicionar linha na tabela |

#### Classe: GUICriarTabela

```http
  /src/GUICriarTabela.py
```

| Parâmetros de Inicialização  | Descrição |
| :---------- | :--------- | 
| Iterador com o banco de dados e janela de início | Janela para criar uma nova tabela |

#### Classe: GUIInicio

```http
  /src/GUIInicio.py
```

| Parâmetros de Inicialização  | Descrição |
| :---------- | :--------- | 
| Iterador com o banco de dados | Janela inicial do programa |

#### Classe: GUINovoBancoDeDados

```http
  /src/GUINovoBancoDeDados.py
```

| Parâmetros de Inicialização  | Descrição |
| :---------- | :--------- | 
| Iterador com o banco de dados e janela de início | Janela para criar um novo banco de dados |

#### Classe: GUITabela

```http
  /src/GUITabela.py
```

| Parâmetros de Inicialização  | Descrição |
| :---------- | :--------- | 
| Iterador com o banco de dados e janela de início | Janela que visualiza e permite modificar uma tabela |



## Autores

- [@MatheusViniciusV](https://www.github.com/MatheusViniciusV)
- [@Dranork](https://www.github.com/Dranork)
- [@paulistaLH](https://www.github.com/MatheusViniciusV)
- [@VPom135](https://www.github.com/MatheusViniciusV)



## Licença

[MIT](https://choosealicense.com/licenses/mit/)
