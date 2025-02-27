"""add officetable,nightstand and drawer model

Revision ID: 6bc54800c183
Revises: 5d11adc429d0
Create Date: 2024-10-31 11:34:26.334089

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6bc54800c183'
down_revision = '5d11adc429d0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('drawer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=100), nullable=True),
    sa.Column('width', sa.Float(), nullable=False),
    sa.Column('length', sa.Float(), nullable=False),
    sa.Column('height', sa.Float(), nullable=False),
    sa.Column('furniture_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['furniture_id'], ['furniture.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('nightstand',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=100), nullable=True),
    sa.Column('width', sa.Float(), nullable=False),
    sa.Column('length', sa.Float(), nullable=False),
    sa.Column('height', sa.Float(), nullable=False),
    sa.Column('furniture_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['furniture_id'], ['furniture.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('office_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=100), nullable=True),
    sa.Column('width', sa.Float(), nullable=False),
    sa.Column('length', sa.Float(), nullable=False),
    sa.Column('height', sa.Float(), nullable=False),
    sa.Column('furniture_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['furniture_id'], ['furniture.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('office_table')
    op.drop_table('nightstand')
    op.drop_table('drawer')
    # ### end Alembic commands ###
