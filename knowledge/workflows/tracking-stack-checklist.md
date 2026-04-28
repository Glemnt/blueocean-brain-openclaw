# Tracking Stack Checklist

Checklist de componentes que devem ser lembrados quando a leitura de mídia, CRM, Sheets ou dashboard parecer inconsistente.

## Componentes a checar

- Meta Ads evento correto / promoted object / `actions[]`
- GTM: tags, triggers, variáveis e persistência de UTMs
- Stape / server-side tracking, quando aplicável
- CAPI: dedupe, event_id, headers e match quality
- n8n: workflow ativo, execução, logs, buffer e retries
- Salesbot: criação/atualização do lead e campos de WhatsApp
- Kommo: campos customizados, owner, pipeline, status e motivo de perda
- Google Sheets: aba correta, fórmula, atualização manual/automática
- SOURCE_MAP / `source_id`: mapeamento de origem e canal
- Dashboard: regra de derivação e atualização

## Sintomas comuns

- plataforma mostra conversão e CRM não mostra lead;
- CRM mostra lead sem campanha/conjunto/anúncio;
- Sheets diverge do Kommo;
- dashboard mostra número que nenhuma fonte primária sustenta;
- CTWA tem muito clique/conversa e pouco Lead Real;
- perda sem motivo registrado contamina leitura comercial.

## Regra de decisão

Se qualquer componente crítico estiver sem validação, rebaixar confiança e usar `playbooks/stack-failure-triage.md` antes de recomendar mídia, copy ou comercial.
