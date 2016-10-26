"""initial migration

Revision ID: 932d90b67fdb
Revises: e3a918862720
Create Date: 2016-10-27 00:27:43.531359

"""

# revision identifiers, used by Alembic.
revision = '932d90b67fdb'
down_revision = 'e3a918862720'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('default', sa.Boolean(), nullable=True))
    op.add_column('roles', sa.Column('permissions', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_roles_default'), 'roles', ['default'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_roles_default'), table_name='roles')
    op.drop_column('roles', 'permissions')
    op.drop_column('roles', 'default')
    ### end Alembic commands ###
