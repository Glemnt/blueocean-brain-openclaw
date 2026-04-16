# Sheets Commercial Reconciliation

Playbook para reconciliar marketing e comercial quando a operação depende fortemente de planilhas Google e o CRM ainda não tem integridade suficiente para ser tratado como verdade superior automática.

## Quando usar
Use este playbook quando:
- a leitura comercial diária estiver mais confiável nas planilhas do que no CRM
- SDRs e Closers não estiverem preenchendo o CRM com disciplina suficiente
- houver necessidade de cruzar captação, reuniões, qualificação e fechamento
- for necessário entender se o problema é mídia, stack, operação comercial ou reconciliação

## Fontes principais no estado atual
### Marketing e tracking operacional
- `CONTROLE DE LEADS GERAL`

### Comercial diário
- `Planilha Comercial x Marketing V.2`

### CRM
- Kommo, apenas como fonte auxiliar ou entidade viva, sem superioridade presumida até a auditoria de integridade

## Regra central
No estado atual da Blue Ocean, a planilha comercial atualizada diariamente pelo Sales Ops pode ser mais confiável do que Kommo para leitura comercial diária.

Isso não significa abandonar o CRM.
Significa apenas que a hierarquia de confiança precisa refletir a operação real, não a arquitetura idealizada.

## Objetivos do playbook
1. verificar se os dados de marketing estão chegando corretamente
2. verificar se a passagem para a camada comercial está íntegra
3. cruzar leads, reuniões, SQL e fechamento com cautela
4. separar falha de stack de falha de operação
5. definir o que já é confiável e o que ainda depende de auditoria

## Perguntas obrigatórias
1. As automações do n8n estão 100% validadas para o período?
2. Os dados da `CONTROLE DE LEADS GERAL` estão chegando completos?
3. Há chaves úteis de ligação entre as duas planilhas, como `ID_LEAD`, nome, data, canal ou origem?
4. A planilha comercial está sendo atualizada diariamente e com critério consistente?
5. O CRM está completo o suficiente para entrar como reforço ou ainda é fonte frágil?

## Passo a passo
### Etapa 1. Validar o stack antes da análise
Antes de cruzar números:
- verificar se o n8n está funcionando
- verificar se entradas estão chegando na planilha de leads
- verificar se não há atraso, duplicidade ou quebra de campos

Se essa etapa falhar:
- não tratar discrepância como problema de mídia ou comercial ainda
- classificar primeiro como possível falha de stack

### Etapa 2. Mapear a ponte entre marketing e comercial
Identificar quais chaves realmente permitem ligação entre planilhas:
- `ID_LEAD`
- `LEAD ID`
- nome
- data
- canal de aquisição
- campanha/origem

Prioridade:
- usar identificador único quando existir
- usar combinação de nome + data + origem apenas com cautela

### Etapa 3. Medir o que fecha e o que não fecha
Classificar o cruzamento em níveis:
- **Fecha bem**: maioria dos registros coerente entre marketing e comercial
- **Fecha com ruído**: base utilizável, mas com perda ou inconsistência parcial
- **Fecha mal**: base insuficiente para leitura forte

### Etapa 4. Separar as hipóteses
Se a base não fecha, distinguir entre:
- falha de automação
- falha de preenchimento operacional
- falha de naming/chaves
- diferença real de comportamento do funil

### Etapa 5. Produzir saída honesta
A saída deve sempre informar:
- o que é confiável
- o que é parcial
- o que depende de validação adicional
- qual camada prevaleceu na leitura

## Saída esperada
### 1. Integridade do stack
- íntegro
- com ressalvas
- frágil

### 2. Confiabilidade da planilha de leads
- forte
- média
- frágil

### 3. Confiabilidade da planilha comercial
- forte
- média
- frágil

### 4. Papel atual do CRM
- complementar
- secundário
- não confiável para decisão do período

### 5. Diagnóstico principal
Exemplo:
- marketing gera lead, mas a ponte para comercial está falhando
- comercial está atualizando bem a planilha, mas CRM está subpreenchido
- os números ainda não podem ser tratados como reconciliação final

### 6. Próximas ações
Exemplo:
- auditar n8n
- padronizar chave entre planilhas
- revisar preenchimento obrigatório no CRM
- validar se `ID_LEAD` está chegando de ponta a ponta

## Regra de honestidade
Se o stack ainda não foi validado completamente, o agente não deve apresentar cruzamento entre marketing e comercial como se fosse base final consolidada.

A análise pode ser útil, mas deve carregar a classe de evidência correta e deixar explícito o grau de integridade da ponte entre as camadas.
