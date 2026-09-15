"""Generic portfolio example — intentionally not production source."""
from dataclasses import dataclass
from enum import StrEnum


class Role(StrEnum):
    ADMIN = "ADMIN"
    MEMBER = "MEMBER"


@dataclass(frozen=True)
class RequestScope:
    actor_id: int
    tenant_id: int
    role: Role
    resource_scope_id: int | None = None


class Forbidden(Exception):
    pass


def resolve_scope(*, actor_id: int, tenant_id: int, membership_repo) -> RequestScope:
    membership = membership_repo.find(actor_id=actor_id, tenant_id=tenant_id)
    if membership is None or not membership.active:
        raise Forbidden("Actor is not authorized for this tenant")

    resource_scope_id = None
    if membership.role == Role.MEMBER:
        profile = membership_repo.member_scope(membership.id)
        if profile is None or not profile.active:
            raise Forbidden("Scoped profile is unavailable")
        resource_scope_id = profile.id

    return RequestScope(
        actor_id=actor_id,
        tenant_id=tenant_id,
        role=membership.role,
        resource_scope_id=resource_scope_id,
    )


def list_records(scope: RequestScope, repository):
    """Tenant filter is mandatory; role may further reduce the scope."""
    filters = {"tenant_id": scope.tenant_id}

    if scope.role == Role.MEMBER:
        filters["resource_scope_id"] = scope.resource_scope_id

    return repository.list(**filters)
