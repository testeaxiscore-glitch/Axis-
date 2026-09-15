-- Generic portfolio example — intentionally not production schema.
-- Demonstrates a database-level invariant against concurrent overlaps.

CREATE EXTENSION IF NOT EXISTS btree_gist;

ALTER TABLE portfolio_bookings
ADD CONSTRAINT no_overlapping_active_bookings
EXCLUDE USING gist (
    tenant_id WITH =,
    resource_id WITH =,
    tstzrange(starts_at, ends_at, '[)') WITH &&
)
WHERE (state IN ('ACTIVE', 'CONFIRMED'));

-- The application can still pre-check availability for UX.
-- The database invariant remains the final concurrency barrier.
