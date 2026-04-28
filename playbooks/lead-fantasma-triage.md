# Lead Fantasma Triage Playbook

Playbook para diagnosticar quando CTWA, WhatsApp, Kommo, Sheets ou dashboard mostram volume que não vira lead operacionalmente válido.

## Quando usar

- CTWA com muito clique/conversa e pouco Lead Real;
- discrepância Meta × Kommo × Sheets em WhatsApp;
- `Status WhatsApp` ausente, inconsistente ou com muito Lead Fantasma;
- CPL real muda muito ao filtrar fantasma;
- suspeita de problema em micro-LP, n8n, Salesbot ou mensagem.

## Objetivo

1. separar volume bruto de volume válido;
2. localizar onde a trilha quebra;
3. decidir se o problema é mídia, mensagem, automação, CRM ou operação;
4. impedir escala/pausa baseada em volume contaminado.

## Sequência

### 1. Separar unidades

- cliques;
- conversas iniciadas;
- leads criados;
- Lead Real;
- Lead Fantasma;
- reuniões/agendamentos.

### 2. Validar fontes

- Meta Ads: evento correto e campanha/conjunto/anúncio;
- Kommo: lead, owner, pipeline, `Status WhatsApp`, campos de campanha;
- Sheets: aba `WHATSAPP` e `TABELA DE CÓDIGOS E MENSAGENS WPP`;
- n8n/Salesbot: webhook, buffer, match temporal, patch de campos.

### 3. Diagnosticar causa provável

- mídia/público: muito clique de baixa intenção;
- mensagem: CTA ou texto pré-preenchido gera ruído;
- automação: webhook/match/patch falha;
- CRM: status não preenchido ou owner incorreto;
- comercial: lead real existe mas não avança.

### 4. Decidir

- pode seguir: Lead Real e trilha íntegra sustentam leitura;
- ressalva: há lacuna parcial, mas leitura útil;
- travar: volume válido não está comprovado;
- subir: erro recorrente contamina decisão executiva.

## Saída obrigatória

1. volume bruto;
2. volume operacionalmente válido;
3. % Lead Fantasma;
4. camada onde a trilha quebra;
5. confiança;
6. owner provável;
7. próxima ação.

## Referências

- `integrations/meta-ads.md`
- `integrations/kommo.md`
- `integrations/n8n.md`
- `integrations/google-sheets-operating-model.md`
- `knowledge/workflows/tracking-stack-checklist.md`
- `playbooks/stack-failure-triage.md`
