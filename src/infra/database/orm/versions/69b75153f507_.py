"""empty message

Revision ID: 69b75153f507
Revises: 36100e7c1d17
Create Date: 2023-04-22 01:02:25.874210

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69b75153f507'
down_revision = '36100e7c1d17'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.drop_column('index')

    with op.batch_alter_table('loan', schema=None) as batch_op:
        batch_op.drop_column('index')

    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.drop_column('index')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.add_column(sa.Column('index', sa.BIGINT(), autoincrement=False, nullable=False))

    with op.batch_alter_table('loan', schema=None) as batch_op:
        batch_op.add_column(sa.Column('index', sa.INTEGER(), autoincrement=False, nullable=True))

    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.add_column(sa.Column('index', sa.INTEGER(), autoincrement=False, nullable=True))

    # ### end Alembic commands ###
