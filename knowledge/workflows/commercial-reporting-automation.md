# Commercial Reporting Automation

Workflow de referência para relatórios comerciais recorrentes sem produzir narrativa bonita em base frágil.

## Objetivo

Gerar leitura diária/semanal/mensal conectando mídia, leads, reuniões, SQL, oportunidades, vendas e riscos.

## Fontes típicas

- Meta Ads: spend, entrega e eventos;
- Kommo: entidade estrutural, owner, pipeline, status e motivo de perda;
- Google Sheets: operação comercial diária, reuniões, próximos passos e fechamento quando estiver mais mantido;
- n8n/webhooks: trilha de captura e enriquecimento;
- dashboard: visualização derivada, nunca fonte final isolada.

## Métricas mínimas

- investimento;
- leads operacionalmente válidos;
- CPL real;
- reuniões agendadas;
- reuniões realizadas;
- SQL/oportunidades;
- vendas/fechamentos;
- CAC de mídia, quando a atribuição for robusta;
- principais riscos de dados.

## Regras

- nunca misturar volume bruto com Lead Real;
- nunca declarar CAC/receita final sem reconciliação;
- sempre informar confiança;
- sempre separar resultado, risco e próxima ação;
- se a stack estiver frágil, o relatório deve dizer isso explicitamente.

## Saída recomendada

Usar `templates/executive-report-output.md` para a camada executiva e anexar uma seção operacional com:

- fontes usadas;
- divergências;
- decisões seguras;
- decisões que devem esperar validação.
