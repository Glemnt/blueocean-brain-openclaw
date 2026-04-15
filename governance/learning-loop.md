# Learning Loop

Regras para melhoria contínua do agente principal da Blue Ocean dentro da arquitetura OpenClaw.

## Princípio
Toda interação relevante pode gerar aprendizado.

Mas aprendizado útil não deve ficar preso em contexto efêmero. Quando algo se prova recorrente, valioso ou corretivo, deve ser promovido para o lugar certo do repositório.

## Regra operacional
Ao final de análises, diagnósticos, reconciliações ou decisões relevantes, avaliar se surgiu algo que deve fortalecer o sistema.

Pergunta de controle:

"Isso foi só útil agora ou deve melhorar o agente nas próximas vezes também?"

Se deve melhorar o agente nas próximas vezes, precisa ser consolidado.

## O que promover
Promover quando surgir:
- benchmark interno novo ou corrigido
- padrão diagnóstico recorrente
- mudança relevante de operação
- regra de governança que faltava
- handoff que precisou ser refinado
- fragilidade conhecida de stack ou integração
- ajuste de source of truth
- aprendizado sobre oferta, ICP, ciclo ou risco operacional

## Destino por tipo de aprendizado
- benchmark validado → `knowledge/benchmarks/`
- padrão recorrente → `knowledge/patterns/`
- regra de source of truth → `knowledge/company-brain/` ou `governance/`
- mudança de identidade, oferta ou ICP → `company/`
- regra de decisão, ownership ou trava → `governance/`
- fluxo operacional reutilizável → `playbooks/`
- fronteira de especialista ou handoff → `subagents/`
- detalhe técnico persistente de stack → `integrations/`

## Quando perguntar ao usuário
Perguntar antes de consolidar quando a mudança:
- altera regra canônica
- muda interpretação da empresa
- adiciona benchmark que passa a orientar decisão
- atualiza operação real da Blue Ocean
- formaliza comportamento novo do agente principal

## Quando não precisa virar canon ainda
Pode continuar como contexto local quando for:
- rascunho de investigação
- hipótese ainda não validada
- snapshot transitório
- relatório temporário
- contexto de sessão ainda em aberto

## Forma recomendada da sugestão
Quando houver oportunidade real de melhoria, usar formato simples:

```text
Oportunidade de melhoria: [descrição curta]
Se eu consolidar isso em [arquivo ou área], o sistema passa a [benefício].
Quer que eu atualize?
```

## Regras de qualidade
- não sugerir melhoria vaga
- não gerar burocracia desnecessária
- não repetir a mesma sugestão se o usuário ignorar
- preferir consolidar menos coisas, mas consolidar as certas
- não deixar regra importante presa em memória local

## Relação com memória local
Memória local ajuda a operar.
Canon versionado ajuda a preservar inteligência.

Os dois coexistem, mas não cumprem o mesmo papel.
