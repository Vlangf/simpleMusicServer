"""smallint to int

Revision ID: 65ab4ee4a037
Revises: 6f2843aace8a
Create Date: 2022-05-09 16:37:21.106963

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65ab4ee4a037'
down_revision = '6f2843aace8a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('songs', 'year')
    op.drop_column('songs', 'bit_rate')
    op.drop_column('songs', 'duration')
    op.drop_column('songs', 'file_size')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('songs', sa.Column('file_size', sa.SMALLINT(), autoincrement=False, nullable=False))
    op.add_column('songs', sa.Column('duration', sa.SMALLINT(), autoincrement=False, nullable=True))
    op.add_column('songs', sa.Column('bit_rate', sa.SMALLINT(), autoincrement=False, nullable=True))
    op.add_column('songs', sa.Column('year', sa.SMALLINT(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###