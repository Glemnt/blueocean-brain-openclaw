# Blue Ocean Brain OpenClaw

Repositório nativo OpenClaw para a operação intelectual da Blue Ocean.

Ele nasce a partir do `blueocean-brain`, mas não tenta copiar o runtime anterior. A proposta aqui é portar a inteligência, reorganizar o canon e deixar a arquitetura mais limpa, portátil e governável.

## Objetivo
Transformar o conteúdo útil do `blueocean-brain` em um brain OpenClaw mais coerente para uso real, com menos duplicação, mais clareza de ownership e melhor separação entre canon, referência, playbooks, especialistas, integrações e templates.

## Status atual
- canon principal migrado
- knowledge essencial portado e expandido com camada competitiva
- playbooks operacionais, estratégicos e executivos centrais criados e validados
- primeira rodada de subagents nativos criada e validada
- documentação das integrações principais consolidada
- templates de entrada e saída adicionados para usos recorrentes
- repositório original preservado como fonte histórica de comparação

## Princípios da migração
- portar a inteligência, não a interface do runtime anterior
- reduzir duplicação e colapso de instruções repetidas
- centralizar regras canônicas em lugares estáveis
- usar playbooks como fluxos operacionais e subagents como especialistas de domínio
- manter referências detalhadas em `knowledge/`
- preservar a fonte mais próxima do evento real ao definir verdade operacional
- melhorar o que estava acoplado ao Claude, em vez de copiar cegamente

## Como navegar
Se você está chegando agora, a leitura recomendada é:
1. `company/identity.md`
2. `company/offers.md`
3. `company/icp.md`
4. `governance/principles.md`
5. `governance/red-lines.md`
6. `governance/decision-framework.md`
7. `knowledge/company-brain/source-truth-rules.md`
8. `integrations/README.md`
9. `playbooks/README.md`
10. `subagents/README.md`
11. `templates/README.md`
12. `evals/README.md`

## Estrutura
- `company/` — identidade, ofertas, ICP e glossário operacional
- `governance/` — princípios, linhas vermelhas, ownership, confiança e decisão
- `knowledge/` — base documental, matrizes, padrões, benchmarks e referências
- `playbooks/` — fluxos operacionais canônicos
- `subagents/` — especialistas OpenClaw por domínio
- `integrations/` — documentação de integrações reais e seus limites
- `templates/` — templates enxutos para entradas e saídas recorrentes
- `schemas/` — contratos profundos de input para análises recorrentes
- `evals/` — cenários de regressão para proteger decisões e armadilhas críticas
- `history/` — evidência histórica curada, sanitizada e datada
- `projects/` — blueprints estruturais multi-camada
- `security/` — checklist e scans de segurança pré-commit
- `scripts/` — validações locais de evals e segurança
- `MIGRATION_PROGRESS.md` — acompanhamento da migração funcional até 100%

## Playbooks atuais
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

## Subagents atuais
- `subagents/meta-ads-analyst.md`
- `subagents/dados-bi-analyst.md`
- `subagents/sdr-comercial-analyst.md`
- `subagents/copy-strategist.md`
- `subagents/competitive-intelligence-analyst.md`

## Templates atuais
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
Quando houver dúvida sobre qual dado prevalece, vale a **fonte mais próxima do evento real**.

Exemplos:
- plataforma para entrega e spend
- CRM para avanço comercial e status do lead
- operação real para saúde da conta
- dashboard como visualização derivada, não verdade final isolada

## Relação com o repositório original
O `blueocean-brain` continua sendo a fonte histórica de referência durante a migração.

Este repositório novo existe para:
- consolidar o que vale manter
- corrigir acoplamentos do runtime anterior
- simplificar a operação em OpenClaw
- servir como base principal e evolutiva do brain

## Revisão de cobertura
- `MIGRATION_COVERAGE_REVIEW.md` — revisão final da migração legado Claude Code → OpenClaw, incluindo o que foi migrado, enriquecido e excluído intencionalmente.
- `history/legacy-design-lineage.md` — linhagem do system prompt e princípios antigos em forma segura e OpenClaw-native.


## Uso operacional
- `OPERATOR_GUIDE.md` — guia curto de qual rota usar para cada tipo de pedido.
- `REPO_INDEX_BY_QUESTION.md` — índice por pergunta/domínio.
- `ROBUSTNESS_HARDENING_LOG.md` — registro das correções de robustez pós-auditoria.
- `INFRA_ROBUSTNESS_AUDIT.md` — auditoria de robustez da infra documental/operacional.
