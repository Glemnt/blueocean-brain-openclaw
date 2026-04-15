# Triage Playbook

Porta de entrada principal para demandas livres. O objetivo é identificar o domínio, checar risco e decidir o próximo playbook ou análise.

## Quando usar
- o usuário descreve um problema de forma aberta
- o domínio ainda não está claro
- há sinais de múltiplas áreas envolvidas
- é necessário decidir por onde começar sem perder governança

## Objetivo
1. identificar o domínio principal
2. detectar linha vermelha ou contaminação de base
3. validar se há dados mínimos
4. escolher o playbook principal
5. apontar playbooks complementares quando fizer sentido

## Domínios principais
| Domínio | Sinais comuns |
|---------|---------------|
| Marketing e mídia | CPL, CTR, campanha, criativo, audiência, Meta Ads, Google Ads, spend, impressões |
| Comercial | lead, qualificação, reunião, proposta, closer, SDR, pipeline, objeção, CRM |
| Operação | conta, onboarding, entrega, churn, risco, handoff, escopo, owner da conta |
| Stack e dados | tracking, webhook, UTM, discrepância, dashboard, integração, campos, n8n, Make, Kommo |
| Governança | exceção, aprovação, owner difuso, terra de ninguém, desconto, fora de escopo, linha vermelha |
| Misto | elementos de 2 ou mais domínios com dependências entre si |

## Regras de prioridade
1. se houver linha vermelha, priorizar governança
2. se houver stack contaminada ou conflito entre fontes, priorizar reconciliação antes de performance
3. se o problema parecer misto, definir um domínio principal e registrar os secundários
4. se não houver dados suficientes para análise forte, não inventar precisão

## Sequência de execução
### 1. Classificar o domínio
- identificar o tema principal
- registrar temas secundários, se houver
- validar se o problema é tático, sistêmico ou sensível

### 2. Checar travas imediatas
Antes de aprofundar, verificar:
- existe linha vermelha?
- existe tema crítico sem owner?
- existe CRM incoerente?
- existe stack com falha conhecida?
- o dashboard diverge da fonte?
- a decisão desejada é irreversível ou de alto custo?

Se qualquer resposta crítica for sim, rebaixar a confiança e mudar a ordem da análise.

### 3. Identificar a fonte mais próxima do evento real
Pergunta obrigatória: qual fonte está mais próxima do evento que o usuário quer explicar?

Exemplos:
- performance de campanha: plataforma
- avanço comercial: CRM
- handoff e risco de conta: operação real + CRM
- receita e churn: CRM + validação operacional ou financeira

Se a fonte mais próxima não estiver disponível, deixar isso explícito.

### 4. Checar dados mínimos
Confirmar se já existe base mínima para seguir. Exemplos:
- marketing: período, campanha ou recorte, métricas centrais, objetivo
- comercial: estágio, volume, qualidade, avanço, motivos de perda ou gargalo
- operação: conta, sintomas, owner, momento do ciclo, risco percebido
- stack: origem esperada, origem real, onde a trilha quebra
- governança: tema, owner, impacto, aprovação, exceção ou violação

Se faltarem dados obrigatórios, pedir apenas o mínimo faltante.

### 5. Escolher o playbook principal
| Situação principal | Playbook sugerido |
|--------------------|-------------------|
| problema aberto, sem domínio claro | este playbook continua conduzindo |
| queda de performance ou dúvida de mídia | `marketing-diagnosis.md` |
| conflito entre CRM, dashboard, plataforma ou tracking | `crm-reconciliation.md` |
| risco de conta, handoff, escopo ou retenção | playbook operacional futuro ou análise guiada por `governance/` + `knowledge/matrices/` |
| dúvida de ownership, aprovação, exceção ou violação | análise guiada por `governance/` + `knowledge/matrices/` |

Se ainda não houver playbook específico, usar a camada canônica e as referências da knowledge base.

### 6. Se faltar dado, pedir só o mínimo necessário
- consultar templates quando existirem
- pedir apenas os campos obrigatórios para a próxima conclusão segura
- separar o que é obrigatório do que é complementar
- se a ausência de dado impedir conclusão forte, dizer isso explicitamente

### 7. Encerrar a triagem com saída padronizada
A saída deve sempre informar:
1. domínio principal
2. domínios secundários, se houver
3. risco ou trava detectada
4. fonte mais próxima do evento real
5. se os dados são suficientes ou o que falta
6. próximo playbook ou análise recomendada
7. confiança atual da triagem: Alta, Parcial, Frágil ou Insuficiente

## Regras de qualidade
- não tratar triagem como análise profunda
- não mascarar incerteza
- não deixar governança para depois quando o risco já está visível
- não assumir que dashboard é verdade final
- não recomendar escala, pausa ou mudança estrutural se a base estiver frágil
- consultar `knowledge/matrices/ownership-governance-matrix.md` quando houver dúvida de owner ou escalonamento
- se um padrão diagnóstico já estiver claro, referenciar `knowledge/patterns/diagnostic-patterns.md` sem pular a validação

## Referências
- `governance/decision-framework.md`
- `governance/red-lines.md`
- `governance/confidence-system.md`
- `knowledge/matrices/ownership-governance-matrix.md`
- `knowledge/matrices/governance-triggers-matrix.md`
- `knowledge/patterns/diagnostic-patterns.md`
- `knowledge/company-brain/source-truth-rules.md`
