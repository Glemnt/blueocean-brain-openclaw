# Kommo Integration

Documentação canônica da integração Kommo dentro do `blueocean-brain-openclaw`.

## Papel da integração
Kommo é a base principal de leitura para:
- identidade estrutural do lead
- avanço comercial
- etapa do funil
- owner comercial
- qualificação
- oportunidade
- ganho, perda e motivo de perda
- rastreabilidade entre lead, SDR e status operacional no CRM

Quando o assunto é o que aconteceu com o lead depois da captação, o Kommo tende a prevalecer sobre dashboard e planilhas, desde que os campos críticos estejam íntegros.

## O que a integração sabe bem
Confiável para leitura direta quando o CRM está íntegro:
- entrada de lead
- owner
- etapa atual
- timestamps operacionais
- avanço no funil
- motivo de perda
- distribuição entre SDRs e closers

## O que requer ressalva
- CPL real depende de cruzamento com spend da plataforma
- qualidade de campos depende da disciplina operacional e das automações
- receita, forecast e leitura executiva dependem de integridade da operação e reconciliação com outras fontes

## Fonte de verdade por tipo de dado
- existência estrutural do lead: Kommo
- pipeline e status CRM: Kommo
- owner e distribuição: Kommo
- validade operacional do funil WhatsApp: Kommo + planilha `WHATSAPP` (via `Status WhatsApp` / `LEAD REAL`)
- leitura comercial diária e próximos passos: planilhas comerciais, especialmente `Planilha Comercial x Marketing V.2`
- dashboard consolidado: derivado, nunca verdade automática
- planilhas: apoio operacional e leitura por funil, não substitutas automáticas do CRM

## Fluxo técnico resumido
### WhatsApp CTWA
Meta Ads → WhatsApp SDR → Kommo → automação preenche campanha, UTMs, conjunto, anúncio e status de lead real/fantasma

### Formulário nativo
Meta Ads Lead Form → automação → Kommo com campanha, conjunto, anúncio e UTM

### Landing Page
LP → formulário → GTM/webhook/n8n → Kommo com campos de tracking e lead

## Campos críticos
- campanha
- conjunto
- anúncio
- UTM
- owner
- etapa
- próximo passo
- motivo de perda
- status WhatsApp

Sem esses campos, a confiança da leitura cai.

## Fragilidades conhecidas
- CRM mal preenchido por SDR contamina diagnóstico
- dashboard pode divergir do Kommo
- automação pode falhar no preenchimento de tracking
- duplicidade de lead distorce volume e avanço
- LP pode perder UTM entre páginas se a persistência falhar
- lead fantasma no WhatsApp gera falso volume se não for filtrado

## Erros comuns de interpretação
- tratar qualquer lead criado como lead válido
- confiar em dashboard acima do CRM
- diagnosticar performance comercial forte com campos críticos vazios
- ignorar que falha de stack pode parecer problema de mídia
- usar pipeline cheio como sinônimo de pipeline saudável

## Regra de leitura
Kommo prevalece quando a pergunta é:
- o lead existiu estruturalmente?
- quem recebeu?
- em que etapa está?
- avançou?
- perdeu? por quê?
- qual SDR/owner ficou responsável?

Mas o Kommo não substitui a plataforma quando a pergunta é spend, entrega ou consumo de mídia, e também não substitui sozinho a leitura operacional diária quando as planilhas carregam nuance humana, próximos passos e filtros específicos por funil.

## Regra especial para WhatsApp
No funil WhatsApp, não tratar qualquer lead criado no Kommo como lead válido automático.

A leitura correta é:
- volume bruto: leads criados
- volume válido: leads com `Status WhatsApp = Lead Real`
- volume de ruído: leads com `Status WhatsApp = Lead Fantasma`

Essa distinção foi confirmada tanto na planilha `WHATSAPP` quanto no próprio Kommo.

## Relação com outras camadas
- reconciliação e integridade: `playbooks/crm-reconciliation.md`
- análise comercial: `subagents/sdr-comercial-analyst.md`
- análise de dados e stack: `subagents/dados-bi-analyst.md`
- leitura de ownership e escalonamento: `knowledge/matrices/ownership-governance-matrix.md`

## Regra final
Kommo é a espinha dorsal da verdade comercial.

Quando ele está íntegro, dá lastro para decisão.
Quando está contaminado, a confiança do sistema inteiro precisa cair junto.
