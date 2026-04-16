# Apify

Documentação da integração Apify dentro da arquitetura do Blue Ocean Brain OpenClaw.

## Papel operacional
Apify entra como camada de coleta e observação externa.

Ele é especialmente útil para:
- mapear concorrentes e referências de mercado
- coletar sinais públicos de LPs, anúncios, páginas e presença digital
- alimentar análises competitivas com mais escala e repetibilidade
- reduzir dependência de coleta manual em pesquisas recorrentes

## O que esta integração sabe bem
Apify é útil para:
- coleta pública estruturada
- crawling recorrente
- descoberta em volume quando o alvo é público
- enriquecer análises comparativas com amostra maior

## O que esta integração não sabe bem
Apify não deve ser tratado como:
- fonte de verdade sobre performance interna de concorrente
- evidência automática de eficácia real
- substituto de leitura estratégica
- confirmação de causalidade

Coleta pública não equivale a acesso ao bastidor operacional.

## Fonte de verdade
Quando Apify entrar na análise:
- ele é fonte de coleta pública
- não é fonte primária sobre resultado interno de negócio
- o insight final continua dependendo de interpretação, contexto e validação

## Riscos de leitura incorreta
Erros comuns:
- tratar presença pública como prova de performance real
- assumir que volume de criativos ou LPs indica eficiência
- transformar scraping em benchmark automático
- confiar em dado coletado sem revisar contexto, data e completude

## Limites de uso pelo agente
Uso recomendado:
- discovery competitivo
- monitoramento de players
- ampliação de amostra para análise comparativa
- coleta recorrente de sinais públicos

Uso não recomendado:
- declarar que concorrente performa bem só porque aparece muito
- sustentar decisão forte sem cruzar com leitura estratégica
- confundir coleta escalável com entendimento profundo

## Perguntas obrigatórias quando usar Apify
- qual hipótese ou pergunta a coleta pretende responder?
- o dado coletado é só presença pública ou sinal forte de padrão?
- a amostra é suficiente?
- existe risco de viés por coleta incompleta?
- a leitura final depende de revisão humana?

## Relação com outras camadas
- usar junto com `knowledge/competitive-intelligence/`
- pode alimentar `playbooks/competitive-intelligence.md`
- pode gerar insumo para `subagents/competitive-intelligence-analyst.md`
- não substitui `company/icp.md` nem o filtro de aderência ao posicionamento da Blue Ocean

## Regra final
Apify é alavanca de observação, não motor automático de verdade.

Ele ajuda a ver mais coisa, não a pensar no lugar da Blue Ocean.
