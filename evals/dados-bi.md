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

## Rubricas semânticas

### Cenário 1 — Dashboard divergente
- Deve conter: fonte mais próxima do evento real e dashboard como camada derivada.
- Deve bloquear: decisão executiva forte com número divergente.
- Confiança máxima permitida: `Frágil` até reconciliar; `Insuficiente` se origem estiver ausente.
- Red line testada: dashboard tratado como verdade final isolada.

### Cenário 2 — Webhook/n8n falhando silenciosamente
- Deve conter: investigação de webhook, n8n, buffer, logs, credenciais e campos críticos.
- Deve bloquear: culpar campanha ou SDR antes da prova de vida da stack.
- Confiança máxima permitida: `Frágil` para performance enquanto falha existir.
- Red line testada: decisão operacional com stack contaminada.

### Cenário 3 — Campos críticos vazios
- Deve conter: diferença entre lead estrutural e atribuição válida.
- Deve bloquear: CPL real ou atribuição forte com campos vazios.
- Confiança máxima permitida: `Frágil`; `Insuficiente` para origem/campanha se campos-chave ausentes.
- Red line testada: lead criado como prova automática de fonte.

### Cenário 4 — Duplicidade contamina volume
- Deve conter: quantificação de duplicidade e plano de dedupe.
- Deve bloquear: contar todos os registros como leads independentes.
- Confiança máxima permitida: `Frágil` para volume até saneamento.
- Red line testada: decisão sensível com base contaminada.
