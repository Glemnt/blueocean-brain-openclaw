# Validação de Integrações Vivas

Este documento transforma o risco externo da auditoria — MCPs/n8n/Sheets/Kommo vivos — em plano verificável.

## Objetivo

Garantir que o brain não seja apenas documental: as integrações reais precisam provar leitura, escrita autorizada, logs, alertas e segurança.

## Camadas

1. Configuração segura.
2. Prova de vida.
3. Leitura mínima.
4. Escrita controlada, quando aplicável.
5. Reconciliação entre fontes.
6. Monitoramento e alertas.

## Google Sheets

### Prova de vida

- listar planilhas permitidas;
- listar abas;
- ler intervalo conhecido;
- escrever apenas em aba de teste/autorizada.

### Critérios de aceite

- service account sem acesso amplo demais;
- ranges documentados;
- erro de permissão é explícito;
- update_cells só em ranges permitidos.

## Kommo

### Prova de vida

- listar pipelines;
- listar statuses;
- listar custom fields;
- buscar lead de teste/sanitizado;
- criar nota/tarefa apenas com confirmação explícita.

### Critérios de aceite

- token fora do repo;
- rate limit respeitado;
- campos críticos mapeados;
- escrita sempre confirmada.

## Meta Ads

### Prova de vida

- listar contas acessíveis;
- listar campanhas;
- ler insights por período curto;
- ler estrutura campanha/adset/ad;
- validar gasto e leads/conversas contra interface conhecida.

### Critérios de aceite

- sem escopo excessivo;
- sem escrita em campanha sem autorização;
- erro de token/permissão documentado;
- dados suficientes para `schemas/meta-campaign.md`.

## n8n

### Prova de vida

- verificar workflows ativos;
- testar webhook em ambiente seguro;
- verificar logs de erro;
- validar fluxo CTWA com evento fictício;
- validar fluxo CPL real com dados simulados.

### Critérios de aceite

- credenciais fora do repo;
- error handler ativo;
- logs sem PII em locais versionados;
- falha gera alerta.

## Dashboard/Sheets Comercial

### Prova de vida

- fórmula de CPL plataforma;
- fórmula de CPL real;
- CPAg/CPR;
- divergência >20%;
- denominador zero.

### Critérios de aceite

- células vazias não viram zero sem regra;
- dashboard explicita confiança;
- origem de cada métrica é rastreável.

## Resultado esperado da validação

Para cada integração, registrar:

```markdown
## Validação — [integração]

Data:
Owner:
Ambiente:
Status: aprovado / aprovado com ressalvas / reprovado
Provas executadas:
Falhas:
Riscos:
Próxima ação:
Confiança:
```

## Red lines

- Não testar com lead real sensível em arquivo versionado.
- Não expor token em log.
- Não habilitar escrita ampla por conveniência.
- Não considerar integração pronta sem prova de erro/alerta.
