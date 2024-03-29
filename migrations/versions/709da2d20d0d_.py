"""empty message

Revision ID: 709da2d20d0d
Revises: 54379b61438e
Create Date: 2019-06-20 20:22:02.227749

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '709da2d20d0d'
down_revision = '54379b61438e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('application_id', table_name='application')
    op.drop_column('application', 'application_id')
    op.drop_index('forms_id', table_name='forms')
    op.drop_column('forms', 'forms_id')
    op.add_column('person', sa.Column('spouse_id', sa.Integer(), nullable=False))
    op.create_unique_constraint(None, 'person', ['spouse_id'])
    op.drop_index('spouse_id', table_name='spouse')
    op.drop_column('spouse', 'spouse_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('spouse', sa.Column('spouse_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.create_index('spouse_id', 'spouse', ['spouse_id'], unique=True)
    op.drop_constraint(None, 'person', type_='unique')
    op.drop_column('person', 'spouse_id')
    op.add_column('forms', sa.Column('forms_id', mysql.VARCHAR(length=120), nullable=False))
    op.create_index('forms_id', 'forms', ['forms_id'], unique=True)
    op.add_column('application', sa.Column('application_id', mysql.VARCHAR(length=120), nullable=False))
    op.create_index('application_id', 'application', ['application_id'], unique=True)
    # ### end Alembic commands ###
