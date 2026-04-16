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
### Uso 1. Complemento operacional do CRM
Quando Kommo estiver disponível, Sheets deve ser usado para:
- complementar contexto
- validar qualidade de leitura
- ler campos de operação comercial não tão bem estruturados no CRM
- rastrear exceções e discrepâncias

Regra:
- CRM prevalece para entidade comercial viva
- Sheets complementa histórico operacional e reconciliação

### Uso 2. Leitura de qualidade por origem
A planilha `CONTROLE DE LEADS GERAL` deve ser usada para:
- comparar diferença de perfil por origem
- entender quais formulários capturam que tipo de lead
- identificar padrões de MRR, segmento, canal e desafio
- observar gargalos de agendamento e fechamentos por origem

### Uso 3. Leitura comercial e de funil real
A planilha `Planilha Comercial x Marketing V.2` deve ser usada para:
- contar reuniões e qualificação por mês
- analisar próximos passos recorrentes
- identificar no-shows, follow, R2 e conversões
- cruzar canal de aquisição com qualidade comercial

### Uso 4. Reconciliação marketing x vendas
Essas planilhas são boas para perguntas como:
- quais origens geram reunião qualificada de verdade?
- qual tipo de lead chega mas não avança?
- qual mês mostra deterioração de SQL ou fechamento?
- qual SDR ou canal parece estar concentrando melhor evolução?

### Uso 5. Diagnóstico de stack
A aba `WHATSAPP` é especialmente útil para:
- detectar `Lead Fantasma`
- separar conversa iniciada de lead efetivo
- apoiar diagnóstico quando Meta e CRM não batem

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
