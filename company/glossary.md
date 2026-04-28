# Glossary

Camada canônica de nomenclaturas essenciais da Blue Ocean.

## Funil e CRM
| Termo | Definição |
|-------|-----------|
| Lead | Contato que entrou por algum canal ou funil e foi registrado em alguma camada operacional confiável, como CRM, planilha de captura ou automação |
| Lead estrutural | Entidade de lead registrada no CRM, útil para identidade, owner, pipeline, status e rastreabilidade estrutural |
| Lead operacionalmente válido | Lead que passou pelo critério de validade do funil em questão, sem falha crítica de captura, duplicidade relevante ou ruído operacional conhecido |
| Lead Real | No funil WhatsApp/CTWA, lead classificado como conversa efetiva ou contato operacionalmente válido, normalmente via `Status WhatsApp` no Kommo e/ou `LEAD REAL` na planilha `WHATSAPP` |
| Lead Fantasma | No funil WhatsApp/CTWA, clique/conversa aparente ou lead criado sem conversa efetiva/validade operacional, que não deve entrar como volume válido |
| Lead qualificado | Lead com aderência mínima de empresa, dor, estrutura e potencial real de avanço |
| Misfit | Lead ou cliente sem aderência ao ICP da Blue Ocean |
| Discovery | Etapa comercial de investigação profunda sobre modelo, dor, estrutura, budget, decisor e urgência |
| Reunião agendada | Reunião com data e horário definidos |
| Reunião realizada | Reunião que de fato aconteceu |
| Oportunidade | Caso com fit real, contexto e viabilidade de proposta |
| Proposta | Oferta comercial formal apresentada ou enviada |
| Ganho | Cliente fechado formalmente |
| Perdido | Oportunidade encerrada com motivo registrado |

## Papéis
| Termo | Definição |
|-------|-----------|
| SDR | Responsável pelo primeiro contato, qualificação inicial e agendamento de reunião |
| Closer | Responsável por conduzir reunião, aprofundar discovery, apresentar proposta e fechar |
| Owner | Responsável principal por tema, conta, fluxo, risco ou decisão |
| Owner da conta | Responsável principal por onboarding, rotina, comunicação, saúde, risco e escalonamento de uma conta |

## Operação e ciclo de vida
| Termo | Definição |
|-------|-----------|
| Handoff | Passagem formal de responsabilidade entre áreas, normalmente comercial para operação, incluindo escopo, promessas, riscos e exceções |
| Kickoff | Reunião inicial de alinhamento entre operação e cliente |
| Onboarding | Processo de transformar a venda em operação executável |
| Conta saudável | Conta com rotina funcional, owner claro, expectativa alinhada e valor percebido preservado |
| Conta em risco | Conta com sinais claros de degradação de saúde, confiança ou execução |
| Pré-churn | Desgaste recorrente com possibilidade de recuperação mediante plano formal |
| Churn iminente | Cancelamento verbalizado ou confiança rompida, exigindo contenção imediata |
| Churn sensível | Churn com impacto estratégico, relevante em receita ou reputação |
| Churn | Clientes que saíram no período sobre a base ativa inicial |

## Governança e integridade
| Termo | Definição |
|-------|-----------|
| Exceção sensível | Exceção com impacto em cliente, margem, escopo ou precedente, exigindo aprovação formal |
| Violação de governança | Quebra de regra crítica sem owner, registro, aprovação ou proteção suficiente |
| Linha vermelha | Situação que nunca deve ser normalizada |
| Terra de ninguém | Situação em que ninguém assume ownership |
| Dado provisório | Dado útil para hipótese e orientação tática, sem validação consolidada |
| Dado frágil | Dado cuja origem, integridade ou consolidação tem problema conhecido |
| Dado contaminado | Dado comprometido por falha técnica, duplicidade ou quebra de trilha |
| Stack contaminada | Stack técnica com falha conhecida que compromete a integridade dos dados |

## Receita e modelo
| Termo | Definição |
|-------|-----------|
| MRR | Monthly Recurring Revenue |
| NRR | Net Revenue Retention |
| Capa azul | Faixa de ticket de R$ 3.000 a R$ 4.500 |
| Capa branca | Faixa de ticket de R$ 4.500 a R$ 5.500 |
| Capa dourada | Faixa de ticket acima de R$ 6.000 |
| Forecast | Projeção de receita futura baseada em pipeline real e probabilidade de fechamento |

## Métricas e força operacional
| Termo | Definição |
|-------|-----------|
| CPL | Mídia dividida por leads operacionalmente válidos no funil analisado; em CTWA, deve excluir Lead Fantasma |
| CPAg | Mídia dividida por reuniões agendadas |
| CPR | Mídia dividida por reuniões realizadas |
| CAC de mídia | Mídia dividida por clientes ganhos atribuídos ao funil |
| Win rate | Ganhos divididos por oportunidades reais |
| Operacionalmente forte | Métrica que pode sustentar decisão operacional direta |
| Útil mas frágil | Métrica útil para investigação, não para veredito forte |
| Não oficial para decisão executiva | Métrica que não deve sustentar narrativa forte ou atribuição definitiva |

## Fonte de verdade
- em métricas, CRM, avanço comercial e resultado, prevalece a fonte mais próxima do evento real
- spend, entrega e consumo de mídia: plataforma
- entidade estrutural do lead, owner, pipeline e status vivo: CRM/Kommo, quando os campos críticos estão íntegros
- validade operacional do topo: depende do funil; em WhatsApp/CTWA, separar sempre Lead Real de Lead Fantasma usando Kommo + planilha `WHATSAPP` quando disponíveis
- reunião, próximos passos e leitura comercial diária: CRM e/ou planilha comercial, conforme integridade operacional comprovada no período
- oportunidade, proposta e venda: CRM, com validação operacional quando houver divergência
- receita: CRM, idealmente com validação financeira
- saúde da conta: operação combinada com CRM e acompanhamento real
- churn: operação combinada com CRM e registro de saída
