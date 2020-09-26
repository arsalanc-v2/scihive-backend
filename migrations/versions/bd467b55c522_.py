"""empty message

Revision ID: bd467b55c522
Revises: a32de8c13f36
Create Date: 2020-09-25 21:55:18.725925

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bd467b55c522'
down_revision = 'a32de8c13f36'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('collection', sa.Column('is_shared', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('collection', 'is_shared')
    # ### end Alembic commands ###
