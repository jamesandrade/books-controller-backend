"""empty message

Revision ID: 36100e7c1d17
Revises: f12b56000fc0
Create Date: 2023-04-22 00:45:34.011904

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36100e7c1d17'
down_revision = 'f12b56000fc0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.alter_column('index',
               existing_type=sa.INTEGER(),
               type_=sa.BigInteger(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.alter_column('index',
               existing_type=sa.BigInteger(),
               type_=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###