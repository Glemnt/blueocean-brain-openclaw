# Blue Ocean Brain OpenClaw

Brain operacional da Blue Ocean para diagnóstico, decisão e execução assistida em marketing, comercial, dados, stack, governança, copy, inteligência competitiva e reporting.

Este repositório é a fonte canônica do agente. Ele organiza a inteligência da Blue Ocean em camadas claras, seguras e utilizáveis no OpenClaw.

## Objetivo

Dar ao agente principal e aos subagentes uma base confiável para:

- diagnosticar problemas de mídia, CRM, comercial, operação e stack;
- proteger escopo, confiança, dados, ownership e retenção;
- decidir quando seguir, quando subir e quando travar;
- produzir relatórios, planos, forecasts, análises competitivas e copy com governança;
- preservar aprendizado recorrente sem versionar dados sensíveis.

## Como navegar

Leitura inicial recomendada:

1. `AGENTS.md`
2. `OPERATOR_GUIDE.md`
3. `REPO_INDEX_BY_QUESTION.md`
4. `company/identity.md`
5. `company/offers.md`
6. `company/icp.md`
7. `governance/principles.md`
8. `governance/red-lines.md`
9. `governance/decision-framework.md`
10. `knowledge/company-brain/source-truth-rules.md`
11. `playbooks/README.md`
12. `subagents/README.md`
13. `integrations/README.md`
14. `templates/README.md`
15. `schemas/README.md`
16. `evals/README.md`

## Estrutura

- `company/` — identidade, ofertas, ICP e glossário operacional.
- `governance/` — princípios, linhas vermelhas, ownership, confiança, decisão e política de dados.
- `knowledge/` — benchmarks, padrões, matrizes, workflows, memória operacional e referência de copy/competitivo.
- `playbooks/` — fluxos operacionais canônicos.
- `subagents/` — especialistas por domínio.
- `integrations/` — contratos e operação das integrações reais.
- `templates/` — formatos de entrada, saída, handoff e status.
- `schemas/` — contratos profundos de dados/input para análises recorrentes.
- `evals/` — cenários de regressão e rubricas semânticas.
- `history/` — evidência curada, sanitizada e datada.
- `projects/` — blueprints estruturais multi-camada.
- `security/` — checklist e política prática de segurança pré-commit.
- `scripts/` — validações locais de evals e segurança.

## Playbooks principais

- `playbooks/triage.md`
- `playbooks/marketing-diagnosis.md`
- `playbooks/meta-ads-formal-audit.md`
- `playbooks/creative-inventory.md`
- `playbooks/ab-test-design.md`
- `playbooks/google-ads-diagnosis.md`
- `playbooks/media-planning.md`
- `playbooks/forecasting.md`
- `playbooks/period-comparison.md`
- `playbooks/crm-reconciliation.md`
- `playbooks/sheets-commercial-reconciliation.md`
- `playbooks/stack-failure-triage.md`
- `playbooks/lead-fantasma-triage.md`
- `playbooks/lead-qualification.md`
- `playbooks/account-risk.md`
- `playbooks/account-onboarding.md`
- `playbooks/sales-to-ops-handoff-review.md`
- `playbooks/governance-escalation.md`
- `playbooks/process-institutionalization-audit.md`
- `playbooks/competitive-intelligence.md`
- `playbooks/executive-reporting.md`
- `playbooks/action-prioritization.md`
- `playbooks/session-continuity.md`

## Subagents

- `subagents/meta-ads-analyst.md`
- `subagents/dados-bi-analyst.md`
- `subagents/sdr-comercial-analyst.md`
- `subagents/copy-strategist.md`
- `subagents/competitive-intelligence-analyst.md`

## Templates essenciais

- `templates/marketing-diagnosis.md`
- `templates/meta-health-score-output.md`
- `templates/ab-test-plan.md`
- `templates/media-plan.md`
- `templates/forecast-output.md`
- `templates/period-comparison.md`
- `templates/crm-reconciliation.md`
- `templates/sdr-analysis.md`
- `templates/lead-qualification.md`
- `templates/account-onboarding.md`
- `templates/competitive-intelligence.md`
- `templates/handoff-subagente.md`
- `templates/status-snapshot.md`
- `templates/response-modes.md`
- `templates/executive-report-output.md`
- `templates/action-prioritization-output.md`

## Regra transversal mais importante

Quando houver dúvida sobre qual dado prevalece, usar a **fonte mais próxima do evento real**.

Exemplos:

- plataforma para entrega e spend;
- Kommo/CRM para status comercial e avanço de lead;
- Sheets/dashboard como camada derivada e operacional quando documentada;
- operação validada pelo usuário quando houver conflito de rotina/ownership;
- evidência histórica apenas como contexto, nunca como dado atual.

## Gates locais

Antes de commit relevante:

```bash
python3 scripts/eval_harness.py
python3 scripts/repo_safety_scan.py
git diff --check
```

## Segurança

Nunca versionar:

- secrets, tokens, service accounts ou `.env`;
- CSV/TSV/export bruto com clientes ou leads;
- payloads reais de webhook;
- nomes, emails, telefones ou documentos em massa;
- logs com PII;
- cache/runtime/vendor.

Se uma evidência real precisa ensinar o brain, criar resumo sanitizado em `history/`, `knowledge/`, `playbooks/` ou `integrations/`.
