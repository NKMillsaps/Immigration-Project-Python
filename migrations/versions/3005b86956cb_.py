"""empty message

Revision ID: 3005b86956cb
Revises: 709da2d20d0d
Create Date: 2019-06-20 22:05:18.295713

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3005b86956cb'
down_revision = '709da2d20d0d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('forms', sa.Column('application_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'forms', 'application', ['application_id'], ['id'])
    op.add_column('person', sa.Column('person_id', sa.Integer(), nullable=False))
    op.create_unique_constraint(None, 'person', ['person_id'])
    op.add_column('spouse', sa.Column('person_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'spouse', 'person', ['person_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'spouse', type_='foreignkey')
    op.drop_column('spouse', 'person_id')
    op.drop_constraint(None, 'person', type_='unique')
    op.drop_column('person', 'person_id')
    op.drop_constraint(None, 'forms', type_='foreignkey')
    op.drop_column('forms', 'application_id')
    # ### end Alembic commands ###
