"""${message}

Revision ID: ${up_revision}
Revises: ${down_revision | comma,n}
Create Date: ${create_date}

"""
from alembic import op
import sqlalchemy as sa
${imports if imports else ""}

# revision identifiers, used by Alembic.
revision = ${repr(up_revision)}
down_revision = ${repr(down_revision)}
branch_labels = ${repr(branch_labels)}
depends_on = ${repr(depends_on)}


def upgrade():
    op.create_table(
        'calculations',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('operator', sa.String()),
        sa.Column('operand1', sa.Integer()),
        sa.Column('operand2', sa.Integer()),
        sa.Column('result', sa.Integer())
    )
    op.create_table(
        'tags',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), unique=True)
    )
    op.create_table(
        'calculation_tag_association',
        sa.Column('calculation_id', sa.Integer(), sa.ForeignKey('calculations.id')),
        sa.Column('tag_id', sa.Integer(), sa.ForeignKey('tags.id'))
    )



def downgrade():
    ${downgrades if downgrades else "pass"}
