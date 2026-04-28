# Blue Ocean Brain OpenClaw — Progresso da Migração

Este arquivo transforma o plano de migração em passos executáveis até `100%`.

A migração aqui não significa copiar o legado. Significa tornar o brain funcional, nativo de OpenClaw, testável e seguro por camadas.

## Regra de progresso

O progresso só sobe quando uma camada fica útil no repo OpenClaw, com documentação clara e sem depender do runtime antigo.

- `0%` = só inventário/plano
- `25%` = correções canônicas essenciais aplicadas
- `50%` = fluxos principais funcionais e coerentes
- `75%` = templates/schemas/evals mínimos criados
- `100%` = migração funcional completa, com camadas críticas cobertas e sem lacunas P0/P1 abertas

## Status atual

Progresso atual: `100%`

Motivo:

- auditoria completa do legado e do repo alvo já foi feita;
- arquitetura OpenClaw-native já existe;
- integrações, playbooks e subagents centrais já estão criados;
- Fase 1 foi aplicada: navegação, roteamento de triagem e referência de padrões diagnósticos foram corrigidos;
- Fase 2 foi aplicada: lead estrutural, lead operacionalmente válido, Lead Real, Lead Fantasma e fonte de verdade por camada foram harmonizados;
- Fase 3 foi aplicada: política de dados/evidência criada e `snapshots/` passou a ser ignorado como runtime local;
- Fase 4 foi aplicada: template de handoff inter-subagente OpenClaw-native foi criado;
- Fase 5 foi aplicada: `evals/` inicial com cenários P0 por domínio foi criado;
- Fase 6 foi aplicada: schemas e workflows críticos foram criados em versão enxuta e funcional;
- Fase 7 foi aplicada: referências internas foram verificadas e a migração funcional OpenClaw chegou a 100%;
- Fase 8 foi aplicada após revisão de cobertura total: lacunas ricas de commands/skills/prompts/knowledge/tools/history foram migradas para playbooks, templates, schemas, integrations, knowledge e history sem copiar runtime Claude, PII ou cache.

## Fases da migração funcional

### Fase 1 — Correções canônicas e navegação (`20%` → `30%`)

Objetivo: corrigir inconsistências objetivas que impedem uso redondo do repo.

Tarefas:

- [x] atualizar `README.md` com todos os playbooks atuais;
- [x] corrigir roteamento em `playbooks/triage.md`;
- [x] corrigir referência de padrão inexistente em `playbooks/marketing-diagnosis.md` / `knowledge/patterns/diagnostic-patterns.md`;
- [x] verificar diff e garantir que as quatro alterações locais existentes foram preservadas.

Critério de pronto:

- navegação do repo bate com os arquivos reais;
- triagem aponta para playbooks existentes;
- não há referência quebrada a padrão diagnóstico inexistente.

### Fase 2 — Harmonização de fonte de verdade e lead válido (`30%` → `45%`)

Objetivo: alinhar Kommo, Sheets, WhatsApp e CRM sem contradição.

Tarefas:

- [x] atualizar `company/glossary.md` com lead estrutural, lead operacionalmente válido, Lead Real e Lead Fantasma;
- [x] harmonizar `playbooks/crm-reconciliation.md`;
- [x] harmonizar `integrations/google-sheets.md`;
- [x] revisar se `knowledge/company-brain/source-truth-rules.md` precisa ressalva curta;
- [x] garantir que dashboard seja sempre tratado como derivado.

Critério de pronto:

- nenhum documento central afirma genericamente que “lead criado no CRM = lead válido”;
- WhatsApp/CTWA exige filtro Lead Real/Fantasma;
- Kommo e Sheets têm papéis complementares e não concorrentes.

### Fase 3 — Política de dados e evidência (`45%` → `55%`)

Objetivo: impedir migração acidental de PII, exports brutos, tokens e ruído runtime.

Tarefas:

- [x] criar política central de dados/evidência;
- [x] decidir o papel de `history/` e `snapshots/`;
- [x] ajustar `.gitignore` se necessário;
- [x] marcar evidência datada em `integrations/google-sheets-operating-model.md` como pendência governada pela política.

Critério de pronto:

- existe política explícita de canon vs evidência curada vs dado bruto;
- repo continua sem secrets ou dados privados brutos.

### Fase 4 — Handoff e contratos mínimos (`55%` → `65%`)

Objetivo: tornar a colaboração entre subagents operacional, não só conceitual.

Tarefas:

- [x] criar `templates/handoff-subagente.md` em formato OpenClaw-native;
- [x] definir como handoffs preservam confiança, evidência, restrições e output esperado;
- [x] revisar referências dos subagents se necessário.

Critério de pronto:

- qualquer subagent consegue transferir contexto para outro sem perder evidência/confiança.

### Fase 5 — Evals mínimos (`65%` → `80%`)

Objetivo: impedir regressão dos comportamentos críticos herdados do legado.

Tarefas:

- [x] criar `evals/README.md`;
- [x] criar evals iniciais de Meta Ads;
- [x] criar evals iniciais de Dados/BI;
- [x] criar evals iniciais de SDR/Comercial;
- [x] criar evals iniciais de Copy;
- [x] criar evals iniciais de Competitive Intelligence.

Critério de pronto:

- existem cenários P0 que testam armadilhas centrais como CPL bom/fundo ruim, Lead Fantasma, dashboard divergente, SDR saudável e promessa proibida.

### Fase 6 — Schemas e workflows críticos (`80%` → `95%`)

Objetivo: recuperar contratos de input e workflows essenciais sem copiar o legado inteiro.

Tarefas:

- [x] criar schemas ou templates profundos para Meta campaign/creative;
- [x] criar schema de integridade de dados;
- [x] criar schema SDR;
- [x] criar schemas de copy prioritários;
- [x] criar tracking-stack checklist;
- [x] criar workflow de Lead Fantasma;
- [x] criar alert calibration / monitoring;
- [x] criar commercial reporting automation;
- [x] criar Kommo field mapping sanitizado.

Critério de pronto:

- os fluxos críticos podem ser executados com entrada/saída previsível;
- componentes históricos de stack não ficam esquecidos.

### Fase 7 — Revisão final e fechamento (`95%` → `100%`)

Objetivo: garantir que o repo está funcional como brain OpenClaw principal.

Tarefas:

- [x] revisar links e referências internas;
- [x] revisar duplicações de fonte de verdade;
- [x] verificar `git diff` final;
- [x] atualizar este progresso para `100%`;
- [ ] preparar commit/push se solicitado.

Critério de pronto:

- não há lacunas P0/P1 abertas;
- a migração está escrita para OpenClaw, não para Claude Code;
- legado permanece apenas como referência histórica, não dependência operacional.

### Fase 8 — Enriquecimento por revisão de cobertura total (`100%` mantido)

Objetivo: responder à revisão final do usuário sobre arquivos, pastas, informações e prompts do legado, garantindo que nenhum conhecimento migrável fique para trás.

Tarefas:

- [x] revisar cobertura de `.claude/commands`, `.claude/skills`, `.claude/rules`, prompts e templates;
- [x] revisar cobertura de `subagents/` incluindo skills, evals, data inputs, rules e knowledge;
- [x] revisar cobertura de `knowledge/`, `tools/`, `projects/`, `contexts/`, `archive/`, `history/`, `snapshots` e relatórios;
- [x] criar `MIGRATION_COVERAGE_REVIEW.md`;
- [x] criar playbooks ricos para auditoria Meta, Andromeda, A/B, Google Ads, mídia, forecast, comparação de períodos, onboarding, handoff comercial-operação, institucionalização e qualificação de lead;
- [x] criar templates e schemas correspondentes;
- [x] migrar CTWA/WhatsApp/n8n/CPL real/dashboard como especificação sanitizada;
- [x] migrar copy frameworks estendidos;
- [x] migrar evidência histórica curada e linhagem do design legado;
- [x] reforçar learning loop e memory governance.

Critério de pronto:

- todo conhecimento migrável identificado na revisão tem destino OpenClaw-native;
- exclusões são intencionais e documentadas;
- nenhuma dependência operacional permanece presa ao runtime Claude Code.

## Red lines

- não copiar o filesystem legado em massa;
- não migrar `everything-claude-code/`;
- não migrar `.mcp-servers/`;
- não versionar secrets, `.env`, service accounts, exports brutos, CSVs de clientes ou leads;
- não criar workflows enormes sem critério;
- não aumentar progresso por documentação bonita sem funcionalidade real.
