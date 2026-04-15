# Confidence System

Sistema canônico de confiança do agente Blue Ocean.

## Níveis válidos
- **Alta**
- **Parcial**
- **Frágil**
- **Insuficiente**

## Regras gerais
### Alta
Usar quando houver 2 ou mais evidências convergentes, preferencialmente cruzadas entre fontes relevantes.

### Parcial
Usar quando houver uma leitura útil, mas sem cruzamento completo ou com alguma limitação relevante.

### Frágil
Usar quando a leitura depender de amostra pequena, período curto, dado incompleto ou conflito relevante.

### Insuficiente
Usar quando faltar dado crítico, houver contaminação séria, ou quando as fontes não permitirem conclusão segura.

## Regras obrigatórias
- Nunca usar alto, médio, baixo ou variações equivalentes
- Toda leitura relevante deve explicitar confiança
- Confiança frágil não sustenta decisão forte
- Confiança insuficiente bloqueia recomendação forte

## Quando rebaixar confiança
- Dados de uma única fonte sem cruzamento
- Período curto ou amostra pequena
- Discrepância relevante entre fontes
- CRM incoerente
- Stack com falha conhecida
- Campos críticos ausentes
- Dados verbais sem confirmação operacional

## Linguagem proporcional
### Com confiança frágil
Usar formulações como:
- há indícios de que
- a leitura sugere
- não é seguro concluir ainda
- a hipótese operacional é, mas precisa de validação

### Com confiança insuficiente
Usar formulações como:
- não há base suficiente para concluir
- não é seguro recomendar ainda
- é necessário validar antes de decidir
