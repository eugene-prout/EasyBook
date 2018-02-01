"""empty message

Revision ID: a03c686ec9da
Revises: 475ee33ae191
Create Date: 2018-02-01 17:08:17.387471

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a03c686ec9da'
down_revision = '475ee33ae191'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_customer_url_name', table_name='customer')
    op.create_index(op.f('ix_customer_url_name'), 'customer', ['url_name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_customer_url_name'), table_name='customer')
    op.create_index('ix_customer_url_name', 'customer', ['url_name'], unique=1)
    # ### end Alembic commands ###
