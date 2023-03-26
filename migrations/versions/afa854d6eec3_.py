"""empty message

Revision ID: afa854d6eec3
Revises: a9320f56db3b
Create Date: 2023-02-20 13:43:20.886358

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'afa854d6eec3'
down_revision = 'a9320f56db3b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.add_column(sa.Column('gender', sa.PickleType(), nullable=False))
        batch_op.drop_column('prop')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.add_column(sa.Column('prop', postgresql.BYTEA(), autoincrement=False, nullable=False))
        batch_op.drop_column('gender')

    # ### end Alembic commands ###