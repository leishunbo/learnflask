"""initial migration

Revision ID: e3a918862720
Revises: 456a945560f6
Create Date: 2016-10-23 15:01:38.337216

"""

# revision identifiers, used by Alembic.
revision = 'e3a918862720'
down_revision = '456a945560f6'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirmed')
    ### end Alembic commands ###
