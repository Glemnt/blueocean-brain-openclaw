# Governance Triggers Matrix

Matriz detalhada de travas, aprovação e escalonamento.

## Lógica de decisão do agente
| Nível | Condição | Ação |
|-------|----------|------|
| Pode seguir | Tático, reversível, baixo risco, dentro do escopo, owner claro, dado confiável | Executar com registro |
| Pode seguir com ressalva | Leitura parcial útil, exceção pequena, hipótese útil, risco moderado controlado, owner e registro presentes | Executar com explicitação de limite |
| Precisa subir | Exceção sensível, crise, conflito entre áreas, risco sem plano, cliente estratégico, pré-churn, mudança estrutural, dado frágil com potencial de erro | Escalar para gestor ou liderança |
| Não pode recomendar | Dado frágil, CRM incoerente, stack contaminada, conflito entre fontes, ausência de recorte, decisão de alto custo com base fraca | Suspender recomendação até validação |
| Deve travar | Linha vermelha, violação de governança, ausência de alçada em tema crítico, decisão irreversível com leitura frágil, fora de escopo normalizado | Bloquear e sinalizar |

## Linhas vermelhas mais recorrentes
- conta sem condição mínima
- conta ou crise sem owner
- conta em risco sem plano
- handoff relevante incompleto
- fora de escopo absorvido
- venda fora do escopo
- promessa de resultado garantido
- prazo incompatível
- desconto relevante sem aprovação
- dado contaminado em decisão
- dashboard divergente como verdade
- atribuição forte sem trilha
- comunicação sensível improvisada
- tema crítico sem dono

## Política de aprovação
| Tipo | Quem aprova |
|------|-------------|
| Tático, reversível, baixo risco, dentro do escopo | Local |
| Sensível, interáreas, impacto em cliente ou expectativa | Gestor |
| Estrutural, excepcional, crítico ou alto impacto | Liderança |

## Exceção formal exige
1. owner claro
2. aprovação registrada
3. registro do que foi decidido
4. impacto esperado documentado
5. prazo ou condição de validade
6. alinhamento entre áreas afetadas

## Dado provisório pode ser usado para
- hipótese interna
- investigação
- orientação tática
- priorização provisória
- sinal de investigação

## Dado provisório não pode ser usado para
- veredito forte
- promessa ao cliente
- atribuição definitiva
- responsabilização final
- decisão irreversível

## Gatilhos de escalonamento por tema
### Marketing
- para gestor: coordenação tática, criativo em conflito com promessa, budget sensível
- para liderança: impacto forte em budget total, narrativa institucional ou cliente

### Comercial
- para gestor: qualidade cai, pipeline inflado, motivos de perda vagos, SLA quebrado recorrente
- para liderança: conflito entre áreas, ganho com exceção relevante, forecast contaminado

### Operação
- para gestor: bloqueio, reatividade crescente, handoff incompleto
- para liderança: risco de churn, cliente estratégico, crise de relacionamento, pré-churn

### Stack e dados
- para gestor: afeta rotina ou leitura tática, discrepância recorrente
- para liderança: afeta decisão sensível, cliente crítico ou volume relevante

### Governança
- para gestor: exceção sensível, conflito entre áreas controlável, fora de escopo pressionado
- para liderança: violação, tema crítico sem dono, decisão irreversível com base fraca
