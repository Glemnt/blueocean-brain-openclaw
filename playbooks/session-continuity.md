# Continuidade de Sessão

## Objetivo

Preservar contexto operacional entre sessões sem depender de memória efêmera, prompts gigantes ou arquivos crus sensíveis.

## Quando usar

Use quando:

- uma análise longa será interrompida;
- há múltiplos subagents ou handoffs;
- existe auditoria, projeto ou análise longa em andamento;
- há decisões e lacunas que precisam sobreviver à troca de sessão;
- o usuário pede para continuar depois.

## O que registrar

### Estado mínimo

- objetivo atual;
- caminho/repo/arquivos envolvidos;
- decisões tomadas;
- próximos passos;
- bloqueios;
- arquivos modificados;
- validações já rodadas;
- confiança e lacunas.

### O que não registrar

- PII;
- tokens;
- payloads brutos;
- dumps completos;
- conversa privada irrelevante;
- logs sensíveis.

## Onde registrar

| Tipo | Destino |
|---|---|
| Continuidade temporária local | memória local / nota de sessão fora do git |
| Auditoria ou projeto versionável | tracker explícito do projeto ou auditoria |
| Evidência histórica curada | `history/` |
| Handoff entre especialistas | `templates/handoff-subagente.md` |
| Status executivo curto | `templates/status-snapshot.md` |
| Aprendizado recorrente | canon em `company/`, `governance/`, `knowledge/`, `playbooks/` ou `integrations/` |

## Formato de checkpoint

```markdown
## Checkpoint — [frente]

**Data:** [YYYY-MM-DD]
**Objetivo:**
**Status:** não iniciado / em andamento / bloqueado / concluído
**Confiança:** Alta / Parcial / Frágil / Insuficiente

### Feito
- 

### Decisões
- 

### Arquivos tocados
- 

### Validações
- 

### Lacunas / bloqueios
- 

### Próxima ação
- 
```

## Regra de retomada

Ao retomar:

1. Ler o checkpoint mais recente.
2. Verificar `git status` ou estado dos arquivos.
3. Validar se alguma fonte viva mudou.
4. Reconfirmar confiança.
5. Continuar do próximo passo, não refazer tudo sem motivo.

## Red lines

- Não usar histórico antigo como dado atual.
- Não versionar raw data para “facilitar continuidade”.
- Não esconder decisão pendente como se estivesse concluída.
- Não elevar confiança só porque o resumo está bem escrito.
