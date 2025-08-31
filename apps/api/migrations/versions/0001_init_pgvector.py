"""init + pgvector

Revision ID: d0a9aaad9418
Revises: 
Create Date: 2025-08-31 10:02:23.972766

"""
from alembic import op

revision = '0001'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.execute("CREATE EXTENSION IF NOT EXISTS vector")

def downgrade():
    op.execute("DROP EXTENSION IF EXISTS vector")
