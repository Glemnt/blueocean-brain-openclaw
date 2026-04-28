# Data and Evidence Policy

Política canônica para separar canon, evidência curada, memória local, exports brutos e dados sensíveis no `blueocean-brain-openclaw`.

## Princípio central

O brain deve aprender com evidência real sem transformar o repositório em depósito de dados privados, exports crus ou ruído de runtime.

A regra é:

- canon durável entra no repo;
- evidência só entra se estiver curada, datada e sanitizada;
- dados brutos, PII, secrets e logs operacionais ficam fora do repo versionado.

## Categorias

### 1. Canon versionado

Conteúdo estável que orienta o comportamento do brain.

Destinos típicos:

- `company/`
- `governance/`
- `knowledge/`
- `playbooks/`
- `subagents/`
- `integrations/`
- `templates/`
- `schemas/`, se existir
- `evals/`, se existir

Pode conter:

- princípios;
- definições;
- regras de fonte de verdade;
- playbooks;
- workflows reutilizáveis;
- critérios de confiança;
- schemas sem dados reais sensíveis;
- exemplos fictícios ou sanitizados.

### 2. Evidência curada

Resumo ou recorte sanitizado usado para explicar por que uma regra existe.

Pode entrar no repo se cumprir todos os critérios:

- tem data ou período;
- tem escopo claro;
- não contém PII bruta;
- não contém tokens, segredos ou credenciais;
- não contém payloads completos de leads/clientes;
- separa fato observado de interpretação;
- declara limites de confiança.

Destinos possíveis:

- `history/` para evidência histórica curada;
- `knowledge/` quando o aprendizado já virou referência recorrente;
- `reports/` apenas se houver política explícita de exceção no `.gitignore`.

Exemplos bons:

- síntese datada de falha de stack;
- resumo agregado de auditoria de Sheets;
- lições aprendidas de CTWA sem leads reais;
- evidência de padrão diagnóstico sem dados pessoais.

### 3. Memória local e rascunho operacional

Conteúdo útil para operar agora, mas não pronto para canon.

Exemplos:

- rascunhos;
- snapshots intermediários;
- notas de sessão;
- relatórios temporários;
- dumps locais para investigação.

Regra:

- pode existir localmente;
- deve ficar fora do Git;
- se virar aprendizado recorrente, deve ser promovido como canon ou evidência curada.

### 4. Dados brutos e sensíveis

Nunca devem entrar no repo versionado.

Inclui:

- `.env`, `.env.*`, OAuth tokens, service account JSON;
- CSVs/TSVs de clientes ou leads;
- listas de audiência;
- exports completos de Kommo, Meta, Sheets, Autentique ou n8n;
- nomes, emails, telefones e documentos em massa;
- payloads de webhooks;
- logs com dados identificáveis;
- screenshots com PII;
- contratos, propostas ou documentos privados sem sanitização;
- caches de scraping ou creative library com identificadores brutos;
- vendor/runtime como `.mcp-servers/` ou `everything-claude-code/`.

## Red lines

Nunca:

- commitar secrets;
- commitar base de leads/clientes;
- commitar export bruto com PII;
- usar evidência datada como canon sem revisão;
- copiar diretórios legados inteiros por conveniência;
- publicar dados sensíveis para “facilitar análise”.

## Como sanitizar evidência

Antes de versionar qualquer evidência:

1. remover nomes pessoais, emails, telefones e documentos;
2. remover IDs sensíveis quando não forem indispensáveis;
3. trocar exemplos reais por exemplos fictícios quando possível;
4. agregar métricas para reduzir risco de reidentificação;
5. deixar claro o período analisado;
6. declarar a fonte de forma genérica quando o detalhe expõe dado privado;
7. registrar limitações e confiança.

## Relação com diretórios históricos

### `history/`

Pode ser usado para evidência curada e datada.

Não deve receber dumps brutos.

### `reports/`, `sessions/`, `archive/`, `snapshots/`

Por padrão, são tratados como áreas locais/runtime ou de rascunho e devem permanecer fora do Git, salvo exceção explícita e sanitizada.

Se uma informação dessas áreas precisar ensinar o brain, promova um resumo sanitizado para `history/`, `knowledge/`, `playbooks/` ou `integrations/`.

## Relação com `.gitignore`

O `.gitignore` deve proteger:

- secrets;
- logs;
- caches;
- runtime local;
- reports/sessions/archive/snapshots brutos.

Ignorar esses diretórios não significa perder inteligência. Significa exigir curadoria antes de versionar.

## Critério final

Antes de adicionar um arquivo ao repo, perguntar:

1. Isso é canon, evidência curada ou dado bruto?
2. Contém PII, secrets ou payloads reais?
3. Ajuda o brain de forma recorrente?
4. Está escrito para OpenClaw, sem dependência do runtime legado?
5. Se alguém ler isso daqui a meses, vai entender o escopo e a confiança?

Se qualquer resposta expuser risco, não versionar ainda.


## Gate pré-commit recomendado

Antes de versionar mudanças relevantes, usar:

```bash
python3 scripts/repo_safety_scan.py
python3 scripts/eval_harness.py
```

O scan é conservador. Se houver falso positivo, documentar a justificativa ou ajustar a sanitização antes do commit.

Checklist humano complementar: `security/pre-commit-safety-checklist.md`.
