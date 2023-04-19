"""empty message

Revision ID: 05bff8f7e6eb
Revises: 4a2e208efb53
Create Date: 2023-04-15 15:47:56.671556

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05bff8f7e6eb'
down_revision = '4a2e208efb53'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), nullable=False))
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('created_by', sa.UUID(), nullable=False))
        batch_op.add_column(sa.Column('updated_by', sa.UUID(), nullable=True))
        batch_op.create_foreign_key(None, 'user', ['created_by'], ['id'])
        batch_op.create_foreign_key(None, 'user', ['updated_by'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('updated_by')
        batch_op.drop_column('created_by')
        batch_op.drop_column('updated_at')
        batch_op.drop_column('created_at')

    # ### end Alembic commands ###
