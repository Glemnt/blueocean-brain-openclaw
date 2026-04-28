# n8n — Fluxo WhatsApp CTWA Sanitizado

## Objetivo

Documentar o fluxo n8n/Salesbot/Kommo sem copiar JSON cru, credenciais ou dados pessoais.

## Fluxo esperado

1. Webhook recebe evento da micro-LP.
2. Valida payload mínimo.
3. Normaliza UTMs e `source_id`.
4. Salva evento em buffer temporário.
5. Aguarda evento de lead/conversa Kommo/Salesbot.
6. Faz match por janela temporal + source_id/campanha.
7. Atualiza campos sanitizados no Kommo.
8. Envia linha agregada para Sheets/dashboard.
9. Registra falha quando match não acontece.

## Nodes conceituais

| Node | Função | Falha comum |
|---|---|---|
| Webhook entrada | receber clique/redirect | endpoint errado/offline |
| Validação | checar campos mínimos | payload incompleto |
| Normalização | padronizar UTM/source_id | naming inconsistente |
| Buffer | armazenar evento temporário | expiração curta/duplicidade |
| Kommo lookup | buscar lead/conversa | campo ausente/token expirado |
| Match temporal | casar evento e lead | janela mal calibrada |
| Update lead | escrever origem no CRM | permissão/campo errado |
| Sheets append/update | alimentar dashboard | range/schema divergente |
| Error handler | logar falhas | erro silencioso |

## Critérios de aceite

- 95%+ dos eventos válidos chegam ao buffer.
- 90%+ dos leads Kommo com origem têm `source_id` ou fallback documentado.
- Erros não ficam silenciosos.
- Duplicidades são identificadas.
- Dashboard diferencia plataforma, CRM, Lead Real e Lead Fantasma.

## Monitoramento

Alertar quando:

- webhook fica sem evento em horário ativo;
- taxa de match cai >20%;
- campos críticos ficam vazios;
- duplicidade aumenta;
- token/credencial expira;
- Salesbot para de disparar.

## Segurança

- Credenciais ficam fora do repo.
- Payloads reais não entram em git.
- Logs versionados devem ser agregados/sanitizados.
