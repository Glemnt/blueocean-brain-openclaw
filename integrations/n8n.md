# n8n Integration

Documentação canônica da integração n8n dentro do `blueocean-brain-openclaw`.

## Papel da integração
n8n é a camada principal de automação e enriquecimento do stack.

Ele não é a fonte final de verdade do negócio, mas é frequentemente a camada que:
- conecta sistemas
- move dados entre plataforma e CRM
- preenche campos críticos
- aciona webhooks
- registra buffers temporários
- dispara monitoramentos e alertas

## O que a integração faz bem
- orquestrar fluxo entre Meta Ads, Kommo, LPs, webhooks e Sheets
- enriquecer leads com dados de tracking
- reduzir trabalho manual de preenchimento
- monitorar anomalias operacionais
- transformar eventos soltos em trilhas mais legíveis

## O que ela não substitui
- não substitui Meta Ads como fonte de spend e entrega
- não substitui Kommo como base principal de avanço comercial
- não substitui reconciliação quando há conflito entre fontes

## Quando n8n é crítico
n8n é crítico quando a operação depende dele para:
- preencher campanha, conjunto, anúncio e UTMs
- conectar LP ou micro-LP ao CRM
- identificar lead real versus lead fantasma
- enriquecer lead após criação automática
- disparar alertas operacionais ou de integridade

No caso Blue Ocean, ele é especialmente crítico na trilha CTWA, porque o desenho operacional documentado depende de:
- micro-LP / redirect antes do clique para WhatsApp
- webhook de tracking para buffer temporário
- evento de criação de lead no Kommo
- match temporal + SDR
- patch de campos estruturais no Kommo (`Campanha`, `Conjunto de Anúncios`, `Anúncio`, UTMs)

Se essa cadeia não estiver visível e auditável, não é seguro tratar relatórios como 100% reais, porque o erro pode nascer antes do CRM e parecer apenas inconsistência de vendas ou mídia.

## Fragilidades conhecidas
- webhook pode falhar silenciosamente
- match temporal pode errar ou não encontrar o lead certo
- automação pode preencher só parte dos campos
- buffers temporários podem introduzir atraso ou inconsistência
- erro no fluxo pode parecer problema de mídia ou comercial

## Erros comuns de interpretação
- tratar dado preenchido por automação como automaticamente íntegro
- culpar mídia quando o problema foi quebra no fluxo n8n
- assumir ausência de campo como ausência de origem, quando pode ser falha de automação
- confiar em fluxo sem validar taxa de match ou taxa de erro

## Exemplos de uso estrutural
- enriquecer leads CTWA via micro-LP + webhook + match com Kommo
- persistir dados transitórios em buffer antes de atualizar CRM
- monitorar anomalias de CPL real, lead fantasma, queda de volume ou falha de webhook
- preencher rastreamento de campanha em múltiplos canais

## Relação com fonte de verdade
n8n participa da trilha do dado, mas não deve ser tratado como verdade final isolada.

Seu papel principal é:
- transportar
- enriquecer
- sincronizar
- monitorar

A verdade final continua dependendo do tipo de dado e da fonte mais próxima do evento real.

## Relação com outras camadas
- integração comercial principal: `integrations/kommo.md`
- integração de mídia principal: `integrations/meta-ads.md`
- modelo operacional de Sheets e funis: `integrations/google-sheets-operating-model.md`
- reconciliação: `playbooks/crm-reconciliation.md`
- especialista de dados: `subagents/dados-bi-analyst.md`

## Regra de auditoria para relatórios confiáveis
Se a exigência for relatório `100% real e seguro`, a auditoria não pode parar em Sheets ou Kommo.
Ela deve cobrir, no mínimo:
- ponto de captura do lead ou clique
- automação intermediária (n8n / webhook / buffer)
- chegada e enriquecimento no Kommo
- passagem para leitura operacional em Sheets

Consequência prática:
- enquanto o agente não tiver acesso auditável às automações relevantes, qualquer leitura cross-source deve ser tratada como forte ou fraca conforme a camada, mas não como verdade total do stack
- para ganhar confiança máxima, o ideal é ter acesso aos workflows ativos, seus gatilhos, buffers, regras de match, logs de execução e pontos de falha

## Regra final
Quando n8n funciona bem, ele aumenta integridade operacional.

Quando falha, ele pode contaminar a leitura inteira sem parecer o culpado à primeira vista.
Por isso, n8n deve ser sempre lido como camada crítica de stack.
