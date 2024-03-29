"""empty message

Revision ID: 0b389171edec
Revises: b5baf422715d
Create Date: 2019-06-27 16:43:58.615608

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b389171edec'
down_revision = 'b5baf422715d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('person', sa.Column('address', sa.String(length=120), nullable=True))
    op.add_column('person', sa.Column('apartment', sa.String(length=120), nullable=True))
    op.add_column('person', sa.Column('city', sa.String(length=120), nullable=True))
    op.add_column('person', sa.Column('country', sa.String(length=120), nullable=True))
    op.add_column('person', sa.Column('state', sa.String(length=120), nullable=True))
    op.add_column('person', sa.Column('zip_code', sa.String(length=120), nullable=True))
    op.add_column('spouse', sa.Column('address', sa.String(length=120), nullable=True))
    op.add_column('spouse', sa.Column('apartment', sa.String(length=120), nullable=True))
    op.add_column('spouse', sa.Column('city', sa.String(length=120), nullable=True))
    op.add_column('spouse', sa.Column('country', sa.String(length=120), nullable=True))
    op.add_column('spouse', sa.Column('state', sa.String(length=120), nullable=True))
    op.add_column('spouse', sa.Column('zip_code', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('spouse', 'zip_code')
    op.drop_column('spouse', 'state')
    op.drop_column('spouse', 'country')
    op.drop_column('spouse', 'city')
    op.drop_column('spouse', 'apartment')
    op.drop_column('spouse', 'address')
    op.drop_column('person', 'zip_code')
    op.drop_column('person', 'state')
    op.drop_column('person', 'country')
    op.drop_column('person', 'city')
    op.drop_column('person', 'apartment')
    op.drop_column('person', 'address')
    # ### end Alembic commands ###
