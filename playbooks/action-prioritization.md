# Action Prioritization Playbook

Playbook principal para transformar diagnóstico em ordem de ação clara, proporcional e executável.

## Quando usar
- após diagnóstico com múltiplas frentes possíveis
- quando há mais problemas do que capacidade de execução imediata
- quando é preciso decidir o que fazer primeiro
- quando há dependência entre correção de stack, operação, mídia ou comercial
- quando a equipe precisa de foco, não de lista infinita

## Objetivo
1. ordenar ações por impacto, urgência, dependência e confiança
2. evitar atacar sintoma antes da causa
3. impedir que ação vistosa passe na frente de correção estrutural
4. gerar sequência de execução realista

## Pré-checagem obrigatória
Antes de priorizar:
- a base está íntegra o suficiente para priorização forte?
- o problema principal já foi identificado?
- existe trava de stack ou governança que bloqueia outras ações?
- quais ações dependem de outras?
- o que é reversível e o que é sensível?

## Hierarquia de priorização
### 1. Travas e bloqueios
Verificar:
- existe falha de stack, red line ou risco sensível?
- algo precisa ser travado antes de qualquer otimização?

### 2. Causa raiz
Verificar:
- a ação ataca causa raiz ou só sintoma?
- existe correção estrutural que destrava outras?

### 3. Impacto
Verificar:
- a ação muda resultado, integridade ou risco de forma material?
- o impacto é local ou sistêmico?

### 4. Confiança
Verificar:
- a ação está sustentada por evidência alta, parcial, frágil ou insuficiente?
- vale executar agora ou esperar validação?

### 5. Sequência de execução
Concluir:
- o que fazer agora
- o que vem em seguida
- o que monitorar antes de agir
- o que deve ficar em espera

## Classes de evidência
Usar esta leitura mínima:
- Classe 1: ação sustentada por causa raiz validada
- Classe 2: ação sustentada por evidência confiável com ressalva limitada
- Classe 3: ação útil baseada em padrão ou leitura comparativa
- Classe 4: ação exploratória baseada em inferência
- Classe 5: ação sem base suficiente ou bloqueada por lacuna relevante

## Confiança
- Classes 1 e 2 predominantes: Alta
- Classes 2 e 3 predominantes: Parcial
- Classes 3 e 4 predominantes: Frágil
- Classes 4 e 5 predominantes: Insuficiente

Usar sempre o sistema: Alta, Parcial, Frágil ou Insuficiente.

## Saída recomendada
A priorização final deve responder:
1. diagnóstico curto de contexto
2. trava principal, se houver
3. ação número 1
4. ação número 2
5. ação número 3
6. o que não deve ser priorizado agora
7. confiança da priorização
8. dependências críticas
9. risco de agir fora de ordem
10. o que ainda precisa validar

## Regras de qualidade
- não priorizar otimização antes de corrigir contaminação da base
- não colocar ação cosmética na frente de causa raiz
- não recomendar sequência longa demais sem foco real
- não priorizar forte com confiança insuficiente sem sinalizar
- usar `playbooks/stack-failure-triage.md` quando a ordem depender da correção de stack
- usar `playbooks/governance-escalation.md` quando houver alçada ou sensibilidade relevante

## Referências
- `governance/decision-framework.md`
- `governance/confidence-system.md`
- `playbooks/stack-failure-triage.md`
- `playbooks/crm-reconciliation.md`
- `playbooks/marketing-diagnosis.md`
