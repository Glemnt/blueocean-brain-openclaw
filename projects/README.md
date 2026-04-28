# Projects

Blueprints de projetos estruturais que atravessam várias camadas do brain.

## Papel

`projects/` guarda iniciativas com arquitetura, fases, critérios de aceite e dependências. Um projeto pode apontar para playbooks, integrations, schemas e templates, mas não substitui essas camadas.

## Quando criar um projeto

Criar quando a iniciativa:

- envolve múltiplas fontes ou áreas;
- precisa de fases e critérios de aceite;
- combina operação, dados, stack e governança;
- não cabe como playbook único.

## Regras

- Não colocar segredo ou export bruto.
- Documentar objetivo, arquitetura, fases, owners e critérios de aceite.
- Apontar para os arquivos canônicos relacionados.
- Quando o projeto virar rotina estável, promover o fluxo para `playbooks/` ou `knowledge/workflows/`.
