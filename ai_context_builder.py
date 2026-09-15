"""Generic portfolio example — intentionally not production source."""
from dataclasses import dataclass


@dataclass(frozen=True)
class AIContext:
    tenant: dict
    metrics: dict
    alerts: list[dict]


def build_ai_context(*, scope, question: str, analytics) -> AIContext:
    """Build a minimized context only after authorization."""
    metrics = analytics.summary(
        tenant_id=scope.tenant_id,
        resource_scope_id=scope.resource_scope_id,
    )

    # Example of role-aware minimization.
    if scope.role == "MEMBER":
        metrics.pop("tenant_financial_summary", None)
        metrics.pop("cross_team_comparison", None)

    alerts: list[dict] = []
    if "alert" in question.lower() or "resumo" in question.lower():
        rows = analytics.allowed_alerts(tenant_id=scope.tenant_id)
        alerts = [
            {
                "category": row.category,
                "severity": row.severity,
            }
            for row in rows
        ]

    # No phone, email, document IDs, addresses or free-form notes are included.
    return AIContext(
        tenant={"id": scope.tenant_id},
        metrics=metrics,
        alerts=alerts,
    )
