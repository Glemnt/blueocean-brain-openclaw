# Schemas

Schemas são contratos de input para análises recorrentes.

Eles são mais completos que `templates/`, mas não devem virar formulário obrigatório em toda conversa.

## Regra de uso

- usar quando a análise precisa de estrutura forte;
- preencher automaticamente via integrações quando possível;
- pedir ao usuário apenas campos realmente faltantes;
- marcar ausências como limitação de confiança.

## Schemas atuais

- `meta-campaign.md`
- `meta-audit.md`
- `meta-creative-inventory.md`
- `experiment.md`
- `data-integrity.md`
- `whatsapp-redirect-event.md`
- `sdr-analysis.md`
- `copy-ads.md`
- `competitive-analysis.md`

## Relação com templates

- `templates/` = entrada/saída leve para conversa;
- `schemas/` = contrato profundo para análise consistente;
- `evals/` = cenários para validar comportamento.
