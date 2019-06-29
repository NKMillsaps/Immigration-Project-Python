"""empty message

Revision ID: 97fc0c85196c
Revises: 72687b73a5d7
Create Date: 2019-06-29 20:39:15.857545

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '97fc0c85196c'
down_revision = '72687b73a5d7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('forms', sa.Column('employerAddress', sa.String(length=120), nullable=True))
    op.add_column('forms', sa.Column('employerApartment', sa.String(length=120), nullable=True))
    op.add_column('forms', sa.Column('employerCity', sa.String(length=120), nullable=True))
    op.add_column('forms', sa.Column('employerCountry', sa.String(length=120), nullable=True))
    op.add_column('forms', sa.Column('employerDayPhone', sa.String(length=12), nullable=True))
    op.add_column('forms', sa.Column('employerName', sa.String(length=120), nullable=True))
    op.add_column('forms', sa.Column('employerOccupation', sa.String(length=120), nullable=True))
    op.add_column('forms', sa.Column('employerState', sa.String(length=120), nullable=True))
    op.add_column('forms', sa.Column('employerZipCode', sa.String(length=120), nullable=True))
    op.add_column('forms', sa.Column('souseLastname', sa.String(length=120), nullable=True))
    op.add_column('forms', sa.Column('spouseAddress', sa.String(length=120), nullable=True))
    op.add_column('forms', sa.Column('spouseApartment', sa.String(length=120), nullable=True))
    op.add_column('forms', sa.Column('spouseCity', sa.String(length=120), nullable=True))
    op.add_column('forms', sa.Column('spouseCountry', sa.String(length=120), nullable=True))
    op.add_column('forms', sa.Column('spouseDayPhone', sa.String(length=20), nullable=True))
    op.add_column('forms', sa.Column('spouseEmail', sa.String(length=120), nullable=False))
    op.add_column('forms', sa.Column('spouseFirstname', sa.String(length=120), nullable=True))
    op.add_column('forms', sa.Column('spouseMiddlename', sa.String(length=120), nullable=True))
    op.add_column('forms', sa.Column('spouseMobile', sa.String(length=20), nullable=True))
    op.add_column('forms', sa.Column('spouseState', sa.String(length=120), nullable=True))
    op.add_column('forms', sa.Column('spouseZipCode', sa.String(length=120), nullable=True))
    op.add_column('forms', sa.Column('zipCode', sa.String(length=120), nullable=True))
    op.create_unique_constraint(None, 'forms', ['spouseEmail'])
    op.drop_column('forms', 'employer_zip_code')
    op.drop_column('forms', 'employer_dayPhone')
    op.drop_column('forms', 'employer_address')
    op.drop_column('forms', 'employer_name')
    op.drop_column('forms', 'zip_code')
    op.drop_column('forms', 'employer_state')
    op.drop_column('forms', 'employer_city')
    op.drop_column('forms', 'logged_in')
    op.drop_column('forms', 'employer_country')
    op.drop_column('forms', 'employer_occupation')
    op.drop_column('forms', 'employer_apartment')
    op.add_column('person', sa.Column('zipCode', sa.String(length=120), nullable=True))
    op.drop_column('person', 'zip_code')
    op.add_column('spouse', sa.Column('souseLastname', sa.String(length=120), nullable=True))
    op.add_column('spouse', sa.Column('spouseAddress', sa.String(length=120), nullable=True))
    op.add_column('spouse', sa.Column('spouseApartment', sa.String(length=120), nullable=True))
    op.add_column('spouse', sa.Column('spouseCity', sa.String(length=120), nullable=True))
    op.add_column('spouse', sa.Column('spouseCountry', sa.String(length=120), nullable=True))
    op.add_column('spouse', sa.Column('spouseDayPhone', sa.String(length=20), nullable=True))
    op.add_column('spouse', sa.Column('spouseEmail', sa.String(length=120), nullable=False))
    op.add_column('spouse', sa.Column('spouseFirstname', sa.String(length=120), nullable=True))
    op.add_column('spouse', sa.Column('spouseMiddlename', sa.String(length=120), nullable=True))
    op.add_column('spouse', sa.Column('spouseMobile', sa.String(length=20), nullable=True))
    op.add_column('spouse', sa.Column('spouseState', sa.String(length=120), nullable=True))
    op.add_column('spouse', sa.Column('spouseZipCode', sa.String(length=120), nullable=True))
    op.drop_index('email', table_name='spouse')
    op.create_unique_constraint(None, 'spouse', ['spouseEmail'])
    op.drop_column('spouse', 'mobile')
    op.drop_column('spouse', 'country')
    op.drop_column('spouse', 'lastname')
    op.drop_column('spouse', 'dayPhone')
    op.drop_column('spouse', 'zip_code')
    op.drop_column('spouse', 'middlename')
    op.drop_column('spouse', 'firstname')
    op.drop_column('spouse', 'city')
    op.drop_column('spouse', 'email')
    op.drop_column('spouse', 'state')
    op.drop_column('spouse', 'address')
    op.drop_column('spouse', 'apartment')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('spouse', sa.Column('apartment', mysql.VARCHAR(length=120), nullable=True))
    op.add_column('spouse', sa.Column('address', mysql.VARCHAR(length=120), nullable=True))
    op.add_column('spouse', sa.Column('state', mysql.VARCHAR(length=120), nullable=True))
    op.add_column('spouse', sa.Column('email', mysql.VARCHAR(length=120), nullable=False))
    op.add_column('spouse', sa.Column('city', mysql.VARCHAR(length=120), nullable=True))
    op.add_column('spouse', sa.Column('firstname', mysql.VARCHAR(length=120), nullable=True))
    op.add_column('spouse', sa.Column('middlename', mysql.VARCHAR(length=120), nullable=True))
    op.add_column('spouse', sa.Column('zip_code', mysql.VARCHAR(length=120), nullable=True))
    op.add_column('spouse', sa.Column('dayPhone', mysql.VARCHAR(length=20), nullable=True))
    op.add_column('spouse', sa.Column('lastname', mysql.VARCHAR(length=120), nullable=True))
    op.add_column('spouse', sa.Column('country', mysql.VARCHAR(length=120), nullable=True))
    op.add_column('spouse', sa.Column('mobile', mysql.VARCHAR(length=20), nullable=True))
    op.drop_constraint(None, 'spouse', type_='unique')
    op.create_index('email', 'spouse', ['email'], unique=True)
    op.drop_column('spouse', 'spouseZipCode')
    op.drop_column('spouse', 'spouseState')
    op.drop_column('spouse', 'spouseMobile')
    op.drop_column('spouse', 'spouseMiddlename')
    op.drop_column('spouse', 'spouseFirstname')
    op.drop_column('spouse', 'spouseEmail')
    op.drop_column('spouse', 'spouseDayPhone')
    op.drop_column('spouse', 'spouseCountry')
    op.drop_column('spouse', 'spouseCity')
    op.drop_column('spouse', 'spouseApartment')
    op.drop_column('spouse', 'spouseAddress')
    op.drop_column('spouse', 'souseLastname')
    op.add_column('person', sa.Column('zip_code', mysql.VARCHAR(length=120), nullable=True))
    op.drop_column('person', 'zipCode')
    op.add_column('forms', sa.Column('employer_apartment', mysql.VARCHAR(length=120), nullable=True))
    op.add_column('forms', sa.Column('employer_occupation', mysql.VARCHAR(length=120), nullable=True))
    op.add_column('forms', sa.Column('employer_country', mysql.VARCHAR(length=120), nullable=True))
    op.add_column('forms', sa.Column('logged_in', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.add_column('forms', sa.Column('employer_city', mysql.VARCHAR(length=120), nullable=True))
    op.add_column('forms', sa.Column('employer_state', mysql.VARCHAR(length=120), nullable=True))
    op.add_column('forms', sa.Column('zip_code', mysql.VARCHAR(length=120), nullable=True))
    op.add_column('forms', sa.Column('employer_name', mysql.VARCHAR(length=120), nullable=True))
    op.add_column('forms', sa.Column('employer_address', mysql.VARCHAR(length=120), nullable=True))
    op.add_column('forms', sa.Column('employer_dayPhone', mysql.VARCHAR(length=12), nullable=True))
    op.add_column('forms', sa.Column('employer_zip_code', mysql.VARCHAR(length=120), nullable=True))
    op.drop_constraint(None, 'forms', type_='unique')
    op.drop_column('forms', 'zipCode')
    op.drop_column('forms', 'spouseZipCode')
    op.drop_column('forms', 'spouseState')
    op.drop_column('forms', 'spouseMobile')
    op.drop_column('forms', 'spouseMiddlename')
    op.drop_column('forms', 'spouseFirstname')
    op.drop_column('forms', 'spouseEmail')
    op.drop_column('forms', 'spouseDayPhone')
    op.drop_column('forms', 'spouseCountry')
    op.drop_column('forms', 'spouseCity')
    op.drop_column('forms', 'spouseApartment')
    op.drop_column('forms', 'spouseAddress')
    op.drop_column('forms', 'souseLastname')
    op.drop_column('forms', 'employerZipCode')
    op.drop_column('forms', 'employerState')
    op.drop_column('forms', 'employerOccupation')
    op.drop_column('forms', 'employerName')
    op.drop_column('forms', 'employerDayPhone')
    op.drop_column('forms', 'employerCountry')
    op.drop_column('forms', 'employerCity')
    op.drop_column('forms', 'employerApartment')
    op.drop_column('forms', 'employerAddress')
    # ### end Alembic commands ###
