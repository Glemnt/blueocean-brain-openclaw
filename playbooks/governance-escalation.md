# Governance Escalation Playbook

Playbook principal para decidir quando seguir, quando sinalizar ressalva, quando subir e quando travar.

## Quando usar
- exceção sensível, conflito entre áreas ou tema sem owner
- desconto, mudança de escopo, comunicação sensível ou decisão estrutural
- linha vermelha, governança quebrada ou decisão importante com base frágil
- dúvida sobre alçada, aprovação ou necessidade de escalonamento
- situação em que o problema principal não é técnico, mas de governança

## Objetivo
1. classificar a situação no nível correto de governança
2. explicitar owner, co-owner e alçada
3. impedir que exceções virem rotina informal
4. travar decisões irreversíveis com base frágil ou sem aprovação

## Pré-checagem obrigatória
Antes de concluir:
- quem é o owner principal do tema?
- existe co-owner legítimo ou responsabilidade difusa?
- o tema é tático, sensível, estrutural ou crítico?
- a base é confiável ou frágil?
- há cliente estratégico, impacto relevante ou risco reputacional?
- existe exceção formal, aprovação registrada e validade clara?

Se o problema for “ninguém sabe de quem é”, tratar isso como prioridade antes de qualquer outra conclusão.

## Hierarquia de leitura
### 1. Ownership
Verificar:
- owner principal existe e está explícito
- há co-owner legítimo ou apenas difusão de responsabilidade
- o tema já está em terra de ninguém

### 2. Integridade da base
Verificar:
- a decisão está apoiada em fonte próxima do evento real
- CRM, stack, dashboard e operação convergem o suficiente
- a base é forte, parcial, frágil ou insuficiente

### 3. Tipo de exceção ou risco
Verificar:
- desconto relevante
- mudança de escopo
- fora de escopo absorvido
- crise de relacionamento
- pré-churn ou churn sensível
- comunicação improvisada
- decisão irreversível ou de alto custo

### 4. Alçada e escalonamento
Classificar se a situação:
- pode seguir
- pode seguir com ressalva
- precisa subir
- não pode recomendar com confiança ainda
- deve travar e sinalizar

### 5. Formalização
Verificar se existe:
- owner claro
- aprovação registrada
- impacto documentado
- prazo ou condição de validade
- alinhamento entre áreas afetadas

## Classes de evidência
Usar esta leitura mínima:
- Classe 1: fato validado e documentado
- Classe 2: fato operacional confiável, mas ainda sem cruzamento completo
- Classe 3: hipótese operacional ou conflito controlado
- Classe 4: inferência provisória com base parcial
- Classe 5: dado ausente, conflito grave ou tema crítico sem dono

Mapeamento para confiança:
- Classes 1 e 2 predominantes: Alta
- Classes 2 e 3 predominantes: Parcial
- Classes 3 e 4 predominantes: Frágil
- Classes 4 e 5 predominantes: Insuficiente

## Travas imediatas
Tratar como trava direta quando houver:
- linha vermelha
- tema crítico sem dono
- decisão irreversível com leitura frágil
- dado contaminado em decisão sensível
- desconto relevante sem aprovação
- fora de escopo sendo normalizado
- comunicação sensível improvisada ao cliente

## Saída recomendada
A análise final deve sempre responder:
1. diagnóstico executivo
2. tipo de problema de governança
3. classe de evidência predominante
4. confiança final: Alta, Parcial, Frágil ou Insuficiente
5. owner principal e co-owner
6. nível de governança: pode seguir, ressalva, precisa subir, não pode recomendar, deve travar
7. nível de alçada: local, gestor ou liderança
8. ação inicial obrigatória
9. formalização necessária
10. principais alertas
11. o que ainda precisa validar

## Regras de qualidade
- não suavizar linha vermelha
- não empurrar problema de ownership para depois
- não deixar exceção sensível sem registro
- não normalizar fora de escopo informal
- não autorizar decisão estrutural com base frágil
- usar `knowledge/matrices/governance-triggers-matrix.md` para validar trava e escalonamento
- usar `knowledge/matrices/ownership-governance-matrix.md` para validar owner real

## Referências
- `governance/principles.md`
- `governance/red-lines.md`
- `governance/ownership.md`
- `governance/decision-framework.md`
- `governance/confidence-system.md`
- `knowledge/matrices/ownership-governance-matrix.md`
- `knowledge/matrices/governance-triggers-matrix.md`
