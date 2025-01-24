"""таблицы активностей и некоторые индексы для поиска

Revision ID: 8be7d9cf7269
Revises: a17281cabc1b
Create Date: 2025-01-24 16:18:00.264795

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8be7d9cf7269'
down_revision: Union[str, None] = 'a17281cabc1b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('activity',
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('main_activities_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', now())"), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['main_activities_id'], ['activity.id'], ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index('idx_name_activity', 'activity', ['name'], unique=False)
    op.create_table('third_activity',
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', now())"), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index('idx_name_third_activity', 'third_activity', ['name'], unique=False)
    op.create_table('activity_third_activity_association',
    sa.Column('main_activities_id', sa.Integer(), nullable=False),
    sa.Column('third_activity_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', now())"), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['main_activities_id'], ['activity.id'], ),
    sa.ForeignKeyConstraint(['third_activity_id'], ['third_activity.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('main_activities_id', 'third_activity_id', name='ind_unique_activity_third_activity')
    )
    op.create_table('organization_activity_association',
    sa.Column('organization_id', sa.Integer(), nullable=False),
    sa.Column('activity_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', now())"), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['activity_id'], ['activity.id'], ),
    sa.ForeignKeyConstraint(['organization_id'], ['organizations.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('organization_id', 'activity_id', name='ind_unique_organization_activity')
    )
    op.create_table('organization_third_activity_association',
    sa.Column('organization_id', sa.Integer(), nullable=False),
    sa.Column('third_activity_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', now())"), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['organization_id'], ['organizations.id'], ),
    sa.ForeignKeyConstraint(['third_activity_id'], ['third_activity.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('organization_id', 'third_activity_id', name='ind_unique_organization_third_activity')
    )
    op.create_index('idx_building_id', 'organizations', ['building_id'], unique=False)
    op.create_index('idx_name', 'organizations', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('idx_name', table_name='organizations')
    op.drop_index('idx_building_id', table_name='organizations')
    op.drop_table('organization_third_activity_association')
    op.drop_table('organization_activity_association')
    op.drop_table('activity_third_activity_association')
    op.drop_index('idx_name_third_activity', table_name='third_activity')
    op.drop_table('third_activity')
    op.drop_index('idx_name_activity', table_name='activity')
    op.drop_table('activity')
    # ### end Alembic commands ###
