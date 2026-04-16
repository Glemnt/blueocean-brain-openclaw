# CRM Reconciliation Template

Usar quando o objetivo for reconciliar fontes, validar integridade de dados ou descobrir onde a trilha quebra.

## Obrigatório
- fontes sendo comparadas
- período analisado
- métrica, evento ou trilha a validar
- canal ou fluxo principal em foco

## Fortemente recomendado
- descrição da divergência percebida
- tamanho aproximado da discrepância
- se a fonte mais próxima do evento real está disponível
- se há suspeita de webhook, automação, duplicidade ou campo vazio

## Opcional
- IDs, links ou nomes exatos de campanha, planilha ou fluxo
- exemplo concreto de lead ou registro
- hipótese inicial

## Pergunta mínima sugerida
```text
Me manda só:
1. quais fontes você quer reconciliar
2. qual período
3. qual métrica ou evento precisa validar
4. qual canal ou fluxo está em foco
```
