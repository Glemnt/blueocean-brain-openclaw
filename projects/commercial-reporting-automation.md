# Projeto — Relatório Comercial Automatizado

## Objetivo

Automatizar relatório comercial conectando mídia, Kommo, Sheets e dashboards sem perder governança de dado.

## Arquitetura alvo

1. Meta Ads fornece gasto, campanha e sinais de plataforma.
2. Kommo fornece lead, status, owner, reunião, perda/ganho.
3. Sheets consolida métricas operacionais e comerciais.
4. n8n orquestra coleta, validação, atualização e alertas.
5. Relatório executivo consome apenas dados reconciliados ou marcados com confiança.

## Fases

### Fase 1 — Base confiável

- Mapear campos Kommo.
- Mapear source_id/UTM.
- Validar planilha/dash.
- Documentar fórmulas.

### Fase 2 — Coleta automatizada

- Buscar Meta Ads por período.
- Buscar Kommo por período.
- Atualizar Sheets.
- Registrar falhas.

### Fase 3 — Reconciliação

- Calcular CPL plataforma, CPL operacional, CPL real, CPAg, CPR.
- Detectar Lead Fantasma.
- Marcar divergência >20%.
- Classificar confiança.

### Fase 4 — Relatório

- Gerar resumo executivo.
- Separar achados, riscos, hipóteses e decisões.
- Criar plano 7/14/30.
- Preservar histórico curado.

## Critérios de aceite

- Fórmulas documentadas.
- Fontes rastreáveis.
- Zero segredo no repo.
- Alertas para falha de stack.
- Dashboard nunca tratado como verdade final isolada.
- Relatório indica confiança.

## Owners típicos

- Dados/BI: reconciliação e fórmulas.
- Marketing: leitura de mídia.
- Comercial: status, SLA e perdas.
- Operação: saúde da conta e plano.
- Governança: alçada/red lines.
