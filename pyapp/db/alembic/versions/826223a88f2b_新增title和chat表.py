"""新增title和chat表

Revision ID: 826223a88f2b
Revises: 86c3f491c4cc
Create Date: 2023-04-03 10:35:26.311786

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '826223a88f2b'
down_revision = '86c3f491c4cc'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('chat',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.Integer(), server_default='', nullable=False, comment='标题'),
    sa.Column('who', sa.String(), server_default='', nullable=False, comment='所属人'),
    sa.Column('content', sa.String(), server_default='', nullable=False, comment='内容'),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text("(DATETIME(CURRENT_TIMESTAMP, 'localtime'))"), nullable=True, comment='创建时间'),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text("(DATETIME(CURRENT_TIMESTAMP, 'localtime'))"), nullable=True, comment='更新时间'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_chat_title'), 'chat', ['title'], unique=False)
    op.create_table('title',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), server_default='', nullable=False, comment='标题'),
    sa.Column('theme', sa.String(), server_default='', nullable=False, comment='主题'),
    sa.Column('model', sa.String(), server_default='gpt-3.5-turbo', nullable=False, comment='模型'),
    sa.Column('temperature', sa.Float(), server_default='1.0', nullable=False, comment='温度参数'),
    sa.Column('news_count', sa.Integer(), server_default='0', nullable=False, comment='记忆消息个数'),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text("(DATETIME(CURRENT_TIMESTAMP, 'localtime'))"), nullable=True, comment='创建时间'),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text("(DATETIME(CURRENT_TIMESTAMP, 'localtime'))"), nullable=True, comment='更新时间'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_title_title'), 'title', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_title_title'), table_name='title')
    op.drop_table('title')
    op.drop_index(op.f('ix_chat_title'), table_name='chat')
    op.drop_table('chat')
    # ### end Alembic commands ###
