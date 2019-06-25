"""empty message

Revision ID: 2399fb9c7c39
Revises: 3005b86956cb
Create Date: 2019-06-21 20:36:51.148799

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2399fb9c7c39'
down_revision = '3005b86956cb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('application', sa.Column('person_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'application', 'person', ['person_id'], ['id'])
    op.drop_index('person_id', table_name='person')
    op.drop_index('spouse_id', table_name='person')
    op.drop_column('person', 'person_id')
    op.drop_column('person', 'spouse_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('person', sa.Column('spouse_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.add_column('person', sa.Column('person_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.create_index('spouse_id', 'person', ['spouse_id'], unique=True)
    op.create_index('person_id', 'person', ['person_id'], unique=True)
    op.drop_constraint(None, 'application', type_='foreignkey')
    op.drop_column('application', 'person_id')
    # ### end Alembic commands ###