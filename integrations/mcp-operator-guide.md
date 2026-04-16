# MCP Operator Guide

Guia operacional para implantar, sustentar e validar a camada MCP da Blue Ocean no host do OpenClaw.

## Objetivo
Sair da fase de desenho e deixar um caminho claro para implantação real de:
- Google Sheets MCP
- Kommo MCP
- Meta Ads MCP

## Princípios operacionais
- infraestrutura do brain deve ficar no servidor, não no laptop
- segredos nunca entram no repositório público
- cada serviço precisa de prova de vida antes da integração com o OpenClaw
- quando houver dúvida entre elegância e confiabilidade, escolher confiabilidade

## Estrutura recomendada no host
Exemplo de organização fora do repositório público:

```bash
/opt/blueocean-mcp/
  google-sheets/
  kommo/
  meta-ads/

/etc/blueocean-mcp/
  google-sheets.env
  kommo.env
  meta-ads.env

/var/log/blueocean-mcp/
  google-sheets.log
  kommo.log
  meta-ads.log
```

## 1. Google Sheets MCP
### Instalação sugerida
Pré-requisito:
- `uv` instalado no host
- credencial de service account válida
- planilhas compartilhadas com o e-mail da service account

### Arquivo de ambiente sugerido
`/etc/blueocean-mcp/google-sheets.env`

```bash
SERVICE_ACCOUNT_PATH=/etc/blueocean-mcp/google-service-account.json
DRIVE_FOLDER_ID=SEU_FOLDER_ID
ENABLED_TOOLS=list_spreadsheets,list_sheets,get_sheet_data,update_cells,get_multiple_sheet_data
```

### Unit file sugerido
`/etc/systemd/system/blueocean-google-sheets-mcp.service`

```ini
[Unit]
Description=Blue Ocean Google Sheets MCP
After=network.target

[Service]
Type=simple
EnvironmentFile=/etc/blueocean-mcp/google-sheets.env
ExecStart=/usr/local/bin/uvx mcp-google-sheets@latest
Restart=always
RestartSec=5
WorkingDirectory=/opt/blueocean-mcp/google-sheets
StandardOutput=append:/var/log/blueocean-mcp/google-sheets.log
StandardError=append:/var/log/blueocean-mcp/google-sheets.log

[Install]
WantedBy=multi-user.target
```

### Observação importante
Se preferir explicitar o filtro por argumento em vez de env var:

```ini
ExecStart=/usr/local/bin/uvx mcp-google-sheets@latest --include-tools list_spreadsheets,list_sheets,get_sheet_data,update_cells,get_multiple_sheet_data
```

### Validação inicial
Validar que o processo sobe sem erro de autenticação.

Depois validar com cliente MCP:
- listar planilhas
- listar abas
- ler um intervalo conhecido

## 2. Kommo MCP
### Instalação sugerida
Pré-requisito:
- Python 3.10+
- token de longo prazo do Kommo
- subdomínio correto

### Estrutura sugerida
```bash
cd /opt/blueocean-mcp
python3 -m venv kommo/.venv
source kommo/.venv/bin/activate
pip install fastmcp httpx pydantic
# copiar server.py validado para /opt/blueocean-mcp/kommo/server.py
```

### Arquivo de ambiente sugerido
`/etc/blueocean-mcp/kommo.env`

```bash
KOMMO_TOKEN=SEU_TOKEN_KOMMO
KOMMO_SUBDOMAIN=comercialblueocean
```

### Unit file sugerido, modo inicial
`/etc/systemd/system/blueocean-kommo-mcp.service`

```ini
[Unit]
Description=Blue Ocean Kommo MCP
After=network.target

[Service]
Type=simple
EnvironmentFile=/etc/blueocean-mcp/kommo.env
WorkingDirectory=/opt/blueocean-mcp/kommo
ExecStart=/opt/blueocean-mcp/kommo/.venv/bin/python /opt/blueocean-mcp/kommo/server.py
Restart=always
RestartSec=5
StandardOutput=append:/var/log/blueocean-mcp/kommo.log
StandardError=append:/var/log/blueocean-mcp/kommo.log

[Install]
WantedBy=multi-user.target
```

### Observação operacional
O candidato atual parece rodar naturalmente em `stdio`.
Isso significa que há duas abordagens válidas:
- usar esse MCP como processo local comandado pelo cliente
- ou adaptar depois para HTTP, se a operação pedir padronização total

Para retorno rápido de capacidade, a primeira opção pode ser suficiente.

### Validação inicial
Validar que o processo sobe sem erro de env vars.

Depois validar com cliente MCP:
- listar pipelines
- listar leads recentes
- listar custom fields
- identificar usuários responsáveis

## 3. Meta Ads MCP
### Decisão pendente
Aqui ainda existe uma decisão arquitetural real:
- usar o Remote MCP do Pipeboard
- ou usar/self-host uma variante local

### Recomendação atual
Não fechar a implantação de Meta antes de esclarecer:
- modelo de autenticação real
- custo e dependência aceitáveis
- aderência aos dados necessários para Blue Ocean
- implicações de licenciamento e operação

### Se a rota escolhida for self-hosted
Arquivo de ambiente sugerido:
`/etc/blueocean-mcp/meta-ads.env`

```bash
PIPEBOARD_API_TOKEN=SEU_TOKEN
```

Unit file ilustrativo:
`/etc/systemd/system/blueocean-meta-ads-mcp.service`

```ini
[Unit]
Description=Blue Ocean Meta Ads MCP
After=network.target

[Service]
Type=simple
EnvironmentFile=/etc/blueocean-mcp/meta-ads.env
WorkingDirectory=/opt/blueocean-mcp/meta-ads
ExecStart=/opt/blueocean-mcp/meta-ads/.venv/bin/python -m meta_ads_mcp --transport streamable-http --host 127.0.0.1 --port 3002
Restart=always
RestartSec=5
StandardOutput=append:/var/log/blueocean-mcp/meta-ads.log
StandardError=append:/var/log/blueocean-mcp/meta-ads.log

[Install]
WantedBy=multi-user.target
```

### Se a rota escolhida for remote MCP
O serviço local pode nem ser necessário. Nesse caso, a integração seria feita diretamente na configuração MCP do OpenClaw usando a URL remota e a forma de autenticação suportada.

### Validação inicial
Validar que conseguimos:
- listar contas
- listar campanhas
- ler insights
- validar leitura útil para estrutura, criativos e sinais de performance

## Comandos de ciclo de vida no servidor
### Recarregar units
```bash
sudo systemctl daemon-reload
```

### Habilitar no boot
```bash
sudo systemctl enable blueocean-google-sheets-mcp
sudo systemctl enable blueocean-kommo-mcp
sudo systemctl enable blueocean-meta-ads-mcp
```

### Subir serviços
```bash
sudo systemctl start blueocean-google-sheets-mcp
sudo systemctl start blueocean-kommo-mcp
sudo systemctl start blueocean-meta-ads-mcp
```

### Ver status
```bash
sudo systemctl status blueocean-google-sheets-mcp
sudo systemctl status blueocean-kommo-mcp
sudo systemctl status blueocean-meta-ads-mcp
```

### Ler logs
```bash
tail -n 100 /var/log/blueocean-mcp/google-sheets.log
tail -n 100 /var/log/blueocean-mcp/kommo.log
tail -n 100 /var/log/blueocean-mcp/meta-ads.log
```

## Integração com OpenClaw
### Estado atual
Hoje o OpenClaw está sem MCPs configurados.

### Estratégia recomendada
Configurar só depois que cada serviço passar na prova de vida local.

### Fluxo sugerido
1. subir serviço
2. validar localmente
3. registrar no OpenClaw
4. testar listagem
5. testar uso real pelo agente

### Comandos de referência
Listar MCPs atuais:
```bash
openclaw mcp list
```

Ver configuração atual:
```bash
openclaw mcp show
```

### Observação importante
O formato exato do `openclaw mcp set` deve ser validado no momento da configuração real, para respeitar o schema aceito pela versão do host.

## Critério de pronto por fase
### Fase 1, prova de vida
Cada MCP sobe sem erro de credencial ou runtime.

### Fase 2, integração OpenClaw
O OpenClaw consegue enxergar e usar o MCP correspondente.

### Fase 3, validação operacional
O agente consegue responder uma análise real usando a fonte live.

## Ordem prática recomendada
1. Google Sheets
2. Kommo
3. Meta Ads
4. cruzamento dos três no OpenClaw

## Regra final
Não considerar a restauração concluída só porque o processo está rodando.

Só estará realmente concluída quando o agente conseguir cruzar mídia, CRM e planilha em uma análise real com evidência forte o suficiente para orientar decisão operacional.
