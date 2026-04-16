# Integrations

Documentação das integrações reais do ecossistema Blue Ocean.

Esta pasta existe para registrar como cada integração deve ser entendida dentro da arquitetura do brain.

## Papel desta camada
Cada integração documentada aqui deve esclarecer:
- finalidade operacional
- fonte de verdade por tipo de dado
- fragilidades conhecidas
- riscos de leitura incorreta
- limites de uso pelo agente principal e pelos especialistas

## Integrações atuais
- `meta-ads.md`
- `kommo.md`
- `google-sheets.md`
- `google-sheets-setup.md`
- `n8n.md`
- `apify.md`
- `mcp-architecture.md`
- `mcp-rebuild-plan.md`
- `mcp-deployment-inventory.md`
- `mcp-operator-guide.md`
- `mcp-bootstrap-checklist.md`

## Regra de qualidade
Documentar uma integração não é só listar campos.

Também deve ficar claro:
- o que essa integração sabe de forma confiável
- o que ela não sabe
- quando ela é fonte primária
- quando ela é derivada
- quais erros comuns de interpretação ela pode induzir
