# ADR-004 — Webhooks idempotentes

**Status:** Accepted

## Contexto

Provedores podem reenviar notificações. O mesmo pagamento não pode ativar assinatura ou lançar receita duas vezes.

## Decisão

Persistir identificadores do provedor, validar o estado autoritativo no gateway e aplicar efeitos dentro de uma operação idempotente.

## Consequência

Replays se tornam seguros e processos de conciliação manual podem reutilizar a mesma lógica do webhook.
