"""empty message

Revision ID: 45a9f063e49e
Revises: 486fc23e3d81
Create Date: 2022-03-27 21:50:14.223303

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45a9f063e49e'
down_revision = '486fc23e3d81'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('card_order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('card_choise', sa.String(length=100), nullable=False),
    sa.Column('select_card', sa.String(length=100), nullable=False),
    sa.Column('currency', sa.String(length=100), nullable=False),
    sa.Column('term', sa.String(length=30), nullable=False),
    sa.Column('main_office', sa.String(length=30), nullable=False),
    sa.Column('document1', sa.String(length=30), nullable=False),
    sa.Column('document2', sa.String(length=30), nullable=False),
    sa.Column('phone_number', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('card_order')
    # ### end Alembic commands ###