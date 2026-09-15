"""Generic portfolio example — intentionally not production source."""


def process_external_payment(event_id: str, *, provider, payments, entitlements, uow):
    """Apply an external payment effect at most once."""
    remote = provider.fetch_event(event_id)

    if remote.status != "approved":
        return {"status": "ignored"}

    with uow.transaction():
        local = payments.lock_by_external_id(event_id)

        if local is not None and local.applied_at is not None:
            return {"status": "already_processed"}

        expected = payments.require_expected_reference(remote.reference)
        if remote.amount_cents != expected.amount_cents:
            raise ValueError("Unexpected amount")

        if local is None:
            local = payments.create_from_external_event(remote)

        entitlements.apply(
            tenant_id=expected.tenant_id,
            entitlement_code=expected.entitlement_code,
            effective_at=remote.approved_at,
        )

        local.mark_applied()

    return {"status": "processed"}
