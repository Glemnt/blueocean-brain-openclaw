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

## Fluxo obrigatório para toda demanda Blue Ocean

Toda demanda Blue Ocean deve seguir este fluxo antes de responder ou executar:

1. **Classificar a demanda**
   - diagnóstico, relatório, reconciliação, copy, SDR, stack, forecast, governança, integração ou migração.
   - se ambígua, começar por `playbooks/triage.md`.

2. **Escolher a rota canônica**
   - usar `OPERATOR_GUIDE.md` e `REPO_INDEX_BY_QUESTION.md` para decidir o playbook/subagent/schema/template correto.
   - não improvisar fluxo novo se já existe rota no repo.

3. **Verificar fonte de verdade**
   - plataforma para entrega/spend;
   - Kommo/CRM para status comercial;
   - Sheets/dashboard como camada derivada;
   - operação validada pelo usuário quando houver conflito;
   - se houver divergência, reduzir confiança.

4. **Aplicar governança antes da otimização**
   - consultar `governance/red-lines.md`, `governance/confidence-system.md` e `governance/decision-framework.md` quando a decisão tiver risco.
   - nunca recomendar escala, pausa forte, responsabilização ou promessa executiva com dado frágil.

5. **Usar o especialista certo**
   - Meta/mídia → `subagents/meta-ads-analyst.md` ou playbooks de marketing.
   - Dados/BI → `subagents/dados-bi-analyst.md`.
   - SDR/comercial → `subagents/sdr-comercial-analyst.md`.
   - Copy → `subagents/copy-strategist.md`.
   - Competitivo → `subagents/competitive-intelligence-analyst.md`.
   - Handoff entre domínios deve usar `templates/handoff-subagente.md`.

6. **Declarar confiança e limites**
   - toda recomendação relevante deve declarar: Alta, Parcial, Frágil ou Insuficiente.
   - separar fato, hipótese e recomendação.
   - declarar o que não dá para concluir.

7. **Fechar com ação operacional**
   - indicar owner ou tipo de owner;
   - próxima ação;
   - dependência;
   - se precisa subir/travar/seguir.

8. **Preservar aprendizado quando necessário**
   - se a demanda gerou regra reutilizável, evidência curada ou ajuste de canon, aplicar `knowledge/memory-governance.md`.
   - não versionar PII, secrets ou exports brutos.

## Proibição operacional

Não responder demanda Blue Ocean apenas com opinião solta. Toda resposta deve estar ancorada em rota, evidência, confiança e próxima ação proporcional.
