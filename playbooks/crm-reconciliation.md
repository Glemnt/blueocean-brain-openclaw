# CRM Reconciliation Playbook

Playbook principal para validar integridade de dados, reconciliar fontes e decidir se a base sustenta análises fortes.

## Quando usar
- conflito entre CRM, dashboard, plataforma ou planilha
- suspeita de webhook quebrado, automação falhando ou trilha incompleta
- necessidade de validar CPL real, avanço comercial ou atribuição
- dúvida se os dados estão íntegros o suficiente para diagnóstico de performance
- discrepância relevante entre fontes

## Objetivo
1. identificar onde a trilha quebra
2. separar conectividade, completude, consistência, duplicidade e atribuição
3. declarar a fonte de verdade por tipo de dado
4. dizer com clareza se a base está limpa, parcial, frágil ou insuficiente

## Pré-checagem obrigatória
Antes de reconciliar:
- quais fontes estão sendo comparadas?
- qual período está em análise?
- qual canal ou funil está em foco?
- qual métrica ou evento precisa ser validado?
- a fonte mais próxima do evento real está disponível?
- existe sinal de dashboard divergente, campo vazio crítico, duplicidade ou ausência de trilha?

Se a pergunta for de performance, mas a integridade não estiver validada, travar a leitura de performance até esclarecer a base.

## Hierarquia de leitura
Toda reconciliação deve seguir esta ordem.

### 1. Conectividade
Verificar:
- MCPs, integrações, webhooks e automações respondem?
- houve gap temporal incompatível com o volume esperado?
- existe indício de workflow parado, salesbot falhando ou captura silenciosa quebrada?

### 2. Completude
Verificar:
- campos críticos preenchidos: campanha, conjunto, anúncio, UTM, source, status, owner, motivo de perda
- percentual de preenchimento por canal ou etapa
- se a ausência do campo impede cálculo ou atribuição relevante

### 3. Consistência entre fontes
Verificar:
- Meta Ads versus CRM
- CRM versus Sheets, se aplicável
- CRM versus dashboard
- nível da discrepância: normal, atenção, significativa ou crítica

Faixas recomendadas:
- abaixo de 10%: normal
- entre 10% e 25%: atenção
- entre 25% e 40%: significativa
- acima de 40%: crítica

### 4. Duplicidade
Verificar:
- mesmo telefone, email ou lead repetido
- duplicidade de webhook ou registros no mesmo minuto
- se a duplicidade contamina leitura de volume, CPL ou avanço

### 5. Atribuição e trilha
Verificar:
- se é possível seguir clique, lead, qualificação, oportunidade e venda
- se campanha, conjunto, anúncio e source estão presentes quando deveriam
- se a atribuição está robusta ou fantasma

### 6. Decisão
Concluir se a base:
- pode seguir
- pode seguir com ressalva
- precisa subir
- não pode recomendar com confiança ainda
- deve travar e sinalizar

## Classes de evidência
Usar esta leitura mínima:
- Classe 1: fato observado em 2 ou mais fontes concordantes
- Classe 2: fato observado em 1 fonte confiável
- Classe 3: discrepância detectada entre fontes
- Classe 4: inferência por ausência
- Classe 5: dado ausente ou contaminado

Mapeamento para confiança:
- Classes 1 e 2 predominantes: Alta
- Classes 2 e 3 predominantes: Parcial
- Classes 3 e 4 predominantes: Frágil
- Classes 4 e 5 predominantes: Insuficiente

## Fonte de verdade por tipo de dado
Regra geral: prevalece a fonte mais próxima do evento real.

Exemplos:
- spend e entrega de campanha: plataforma
- lead válido, qualificação, oportunidade e avanço comercial: CRM
- dashboard: visualização derivada, nunca verdade final por si só
- receita e churn: CRM com validação operacional ou financeira quando necessário
- saúde da conta: operação real combinada com CRM

## Impacto sobre outras análises
Se a reconciliação indicar base frágil ou insuficiente:
- travar diagnósticos fortes de marketing
- rebaixar conclusões comerciais dependentes do CRM
- impedir atribuição forte de receita, CPL real ou CAC
- sinalizar explicitamente quais decisões não devem ser tomadas ainda

## Saída recomendada
A análise final deve sempre responder:
1. diagnóstico executivo
2. principal tipo de problema
3. classe de evidência predominante
4. confiança final: Alta, Parcial, Frágil ou Insuficiente
5. tabela ou resumo de reconciliação entre fontes
6. fonte de verdade por dado relevante
7. owner principal do problema
8. precisa escalar ou não, e para qual nível
9. plano de correção priorizado
10. impacto nas análises e decisões dependentes
11. o que ainda precisa validar

## Regras de qualidade
- não reconciliar por média entre fontes divergentes
- não declarar dado limpo sem cruzar pelo menos duas fontes quando o tema exigir
- não deixar dashboard substituir CRM ou plataforma
- não autorizar análise forte de performance sobre base contaminada
- não atribuir receita a campanha sem trilha robusta
- se a discrepância for grave, quantificar e travar
- usar `knowledge/matrices/ownership-governance-matrix.md` quando houver dúvida de owner
- aplicar `governance/decision-framework.md` quando a integridade do dado afetar decisão sensível ou irreversível

## Referências
- `governance/confidence-system.md`
- `governance/decision-framework.md`
- `knowledge/company-brain/source-truth-rules.md`
- `knowledge/matrices/ownership-governance-matrix.md`
- `knowledge/matrices/governance-triggers-matrix.md`
- `knowledge/patterns/diagnostic-patterns.md`
