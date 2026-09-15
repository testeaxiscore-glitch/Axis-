# ADR-001 — PostgreSQL como banco de produção

**Status:** Accepted

## Contexto

O protótipo inicial podia operar com SQLite, mas o produto passou a ter multi-tenancy, billing, agenda concorrente e necessidade de deploy real.

## Decisão

Usar PostgreSQL em produção e manter Alembic como mecanismo de evolução de schema.

## Motivos

- concorrência real;
- constraints avançadas;
- transações robustas;
- melhor caminho de escala;
- suporte nativo a ranges/GiST para agenda;
- tooling maduro de backup/restore.

## Consequências

Positivas: maior integridade e previsibilidade de produção.

Negativas: infraestrutura mais complexa que SQLite e necessidade de estratégia de migrations/backups.
