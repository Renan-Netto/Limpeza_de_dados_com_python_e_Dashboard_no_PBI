# Análise do dataset "Quantidade de Usinas Termelétricas por Tipo"

Este projeto teve como objetivo a análise visual do atual cenário da distribuição dos combustíveis usados na geração de energia em usinas termoelétricas, o produto da análise (dashboard) pode ser usado para verificar as tendências do segmento com base no período entre 2012 e 2024.

## Conteúdo

- [Fonte dos Dados](#-fonte-dos-dados)
- [Visão Geral do Projeto](#visao-geral-do-projeto)
- [Conclusões](#conclusoes)

### Fonte dos Dados

O dataset usado neste projeto foi extraído do "Portal de Dados Abertos" do Governo Federal no link: "https://dados.gov.br/dados/conjuntos-dados/usinas-termeletricas-por-tipo1", identificado como "usina-termeletrica-tipo.csv".

### Visão Geral do Projeto

#### Visualização dos Dados

O arquivo "usina-termeletrica-tipo.csv" foi alterado para UTF-8 e os caracteres foram alterados para "," para a separação de colunas e para "." para a separação de casas decimais.
O arquivo então foi aberto no jupyter notebook com o pacote pandas, onde vários métodos foram usados para verificar a integridade dos dados: tipo das variáveis, formato, busca por vazios, nome das colunas e valores duplicados.

#### Limpeza dos Dados

As colunas foram renomeadas e os valores de data foram alterados de object para tipo data, por meio do pacote datetime.
As variáveis descritivas do dataset foram uniformizadas, de modo a impedir que diferentes variáveis representassem um mesmo valor.

#### Armazenagem dos Dados Limpos

Os dados limpos fora armazenados no formato .csv.

#### Confecção do Dashboard

O dasnboard foi feito no PBI pela importação do arquivo .csv.
A segmentação dos dados foi feita para análises por data e origem do combustível (fóssil ou biomassa).

#### Linguagens e Pacotes Utilizados

- Python: pandas.
- PBI: DAX para criação de medida.

### Conclusões

- A maior parte da potência é gerada a partir de combustíveis fósseis.
- Entre 2012 e 2014 houve principalmente a proliferação de usinas a partir de combustíveis fósseis.
- Usinas a base de combustíveis fósseis representam cerca de 80% do total.
- Há grande variabilidade entre os combustíveis usados para a geração de energia em termelétricas.
