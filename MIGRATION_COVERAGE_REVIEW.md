# Revisão de Cobertura da Migração — Legado Claude Code → OpenClaw

## Veredito

A migração não é uma cópia 1:1 do filesystem legado. Ela preserva a inteligência migrável em arquitetura OpenClaw-native e exclui intencionalmente segredo, PII, cache, vendor, runtime Claude e exports crus.

Após a segunda revisão de cobertura, as lacunas migráveis remanescentes foram incorporadas como documentos ricos em:

- `playbooks/`
- `templates/`
- `schemas/`
- `integrations/`
- `knowledge/`
- `history/`
- `projects/`

## Famílias migradas por intenção

### `.claude/commands` e `.claude/skills`

Não foram copiadas como slash commands/SKILL.md Claude. Foram reescritas como playbooks, templates, schemas e evals.

Cobertura adicional criada:

- auditoria formal Meta;
- health score;
- Andromeda/inventário criativo;
- A/B testing;
- Google Ads;
- planejamento de mídia;
- forecast;
- comparação de períodos;
- onboarding de conta;
- handoff comercial → operação;
- institucionalização;
- qualificação de lead;
- status operacional rápido.

### Subagents

Os subagents foram preservados como especialistas OpenClaw, com reforço em:

- copy frameworks;
- schemas de input;
- evals;
- Lead Fantasma;
- dados/BI;
- SDR/comercial;
- competitive intelligence.

### Knowledge

Conteúdo útil foi distribuído por camadas:

- canon empresarial em `company/`;
- governança em `governance/`;
- padrões, benchmarks e matrizes em `knowledge/`;
- workflows operacionais em `knowledge/workflows/`;
- copy em `knowledge/copy/`;
- evidência datada em `history/`.

### Tools / n8n / WhatsApp

JSONs, HTML e workflows não foram copiados crus. A lógica operacional foi migrada como especificação sanitizada:

- `integrations/whatsapp-ctwa-tracking.md`
- `integrations/n8n-whatsapp-ctwa.md`
- `integrations/n8n-cpl-real.md`
- `integrations/dashboard-derived-metrics.md`
- `schemas/whatsapp-redirect-event.md`

### Reports, sessions, snapshots, archive

Não foram migrados crus por risco de PII/ruído/datado. Aprendizados foram preservados em:

- `history/legacy-design-lineage.md`
- `history/2026-04-week1-snapshots-summary.md`
- `history/2026-03-04-meta-ads-and-commercial-reports-summary.md`

## Exclusões intencionais

- `.env.kommo` e tokens.
- `.mcp-servers/` e dependências.
- `everything-claude-code/` como vendor/reference externo.
- `reports/raw/` e exports com clientes/leads.
- TSVs/CSVs com PII.
- cache de creative library, thumbnails, `.DS_Store`, Obsidian UI state.
- prompts como system prompt ativo quando a informação já virou canon/playbook.

## Critério de completude

A migração é completa quando:

- o conhecimento migrável tem destino OpenClaw-native;
- não há dependência de arquivo Claude-specific para operar;
- dados sensíveis não foram copiados;
- lacunas conhecidas têm playbook/template/schema ou política;
- referências internas passam na checagem.
