# Kommo Field Mapping — Sanitized Reference

Referência sanitizada dos campos e conceitos críticos do Kommo para análise Blue Ocean.

Não versionar aqui tokens, payloads, exports brutos, telefones, emails, nomes de leads ou listas de clientes.

## Entidades principais

- lead/deal;
- contact;
- company;
- task;
- pipeline;
- status/stage;
- responsible user / owner;
- custom fields;
- notes/events.

## Campos críticos para análise

### Identidade e ownership

- lead ID;
- contact/company link;
- responsible user;
- pipeline;
- status;
- created_at / updated_at.

### Origem e atribuição

- campanha;
- conjunto de anúncios;
- anúncio;
- UTM source;
- UTM medium;
- UTM campaign;
- UTM content;
- source/source_id quando disponível.

### WhatsApp / CTWA

- Status WhatsApp;
- Lead Real;
- Lead Fantasma;
- SDR/owner relacionado;
- campos de campanha preservados após automação.

### Comercial

- etapa;
- qualificação;
- próximo passo;
- motivo de perda;
- oportunidade;
- proposta;
- ganho/perdido.

## Regras

- lead criado no Kommo é entidade estrutural, não validade operacional automática;
- em CTWA, filtrar Lead Real/Fantasma antes de CPL real;
- campos vazios reduzem confiança;
- motivo de perda ausente contamina diagnóstico comercial;
- dashboard derivado não substitui Kommo nem Sheets quando houver divergência.

## Próxima evolução

Quando houver acesso live ao Kommo MCP, validar e atualizar esta referência com nomes de campos reais sanitizados, sem expor dados privados.
