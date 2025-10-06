"""add foreign_ket to post table

Revision ID: 8e98db6f7429
Revises: 33624c2aca4f
Create Date: 2025-10-04 08:47:17.299818

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8e98db6f7429'
down_revision: Union[str, Sequence[str], None] = '33624c2aca4f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_foreign_key('post_users_fk',source_table="posts", referent_table="users", local_cols=['owner_id'], remote_cols=['id'],ondelete="CASCADE")
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('post', 'owner_id')
    pass
