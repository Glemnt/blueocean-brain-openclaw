# Desenho de Teste A/B

## Objetivo

Evitar testes que parecem científicos, mas não têm hipótese, métrica, duração ou critério de decisão.

## Hipótese

Formato obrigatório:

> Se alterarmos `[variável]` de `[A]` para `[B]`, esperamos `[efeito]` em `[métrica]`, porque `[racional]`.

## Uma variável por teste

Exemplos válidos:

- Hook A vs Hook B.
- Oferta A vs Oferta B.
- LP curta vs LP longa.
- CTA diagnóstico vs CTA demonstração.
- Público aberto vs interesse específico.

Evitar testar ao mesmo tempo: público + criativo + orçamento + LP.

## Métricas

- Métrica primária: uma só.
- Métricas guardrail: impedem vitória falsa.
- Métrica real: sempre que possível, validar além da plataforma.

Exemplo:

- Primária: CPL real.
- Guardrails: CTR, frequência, Lead Fantasma, no-show.
- Real: reunião realizada ou oportunidade.

## Duração e amostra

- Não decidir antes de 3 dias completos, salvo red line ou erro técnico.
- Evitar decisão com menos de 30 conversões por variante quando a métrica é lead.
- Para métricas mais profundas, usar leitura por tendência e confiança `Parcial` ou `Frágil`.
- Se budget for baixo, declarar que o teste é exploratório.

## MDE — efeito mínimo detectável

Defina antes:

- Que diferença justifica decisão?
- 5% raramente sustenta decisão com baixo volume.
- 20–30% pode ser suficiente para teste tático.
- Para decisão de alto custo, exigir evidência cruzada.

## Critérios de vitória

Uma variante vence só se:

- Melhorar a métrica primária acima do MDE.
- Não piorar guardrails críticos.
- Não aumentar Lead Fantasma ou no-show de forma relevante.
- Não violar promessa, escopo ou política.

## Saída obrigatória

1. Hipótese.
2. Variantes.
3. Público/recorte.
4. Métrica primária.
5. Guardrails.
6. Duração mínima.
7. MDE.
8. Critério de decisão.
9. Riscos e red lines.
10. Confiança esperada.
