# Operator Guide — Como usar o Blue Ocean Brain OpenClaw

Este guia responde: **qual arquivo usar para cada tipo de pergunta?**

## Regra-mãe

Comece pelo menor caminho que resolve a decisão, mas sempre preserve:

- fonte de verdade;
- confiança;
- owner;
- red lines;
- diferença entre fato, hipótese e recomendação.

## Roteiro por pergunta

| Pergunta do usuário | Comece por | Depois consulte | Saída recomendada |
|---|---|---|---|
| “O que está acontecendo?” | `playbooks/triage.md` | `governance/decision-framework.md` | classificação + próximo playbook |
| “A campanha está boa?” | `playbooks/marketing-diagnosis.md` | `schemas/meta-campaign.md`, `knowledge/benchmarks/blue-ocean-benchmarks.md` | diagnóstico com confiança |
| “Faça uma auditoria Meta completa” | `playbooks/meta-ads-formal-audit.md` | `templates/meta-health-score-output.md`, `schemas/meta-audit.md` | health score |
| “Por que Meta mostra lead e CRM não?” | `playbooks/lead-fantasma-triage.md` | `integrations/whatsapp-ctwa-tracking.md`, `schemas/whatsapp-redirect-event.md` | camada de quebra |
| “Os dados batem?” | `playbooks/crm-reconciliation.md` | `schemas/data-integrity.md`, `integrations/dashboard-derived-metrics.md` | reconciliação |
| “Sheets está mais confiável que CRM?” | `playbooks/sheets-commercial-reconciliation.md` | `integrations/google-sheets-operating-model.md` | regra de prevalência |
| “Stack quebrou?” | `playbooks/stack-failure-triage.md` | `knowledge/workflows/tracking-stack-checklist.md` | origem da falha |
| “Planeje mídia” | `playbooks/media-planning.md` | `templates/media-plan.md` | plano por canal/budget |
| “Projete resultado” | `playbooks/forecasting.md` | `templates/forecast-output.md` | cenários |
| “Compare períodos” | `playbooks/period-comparison.md` | `templates/period-comparison.md` | leitura normalizada |
| “Qualifique esse lead” | `playbooks/lead-qualification.md` | `templates/lead-qualification.md` | classificação e próxima ação |
| “Analise SDR/comercial” | `subagents/sdr-comercial-analyst.md` | `schemas/sdr-analysis.md`, `evals/sdr-comercial.md` | diagnóstico comercial |
| “Crie/revise copy” | `subagents/copy-strategist.md` | `knowledge/copy/frameworks.md`, `schemas/copy-ads.md` | copy com red lines |
| “Analise concorrente” | `playbooks/competitive-intelligence.md` | `knowledge/competitive-intelligence/analysis-frameworks.md`, `schemas/competitive-analysis.md` | aprendizado adaptável |
| “Prepare relatório executivo” | `playbooks/executive-reporting.md` | `templates/executive-report-output.md` | resumo executivo |
| “Priorize ações” | `playbooks/action-prioritization.md` | `templates/action-prioritization-output.md` | matriz de ação |
| “Conta está em risco?” | `playbooks/account-risk.md` | `governance/ownership.md`, `governance/red-lines.md` | contenção por owner |
| “Precisa escalar/travar?” | `playbooks/governance-escalation.md` | `governance/decision-framework.md` | decisão de alçada |

## Fluxo padrão de trabalho

1. Identifique o tipo de problema.
2. Escolha o playbook/subagent.
3. Verifique fonte de verdade.
4. Classifique confiança.
5. Procure red lines.
6. Declare owner.
7. Recomende próxima ação proporcional.
8. Se gerou aprendizado recorrente, aplique `governance/learning-loop.md`.

## Quando usar schemas

Use `schemas/` quando:

- a análise é recorrente;
- há múltiplas fontes;
- falta dado importante;
- a decisão tem custo alto;
- você precisa reduzir ambiguidade.

Não transforme schema em formulário completo para o usuário. Peça só o que falta para decidir com segurança.

## Quando usar evals

Use `evals/` antes de mudanças grandes em playbooks/subagents ou quando quiser validar se uma resposta respeita as armadilhas críticas.

Rode também `scripts/eval_harness.py` para checar a integridade estrutural dos cenários.

## Quando usar history

Use `history/` para entender por que uma regra existe. Não use histórico como dado atual de performance.

## Red lines operacionais

- Não inferir receita/qualidade só por Meta.
- Não chamar lead estrutural de Lead Real.
- Não usar dashboard como fonte final isolada.
- Não recomendar escala com stack contaminada.
- Não versionar PII, token, CSV/TSV cru ou payload real.
