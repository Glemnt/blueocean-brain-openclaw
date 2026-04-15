# Account Risk Playbook

Playbook principal para avaliar saúde de conta, detectar risco, formalizar pré-churn e impedir que degradação operacional vire surpresa.

## Quando usar
- sinais de conta em risco, cliente reativo ou confiança caindo
- handoff incompleto ou onboarding contaminado
- dúvida sobre saúde da conta, retenção ou expansão
- conta com desgaste recorrente, escopo elástico ou pré-churn
- necessidade de decidir se a situação é tática, sensível ou linha vermelha

## Objetivo
1. identificar se a conta está saudável, em risco, em pré-churn ou em churn iminente
2. separar problema de rotina, relacionamento, escopo, handoff, entrega ou governança
3. formalizar owner, plano e necessidade de escalonamento
4. impedir normalização de risco sem dono ou sem plano

## Pré-checagem obrigatória
Antes de concluir sobre a conta:
- quem é o owner principal da conta?
- em que momento do ciclo ela está: handoff, onboarding, execução, risco, pré-churn?
- quais são os sintomas observáveis?
- existe registro de risco, plano ou alinhamento interno?
- há promessa, escopo ou expectativa desalinhada?
- existe cliente estratégico, impacto relevante de receita ou risco reputacional?

Se não houver owner claro, tratar isso primeiro como problema de governança.

## Hierarquia de leitura
Toda análise deve seguir esta ordem.

### 1. Handoff e origem da conta
Verificar:
- handoff veio completo ou contaminado
- promessas, exceções e riscos foram registrados
- operação recebeu contexto suficiente para executar

### 2. Onboarding e condição mínima
Verificar:
- acessos, rotina, alinhamentos e checklist básico existem
- cliente entendeu o que foi vendido, o que não foi vendido e os limites da operação
- a conta começou com base executável ou já nasceu comprometida

### 3. Rotina operacional e saúde atual
Verificar:
- owner está conduzindo a conta de forma ativa
- cliente responde e mantém rotina mínima
- pendências avançam ou acumulam
- percepção de valor está preservada ou degradando

### 4. Risco, retenção e relacionamento
Verificar:
- sinais claros de degradação de confiança
- desgaste recorrente, reatividade crescente ou silêncio perigoso
- conta em risco formalizada ou apenas intuída
- se o caso é risco, pré-churn ou churn iminente

### 5. Escopo, expansão e precedentes
Verificar:
- fora de escopo está sendo absorvido
- demanda extra já virou rotina informal
- há tentativa de expansão em conta doente
- existe precedente ruim sendo criado

### 6. Decisão
Concluir se a situação é:
- saudável
- atenção com ressalva
- conta em risco
- pré-churn
- churn iminente
- linha vermelha operacional ou de governança

## Classes de evidência
Usar esta leitura mínima:
- Classe 1: fato operacional observado e registrado
- Classe 2: fato cruzado entre operação, CRM e rotina da conta
- Classe 3: hipótese operacional baseada em padrão comportamental
- Classe 4: inferência provisória por sinais indiretos
- Classe 5: dado ausente, conflito grave ou falta de owner/plano

Mapeamento para confiança:
- Classes 1 e 2 predominantes: Alta
- Classes 2 e 3 predominantes: Parcial
- Classes 3 e 4 predominantes: Frágil
- Classes 4 e 5 predominantes: Insuficiente

## Sinais que exigem atenção imediata
- conta sem owner
- risco sem plano
- handoff relevante incompleto
- churn verbalizado
- crise de relacionamento sem alinhamento interno
- fora de escopo absorvido como rotina
- expansão em conta instável

## Lógica de escalonamento
Classificar assim:
- saudável, reversível, owner claro e risco baixo: pode seguir
- atenção localizada, risco controlado e plano claro: pode seguir com ressalva
- conta em risco com impacto operacional ou relacional: precisa subir
- pré-churn com base parcial, owner instável ou plano fraco: não pode recomendar com confiança ainda
- churn iminente, linha vermelha ou conta crítica sem contenção: deve travar e sinalizar

## Saída recomendada
A análise final deve sempre responder:
1. diagnóstico executivo
2. estágio da conta: saudável, atenção, risco, pré-churn ou churn iminente
3. classe de evidência predominante
4. confiança final: Alta, Parcial, Frágil ou Insuficiente
5. principal tipo de problema
6. owner principal e co-owner
7. precisa escalar ou não, e para qual nível
8. ação inicial obrigatória
9. plano de contenção ou recuperação
10. principais alertas
11. o que ainda precisa validar

## Regras de qualidade
- não tratar silêncio prolongado como neutralidade
- não esperar o cliente reclamar para formalizar risco
- não deixar conta em risco sem owner e sem plano
- não normalizar fora de escopo absorvido
- não recomendar expansão em conta doente
- usar `knowledge/matrices/ownership-governance-matrix.md` para validar ownership e escalonamento
- aplicar `governance/red-lines.md` quando houver linha vermelha operacional

## Referências
- `company/glossary.md`
- `governance/red-lines.md`
- `governance/decision-framework.md`
- `governance/confidence-system.md`
- `knowledge/matrices/ownership-governance-matrix.md`
- `knowledge/matrices/governance-triggers-matrix.md`
- `knowledge/patterns/diagnostic-patterns.md`
