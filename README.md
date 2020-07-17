# bradesco-cnab240
Padrão Bradesco Multipag CNAB240 para folha de pagamento, remessa apenas.

No Bradesco Net Empresas, Transmissão de Arquivos, escolha a opção MULTIPAG (você precisa ter essa opção habilitada com a sua agência). Enviar por "FOLHA DE PAGAMENTO 240" não vai funcionar, palavra dita com experiência.

O CNAB240 é um padrão definido pela FEBRABAN e implementado por bancos Brasileiros para a troca de informações.
A estrutura dele é dado:

* Ter em mente:
    * Num  - alinhado a direita com zeros a esquerda
    * Alfa - alinhado a esquerda com espaços em branco a direita


    ARQUIVO.txt (1)

        Header de Arquivo - TIPO 0 (1)
            LOTE (1-N)
                Header de Lote - TIPO 1 (1)
                Registros Inicias do Lote - TIPO 2 (0-N)
                Registros de Detalhe do Segmentos - TIPO 3 (1-N)
                Registros Finais do Lote - TIPO 4 (0-N)
                Registro Trailer de Lote - TIPO 5 (1)      
        Registro Trailer de Arquivo - TIPO 9 (1)


É importante se ater a obrigatóriedade ou não de segmentos conforme o lote.

Pagamento crédito em conta, cheque, op, DOC ou pagamento com autenticação
    Serviço/Produto - Pagamentos
    Segmento

        Remessa
            A (obrigatório)
            B (opcional) #Apesar de no PDF ter a tabela dizendo que é opcional, é obrigatório, de verdade.
            C (opcional)
            5 (opcional)
        
        Retorno
            A (obrigatório)
            B (opcional)
            C (opcional)
            5 (opcional)

# Configuração

## Conf
A primeira coisa a ser feita é criar uma configuração para a sua empresa, é possível ter mais de uma empresa utilizando esse projeto. Basta que você crie um arquivo de configuração para cada uma e a defina corretamente na execução do exec.py.

Dentro da pasta cnab240 há uma pasta chamada confs onde todos os arquivos de configuração precisam ficar. Duplique o arquivo exemplo.conf e crie um novo com o nome/código da sua empresa adicionando ".prod.conf".

O exec.py só aceita os arquivos de configuração que tenham o ".prod.conf" no nome do arquivo. 

Exemplo:
```shell
cp exemplo.conf minhaempresa.prod.conf
```

Depois de copiado abra num editor de texto de sua preferência (vim, nano, notepad++,vscode ...) e substitua os valores que estão lá pelos seus. Esses valores podem ser adquiridos juntos ao TI do Bradesco que está te ajudando a fazer essa integração.

Antes de ligar dá uma lida na documentação que está em docs, é possível que você já tenha grande parte dessas informações.

## CSV

O segundo passo é o de exportar do seu ERP, sistema que gerencia os seus funcionários ou até fazer na mão, um arquivo CSV separado por ponto e virgula ( ; ).

O arquivo precisa respeitar a seguinte ordem de colunas.

```csv
código do banco; agência; agência digito; conta; conta digito; nome do funcionário; valor; data pagamento;cpf
```
Arquivo em si que precisa ser gerado ( sem o cabeçalho dentro do próprio arquivo).

```csv
237;0279;8;099999;2;THIAGO SALARIO MINIMO;104500;03052019;11111111111
237;0279;8;099999;2;THIAGO SALARIO MINIMO 1;104500;03052019;22222222222
237;0279;8;099998;2;THIAGO SALARIO MINIMO 3;104500;03052019;33333333333
```

Por enquanto esse é o único driver disponível para esse projeto, no entanto se você fizer um que tenha como entrada JSON, XML ou qualquer outro manda um pull request!

# Utilização
Por padrão o exec.py vai cuspir tudo no teu terminal (stdout) mas você consegue jogar esse buffer para um arquivo. Salvar ele para enviar para o banco.

```shell
python3 exec.py -c minhaempresa -a "tmp/funcionarios.csv" > saida_cnab240_052020.txt
````

## Parâmetros do exec
    -c, --conf      nome do arquivo de configuracao antes do '.prod.conf'
    -a, --arquivo   caminho do arquivo de entrada que será usado para processamento
    -d, --driver    driver para tratar o arquivo de entrada | padrão csv
    -l, --list      combinado com qualquer outro argumento lista os confs, drivers disponiveis e arquivo passado | não implementado
