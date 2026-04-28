# Integrations

Documentação das integrações reais do ecossistema Blue Ocean.

Esta pasta existe para registrar como cada integração deve ser entendida dentro da arquitetura do brain.

## Papel desta camada
Cada integração documentada aqui deve esclarecer:
- finalidade operacional
- fonte de verdade por tipo de dado
- fragilidades conhecidas
- riscos de leitura incorreta
- limites de uso pelo agente principal e pelos especialistas

## Integrações atuais
- `meta-ads.md`
- `kommo.md`
- `kommo-field-mapping.md`
- `kommo-setup.md`
- `google-sheets.md`
- `google-sheets-setup.md`
- `google-sheets-operating-model.md`
- `n8n.md`
- `apify.md`
- `mcp-architecture.md`
- `mcp-rebuild-plan.md`
- `mcp-deployment-inventory.md`
- `mcp-operator-guide.md`
- `mcp-bootstrap-checklist.md`

## Regra de qualidade
Documentar uma integração não é só listar campos.

Também deve ficar claro:
- o que essa integração sabe de forma confiável
- o que ela não sabe
- quando ela é fonte primária
- quando ela é derivada
- quais erros comuns de interpretação ela pode induzir


## Especificações operacionais adicionadas
- `whatsapp-ctwa-tracking.md` — arquitetura CTWA/micro-LP/source_id/Lead Real.
- `n8n-whatsapp-ctwa.md` — fluxo n8n/Salesbot/Kommo sanitizado para CTWA.
- `n8n-cpl-real.md` — workflow conceitual de CPL real e dashboard comercial.
- `dashboard-derived-metrics.md` — fórmulas e regras de confiança para métricas derivadas.


## Validação operacional viva
- `live-integration-validation.md` — plano de prova de vida para MCPs, n8n, Kommo, Sheets, Meta Ads e dashboards.
- `validation/` — registros sanitizados de validações reais.
