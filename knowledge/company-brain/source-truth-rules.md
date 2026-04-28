# Source Truth Rules

Regras detalhadas de prevalência de evidência e fonte de verdade para a Blue Ocean.

## Classes de evidência
1. fato validado pelo usuário
2. padrão operacional provisório definido pelo usuário
3. documento interno oficial
4. fonte operacional oficial
5. fato validado pelo site
6. hipótese operacional assumida
7. inferência provisória até validação interna
8. ponto não confirmado

## Regra de prevalência contextual
A evidência que prevalece depende do tema.

### Rotina operacional, ownership, handoff, escalonamento, governança e execução real
Fato validado pelo usuário > padrão operacional provisório > fonte operacional oficial.

### Posicionamento institucional, narrativa pública e branding
Fato validado pelo site pode servir como contexto, desde que não conflite com validação do usuário.

### Métricas, CRM, avanço comercial, funil e resultado
Prevalece a fonte mais próxima do evento real.

Aplicações importantes:
- plataforma prevalece para spend, entrega e consumo de mídia;
- Kommo/CRM prevalece para entidade estrutural do lead, owner, pipeline e status vivo quando os campos críticos estão íntegros;
- validade operacional do topo depende do funil; em WhatsApp/CTWA, separar sempre Lead Real de Lead Fantasma;
- Sheets pode prevalecer em leitura comercial diária quando estiver mais íntegro que o CRM para reuniões, próximos passos ou acompanhamento operacional;
- dashboard é visualização derivada e nunca deve prevalecer sozinho sobre a fonte operacional mais próxima.

### Conflito entre classes fortes
- explicitar o conflito
- reduzir a força da conclusão
- tratar a leitura como provisória até validação

## Regra prática
- padrão operacional provisório orienta a operação, mas não vira benchmark histórico automaticamente
- o site não substitui CRM, stack, operação, handoff, rotina real ou validação do usuário
- sempre distinguir o que é regra da Blue Ocean do que é comportamento esperado do agente
