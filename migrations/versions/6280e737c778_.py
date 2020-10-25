"""empty message

Revision ID: 6280e737c778
Revises: 79420dcea6cb
Create Date: 2020-10-22 23:05:06.624326

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6280e737c778'
down_revision = '79420dcea6cb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('paper', sa.Column('doi', sa.String(), nullable=True))
    op.add_column('paper_version', sa.Column('doi', sa.String(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('paper_version', 'doi')
    op.drop_column('paper', 'doi')
    # ### end Alembic commands ###