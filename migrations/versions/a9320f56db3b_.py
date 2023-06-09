"""empty message

Revision ID: a9320f56db3b
Revises: 
Create Date: 2023-02-20 13:03:07.250233

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9320f56db3b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.add_column(sa.Column('type', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('entityId', sa.Integer(), nullable=True))
        batch_op.alter_column('uid',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.drop_column('favorites')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.add_column(sa.Column('favorites', sa.VARCHAR(), autoincrement=False, nullable=False))
        batch_op.alter_column('uid',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.drop_column('entityId')
        batch_op.drop_column('type')

    # ### end Alembic commands ###
