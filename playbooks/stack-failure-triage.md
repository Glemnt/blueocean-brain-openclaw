# Stack Failure Triage Playbook

Playbook principal para localizar falha de stack, separar problema técnico de leitura errada e decidir quando travar diagnósticos dependentes.

## Quando usar
- discrepância entre plataforma, CRM, dashboard ou planilha
- campos críticos vazios sem explicação clara
- suspeita de webhook quebrado, automação falhando ou tracking contaminado
- queda súbita de volume ou avanço sem causa aparente
- sensação de que o problema pode estar na stack, e não na mídia ou no comercial

## Objetivo
1. localizar em que camada a trilha está quebrando
2. distinguir falha técnica, falha operacional e erro de interpretação
3. identificar owner principal da correção
4. decidir se a leitura pode seguir, se precisa subir ou se deve travar

## Pré-checagem obrigatória
Antes de concluir:
- qual evento ou dado deveria existir e não está aparecendo?
- onde esse dado nasce?
- por quais camadas ele deveria passar?
- qual é a fonte mais próxima do evento real?
- a falha é de ausência, atraso, divergência ou preenchimento incompleto?
- existe impacto em decisão sensível?

## Hierarquia de leitura
### 1. Origem do evento
Verificar:
- o evento nasceu de fato na fonte primária?
- a plataforma ou sistema de origem confirma o evento?
- o problema pode ser leitura errada do evento em vez de falha real?

### 2. Transporte e automação
Verificar:
- webhook, n8n, Make ou fluxo equivalente disparou?
- houve atraso, falha silenciosa ou erro de match?
- a automação enriqueceu o dado corretamente ou só parcialmente?

### 3. Entrada no sistema de destino
Verificar:
- o registro chegou ao CRM, planilha ou destino esperado?
- chegou duplicado, incompleto ou no lugar errado?
- existe perda de campo crítico na entrada?

### 4. Consolidação e visualização
Verificar:
- dashboard ou planilha derivada está fiel à origem?
- o cálculo consolidado respeita a regra de source of truth?
- há filtro errado, atraso de atualização ou lógica quebrada?

### 5. Decisão
Concluir se o caso é:
- leitura equivocada
- falha técnica localizada
- falha operacional recorrente
- stack contaminada
- risco sensível que exige trava

## Classes de evidência
Usar esta leitura mínima:
- Classe 1: fato confirmado na origem e na camada seguinte
- Classe 2: fato confirmado em uma fonte confiável com trilha parcial
- Classe 3: discrepância detectada entre camadas
- Classe 4: inferência por ausência, atraso ou campo vazio
- Classe 5: dado ausente, trilha quebrada ou conflito grave

## Confiança
- Classes 1 e 2 predominantes: Alta
- Classes 2 e 3 predominantes: Parcial
- Classes 3 e 4 predominantes: Frágil
- Classes 4 e 5 predominantes: Insuficiente

Usar sempre o sistema: Alta, Parcial, Frágil ou Insuficiente.

## Saída recomendada
A análise final deve responder:
1. diagnóstico executivo
2. camada onde a falha parece estar
3. tipo de problema: origem, automação, entrada, consolidação ou leitura
4. classe de evidência predominante
5. confiança final
6. fonte mais próxima do evento real
7. owner principal do problema
8. precisa escalar ou não, e para qual nível
9. ação inicial obrigatória
10. impacto nas análises dependentes
11. o que ainda precisa validar

## Regras de qualidade
- não culpar mídia ou comercial antes de revisar stack
- não tratar dashboard divergente como falha da origem automaticamente
- não sustentar decisão forte com trilha quebrada
- não confundir ausência de campo com ausência de evento sem revisar automação
- usar `knowledge/matrices/ownership-governance-matrix.md` quando o owner não estiver claro
- aplicar `playbooks/crm-reconciliation.md` quando o problema exigir reconciliação mais profunda

## Referências
- `integrations/meta-ads.md`
- `integrations/kommo.md`
- `integrations/n8n.md`
- `integrations/google-sheets.md`
- `knowledge/company-brain/source-truth-rules.md`
- `governance/decision-framework.md`
- `governance/confidence-system.md`
