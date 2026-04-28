# Linhagem de Design do Legado Blue Ocean

Este arquivo preserva a genealogia útil do projeto Claude Code sem portar runtime, segredo, cache ou acoplamento de ferramenta.

## Origem

O legado definia o agente como especialista Blue Ocean para marketing, comercial, operação, dados, stack e governança. A migração OpenClaw preserva esse papel como arquitetura de camadas:

- `company/` para identidade, ofertas, ICP e glossário;
- `governance/` para princípios, red lines, confiança, ownership e decisão;
- `knowledge/` para benchmarks, padrões, matrizes e referência;
- `playbooks/` para fluxos;
- `subagents/` para especialistas;
- `integrations/` para stack real;
- `templates/`, `schemas/` e `evals/` para execução consistente.

## Prioridades herdadas

1. Proteger escopo.
2. Proteger confiança do cliente.
3. Proteger integridade do dado.
4. Proteger ownership e alçada.
5. Proteger retenção e saúde da conta.
6. Só depois otimizar performance tática.

## Classes de evidência herdadas

A migração consolidou o modelo de confiança em `governance/confidence-system.md`, mantendo a lógica:

- fato validado pelo usuário;
- padrão operacional provisório;
- documento/fonte operacional oficial;
- fonte mais próxima do evento real;
- hipótese operacional;
- inferência provisória;
- ponto não confirmado.

## Validações obrigatórias preservadas

Antes de recomendação relevante, verificar:

- owner principal;
- co-owner ou responsabilidade difusa;
- coerência do CRM;
- integridade da stack;
- aderência do dashboard à origem;
- camada de quebra do funil;
- reversibilidade/custo da decisão;
- necessidade de gestor, liderança ou trava.

## Não migrado literalmente

- slash commands `.claude/commands/`;
- frontmatter e wrappers de agentes Claude;
- SKILL.md acoplado ao runtime Claude;
- MCP servers locais/vendor;
- tokens, exports crus, cache, PII;
- prompts como system prompt ativo.

A inteligência foi reescrita em documentos operacionais OpenClaw-native.
