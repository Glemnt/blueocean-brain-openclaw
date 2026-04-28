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

## Regras de confiança

- Menos de 7 dias: máximo `Parcial`.
- Mudança de tracking no período: máximo `Frágil`.
- Sem CRM: `Insuficiente` para receita.
- Discrepância >20% entre fontes: máximo `Frágil`.

## Saída obrigatória

- Resultado realizado.
- Projeção conservadora/base/agressiva.
- Premissas.
- Sensibilidades.
- O que pode invalidar a projeção.
- Decisões que podem ou não ser tomadas.
- Confiança.
