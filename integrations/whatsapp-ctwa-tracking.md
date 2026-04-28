# WhatsApp CTWA Tracking — Micro-LP, source_id e Lead Real

## Objetivo

Preservar atribuição de campanhas Click-to-WhatsApp sem tratar conversa iniciada pela Meta como lead real automaticamente.

## Arquitetura lógica

1. Usuário clica no anúncio CTWA.
2. Link passa por micro-LP/redirect com UTMs e `source_id`.
3. Micro-LP registra evento de clique/redirect.
4. Usuário abre WhatsApp.
5. Mensagem é enviada ou não.
6. n8n/webhook/buffer tenta casar clique, conversa e lead Kommo.
7. Kommo recebe lead/campo de origem.
8. Sheets/dashboard calcula Lead Real e CPL real.

## Por que micro-LP existe

O clique para WhatsApp pode gerar sinal de plataforma sem garantir resposta humana. A micro-LP cria uma trilha intermediária para:

- preservar UTMs/source_id;
- medir intenção de abrir WhatsApp;
- reduzir perda de atribuição;
- apoiar match temporal com Kommo;
- diferenciar clique, conversa iniciada e Lead Real.

## Campos mínimos

- `source_id`
- `utm_source`
- `utm_medium`
- `utm_campaign`
- `utm_content`
- campanha/adset/ad sanitizados
- timestamp
- redirect status
- match com Kommo
- janela temporal
- confiança do match

## Lead Fantasma

É suspeita quando:

- Meta reporta conversa/lead;
- não há lead correspondente no Kommo;
- não há resposta humana verificável;
- ou o match temporal é frágil.

Não significa fraude automaticamente. Pode ser:

- clique sem envio da mensagem;
- perda de UTMs;
- webhook falhou;
- Salesbot não rodou;
- lead criado sem campos;
- delay fora da janela.

## Janela de match

- Ideal: até 5 minutos.
- Aceitável: até 30 minutos com sinais convergentes.
- Frágil: acima de 30 minutos ou campos incompletos.
- Insuficiente: sem source_id/UTM/lead correspondente.

## Red lines

- Não reportar CTWA como Lead Real sem validação.
- Não calcular CPL real só com Meta.
- Não versionar telefone/mensagem/ID pessoal.
- Não copiar JSON de workflow com credenciais.

## Saída operacional

- Taxa de clique → WhatsApp aberto.
- WhatsApp aberto → lead Kommo.
- Kommo → Lead Real.
- % Lead Fantasma.
- Falhas por camada: micro-LP, webhook, Salesbot, Kommo, Sheets.
