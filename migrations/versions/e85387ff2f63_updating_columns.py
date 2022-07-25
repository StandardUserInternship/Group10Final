"""Updating columns

Revision ID: e85387ff2f63
Revises: 3048f01cfa14
Create Date: 2022-07-24 18:56:07.059376

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e85387ff2f63'
down_revision = '3048f01cfa14'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('date_created', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'date_created')
    # ### end Alembic commands ###
