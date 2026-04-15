# Meta Ads Integration

Documentação canônica da integração Meta Ads dentro do `blueocean-brain-openclaw`.

## Papel da integração
Meta Ads é a fonte primária para leitura de:
- entrega
- spend
- alcance
- cliques
- CTR
- CPM
- CPC
- consumo de criativo na plataforma

Ela não é, sozinha, fonte final para qualidade de lead, avanço comercial ou receita.

## O que a integração sabe bem
Confiável para leitura direta:
- impressões
- alcance
- frequência
- CPM
- cliques
- CTR
- CPC
- video views
- spend

## O que requer cruzamento
Útil, mas só sustenta decisão forte quando cruzado com CRM:
- conversões
- CPL da plataforma
- custo por conversa iniciada
- desempenho por campanha quando a pergunta real é qualidade de lead

## O que não deve ser usado isoladamente
- ROAS sem integração de receita validada
- conversões atribuídas sem validar evento e CRM
- leads da plataforma sem confirmação de entrada e integridade no CRM

## Regra central de leitura
Nunca ler Meta Ads isoladamente.

Sempre conectar:
- plataforma → CRM
- CRM → comercial
- comercial → avanço e resultado

## Fonte de verdade por tipo de dado
- entrega e spend: Meta Ads
- lead válido: CRM
- avanço comercial: CRM
- leitura executiva consolidada: depende de reconciliação

## Regras operacionais importantes
- CPL da plataforma não é CPL real
- Lead Fantasma não é lead válido
- nunca recomendar escala sem verificar fundo do funil e capacidade de absorção
- problema de mídia pode ser, na verdade, problema de stack, oferta, comercial ou tracking

## CTWA
Para Click-to-WhatsApp:
- métrica principal: `onsite_conversion.messaging_first_reply`
- lead real exige confirmação no CRM
- lead fantasma é clique sem mensagem efetiva
- cálculos fortes dependem de filtro por `Status WhatsApp = Lead Real`

## Eventos de conversão
Cada campanha pode ter seu próprio evento de conversão.

Regra:
1. identificar o evento correto no ad set
2. só depois interpretar `actions[]`
3. se o evento certo não estiver sendo lido, 0 lead pode significar evento errado, não campanha sem resultado

## Fragilidades conhecidas
- leitura errada do evento de conversão gera diagnóstico falso
- discrepância entre plataforma e CRM pode vir de webhook, duplicidade ou lead fantasma
- atribuição pode quebrar se tracking ou preenchimento de campos falhar
- performance agregada pode esconder criativo ou público ruim

## Erros comuns de interpretação
- tratar CPL de plataforma como CPL real
- recomendar escala sem validar lead e avanço
- culpar mídia quando o problema está no CRM, na automação ou no comercial
- usar ROAS da plataforma como leitura final
- assumir que 0 conversão significa falha de campanha sem revisar o evento certo

## Relação com outras camadas
- análise operacional: `playbooks/marketing-diagnosis.md`
- reconciliação e integridade: `playbooks/crm-reconciliation.md`
- especialista principal: `subagents/meta-ads-analyst.md`
- governança de decisão: `governance/decision-framework.md`

## Regra final
Meta Ads mede muito bem entrega.
Mas entrega boa só vira inteligência útil quando é reconciliada com o que aconteceu depois do clique.
