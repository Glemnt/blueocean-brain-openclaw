# AGENTS.md - Blue Ocean Brain OpenClaw

Este workspace contém a versão OpenClaw do brain da Blue Ocean.

## Regras de migração
- Não portar a estrutura Claude de forma literal
- Não duplicar regras canônicas em múltiplos arquivos sem necessidade
- Priorizar referências curtas no núcleo e detalhes em arquivos específicos
- Separar claramente: identidade, governança, playbooks, knowledge, integrações e operação

## Direção
O objetivo é criar um agente:
- mais enxuto
- mais confiável
- mais fácil de manter
- mais forte em governança
- mais natural no runtime do OpenClaw

## Estrutura canônica
- `company/` concentra identidade e negócio
- `governance/` concentra regras globais e sistema de confiança
- `playbooks/` concentra fluxos operacionais
- `knowledge/` concentra referências detalhadas
- `subagents/` concentra especialistas com prompts curtos

## Regras operacionais
- Antes de criar novos arquivos, verificar se já existe um lugar canônico
- Evitar repetir red lines, confidence system e ownership em toda camada
- Knowledge longa deve ficar em referência, não no prompt residente
- Subagentes devem herdar o núcleo central e adicionar apenas especialização
