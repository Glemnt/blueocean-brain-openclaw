# MCP Deployment Inventory

Inventário técnico para implantação da camada MCP always-on da Blue Ocean no host do OpenClaw.

## Objetivo
Traduzir a estratégia de reconstrução em um plano de execução por serviço, com foco em:
- runtime
- dependências
- variáveis de ambiente
- comando de execução
- healthcheck
- encaixe no OpenClaw

## Premissas operacionais
- os serviços devem rodar no mesmo host do OpenClaw, salvo necessidade futura real
- preferir bind em `127.0.0.1`
- preferir `systemd` para sustentação do processo
- credenciais ficam fora do repositório público
- validar cada MCP isoladamente antes de integrar no OpenClaw

## 1. Google Sheets MCP
### Candidato atual
- `xing5/mcp-google-sheets`

### Leitura de adequação
Bom candidato para primeira restauração porque:
- escopo de leitura e escrita é suficiente para a camada operacional derivada
- autenticação por service account é previsível
- pode ser reduzido por tool filtering para economizar contexto

### Runtime recomendado
- Python/`uvx`
- execução no host local
- preferencialmente encapsulado por `systemd`

### Dependências
- `uv` instalado no host
- credencial de service account do Google Cloud
- APIs Google Drive e Google Sheets habilitadas

### Variáveis de ambiente mínimas
- `SERVICE_ACCOUNT_PATH`
- `DRIVE_FOLDER_ID` (se quiser restringir navegação a uma pasta operacional)

### Ferramentas recomendadas para habilitar primeiro
Para reduzir ruído/contexto, começar apenas com:
- `list_spreadsheets`
- `list_sheets`
- `get_sheet_data`
- `update_cells`
- `get_multiple_sheet_data`

### Comando inicial sugerido
```bash
uvx mcp-google-sheets@latest --include-tools list_spreadsheets,list_sheets,get_sheet_data,update_cells,get_multiple_sheet_data
```

### Healthcheck prático
Validar via MCP:
- listar planilhas
- listar abas de uma planilha conhecida
- ler intervalo controlado

### Riscos principais
- service account sem acesso às planilhas reais
- excesso de ferramentas habilitadas consumindo contexto à toa
- Drive folder mal definido restringindo demais ou de menos a busca

### Status de prontidão atual
Alto potencial de implantação rápida.

## 2. Kommo MCP
### Candidato atual
- `NatrixAi/kommo-mcp`

### Leitura de adequação
Bom candidato para restauração inicial porque:
- cobre leads, pipelines, usuários, custom fields, tarefas, tags e eventos
- autenticação parece simples
- atende bem a primeira camada de reconciliação e leitura operacional

### Runtime recomendado
- Python
- ambiente virtual dedicado no host
- `systemd` para persistência

### Dependências
Arquivo de requirements observado:
- `fastmcp>=0.4.0`
- `httpx>=0.27.0`
- `pydantic>=2.0.0`

### Variáveis de ambiente mínimas
- `KOMMO_TOKEN`
- `KOMMO_SUBDOMAIN`

### Comando inicial sugerido
A implementação encontrada hoje parece pensada em `stdio`, então há duas rotas possíveis:

#### Rota A, adaptação leve para HTTP MCP
Criar uma camada de execução HTTP sobre o servidor atual para encaixar no padrão dos outros serviços.

#### Rota B, stdio gerenciado pelo próprio OpenClaw
Usar o servidor como comando local gerenciado pelo OpenClaw, se isso simplificar a primeira restauração.

### Recomendação atual
Se o OpenClaw aceitar bem esse MCP como processo local comandado por configuração, essa pode ser a forma mais rápida de voltar a ter leitura live de Kommo.

Se quisermos máxima simetria operacional entre todos os MCPs, vale adaptar para HTTP local depois.

### Healthcheck prático
Validar via MCP:
- listar pipelines
- listar leads recentes
- listar custom fields
- identificar responsible users

### Riscos principais
- permissões insuficientes do token
- respostas boas para CRUD, mas superficiais demais para leitura analítica mais refinada
- eventual necessidade de filtros mais específicos da operação Blue Ocean

### Status de prontidão atual
Boa chance de recuperação rápida para leitura operacional.

## 3. Meta Ads MCP
### Candidato atual
- `pipeboard-co/meta-ads-mcp`

### Leitura de adequação
É o candidato mais forte em amplitude funcional, mas também o mais sensível do ponto de vista de autenticação e modelo de serviço.

### Ponto técnico importante
A documentação encontrada mostra duas possibilidades:
- uso do remote MCP do Pipeboard
- self-hosted em `streamable-http`

Mas o modo self-hosted descrito depende fortemente de credenciais e modelo do projeto Pipeboard.

### Runtime recomendado
Há duas rotas plausíveis:

#### Rota A, Remote MCP do fornecedor
Mais rápida para recuperar capacidade, desde que:
- aceite bem o modelo de segurança
- custo/dependência externa sejam aceitáveis
- cubra as leituras específicas da Blue Ocean

#### Rota B, self-hosted local
Mais alinhada ao controle do stack, mas exige confirmar:
- como autenticar sem atrito
- se o projeto é realmente apropriado para self-hosting operacional contínuo
- se o licenciamento e o modelo técnico servem ao uso desejado

### Dependências observadas
- Python
- `mcp[cli]`
- `httpx`
- `requests`
- `Pillow`
- outras libs auxiliares

### Variáveis/credenciais a confirmar
Uma parte crítica ainda precisa ser validada antes de adotar esse candidato como padrão:
- token Pipeboard ou credencial Meta direta
- escopos adequados para leitura analítica
- ad accounts relevantes

### Comando inicial observado para HTTP
```bash
python -m meta_ads_mcp --transport streamable-http --host 127.0.0.1 --port 3002
```

### Healthcheck prático
Validar via MCP:
- listar contas
- listar campanhas
- buscar insights por campanha e por ad set
- confirmar se conseguimos descobrir ou inferir o evento correto quando a campanha usa evento customizado

### Riscos principais
- dependência excessiva do ecossistema Pipeboard
- licenciamento e operação self-hosted possivelmente menos livres do que Kommo/Sheets
- necessidade de confirmar cobertura para casos críticos da Blue Ocean, especialmente CTWA e campanhas com eventos customizados

### Status de prontidão atual
Promissor, mas precisa due diligence técnica maior do que Kommo e Sheets.

## Estratégia de integração com OpenClaw
### Direção preferida
Sempre que possível, configurar MCPs de modo nativo no OpenClaw após a prova de vida.

### Alvo operacional
- Google Sheets: integrado primeiro
- Kommo: integrado em seguida
- Meta Ads: integrar após fechar a decisão entre remote e self-hosted

### Estado atual conhecido
Hoje o OpenClaw não tem MCPs configurados.

## Ordem executiva recomendada
1. preparar credencial de Google Sheets e validar prova de vida
2. preparar token/subdomínio de Kommo e validar prova de vida
3. decidir rota de Meta Ads: remote ou self-hosted
4. integrar os MCPs no OpenClaw
5. rodar validação analítica real cruzando período conhecido

## Decisões já tomadas
- não voltar ao modelo laptop-local
- não tratar `.mcp-servers/` antiga como dependência estrutural
- priorizar recuperação de capacidade live antes de customização profunda
- adotar build próprio apenas se as lacunas aparecerem na prática

## Próxima saída esperada
Depois deste inventário, o próximo artefato útil deve ser um guia operacional de implantação com exemplos de:
- unit files de `systemd`
- environment files
- comandos de teste
- configuração `openclaw mcp set` para cada serviço
