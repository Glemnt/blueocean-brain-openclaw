# Robustness Hardening Log

Registro das correções feitas após a auditoria de robustez.

## Rodada 1 — robustez infra

Correções:

- `history/README.md`
- `projects/README.md`
- atualização do `README.md` raiz
- `INFRA_ROBUSTNESS_AUDIT.md`

## Rodada 2 — camadas rasas virando robustas

Problemas rasos identificados:

- navegação por pergunta ainda dependia dos READMEs gerais;
- evals eram apenas Markdown conceitual;
- segurança pré-commit não tinha checklist/script próprio;
- integrações vivas tinham docs de arquitetura, mas faltava plano explícito de validação operacional;
- P2 de volume documental exigia guia operacional.

Correções aplicadas:

- `OPERATOR_GUIDE.md`
- `REPO_INDEX_BY_QUESTION.md`
- `evals/eval-manifest.md`
- `scripts/eval_harness.py`
- `security/README.md`
- `security/pre-commit-safety-checklist.md`
- `scripts/repo_safety_scan.py`
- `integrations/live-integration-validation.md`
- `integrations/validation/README.md`

Resultado esperado:

- arquitetura mais navegável;
- domínio mais acionável por pergunta;
- evals estruturalmente verificáveis;
- segurança com gate pré-commit;
- integração viva com checklist de prova de vida.
