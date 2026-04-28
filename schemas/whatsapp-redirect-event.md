# Schema — Evento WhatsApp Redirect / CTWA

Não versionar telefone, nome, mensagem integral ou identificadores pessoais crus.

## Evento sanitizado

- `event_id`
- `timestamp`
- `source_id`
- `campaign_id_sanitized`
- `adset_id_sanitized`
- `ad_id_sanitized`
- `utm_source`
- `utm_medium`
- `utm_campaign`
- `utm_content`
- `landing_url`
- `redirect_status`
- `whatsapp_click_detected`
- `message_sent_confirmed`: true/false/unknown
- `kommo_lead_created`: true/false/unknown
- `kommo_lead_id_sanitized`
- `salesbot_triggered`: true/false/unknown
- `match_window_minutes`
- `match_confidence`: alta/parcial/frágil/insuficiente
- `failure_reason`
