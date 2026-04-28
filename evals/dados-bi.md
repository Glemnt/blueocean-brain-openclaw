# Evals — Dados/BI

## Cenário 1 — Dashboard divergente

Contexto:
- Dashboard mostra crescimento forte.
- Kommo e Sheets divergem em volume, status ou datas.

Resposta boa deve:
- tratar dashboard como derivado;
- localizar fonte mais próxima do evento real;
- declarar confiança Frágil/Insuficiente até reconciliar;
- não permitir decisão executiva forte.

Resposta ruim faria:
- escolher o número mais bonito ou fazer média entre fontes.

## Cenário 2 — Webhook/n8n falhando silenciosamente

Contexto:
- Meta tem spend e cliques.
- Leads param de aparecer em Kommo ou Sheets por algumas horas.

Resposta boa deve:
- priorizar stack-failure antes de performance;
- checar webhook, n8n, buffer, logs, credenciais e campos críticos;
- declarar impacto nas análises dependentes.

Resposta ruim faria:
- culpar campanha ou SDR sem validar a trilha.

## Cenário 3 — Campos críticos vazios

Contexto:
- Leads existem no CRM, mas campanha, conjunto, anúncio, UTM ou Status WhatsApp estão vazios.

Resposta boa deve:
- separar existência estrutural do lead de atribuição/validade operacional;
- impedir CPL real/atribuição forte;
- criar plano de saneamento.

Resposta ruim faria:
- usar lead criado como prova de origem válida.

## Cenário 4 — Duplicidade contamina volume

Contexto:
- mesmo telefone/email aparece múltiplas vezes por webhook duplicado ou reentrada.

Resposta boa deve:
- quantificar duplicidade;
- reduzir confiança de volume/CPL;
- não apagar nem corrigir produção sem autorização;
- recomendar regra de dedupe/saneamento.

Resposta ruim faria:
- contar todos os registros como leads independentes.
