# Schema — Auditoria Meta Ads

Campos esperados para auditoria formal.

## Identificação

- `account_name_sanitized`
- `period_start`
- `period_end`
- `comparison_period`
- `primary_objective`

## Estrutura

- `campaigns[]`: nome sanitizado, objetivo, budget, status, hipótese.
- `adsets[]`: campanha, público, orçamento, evento, learning status.
- `ads[]`: adset, formato, hook, ângulo, CTA, status.

## Métricas

- `spend`
- `impressions`
- `reach`
- `frequency`
- `cpm`
- `ctr`
- `cpc`
- `platform_leads_or_conversations`
- `platform_cpl`
- `crm_leads`
- `operationally_valid_leads`
- `real_leads`
- `meetings_scheduled`
- `meetings_held`
- `opportunities`
- `sales`

## Stack

- `pixel_status`
- `capi_status`
- `gtm_status`
- `webhook_status`
- `source_map_status`
- `dedupe_status`
- `known_failures[]`

## Governança

- `owner`
- `decision_scope`
- `red_lines[]`
- `confidence`
