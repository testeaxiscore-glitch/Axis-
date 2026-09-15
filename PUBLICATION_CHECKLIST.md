# Public Publication Checklist

Checklist utilizado antes de publicar mudanças neste case.

## Nunca publicar

- `.env`, secrets, tokens, API keys ou cookies;
- URLs privadas, IDs de infraestrutura ou credenciais;
- dumps, migrations completas ou schema integral de produção;
- dados reais de clientes, logs com PII ou screenshots de contas reais;
- prompts internos completos ou regras de negócio proprietárias;
- preços internos, roadmap, estratégia comercial ou features ainda não públicas;
- código copiado diretamente do repositório privado.

## Antes de cada commit público

1. confirmar que exemplos foram reescritos para portfólio;
2. revisar screenshots e remover nomes, e-mails, slugs, valores, IDs e dados reais;
3. generalizar provedores quando o nome não agrega valor técnico;
4. procurar secrets e URLs com `grep`/secret scanner;
5. revisar metadados de imagens e arquivos;
6. confirmar que o conteúdo demonstra o padrão técnico, não a implementação proprietária;
7. revisar `git diff` antes de `push`.

## Regra prática

O repositório deve responder **"qual problema de engenharia foi resolvido e qual padrão foi usado?"** sem responder **"como reconstruir o produto comercial?"**.
