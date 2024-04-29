"""empty message

Revision ID: 646f5a7c5f0a
Revises: 59344485de26
Create Date: 2024-04-23 18:19:23.332036

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '646f5a7c5f0a'
down_revision = '59344485de26'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('habit', schema=None) as batch_op:
        batch_op.drop_column('last_completed')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('habit', schema=None) as batch_op:
        batch_op.add_column(sa.Column('last_completed', sa.DATE(), nullable=True))

    # ### end Alembic commands ###
