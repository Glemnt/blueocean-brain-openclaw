# Projeção de Resultado

## Objetivo

Projetar cenários com incerteza explícita, sem transformar tendência parcial em promessa executiva.

## Entradas

- Período realizado e dias restantes.
- Gasto, leads, CPL, CPL real, reuniões, oportunidades, vendas.
- Sazonalidade conhecida.
- Mudanças de budget/campanha/stack/SDR.
- Histórico comparável.

## Tipos de projeção

### Run-rate simples

Útil quando o período é estável. Frágil se houve mudança relevante.

### Cenários

- Conservador: mantém ritmo pior recente ou aplica penalidade por risco.
- Base: ritmo atual ajustado por sazonalidade.
- Agressivo: considera melhorias já implementadas, mas não garantidas.

### Forecast por funil

Projetar etapa a etapa:

- gasto → leads;
- leads → leads operacionais válidos;
- válidos → reuniões;
- reuniões → oportunidades;
- oportunidades → ganho.

## Thresholds de confiança

| Condição | Confiança máxima |
|---|---|
| Menos de 7 dias de dados | Parcial |
| Uma única fonte sem cruzamento | Parcial |
| Dados verbais sem sistema | Frágil |
| Mudança de tracking no período | Frágil |
| Discrepância >20% entre fontes | Frágil |
| Sem CRM para forecast de receita | Insuficiente |
| Campos críticos CRM >50% vazios | Frágil |
| Stack contaminada conhecida | Frágil |
| Denominador zero em métrica-chave | Insuficiente para aquela métrica |

## Thresholds operacionais

### Volume mínimo

- Menos de 7 dias: tendência, não forecast forte.
- Menos de 30 leads no recorte: leitura Frágil para taxa profunda.
- Menos de 10 reuniões: cuidado ao projetar oportunidade/venda.
- Sem histórico comparável: usar cenários amplos.

### Variação relevante

- Variação <10%: pode ser ruído, salvo volume alto.
- Variação 10–20%: sinal de atenção.
- Variação >20%: investigar causa antes de decisão forte.
- Variação >30% em métrica real: exige hipótese e owner.

### Conversão e funil

- Lead Fantasma >30%: penalizar cenário base.
- No-show >40%: penalizar reunião realizada/oportunidade.
- SLA crítico: limitar cenário agressivo.
- Campos de perda ausentes: reduzir confiança em causa comercial.

## Fórmulas base

- Run-rate = realizado / dias decorridos × dias totais.
- CPL projetado = gasto projetado / leads projetados.
- CPL real projetado = gasto projetado / Lead Real projetado.
- CPAg projetado = gasto projetado / reuniões agendadas projetadas.
- CPR projetado = gasto projetado / reuniões realizadas projetadas.

## Sensibilidades obrigatórias

Simular impacto de:

- CPL real +20% / -20%;
- taxa de Lead Real +10pp / -10pp;
- no-show +10pp / -10pp;
- budget +20% / -20%;
- perda de tracking ou campos vazios.

## Regras de confiança

- Menos de 7 dias: máximo `Parcial`.
- Mudança de tracking no período: máximo `Frágil`.
- Sem CRM: `Insuficiente` para receita.
- Discrepância >20% entre fontes: máximo `Frágil`.
- Forecast agressivo nunca pode ter confiança maior que o cenário base.

## Saída obrigatória

- Resultado realizado.
- Projeção conservadora/base/agressiva.
- Premissas.
- Sensibilidades.
- O que pode invalidar a projeção.
- Decisões que podem ou não ser tomadas.
- Confiança.
