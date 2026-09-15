# Interview notes — pontos para explicar o projeto

Este arquivo serve como roteiro de preparação para entrevistas técnicas.

## “Por que PostgreSQL?”

Porque o produto deixou de ser apenas protótipo e passou a depender de integridade transacional e concorrência real. O PostgreSQL também permitiu mover a proteção contra sobreposição de agenda para uma constraint atômica no banco.

## “Por que não microservices?”

O problema atual não exigia escalabilidade independente por domínio. Um modular monolith diminui custo operacional, mantém transações simples e acelera evolução. As integrações e módulos foram isolados para permitir extração futura se houver motivo concreto.

## “Qual bug/risco técnico foi mais interessante?”

Double booking. Uma checagem `SELECT -> if free -> INSERT` parece correta em desenvolvimento, mas quebra sob concorrência. A solução foi manter a checagem amigável no backend e adicionar uma constraint de exclusão no PostgreSQL como autoridade final.

## “Como você protegeu a IA?”

O modelo não recebe banco nem SQL. Primeiro o backend aplica tenant/RBAC, calcula métricas e produz um snapshot mínimo. Só esse snapshot é enviado ao modelo.

## “Como tratou webhooks?”

Como mensagens que podem ser repetidas. O efeito financeiro é idempotente e vinculado ao identificador do pagamento no provedor.

## “O que faria diferente em escala maior?”

Dependendo de métricas reais: fila para workloads assíncronos, cache seletivo, observabilidade distribuída e, apenas se necessário, extração de domínios de alta carga. A decisão seria baseada em dados e não em arquitetura por antecipação.
