# Kommo MCP Setup

Passo a passo operacional para configurar o Kommo MCP da Blue Ocean no ambiente atual, com foco inicial em auditoria e comparação, não em autoridade automática do CRM.

## Objetivo
Conectar Kommo ao OpenClaw para que o agente consiga:
- ler pipelines, leads, usuários e campos customizados
- auditar integridade do CRM contra as planilhas
- medir o quanto Kommo hoje é utilizável como fonte operacional real

## Princípio importante
No estado atual da Blue Ocean, Kommo não entra como verdade superior por padrão.

A integração inicial deve servir para:
- auditoria
- comparação
- validação de preenchimento
- leitura de entidade viva onde houver integridade suficiente

## O que será necessário
### 1. Subdomínio da conta Kommo
Exemplo:
- se a URL é `https://comercialblueocean.kommo.com`, então:
- `KOMMO_SUBDOMAIN=comercialblueocean`

### 2. Token de longo prazo
Caminho típico no Kommo:
- Configurações
- Integrações / API
- chave ou token de longo prazo

O nome exato pode variar, mas precisamos de um token que permita leitura da API v4.

## Estratégia recomendada
### Fase 1. Registrar no OpenClaw como MCP local comandado por processo
Como o candidato atual parece pensado para `stdio`, a forma mais rápida de recuperar utilidade é usar o servidor local como comando MCP.

### Fase 2. Validar leituras reais
Testar:
- pipelines
- leads recentes
- usuários responsáveis
- custom fields

### Fase 3. Medir confiabilidade
Comparar Kommo com:
- `CONTROLE DE LEADS GERAL`
- `Planilha Comercial x Marketing V.2`

## Estrutura local sugerida no host
```bash
mkdir -p /opt/blueocean-mcp/kommo
cd /opt/blueocean-mcp/kommo
python3 -m venv .venv
source .venv/bin/activate
pip install fastmcp httpx pydantic
```

Depois copiar ou reconstruir um `server.py` equivalente ao MCP escolhido.

## Arquivo de ambiente sugerido
Exemplo:
- `/etc/blueocean-mcp/kommo.env`

Conteúdo:
```bash
KOMMO_TOKEN=SEU_TOKEN
KOMMO_SUBDOMAIN=comercialblueocean
```

## Registro MCP no OpenClaw, modelo conceitual
Como o `openclaw mcp set` aceita objeto JSON por servidor, o formato alvo será algo nesta linha:

```bash
openclaw mcp set kommo '{
  "command": "/opt/blueocean-mcp/kommo/.venv/bin/python",
  "args": ["/opt/blueocean-mcp/kommo/server.py"],
  "env": {
    "KOMMO_TOKEN": "SEU_TOKEN",
    "KOMMO_SUBDOMAIN": "comercialblueocean"
  }
}'
```

## Validação inicial esperada
Após configurar:
- `openclaw mcp list`
- `openclaw mcp show kommo`

E depois testes reais de leitura.

## O que observar na auditoria
Quando Kommo estiver de pé, o objetivo não é apenas perguntar se conecta.

Queremos medir:
- se os leads relevantes existem no CRM
- se `responsible_user_id` e equivalentes batem com SDRs reais
- se campos customizados úteis existem e estão preenchidos
- se o volume e integridade de preenchimento sustentam uso analítico
- se a ponte entre marketing, CRM e planilhas fecha ou se quebra

## Critério de pronto
Kommo MCP só deve ser considerado pronto para o uso do brain quando:
- conectar e ler entidades reais
- expor pipelines, leads, usuários e campos customizados com consistência
- permitir auditoria comparativa contra as planilhas
- deixar claro o que já é confiável e o que ainda é frágil

## Próximo passo operacional
Antes de executar a configuração, precisamos confirmar:
- `KOMMO_SUBDOMAIN`
- disponibilidade do token de longo prazo

Sem isso, não vale avançar para o deploy real.
