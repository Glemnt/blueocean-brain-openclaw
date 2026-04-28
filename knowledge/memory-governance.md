# Memory Governance

Política para separar memória operacional local de inteligência consolidada do `blueocean-brain-openclaw`.

## Princípio central
O agente principal pode operar com memória local e contexto transitório, mas a inteligência durável da Blue Ocean deve ser promovida para o repositório versionado quando passar a ter valor recorrente.

Em outras palavras:
- estado local ajuda a operar
- canon versionado ajuda a lembrar certo

## Regra-mãe
Tudo que for importante apenas para a execução local pode ficar fora do git.

Tudo que passar a ser:
- decisão estável
- framework reutilizável
- regra operacional recorrente
- referência que reduz erro futuro
- aprendizado relevante sobre a Blue Ocean

deve ser promovido para um arquivo versionado no repositório.

## O que pode ficar só na memória local
Exemplos:
- contexto transitório de conversa
- lembretes de curto prazo
- rascunhos de investigação
- snapshots intermediários
- relatórios ainda não consolidados
- estado de sessões em andamento
- material temporário de triagem

## O que deve virar inteligência versionada
Exemplos:
- decisões de governança
- mudança de posicionamento, oferta ou ICP
- novos critérios de ownership
- padrões diagnósticos recorrentes
- regras de source of truth
- playbooks estabilizados
- fronteiras e handoffs entre subagents
- benchmarks ou definições que passaram a orientar decisão real
- integrações e fragilidades conhecidas do stack

## Destino recomendado por tipo de aprendizado
- identidade, posicionamento, oferta, ICP, glossário → `company/`
- governança, ownership, confiança, decisão, linhas vermelhas → `governance/`
- referência recorrente, padrões, benchmarks, matrizes → `knowledge/`
- fluxo operacional reutilizável → `playbooks/`
- especialização de domínio e fronteira de atuação → `subagents/`
- detalhe técnico de integração real → `integrations/`

## Regra operacional para o agente principal
Como agente principal da Blue Ocean:
- tratar memória local como apoio, não como verdade final
- consolidar no repositório tudo que virar inteligência de longo prazo
- não deixar aprendizados importantes presos apenas em contexto efêmero
- preferir canon enxuto e forte em vez de acúmulo de notas soltas

## Relação com o `.gitignore`
O `.gitignore` pode esconder ruído operacional local, como `memory/`, `reports/`, `sessions/` e snapshots.

Isso é correto desde que o que realmente importa seja promovido depois para o repositório versionado.

O problema não é ignorar memória local.
O problema seria depender dela como repositório final da inteligência.

## Pergunta de controle
Antes de deixar algo só na memória local, perguntar:

"Isso ajuda apenas agora ou deveria continuar ensinando o sistema depois?"

Se deveria continuar ensinando, precisa virar arquivo versionado.

## Regras herdadas de operação do agente

A migração preserva a intenção do legado Claude Code, mas em forma OpenClaw-native.

### Quando sugerir salvar aprendizado

Sugerir consolidação quando uma interação gerar:

- benchmark real novo;
- diagnóstico com valor histórico;
- padrão repetido;
- mudança de SDR, campanha, pipeline, source_id ou campo;
- regra que evitou erro;
- lacuna de template/schema;
- fragilidade de integração recorrente.

### Onde salvar

| Aprendizado | Destino OpenClaw |
|---|---|
| Snapshot bruto/local | fora do git ou `snapshots/` local |
| Evidência curada datada | `history/` |
| Benchmark validado | `knowledge/benchmarks/` |
| Padrão diagnóstico | `knowledge/patterns/` |
| Regra operacional | `governance/` ou `playbooks/` |
| Integração/stack | `integrations/` |
| Campo/schema | `schemas/` |

### Regra de autorização

- Não promover dado sensível, PII, token, export bruto ou conversa privada.
- Mudanças canônicas relevantes devem ser explicitadas ao usuário.
- Evidência histórica deve ser sanitizada e datada.

### Continuidade de sessão

No OpenClaw, continuidade deve usar:

- memória local para contexto transitório;
- `MIGRATION_PROGRESS.md` ou trackers explícitos para migrações;
- `history/` para evidência curada;
- `templates/handoff-subagente.md` para passagem entre especialistas;
- TaskFlow/cron apenas quando houver trabalho durável ou espera real.

## Continuidade operacional obrigatória

Para trabalhos longos, aplicar `playbooks/session-continuity.md`.

A continuidade deve preservar:

- objetivo;
- decisões;
- arquivos;
- validações;
- lacunas;
- próxima ação.

A continuidade não deve preservar dados sensíveis ou dumps crus.

Se o trabalho atravessar subagents, usar `templates/handoff-subagente.md` para cada transferência de domínio.
