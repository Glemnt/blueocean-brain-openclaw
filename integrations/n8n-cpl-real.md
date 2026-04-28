# n8n — CPL Real e Dashboard Comercial

## Objetivo

Especificar como workflows de CPL real devem transformar eventos de mídia, CRM e Sheets em métricas confiáveis.

## Fontes

- Meta Ads: gasto, campanha, adset, anúncio, leads/conversas de plataforma.
- Kommo: leads, status, owner, perda/ganho, reunião.
- Sheets: camada operacional e cálculo/dash.
- n8n: orquestração, validação, logs e alertas.

## Métricas derivadas

- CPL plataforma = gasto / leads Meta.
- CPL operacional = gasto / leads operacionalmente válidos.
- CPL real = gasto / Lead Real.
- CPAg = gasto / reuniões agendadas.
- CPR = gasto / reuniões realizadas.
- Taxa Lead Fantasma = 1 - Lead Real / lead plataforma, quando aplicável.

## Fluxo diário

1. Buscar gasto e leads Meta do dia/período.
2. Buscar leads Kommo do mesmo recorte.
3. Normalizar source_id/campanha.
4. Resolver matches e exceções.
5. Atualizar planilha/dash.
6. Comparar com dia anterior/semana.
7. Gerar alerta se houver anomalia.

## Validações

- Gasto não pode ser negativo.
- Lead Real não pode exceder lead operacional sem explicação.
- CPL real não deve ser calculado se denominador = 0; marcar como `Insuficiente`.
- Discrepância >20% entre fontes precisa anotação.
- Mudança de schema trava update automático.

## Saída mínima

| Campo | Descrição |
|---|---|
| date | data |
| spend | gasto |
| platform_leads | leads/conversas Meta |
| crm_leads | leads Kommo |
| valid_leads | leads operacionalmente válidos |
| real_leads | Leads Reais |
| meetings_scheduled | reuniões agendadas |
| meetings_held | reuniões realizadas |
| cpl_platform | CPL plataforma |
| cpl_real | CPL real |
| cpag | custo por reunião agendada |
| cpr | custo por reunião realizada |
| confidence | confiança |

## Red lines

- Não sobrescrever histórico sem snapshot.
- Não ocultar falha de match.
- Não misturar períodos/timezones.
- Não tratar célula vazia como zero sem regra explícita.
