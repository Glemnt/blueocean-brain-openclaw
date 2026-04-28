# Auditoria Formal de Meta Ads

Use este playbook quando a conta precisa de uma revisão completa, não apenas diagnóstico pontual de campanha.

## Objetivo

Produzir um health score operacional da conta Meta Ads, conectando mídia, funil, CRM, stack, qualidade comercial e governança. A auditoria não deve transformar métricas de plataforma em verdade final.

## Entradas mínimas

- Período auditado e período de comparação.
- Estrutura de campanhas, conjuntos e anúncios.
- Objetivos, budget, eventos otimizados e learning status.
- Métricas por campanha/adset/anúncio: gasto, impressões, CPM, CTR, CPC, leads/conversas, CPL, frequência, conversões intermediárias.
- CRM/Kommo: leads recebidos, origem, owner, status, reunião, perda/ganho.
- Sheets/dashboard: CPL real, lead operacionalmente válido, reuniões, receita quando houver.
- Alertas conhecidos de stack: webhook, GTM, CAPI, Salesbot, SOURCE_MAP, dedupe, headers.

## Score 0–100

| Bloco | Peso | O que avalia |
|---|---:|---|
| Estrutura de conta | 10 | Organização, naming, separação de testes, objetivos corretos |
| Tracking e eventos | 15 | Pixel/CAPI/GTM, dedupe, eventos, UTMs, source_id |
| Qualidade do dado | 15 | Meta × Kommo × Sheets, campos críticos, divergências |
| Criativos e diversidade | 15 | Volume, fadiga, ângulos, hooks, formatos, Andromeda |
| Público e segmentação | 10 | Fit, saturação, exclusões, overlap, escala |
| Performance de mídia | 10 | CPM/CTR/CPL/frequência vs benchmark e recorte |
| Funil pós-clique/CTWA | 10 | Drop-off, Lead Fantasma, mensagem, LP/form |
| Comercial/CRM | 10 | SLA, owner, progressão, no-show, motivos de perda |
| Governança | 5 | Owner, alçada, decisões reversíveis, riscos e red lines |

## Gates críticos

Se qualquer gate abaixo falhar, a confiança máxima da auditoria é `Frágil`, mesmo com score alto:

- Stack contaminada ou evento duplicado.
- CRM não recebe leads de forma confiável.
- Dashboard diverge >20% da origem sem explicação.
- Atribuição forte de receita sem trilha robusta.
- Mais de 50% dos campos críticos do CRM vazios.
- Conta em risco sem owner/plano.

## Privacy gate

Antes de usar exemplos reais:

- Não versionar e-mails, telefones, IDs pessoais, CSVs de cliente, exports crus ou tokens.
- Usar agregados, percentuais e exemplos anonimizados.
- Se precisar preservar evidência, criar resumo curado em `history/`, não copiar raw.

## Checklist de auditoria

### 1. Estrutura

- Campanhas têm objetivo coerente com o funil?
- Há separação clara entre aquisição, remarketing, teste e escala?
- Naming permite ligar campanha → conjunto → anúncio → source_id?
- Budget está concentrado em vencedores ou pulverizado sem hipótese?
- Há campanhas antigas gerando ruído de atribuição?

### 2. Tracking

- Pixel ativo e eventos chegando?
- CAPI ativo sem duplicar evento?
- Event ID/dedupe coerente?
- GTM preserva UTMs/source_id?
- SOURCE_MAP cobre campanhas ativas?
- Webhook/n8n/Salesbot estão vivos?

### 3. Dados e reconciliação

- Meta Leads/Conversations batem com Kommo dentro da margem explicada?
- Kommo bate com Sheets/dashboard?
- Há Lead Fantasma acima do aceitável?
- Há campos críticos vazios?
- Há mudança de pipeline/status no período?

### 4. Criativos

- Há pelo menos 10 criativos realmente distintos para fase de escala?
- Frequência e CTR indicam fadiga?
- Hooks filtram ICP ou atraem curiosos?
- Promessas respeitam escopo e prova?
- Existe variação por dor, mecanismo, prova e CTA?

### 5. Público

- Segmentação condiz com ICP SaaS B2B?
- Público está saturado?
- Existe overlap relevante?
- Remarketing está separado e dimensionado?
- Lookalikes/interesses/open targeting têm hipótese clara?

### 6. Comercial

- Todo lead operacionalmente válido tem owner?
- SLA de primeiro contato está dentro do esperado?
- Motivos de perda estão preenchidos?
- No-show e reunião realizada foram medidos?
- Há diferença de performance por SDR/source_id?

## Classificação final

- `80–100`: saudável, mas ainda sujeito aos gates críticos.
- `60–79`: funcional com pontos de atenção; priorizar quick wins e validação.
- `40–59`: risco operacional; precisa plano por owner.
- `<40`: conta/stack/funil contaminado; não recomendar escala.

## Saída obrigatória

1. Resumo executivo.
2. Score por bloco e score final.
3. Gates críticos: passou/falhou.
4. O que é fato, hipótese e lacuna.
5. Top 5 riscos.
6. Top 5 quick wins.
7. Plano 7/14/30 dias.
8. Confiança: `Alta`, `Parcial`, `Frágil` ou `Insuficiente`.
