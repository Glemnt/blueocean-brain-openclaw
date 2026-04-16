# Blue Ocean Brain OpenClaw

Repositório nativo OpenClaw para a operação intelectual da Blue Ocean.

Ele nasce a partir do `blueocean-brain`, mas não tenta copiar o runtime anterior. A proposta aqui é portar a inteligência, reorganizar o canon e deixar a arquitetura mais limpa, portátil e governável.

## Objetivo
Transformar o conteúdo útil do `blueocean-brain` em um brain OpenClaw mais coerente para uso real, com menos duplicação, mais clareza de ownership e melhor separação entre canon, referência, playbooks e especialistas.

## Status atual
- canon principal migrado
- knowledge essencial portado
- playbooks centrais iniciais criados e validados
- primeira rodada de subagents nativos criada e validada
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
8. `playbooks/README.md`
9. `subagents/README.md`

## Estrutura
- `company/` — identidade, ofertas, ICP e glossário operacional
- `governance/` — princípios, linhas vermelhas, ownership, confiança e decisão
- `knowledge/` — base documental, matrizes, padrões, benchmarks e referências
- `playbooks/` — fluxos operacionais canônicos
- `subagents/` — especialistas OpenClaw por domínio
- `integrations/` — documentação de integrações reais e seus limites
- `templates/` — inputs mínimos recomendados para análises recorrentes

## Playbooks atuais
- `playbooks/triage.md`
- `playbooks/marketing-diagnosis.md`
- `playbooks/crm-reconciliation.md`
- `playbooks/account-risk.md`
- `playbooks/governance-escalation.md`

## Subagents atuais
- `subagents/meta-ads-analyst.md`
- `subagents/dados-bi-analyst.md`
- `subagents/sdr-comercial-analyst.md`
- `subagents/copy-strategist.md`
- `subagents/competitive-intelligence-analyst.md`

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
- servir como futura base principal do brain
