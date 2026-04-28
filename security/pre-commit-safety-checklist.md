# Checklist de Segurança Pré-Commit

Use antes de commitar/pushar mudanças do Blue Ocean Brain.

## 1. Escopo

- [ ] O diff é intencional?
- [ ] Não há cópia em massa do legado?
- [ ] Arquivos protegidos modificados foram revisados conscientemente?
- [ ] Novos arquivos têm destino correto por camada?

## 2. Dados sensíveis

- [ ] Sem `.env`, token, service account, chave privada ou payload real.
- [ ] Sem CSV/TSV/XLSX/PDF/HTML/JSON bruto.
- [ ] Sem nomes, emails, telefones, documentos ou listas de leads/clientes.
- [ ] Evidência histórica está sanitizada e datada.

## 3. OpenClaw-native

- [ ] Não depende de `.claude/`, slash-command ou MCP local antigo para operar.
- [ ] Prompts antigos viraram canon/playbook/schema/template, não system prompt colado.
- [ ] Integrações vivas ficam fora do repo quando exigem segredo.

## 4. Qualidade

- [ ] `python3 scripts/eval_harness.py` passa.
- [ ] `python3 scripts/repo_safety_scan.py` passa ou achados foram justificados.
- [ ] Checagem de links/referências passa.
- [ ] `git diff --check` passa.

## 5. Decisão

Se qualquer item crítico falhar, não commitar. Corrigir, sanitizar ou mover para área local ignorada.
