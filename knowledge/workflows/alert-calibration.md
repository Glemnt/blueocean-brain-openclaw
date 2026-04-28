# Alert Calibration

Referência para calibrar alertas operacionais sem gerar ruído ou falsa urgência.

## Alertas prioritários

### CPL real disparou
- comparar ontem ou últimos 7 dias contra média anterior;
- usar spend da plataforma + leads operacionalmente válidos;
- não usar CPL plataforma como alerta final.

### Leads caíram
- validar campanha ativa, spend, webhook, n8n e Kommo/Sheets;
- diferenciar queda real de falha de captura.

### Lead Fantasma alto
- calcular proporção em CTWA;
- separar Lead Real de Lead Fantasma;
- investigar CTA, mensagem, público, automação e status WhatsApp.

### Webhook ou automação falhou
- checar gaps em horário comercial;
- validar logs, retries, credenciais e buffer.

### Frequência alta / fadiga
- cruzar frequência, CTR, CPM e qualidade de fundo;
- não alertar só por uma métrica isolada.

## Severidade

- Monitorar: sinal inicial, sem impacto confirmado;
- Investigar: padrão aparece, mas falta causa raiz;
- Alerta: impacto operacional provável;
- Crítico: decisão ou operação pode estar contaminada.

## Saída mínima do alerta

- tipo de alerta;
- período;
- fonte usada;
- confiança;
- hipótese principal;
- próxima validação;
- owner provável.
