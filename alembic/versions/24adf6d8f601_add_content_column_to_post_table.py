"""add content column to post table

Revision ID: 24adf6d8f601
Revises: 96d56e6bd877
Create Date: 2025-10-04 08:28:32.448205

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '24adf6d8f601'
down_revision: Union[str, Sequence[str], None] = '96d56e6bd877'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        'posts',
        sa.Column('info', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'info')
    pass
