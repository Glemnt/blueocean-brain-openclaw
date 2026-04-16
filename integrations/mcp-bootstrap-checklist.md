# MCP Bootstrap Checklist

Checklist prático para sair da documentação e entrar na implantação real da camada MCP da Blue Ocean.

## Objetivo
Separar claramente:
- o que pode ser preparado sem dependência externa
- o que exige credenciais ou decisões do operador
- qual é a ordem exata para colocar o primeiro MCP no ar

## O que já está resolvido
- arquitetura alvo definida
- plano de reconstrução definido
- inventário técnico definido
- guia operacional documentado
- ordem inicial decidida: Google Sheets, depois Kommo, depois Meta Ads
- formato do `openclaw mcp set` confirmado: aceita um objeto JSON por servidor

## O que ainda falta para implantação real
### Google Sheets
Necessário obter ou confirmar:
- arquivo de service account do Google
- permissão da service account nas planilhas ou pasta correta
- `DRIVE_FOLDER_ID` se quisermos restringir o escopo inicial

### Kommo
Necessário obter ou confirmar:
- `KOMMO_TOKEN`
- `KOMMO_SUBDOMAIN`

### Meta Ads
Necessário decidir:
- rota `remote MCP` versus `self-hosted`

Se a rota for remote:
- token/API key compatível

Se a rota for self-hosted:
- credencial e modelo técnico compatíveis com o servidor adotado
- confirmação de que a opção escolhida cobre o uso Blue Ocean

## O que pode ser preparado antes das credenciais
### No host
- diretórios de runtime
- diretórios de log
- estrutura de environment files
- rascunhos de unit files
- comando `openclaw mcp set` para MCPs locais por processo

### No repo
- documentação de bootstrap e validação
- exemplos seguros sem segredos

## Primeira implantação recomendada
### Alvo
Google Sheets MCP

### Motivo
- menor atrito esperado
- credencial previsível
- bom primeiro teste da integração always-on
- menor risco de bloqueio por licenciamento ou auth complexo

## Sequência sugerida para Google Sheets
1. receber a credencial da service account
2. confirmar quais planilhas ou pasta devem ficar acessíveis
3. instalar `uv` no host, se necessário
4. validar subida manual do MCP
5. configurar o MCP no OpenClaw
6. validar leitura real de uma planilha conhecida
7. só então transformar em processo persistente, se necessário

## Sequência sugerida para Kommo
1. receber token e subdomínio
2. subir servidor em modo local
3. validar leitura de pipelines, leads e campos
4. registrar no OpenClaw
5. persistir com `systemd` ou outro modelo final

## Sequência sugerida para Meta Ads
1. fechar decisão de rota
2. testar leitura mínima de contas e campanhas
3. validar aderência às leituras críticas da Blue Ocean
4. integrar no OpenClaw
5. só então considerar pronto

## Princípio de implantação
Não subir toda a stack de uma vez.

Subir um MCP, validar, integrar, testar em uso real, depois avançar.

## Próxima pergunta operacional certa
Para sair do papel e entrar na primeira implantação, a primeira peça realmente necessária é:
- a credencial da service account do Google Sheets

Sem isso, ainda podemos preparar estrutura, mas não concluir a primeira prova de vida.
