"""add cpe

Revision ID: dd87c9205752
Revises: df1e39a4f1bc
Create Date: 2023-07-11 06:47:33.012452

"""
import sqlalchemy as sa
from alembic import op
from litestar.contrib.sqlalchemy.types import GUID, ORA_JSONB, DateTimeUTC



sa.GUID = GUID
sa.DateTimeUTC = DateTimeUTC
sa.ORA_JSONB = ORA_JSONB

# revision identifiers, used by Alembic.
revision = 'dd87c9205752'
down_revision = 'df1e39a4f1bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cpe',
    sa.Column('device_id', sa.String(), nullable=False),
    sa.Column('routername', sa.String(), nullable=False),
    sa.Column('os', sa.String(), nullable=False),
    sa.Column('mgmt_ip', sa.String(), nullable=False),
    sa.Column('sec_mgmt_ip', sa.String(), nullable=True),
    sa.Column('id', sa.GUID(length=16), nullable=False),
    sa.Column('_sentinel', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTimeUTC(timezone=True), nullable=False),
    sa.Column('updated_at', sa.DateTimeUTC(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_cpe'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cpe')
    # ### end Alembic commands ###
