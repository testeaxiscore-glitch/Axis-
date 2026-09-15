# Segurança

Este documento resume decisões de segurança relevantes do case.

## Principais riscos e controles

| Risco | Controle |
|---|---|
| Acesso entre tenants | Membership + filtros por organization_id no backend |
| Escalada de privilégio | RBAC e validações por recurso |
| Roubo de refresh token via JS | Cookie HttpOnly |
| Reuso de refresh token | Rotação de refresh sessions |
| CSRF em refresh/logout cross-site | Validação de Origin quando presente |
| Convite reutilizável | Token de uso único, hash no banco e expiração |
| Double booking | Validação de app + exclusion constraint PostgreSQL |
| Manipulação de preço no checkout | Catálogo/valor resolvido no servidor |
| Webhook duplicado | Provider payment ID + processamento idempotente |
| Vazamento de PII para IA | Snapshot minimizado e autorizado |
| Configuração insegura em produção | Fail-fast no startup |

## Tokens públicos

Booking e portais públicos exigem atenção especial porque o visitante pode não possuir uma conta tradicional.

Princípios utilizados:

- token imprevisível;
- escopo mínimo;
- evitar assumir identidade apenas por telefone/e-mail digitado anonimamente;
- limitar o token ao recurso necessário;
- não transformar dados fornecidos pelo navegador em autenticação implícita.

## Produção

A aplicação rejeita configurações inseguras em ambiente de produção, como:

- secret JWT padrão;
- SQLite em produção;
- cookie sem `Secure`;
- origem de frontend insegura;
- CORS permissivo indevido.

A ideia é transformar erros de configuração em falhas visíveis no deploy, em vez de vulnerabilidades silenciosas em runtime.
