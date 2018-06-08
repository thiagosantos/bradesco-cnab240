# bradesco-cnab240
Padrão Bradesco Multipag CNAB240 para folha de pagamento, remessa apenas.

No Bradesco Net Empresas, Transmissão de Arquivos, escolha a opção MULTIPAG (você precisa ter essa opção habilitada com a sua agência). Enviar por "FOLHA DE PAGAMENTO 240" não vai funcionar, palavra dita com experiência.

O CNAB240 é um padrão definido pela FEBRABAN e implementado por bancos Brasileiros para a troca de informações.
A estrutura dele é dado:

Ter em mente:
    Num  - alinhado a direita com zeros a esquerda
    Alfa - alinhado a esquerda com espaços em branco a direita

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