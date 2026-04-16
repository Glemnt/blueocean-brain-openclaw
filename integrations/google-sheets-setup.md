# Google Sheets MCP Setup

Passo a passo operacional para configurar o Google Sheets MCP da Blue Ocean do zero no ambiente atual.

## Objetivo
Restaurar o acesso live a planilhas operacionais no OpenClaw via MCP, usando uma configuração limpa, sempre disponível e independente de máquina local.

## Visão geral
Fluxo recomendado:
1. criar projeto no Google Cloud
2. habilitar Google Sheets API e Google Drive API
3. criar service account
4. gerar chave JSON
5. compartilhar as planilhas com a service account
6. copiar a chave para o host do OpenClaw
7. registrar o MCP no OpenClaw
8. validar leitura real

## 1. Criar projeto no Google Cloud
Acesse:
- `https://console.cloud.google.com/`

Depois:
- criar novo projeto, por exemplo `blueocean-mcp`
- selecionar esse projeto antes dos próximos passos

## 2. Habilitar APIs necessárias
No projeto, habilitar:
- `Google Sheets API`
- `Google Drive API`

Caminho:
- `APIs & Services` → `Library`

## 3. Criar service account
Caminho:
- `IAM & Admin` → `Service Accounts` → `Create Service Account`

Sugestão:
- Nome: `blueocean-sheets-mcp`
- Descrição: `Service account for Blue Ocean Google Sheets MCP`

Não é necessário dar papéis amplos no projeto para o caso básico de acesso a planilhas compartilhadas diretamente com a conta.

## 4. Gerar chave JSON
Dentro da service account:
- abrir aba `Keys`
- `Add key` → `Create new key`
- escolher `JSON`

O Google vai baixar um arquivo JSON.

## 5. Descobrir o client email da service account
Abrir o JSON e localizar o campo:
- `client_email`

Esse é o endereço que deve receber acesso às planilhas ou à pasta compartilhada no Google Drive.

## 6. Compartilhar planilhas com a service account
No Google Sheets ou Google Drive:
- abrir a planilha ou pasta relevante
- clicar em `Compartilhar`
- adicionar o `client_email` da service account
- dar permissão de:
  - `Leitor`, se quiser só leitura
  - `Editor`, se quiser escrita também

## 7. Descobrir o DRIVE_FOLDER_ID, opcional
Se quiser restringir a busca do MCP a uma pasta específica do Drive:
- abrir a pasta no navegador
- copiar o ID da URL

Exemplo:
- URL: `https://drive.google.com/drive/folders/ABC123XYZ`
- `DRIVE_FOLDER_ID=ABC123XYZ`

Esse campo é opcional.

## 8. Copiar a chave JSON para o host
Sugestão de local:
- `/etc/blueocean-mcp/google-service-account.json`

Criar diretório seguro:

```bash
sudo mkdir -p /etc/blueocean-mcp
sudo chown root:root /etc/blueocean-mcp
sudo chmod 700 /etc/blueocean-mcp
```

Copiar o arquivo para esse caminho e ajustar permissão:

```bash
sudo chmod 600 /etc/blueocean-mcp/google-service-account.json
```

## 9. Instalar uv no host, se necessário
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Depois verificar:

```bash
uv --version
uvx --version
```

## 10. Testar o MCP manualmente
Exportar variáveis de ambiente:

```bash
export SERVICE_ACCOUNT_PATH=/etc/blueocean-mcp/google-service-account.json
export ENABLED_TOOLS=list_spreadsheets,list_sheets,get_sheet_data,update_cells,get_multiple_sheet_data
```

Se quiser limitar a uma pasta:

```bash
export DRIVE_FOLDER_ID=SEU_FOLDER_ID
```

Executar:

```bash
uvx mcp-google-sheets@latest
```

Se subir sem erro, a configuração base está correta.

## 11. Registrar no OpenClaw
Exemplo de configuração:

```bash
openclaw mcp set google-sheets '{
  "command": "uvx",
  "args": ["mcp-google-sheets@latest"],
  "env": {
    "SERVICE_ACCOUNT_PATH": "/etc/blueocean-mcp/google-service-account.json",
    "ENABLED_TOOLS": "list_spreadsheets,list_sheets,get_sheet_data,update_cells,get_multiple_sheet_data",
    "DRIVE_FOLDER_ID": "SEU_FOLDER_ID"
  }
}'
```

Se não quiser restringir por pasta, remover `DRIVE_FOLDER_ID`.

## 12. Validar no OpenClaw
Executar:

```bash
openclaw mcp list
openclaw mcp show google-sheets
```

Depois validar leitura real com:
- listagem de planilhas
- leitura de aba conhecida
- leitura de intervalo conhecido

## Critério de pronto
O Google Sheets MCP só deve ser considerado pronto quando:
- o OpenClaw enxergar o MCP configurado
- uma planilha real puder ser listada
- uma aba real puder ser lida sem erro
- o agente conseguir usar esses dados numa análise operacional real

## Observações
- não salvar o JSON no repositório público
- preferir começar com poucas ferramentas habilitadas
- ampliar escopo só quando houver necessidade real
