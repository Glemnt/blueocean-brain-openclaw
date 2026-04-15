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
