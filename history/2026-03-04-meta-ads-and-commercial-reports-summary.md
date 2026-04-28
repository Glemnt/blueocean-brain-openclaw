# Evidência Curada — Relatórios Meta Ads e Comercial Março/Abril 2026

## Status

Resumo sanitizado de relatórios históricos. Arquivos HTML/PDF/exports crus não devem ser versionados literalmente.

## Aprendizados de arquitetura

- Relatório executivo deve conectar mídia, CRM, comercial e operação.
- Planos de campanha precisam declarar hipótese, budget, métrica, owner e condição de pausa.
- Consolidações mensais/semanais devem incluir riscos de tracking e confiança dos dados.
- Apresentações para cliente precisam evitar excesso técnico e separar decisão de investigação.
- Quando a stack está instável, o relatório deve abrir com limitação de confiança.

## Implicações no repo OpenClaw

- `playbooks/executive-reporting.md` conduz a narrativa.
- `integrations/n8n-cpl-real.md` e `integrations/dashboard-derived-metrics.md` protegem cálculo.
- `templates/executive-report-output.md`, `templates/forecast-output.md` e `templates/period-comparison.md` padronizam saída.

Confiança: `Parcial`.
