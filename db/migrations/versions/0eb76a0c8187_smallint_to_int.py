"""smallint to int

Revision ID: 0eb76a0c8187
Revises: 65ab4ee4a037
Create Date: 2022-05-09 16:38:07.675588

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0eb76a0c8187'
down_revision = '65ab4ee4a037'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('songs', sa.Column('bit_rate', sa.Integer(), nullable=True))
    op.add_column('songs', sa.Column('duration', sa.Integer(), nullable=True))
    op.add_column('songs', sa.Column('file_size', sa.Integer(), nullable=False))
    op.add_column('songs', sa.Column('year', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('songs', 'year')
    op.drop_column('songs', 'file_size')
    op.drop_column('songs', 'duration')
    op.drop_column('songs', 'bit_rate')
    # ### end Alembic commands ###