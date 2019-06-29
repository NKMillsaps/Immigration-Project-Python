"""empty message

Revision ID: 72687b73a5d7
Revises: 5916f3ee4c79
Create Date: 2019-06-27 18:34:14.148573

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72687b73a5d7'
down_revision = '5916f3ee4c79'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('forms', sa.Column('employer_address', sa.String(length=120), nullable=True))
    op.add_column('forms', sa.Column('employer_apartment', sa.String(length=120), nullable=True))
    op.add_column('forms', sa.Column('employer_city', sa.String(length=120), nullable=True))
    op.add_column('forms', sa.Column('employer_country', sa.String(length=120), nullable=True))
    op.add_column('forms', sa.Column('employer_dayPhone', sa.String(length=12), nullable=True))
    op.add_column('forms', sa.Column('employer_name', sa.String(length=120), nullable=True))
    op.add_column('forms', sa.Column('employer_occupation', sa.String(length=120), nullable=True))
    op.add_column('forms', sa.Column('employer_state', sa.String(length=120), nullable=True))
    op.add_column('forms', sa.Column('employer_zip_code', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('forms', 'employer_zip_code')
    op.drop_column('forms', 'employer_state')
    op.drop_column('forms', 'employer_occupation')
    op.drop_column('forms', 'employer_name')
    op.drop_column('forms', 'employer_dayPhone')
    op.drop_column('forms', 'employer_country')
    op.drop_column('forms', 'employer_city')
    op.drop_column('forms', 'employer_apartment')
    op.drop_column('forms', 'employer_address')
    # ### end Alembic commands ###