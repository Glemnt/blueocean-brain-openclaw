# Google Sheets Operating Model

Modelo operacional para uso das planilhas Google já conectadas ao brain da Blue Ocean.

## Objetivo
Definir:
- quais dados existem hoje nas planilhas acessíveis
- como o agente deve usá-los no dia a dia
- quais limites de confiança devem ser respeitados
- como o Drive deve ser organizado para evitar caos operacional

## Planilhas atualmente acessíveis
### 1. CONTROLE DE LEADS GERAL
ID:
- `1c2S8xH_-SwJWraxmDlMPTE2bcgZxJREekwVKqXyln00`

### 2. Planilha Comercial x Marketing V.2
ID:
- `1FsxlJ8bWEy9-NKKW5EP4gwIYBYUkBf5tSFG0G-wYkvA`

### 3. Pasta Drive de organização
ID:
- `1Vv0iqJ0zFnRDRTswO118J0M8B_zRzD5M`
- nome: `BO Brain - ORGANIZAÇÃO`

## Leitura geral das planilhas
### CONTROLE DE LEADS GERAL
Essa planilha funciona como camada de captura e classificação inicial por origem/oferta/formato.

Abas observadas:
- `MVP`
- `B2B`
- `SAAS PADRÃO`
- `TYPEBOT`
- `BIO IG`
- `LP V2`
- `LP INSTITUCIONAL`
- `LP PADRÃO`
- `LP YOUTUBE`
- `WHATSAPP`
- `INLEAD`
- `TABELA DE CÓDIGOS E MENSAGENS WPP`

#### Padrão estrutural
As abas dessa planilha normalmente combinam:
1. dados individuais do lead
2. metadados de origem e campanha
3. status operacional simples
4. pequenos blocos agregados manuais por SDR no lado direito

Regra importante: essa planilha não deve ser tratada como uma tabela única homogênea. Cada aba representa um funil, origem ou oferta diferente, com schema próprio e regras próprias de validade operacional.

#### Campos recorrentes mapeados
Identidade e contato:
- `DATA`
- `NOME`
- `EMAIL`
- `TELEFONE`
- `SITE`
- `ID_LEAD`

Qualificação/contexto:
- `SITUAÇÃO ATUAL`
- `MAIOR DESAFIO`
- `PRINCIPAL DESAFIO`
- `DESAFIO`
- `META`
- `MRR`
- `MQLS / MÊS`
- `CARGO`
- `SEGMENTO`
- `CANAIS DE AQUISIÇÃO`
- `CANAL DE AQUISIÇÃO`
- `EXPECTATIVA`

Origem/tracking:
- `CAMPANHA`
- `CONJUNTO`
- `ANÚNCIO`
- `SDR Responsável`

Status/resultados simples:
- `Agendou?`
- `Fechou?`
- `Observação` / `Observações`
- `LEAD REAL`

Blocos agregados laterais:
- `Leads pegos`
- `Leads agendados`
- `Tx. de agendamento`
- `Fechamentos`

#### Função operacional real
Essa planilha é útil para:
- entender como cada origem/canal/captura estrutura os leads
- identificar enriquecimento de contexto que às vezes não está claro no CRM
- apoiar leitura de qualidade do lead por origem
- monitorar CTWA e `Lead Fantasma` na aba `WHATSAPP`
- ler diferenças entre captação via form, LP, bio, inlead e WhatsApp
- aplicar leitura por funil em vez de assumir que todas as abas medem a mesma coisa do mesmo jeito

#### Regras de leitura por funil já confirmadas

Status operacional sugerido para leitura do brain:
- `ativo`: há sinais recentes de uso e o funil deve entrar naturalmente nas leituras atuais
- `histórico relevante`: não parece central no momento, mas explica histórico e pode voltar a ser usado
- `baixa atividade / experimental`: volume ou continuidade muito baixos; manter no mapa, mas sem sobrepeso analítico
- `reativável`: mesmo sem uso recente, o funil merece documentação porque pode voltar sem aviso

Esses status não substituem confirmação operacional humana. Eles servem para orientar a leitura do agente, priorização analítica e cautela interpretativa.
##### WHATSAPP
- unidade bruta: qualquer linha com `ID_LEAD`
- unidade válida: linhas classificadas como `Lead Real`
- fonte principal: planilha `WHATSAPP` + Kommo quando o campo `Status WhatsApp` estiver íntegro
- fonte de auditoria: Kommo
- filtro crítico: `LEAD REAL`
- confirmação cruzada: a distinção `Lead Real` / `Lead Fantasma` também aparece no Kommo no campo `Status WhatsApp`
- pergunta que esse funil responde melhor: quanto do volume bruto de CTWA virou lead operacionalmente válido?
- sinal operacional observado: amostra consultada mostra atividade forte em abril de 2026, com alto volume bruto e proporção material de `Lead Fantasma`
- status operacional sugerido: `ativo`
- achado de auditoria confirmado: em amostra auditada de 12 `Lead Real` da planilha, 12 de 12 existiam no Kommo, 12 de 12 preservavam `Status WhatsApp = Lead Real`, 12 de 12 preservavam campanha e `utm_source = meta`, enquanto `Conjunto` e `Anúncio` apareciam preenchidos em cerca de metade da amostra
- implicação: análises de volume, qualidade, agendamento e fechamento do funil WhatsApp não devem usar o volume bruto sem separar os fantasmas

##### SAAS PADRÃO
- unidade bruta: linha capturada na aba
- unidade válida: lead com contexto suficiente para leitura comercial e de marketing, mesmo quando a reconciliação estrutural depender de matching adicional
- fonte principal: aba `SAAS PADRÃO`
- fonte de auditoria: Kommo quando houver matching confiável por telefone/nome/outros sinais, já que `ID_LEAD` aparece fraco na amostra
- função principal: captura rica de contexto comercial e de marketing para o funil SaaS padrão
- schema mais útil para: `DESAFIO`, `MQLS / MÊS`, `MRR`, `CANAIS DE CAPTAÇÃO`, `CARGO`, `META`, `SITE`, `CAMPANHA`, `CONJUNTO`, `ANÚNCIO`, `SDR Responsável`
- pergunta que esse funil responde melhor: que tipo de lead SaaS está entrando, com qual maturidade de aquisição e qual urgência comercial?
- sinal operacional observado: amostra consultada mostra atividade concentrada em janeiro de 2026, com forte riqueza de contexto e tracking, mas pouca presença de `ID_LEAD`
- status operacional sugerido: `histórico relevante` + `reativável`
- observação: nem toda linha possui `ID_LEAD`, então a aba ajuda muito na leitura da qualidade de captura, mas pode não ser suficiente sozinha para reconciliação estrutural com CRM

##### MVP
- unidade bruta: linha capturada na aba
- unidade válida: lead com contexto suficiente para leitura de estágio do produto, dor principal e expectativa
- fonte principal: aba `MVP`
- fonte de auditoria: planilha comercial e Kommo apenas quando houver ponte confiável, pois `ID_LEAD` aparece fraco na amostra
- função principal: captura de contexto específico do funil MVP
- schema mais útil para: `SITUAÇÃO ATUAL`, `MAIOR DESAFIO`, `SE TIVESSE VALIDADO...`, `EXPECTATIVA`, `CAMPANHA`, `CONJUNTO`, `ANÚNCIO`, `SDR Responsável`, `Agendou?`, `Observação`
- pergunta que esse funil responde melhor: em que estágio o prospect de MVP está e qual tipo de bloqueio de validação/comercial ele relata?
- sinal operacional observado: amostra consultada mostra atividade concentrada em janeiro de 2026, com forte densidade qualitativa e muitos sinais úteis de operação SDR nas observações
- status operacional sugerido: `histórico relevante` + `reativável`
- observação: serve melhor para leitura de perfil, estágio e qualificação do que para reconciliação comercial final

##### B2B
- unidade bruta: linha capturada na aba
- unidade válida: lead com contexto comercial suficiente para triagem e, idealmente, ponte confiável para operação comercial
- fonte principal: aba `B2B`
- fonte de auditoria: planilha comercial e Kommo quando houver matching confiável
- função principal: leitura de perfil e intenção para um funil B2B com foco em empresa, cargo, canal de aquisição e janela de decisão
- schema mais útil para: `MRR`, `CANAIS DE AQUISIÇÃO`, `CARGO`, `META`, `SITE`, `CAMPANHA`, `CONJUNTO`, `ANÚNCIO`, `SDR Responsável`
- pergunta que esse funil responde melhor: que tipo de empresa e decisor está entrando no B2B e com qual urgência/intenção?
- sinal operacional observado: amostra consultada mostra atividade concentrada em janeiro de 2026
- status operacional sugerido: `histórico relevante` + `reativável`
- observação: há muitos registros sem `ID_LEAD`, então a aba é melhor para leitura de perfil, origem e operação inicial do que para reconciliação estrutural forte

##### BIO IG
- unidade bruta: linha com `ID_LEAD` ou captura identificável da bio
- unidade válida: lead capturado com contexto mínimo de site, segmento e MRR; quando houver, `ID_LEAD` melhora a reconciliação
- fonte principal: aba `BIO IG`
- fonte de auditoria: Kommo e planilha comercial quando houver correspondência por `ID_LEAD` ou matching confiável
- função principal: leitura dos leads vindos de link na bio, com baixa profundidade de tracking de campanha e forte valor para entender perfil/orgânico-social
- schema mais útil para: `SITE`, `SEGMENTO`, `MRR`, `ID_LEAD`, `SDR Responsável`, `Agendou?`, `Fechou?`
- pergunta que esse funil responde melhor: que perfil de lead chega organicamente ou semi-organicamente via bio e com que densidade de contexto?
- sinal operacional observado: amostra consultada mostra atividade principalmente entre fim de fevereiro e março de 2026
- status operacional sugerido: `histórico relevante`, com possibilidade de ainda servir como canal recente dependendo do período analisado
- observação: tracking de `CAMPANHA`/`ANÚNCIO` aparece fraco ou vazio em boa parte das linhas; esse funil é melhor para leitura de perfil de entrada do que para atribuição de mídia detalhada

##### INLEAD
- unidade bruta: linha capturada na aba
- unidade válida: lead com contexto suficiente de segmento, desafio, MRR e canal; reconciliação estrutural depende de ponte adicional, pois `ID_LEAD` aparece fraco ou vazio
- fonte principal: aba `INLEAD`
- fonte de auditoria: planilha comercial e Kommo quando houver matching confiável por telefone/nome/outros sinais
- função principal: leitura diagnóstica da dor principal e do canal declarado de aquisição
- schema mais útil para: `SEGMENTO`, `PRINCIPAL DESAFIO`, `MRR`, `CANAL DE AQUISIÇÃO`, `SITE`
- pergunta que esse funil responde melhor: que dores e canais declarados estão entrando nesse formato de captação?
- sinal operacional observado: amostra consultada mostra atividade principalmente em março de 2026
- status operacional sugerido: `histórico relevante` ou `reativável`, pendente de leitura completa do período mais recente
- observação: por ter pouco `ID_LEAD` visível na amostra, é uma aba forte para leitura qualitativa do topo do funil, mas mais frágil para reconciliação CRM sem apoio adicional

##### TYPEBOT
- unidade bruta: linha capturada na aba, inclusive linhas incompletas
- unidade válida: lead com identidade e contexto mínimos preenchidos; linhas vazias ou muito quebradas não devem entrar em leitura de qualidade
- fonte principal: aba `TYPEBOT`
- fonte de auditoria: planilha comercial e Kommo apenas quando houver matching confiável
- função principal: histórico de captação via typeform/typebot com forte variação de completude entre registros
- schema mais útil para: `MRR`, `SITE`, `PRINCIPAL DESAFIO`, `CANAIS DE AQUISIÇÃO`, `CAMPANHA`, `CONJUNTO`, `ANÚNCIO`
- pergunta que esse funil responde melhor: que perfil de lead entrou pelos fluxos conversacionais e com qual qualidade de preenchimento?
- sinal operacional observado: amostra consultada mostra atividade concentrada em janeiro de 2026
- status operacional sugerido: `histórico relevante` + `reativável`
- observação: presença visível de linhas incompletas, duplicadas ou com campos quebrados exige filtro forte de qualidade antes de qualquer leitura operacional

##### LP PADRÃO
- unidade bruta: linha capturada na aba
- unidade válida: lead com contexto mínimo de contato, site, segmento e MRR; como o tracking aparece fraco, a validade aqui é mais comercial do que analítica de mídia
- fonte principal: aba `LP PADRÃO`
- fonte de auditoria: planilha comercial e Kommo quando houver matching confiável
- função principal: leitura de leads oriundos de landing page padrão
- schema mais útil para: `SITE`, `SEGMENTO`, `MRR`, `SDR Responsável`, `Agendou?`, `Fechou?`, `Observação`
- pergunta que esse funil responde melhor: que perfil básico de lead a LP padrão trouxe e como a operação reagiu a esses leads?
- sinal operacional observado: amostra consultada mostra atividade concentrada em janeiro de 2026
- status operacional sugerido: `histórico relevante` + `reativável`
- observação: `CAMPANHA`, `CONJUNTO` e `ANÚNCIO` aparecem amplamente vazios na amostra, então a aba serve mais para leitura comercial de entrada do que para atribuição de mídia

##### LP V2
- unidade bruta: linha capturada na aba
- unidade válida: lead com contexto mínimo preenchido e, quando existir, `ID_LEAD` reconciliável
- fonte principal: aba `LP V2`
- fonte de auditoria: planilha comercial e Kommo
- função principal: versão posterior da landing page com mistura de registros mais antigos sem ID e registros mais recentes com `ID_LEAD`
- schema mais útil para: `ID_LEAD`, `SITE`, `SEGMENTO`, `MRR`, `SDR Responsável`, `Agendou?`, `Fechou?`
- pergunta que esse funil responde melhor: como a segunda versão da LP capturou perfil de lead e em que medida essa captação ficou reconciliável depois?
- sinal operacional observado: amostra consultada mostra atividade de janeiro a fevereiro de 2026
- status operacional sugerido: `histórico relevante`, com valor de transição instrumental e possível reuso
- observação: a aba parece misturar fases diferentes de instrumentação; registros mais novos são mais úteis para reconciliação do que os mais antigos

##### LP INSTITUCIONAL
- unidade bruta: linha com `ID_LEAD`
- unidade válida: lead identificado com contexto mínimo de site, segmento e MRR
- fonte principal: aba `LP INSTITUCIONAL`
- fonte de auditoria: Kommo e planilha comercial
- função principal: captura via landing page institucional, aparentemente com instrumentação mais consistente de `ID_LEAD`
- schema mais útil para: `ID_LEAD`, `SITE`, `SEGMENTO`, `MRR`, `Agendou?`, `Fechou?`
- pergunta que esse funil responde melhor: que perfil chega pela LP institucional e com que volume identificado estruturalmente?
- sinal operacional observado: amostra consultada mostra atividade de fevereiro até pelo menos início de abril de 2026, então não deve ser tratado como histórico morto
- status operacional sugerido: `ativo` ou pelo menos `recentemente ativo`
- observação: tracking de mídia continua fraco na amostra, mas a presença de `ID_LEAD` melhora bem a ponte com CRM

##### LP YOUTUBE
- unidade bruta: linha capturada na aba
- unidade válida: lead com dados básicos mínimos; amostra atual é pequena demais para leitura forte
- fonte principal: aba `LP YOUTUBE`
- fonte de auditoria: outras planilhas e Kommo quando houver matching confiável
- função principal: histórico de captação derivada de YouTube ou oferta associada
- schema mais útil para: `SITE`, `SEGMENTO`, `MRR`
- pergunta que esse funil responde melhor: houve captação mínima nesse canal e qual perfil básico apareceu?
- sinal operacional observado: amostra consultada mostra pouquíssimos registros em fevereiro de 2026
- status operacional sugerido: `baixa atividade / experimental`, mas documentado para eventual reuso
- observação: por enquanto a base é pequena demais para qualquer conclusão mais forte

##### TABELA DE CÓDIGOS E MENSAGENS WPP
- unidade bruta: linha de configuração de campanha/mensagem
- unidade válida: linha ativa com código WhatsApp, modelo, SDR e mensagem coerentes
- fonte principal: aba `TABELA DE CÓDIGOS E MENSAGENS WPP`
- fonte de auditoria: aba `WHATSAPP`, Kommo, templates ativos no WhatsApp Business e automações que usam esses códigos
- função principal: camada operacional de governança do CTWA, não funil de lead
- schema mais útil para: `Campanha`, `SDR`, `Conjunto`, `Anúncio`, `Criativo`, `Código WA`, `Nome do Modelo`, `Mensagem Pronta`, `Status`
- pergunta que essa aba responde melhor: qual código/modelo de mensagem foi associado a cada combinação de SDR, conjunto, anúncio e criativo no WhatsApp?
- sinal operacional observado: a aba lista campanhas ativas por SDR e parece servir como dicionário operacional entre criativo, código WA e template de abertura
- status operacional sugerido: `ativo`
- observação: essa aba deve ser tratada como tabela de suporte operacional e rastreabilidade do CTWA. Ela não mede performance diretamente, mas é crítica para auditoria de mensagens, naming, roteamento e eventual diagnóstico de quebra entre campanha, criativo e abordagem comercial

#### Limites
Essa planilha não deve ser tratada automaticamente como fonte final para:
- fechamento financeiro final
- contagem oficial de vendas
- decisão executiva irreversível

Motivo:
- há campos vazios e inconsistências entre abas
- existem colunas agregadas manuais misturadas à base linha a linha
- parte dos dados parece depender de operação manual ou semiautomática

### Planilha Comercial x Marketing V.2
Essa planilha funciona como camada comercial e de reconciliação marketing x vendas ao longo do tempo.

Abas observadas:
- `CAMPANHAS - OUT.`
- `CAMPANHAS - NOV.`
- `CAMPANHAS - DEZ.`
- `VENDAS - MODELO`
- `VENDAS - OUTUBRO`
- `VENDAS - NOVEMBRO`
- `VENDAS - DEZEMBRO`
- `VENDAS - JANEIRO/26`
- `VENDAS - FEVEREIRO/26`
- `VENDAS - MARÇO/26`
- `VENDAS - ABRIL/26`
- várias abas intermediárias de leads Meta Ads e logs

#### Campos recorrentes em abas de campanhas
- `Data`
- `Canal de Aquisição`
- `Campanha`
- `Status`
- `Investimento Diário`
- `Objetivo da Campanha`
- `Leads Diários`
- `CPL`
- `MQL`
- `Fechamentos`
- `Receita`
- `CAC`
- `Investimento Restante`

#### Campos recorrentes em abas de vendas
- `NOME DA CALL`
- `DATA`
- `HORA`
- `TIPO DA CALL` / `TIPO DA REUNIÃO`
- `SDR`
- `CLOSER`
- `QUALIFICADA (SQL)`
- `PRÓXIMO PASSO`
- `CANAL DE AQUISIÇÃO`
- `FECHAMENTO`
- `VALOR`
- `CLOSER FECHOU`
- `SDR FECHOU`
- `DATA DE ENTRADA`
- `ASSINATURA`
- `PAGAMENTO`
- `OBSERVAÇÃO E PRÓXIMOS PASSOS`
- em abril/26 aparecem também `LEAD ID` e `MQL`

#### Função operacional real
Essa planilha é útil para:
- acompanhar evolução comercial por mês
- entender o fluxo de R1, R2, follow e no-show
- ligar origem de aquisição ao andamento comercial
- ler resultado comercial com mais nuance que apenas status de CRM
- comparar volume, SQL, fechamento e valor ao longo dos meses
- apoiar leitura de qualidade por canal e por SDR

#### Limites
Essa planilha também não deve ser tratada automaticamente como verdade única para tudo.

Motivo:
- existe mistura de dados operacionais, comentários e blocos manuais
- a estrutura evolui entre meses
- algumas colunas aparecem só em meses recentes
- ainda precisa cruzamento com CRM para integridade de lead/opportunity

## Como o agente deve usar essas planilhas no dia a dia
### Uso 1. CONTROLE DE LEADS GERAL, quando a pergunta é sobre origem, perfil e validade do topo
Usar `CONTROLE DE LEADS GERAL` quando a pergunta for:
- de onde esse lead veio?
- que tipo de lead entrou por esse funil?
- qual dor, contexto ou estágio apareceu na captação?
- esse volume parece válido ou está contaminado por ruído operacional?

Essa planilha é mais forte para:
- leitura por funil
- leitura de perfil e contexto
- diferenças entre formatos de captação
- primeiros sinais de validade operacional

### Uso 2. Planilha Comercial x Marketing V.2, quando a pergunta é sobre operação comercial diária
Usar `Planilha Comercial x Marketing V.2` quando a pergunta for:
- quantas reuniões aconteceram?
- qual foi o próximo passo?
- houve SQL, no-show, R2, follow ou fechamento?
- qual canal parece estar gerando evolução comercial real no mês?

Essa planilha é mais forte para:
- leitura comercial diária
- nuance operacional humana
- acompanhamento de andamento e fechamento
- leitura mensal de qualidade comercial

Achado de auditoria importante:
- a aba `VENDAS - ABRIL/26` já permite cruzamentos muito mais fortes quando `LEAD ID` está preenchido
- isso transforma a planilha comercial de um diário operacional em uma ponte estrutural relevante com o Kommo
- ainda assim, a integridade precisa ser validada caso a caso, porque há linhas sem `LEAD ID` e há pelo menos sinais de origem/classificação que merecem auditoria adicional

### Uso 3. Kommo, quando a pergunta é sobre entidade viva e rastreabilidade estrutural
Quando Kommo estiver disponível, ele deve ser usado para:
- confirmar existência estrutural do lead
- verificar owner, pipeline e status
- auditar tracking e completude de campos
- validar se a ponte para CRM está íntegra

Regra:
- Kommo prevalece para entidade comercial viva e rastreabilidade estrutural
- Sheets prevalece quando a nuance operacional diária estiver melhor representada fora do CRM

### Uso 4. Reconciliação marketing x vendas
A leitura combinada das camadas deve seguir esta lógica:
- `CONTROLE DE LEADS GERAL` responde melhor o topo: origem, contexto, validade inicial, diferenças entre funis
- `Planilha Comercial x Marketing V.2` responde melhor o meio e fundo operacional: reunião, SQL, follow, fechamento e próximos passos
- Kommo responde melhor a estrutura viva: owner, pipeline, status, rastreabilidade e auditoria de integridade

Essas camadas juntas respondem perguntas como:
- quais origens geram reunião qualificada de verdade?
- qual tipo de lead chega mas não avança?
- qual mês mostra deterioração de SQL ou fechamento?
- a perda está no topo, na passagem ou no CRM?

Achado de auditoria importante:
- no recorte de abril, linhas de `WHATSAPP` na planilha comercial já aparecem com `LEAD ID` em alguns casos, o que permite ponte objetiva com Kommo
- porém a confiança dessa ponte não pode ser automática só porque o canal está marcado como `WHATSAPP`
- em amostra auditada, houve casos comercialmente marcados como `WHATSAPP` cujo lead no Kommo seguia com `Status WhatsApp = Lead Fantasma`, mostrando que canal comercial e validade operacional do topo não são sinônimos
- também apareceu ao menos um caso com `LEAD ID` na planilha comercial que não preservava mais os campos estruturais esperados de CTWA no Kommo, exigindo auditoria adicional antes de usar esse tipo de linha como prova forte
- apareceu ainda ao menos um caso em que o `LEAD ID` bate e o lead é `Lead Real`, mas o SDR da planilha comercial não coincide com o campo `SDR` do Kommo, mostrando que a ponte entre camada comercial e CRM é útil para identidade e validade, mas ainda não deve ser tratada como prova automática de atribuição operacional
- em amostra inicial de `Lead Real` auditados no `WHATSAPP`, a passagem para `VENDAS - ABRIL/26` parece bem mais estreita do que a passagem para Kommo, sugerindo que a camada comercial não deve ser usada como proxy de cobertura do topo sem medição própria de entrada/aproveitamento

Playbooks relacionados:
- `playbooks/sheets-commercial-reconciliation.md`
- `playbooks/crm-reconciliation.md`
- `playbooks/stack-failure-triage.md`

### Uso 5. Diagnóstico de stack e CTWA
O WhatsApp deve ser lido em camadas:
- aba `WHATSAPP` para separar `Lead Real` de `Lead Fantasma`
- aba `TABELA DE CÓDIGOS E MENSAGENS WPP` para rastrear código, SDR, criativo e template
- Kommo para validar persistência estrutural do lead no CRM

Essa combinação é a mais forte quando a pergunta for:
- o CTWA está gerando lead operacionalmente válido ou muito ruído?
- qual criativo/mensagem/código está associado ao fluxo?
- a falha foi na mídia, na automação, na triagem ou na persistência CRM?

Playbooks relacionados:
- `playbooks/stack-failure-triage.md`
- `playbooks/marketing-diagnosis.md`
- `playbooks/sheets-commercial-reconciliation.md`

## Leitura transversal das abas da CONTROLE DE LEADS GERAL
### Abas mais fortes para leitura qualitativa de perfil, dor e contexto
- `MVP`
- `SAAS PADRÃO`
- `INLEAD`
- `B2B`

Essas abas ajudam especialmente quando a pergunta é:
- quem está entrando?
- em que estágio está?
- qual dor principal aparece?
- quão madura parece a demanda?

### Abas mais fortes para leitura de validade e integridade operacional
- `WHATSAPP`
- `LP INSTITUCIONAL`
- `BIO IG`

Essas abas ajudam especialmente quando a pergunta é:
- o lead está identificado estruturalmente?
- existe filtro claro de validade?
- dá para cruzar com CRM ou com operação comercial com menos ambiguidade?

### Abas mais fracas para reconciliação estrutural, mas úteis historicamente
- `TYPEBOT`
- `LP PADRÃO`
- `LP YOUTUBE`
- parte da `LP V2`

Essas abas ajudam mais como:
- repertório histórico
- leitura de testes ou ofertas passadas
- memória de formatos de captura

### Abas com papel híbrido
- `LP V2`
- `BIO IG`
- `SAAS PADRÃO`

Elas combinam alguma utilidade operacional atual com limitações relevantes de tracking, schema ou reconciliação.

### Camada operacional auxiliar, não funil
- `TABELA DE CÓDIGOS E MENSAGENS WPP`

Essa aba serve para:
- rastreabilidade de abordagem no CTWA
- auditoria de códigos e templates
- governança entre criativo, SDR e mensagem

### Regra transversal de uso
Ao analisar a `CONTROLE DE LEADS GERAL`, o agente deve primeiro decidir qual tipo de pergunta está tentando responder:
- pergunta de perfil e dor
- pergunta de validade operacional
- pergunta de reconciliação estrutural
- pergunta histórica ou de repertório
- pergunta de operação WhatsApp

A aba certa depende da pergunta certa.
Não existe uma única aba superior para tudo.

## Hierarquia de confiança por tipo de pergunta

Resumo rápido para consulta operacional:
- perfil, dor e estágio -> `CONTROLE DE LEADS GERAL`
- validade operacional do topo -> `CONTROLE DE LEADS GERAL` + Kommo quando houver ponte
- reunião, SQL e próximos passos -> `Planilha Comercial x Marketing V.2`
- owner, pipeline e status vivo -> Kommo
- CTWA, ruído e rastreabilidade de mensagem -> `WHATSAPP` + `TABELA DE CÓDIGOS E MENSAGENS WPP` + Kommo
- fechamento e leitura executiva irreversível -> reconciliação obrigatória entre camadas
### 1. Pergunta de perfil, dor, contexto e estágio do lead
Fonte principal:
- `CONTROLE DE LEADS GERAL`

Fontes de apoio:
- `Planilha Comercial x Marketing V.2`
- Kommo, quando houver ponte confiável

Abas mais fortes:
- `MVP`
- `SAAS PADRÃO`
- `INLEAD`
- `B2B`
- `BIO IG`

### 2. Pergunta de validade operacional do topo do funil
Fonte principal:
- `CONTROLE DE LEADS GERAL`

Fontes de apoio:
- Kommo
- automações e camada operacional do WhatsApp, quando aplicável

Abas mais fortes:
- `WHATSAPP`
- `LP INSTITUCIONAL`
- `BIO IG`

Regra crítica:
- no WhatsApp, volume bruto não é volume válido

### 3. Pergunta de reunião, SQL, andamento comercial e próximos passos
Fonte principal:
- `Planilha Comercial x Marketing V.2`

Fontes de apoio:
- Kommo
- `CONTROLE DE LEADS GERAL`, apenas como contexto de origem

Regra crítica:
- no estado atual da operação, a nuance comercial diária pode estar mais confiável na planilha comercial do que no CRM

### 4. Pergunta de owner, pipeline, status vivo e rastreabilidade estrutural
Fonte principal:
- Kommo

Fontes de apoio:
- `Planilha Comercial x Marketing V.2`
- `CONTROLE DE LEADS GERAL`

Regra crítica:
- quando a pergunta é sobre entidade comercial viva, o CRM tende a prevalecer, desde que a integridade dos campos esteja aceitável

### 5. Pergunta de CTWA, ruído operacional e rastreabilidade de mensagem
Fonte principal:
- combinação entre `WHATSAPP`, `TABELA DE CÓDIGOS E MENSAGENS WPP` e Kommo

Fontes de apoio:
- Meta Ads, quando a integração estiver disponível

Regra crítica:
- separar sempre `Lead Real` de `Lead Fantasma`
- não analisar criativo ou mensagem de CTWA sem considerar o código WA e o template operacional associado

### 6. Pergunta de fechamento, receita e leitura executiva irreversível
Fonte principal:
- nenhuma fonte isolada deve receber confiança automática

Fontes de apoio obrigatórias:
- `Planilha Comercial x Marketing V.2`
- Kommo
- reconciliação com a camada correta do stack

Regra crítica:
- não decretar verdade executiva final a partir de uma única planilha ou de uma única leitura CRM sem reconciliação

Playbooks relacionados:
- `playbooks/executive-reporting.md`
- `playbooks/action-prioritization.md`
- `playbooks/crm-reconciliation.md`
- `playbooks/sheets-commercial-reconciliation.md`

## Como o agente não deve usar essas planilhas
Não usar isoladamente para:
- decretar CAC oficial final
- decretar receita oficial final
- substituir CRM em entidade viva
- tomar decisão executiva irreversível sem reconciliação

## Modelo de organização do Drive
### Objetivo da pasta `BO Brain - ORGANIZAÇÃO`
Essa pasta deve ser o espaço canônico de materiais operacionais derivados que o agente precisa consultar ou produzir com recorrência.

### Estrutura recomendada
```text
BO Brain - ORGANIZAÇÃO/
  01-fontes-vivas/
    CONTROLE DE LEADS GERAL
    Planilha Comercial x Marketing V.2
  02-analises-recorrentes/
    diagnosticos-campanhas/
    reconciliacoes-crm/
    relatorios-executivos/
    priorizacao-de-acoes/
  03-operacao-comercial/
    acompanhamento-sdr/
    acompanhamento-closer/
    no-show-e-follow/
  04-stack-e-monitoramento/
    anomalias/
    falhas-de-tracking/
    validacoes-de-webhook/
  05-arquivo/
    snapshots-antigos/
    exportacoes/
```

### Regras de organização
#### 01-fontes-vivas
Guardar apenas planilhas principais realmente usadas como entrada recorrente.

#### 02-analises-recorrentes
Guardar saídas derivadas do agente ou da operação que merecem reaproveitamento.
Exemplos:
- diagnósticos mensais
- comparativos de período
- relatórios executivos

#### 03-operacao-comercial
Guardar materiais de gestão de rotina comercial, sem misturar com fontes principais.

#### 04-stack-e-monitoramento
Guardar checklists, logs exportados, validações e materiais de falha operacional.

#### 05-arquivo
Guardar material antigo ou de suporte, sem poluir a camada viva.

## Política de uso do Drive pelo agente
### O agente deve usar o Drive para
- localizar fontes e materiais recorrentes
- armazenar derivados úteis de operação
- manter organização temática simples e estável

### O agente não deve usar o Drive para
- despejar arquivos temporários sem critério
- duplicar planilhas principais sem motivo
- criar subpastas excessivas ou burocráticas
- transformar o Drive em arquivo morto desorganizado

## Prioridade de confiança
Para o dia a dia, a ordem recomendada de confiança é:
1. fonte mais próxima do evento real
2. plataforma para spend/entrega
3. camada operacional mais bem mantida no processo real
4. CRM para entidade comercial viva, quando o preenchimento estiver íntegro
5. Sheets para reconciliação, contexto operacional e complementação, ou como camada operacional principal quando estiverem mais sólidos que o CRM
6. relatórios derivados para leitura secundária

### Regra específica do estado atual da Blue Ocean
No estado atual informado pela operação:
- a planilha `Planilha Comercial x Marketing V.2` está mais sólida do que Kommo para parte relevante da leitura comercial
- isso acontece porque o preenchimento em Kommo ainda sofre com disciplina operacional irregular de SDRs e Closers
- João Lopes atua hoje como Sales Ops e atualiza diariamente a planilha comercial, o que aumenta a confiabilidade operacional dessa camada

Portanto, até nova validação estrutural:
- `Planilha Comercial x Marketing V.2` deve ser tratada como camada comercial mais confiável para leitura diária de reuniões, qualificação, próximos passos e fechamento operacional
- Kommo não deve ser presumido como verdade superior por padrão sem auditoria de integridade
- a hierarquia final deve ser recalibrada depois de validar o stack, o preenchimento real no CRM e a consistência das automações

## Casos práticos que o agente poderá responder melhor agora
Com o Google Sheets já disponível, o agente passa a conseguir:
- mapear tipos de lead por origem e segmento
- comparar canais por qualidade percebida
- ler reuniões qualificadas e próximos passos por mês
- identificar presença de no-show, follow, R2 e fechamento
- cruzar planilha de leads com planilha comercial para leitura parcial de funil
- detectar sinais de `Lead Fantasma` na operação WhatsApp

## Necessidade crítica antes da reconciliação final
Antes de tratar o cruzamento entre marketing e comercial como confiável, é necessário validar:
- se as automações do n8n estão 100%
- se os dados da planilha `CONTROLE DE LEADS GERAL` estão chegando de forma correta
- se os campos necessários para ligação entre captação e comercial estão íntegros
- se a passagem entre marketing, planilha e comercial não está perdendo ou distorcendo informação

Sem essa validação, qualquer cruzamento entre as duas planilhas deve ser tratado como útil, porém ainda sujeito a falhas de stack.

## Próxima evolução natural
Depois de integrar Kommo, o uso ideal será:
- Meta Ads como camada de aquisição e entrega
- `CONTROLE DE LEADS GERAL` como camada de entrada e tracking operacional de marketing
- `Planilha Comercial x Marketing V.2` como camada comercial diária enquanto continuar mais confiável que o CRM
- Kommo como fonte de entidade comercial viva apenas na medida em que passar na auditoria de integridade operacional

A força real virá do cruzamento entre as três camadas mais o stack de automação validado, não do uso isolado de nenhuma delas.
