from sqlalchemy import Column, \
    Integer, \
    String, \
    DateTime, \
    ForeignKey, \
    Boolean, \
    Table
# from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from dictalchemy import make_class_dictable
from datetime import datetime


DbModel = declarative_base()
make_class_dictable(DbModel)


class GitHubUser(DbModel):
    __tablename__ = 'github_user'

    id = Column(Integer, primary_key=True)
    login = Column(String, nullable=False)
    html_url = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    issues = relationship('Issue', secondary=lambda: issue_assignee, back_populates='assignees')


class Project(DbModel):
    __tablename__ = 'project'

    id = Column(Integer, primary_key=True)
    number = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    html_url = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    columns = relationship('Board_Column', back_populates='project')
    cards = relationship('Card', back_populates='project')


class Board_Column(DbModel):
    __tablename__ = 'board_column'

    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey(Project.id), nullable=False)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    project = relationship('Project', back_populates='columns')


class Card(DbModel):
    __tablename__ = 'card'

    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey(Project.id), nullable=False)
    note = Column(String, nullable=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    created_by = Column(Integer, ForeignKey(GitHubUser.id))

    moves = relationship('CardMoveHistory')
    issue = relationship('Issue', back_populates='card')
    project = relationship('Project', back_populates='cards')


class CardMoveHistory(DbModel):
    __tablename__ = 'board_column_card'

    id = Column(Integer, primary_key=True)
    board_column_id = Column(Integer, ForeignKey(Board_Column.id), nullable=False)
    card_id = Column(Integer, ForeignKey(Card.id), nullable=False)
    placed_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    removed_at = Column(DateTime, nullable=True)


class Issue(DbModel):
    __tablename__ = 'issue'

    id = Column(Integer, primary_key=True)
    card_id = Column(Integer, ForeignKey(Card.id), nullable=False)
    number = Column(Integer, nullable=False)
    title = Column(String, nullable=False)
    state = Column(String, nullable=False)
    repository = Column(String, nullable=False)
    is_pull_request = Column(Boolean, nullable=False)
    html_url = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    created_by = Column(Integer, ForeignKey(GitHubUser.id))

    card = relationship('Card', back_populates='issue', uselist=False)
    labels = relationship('Issue_Label', back_populates='issue', lazy='joined')
    assignees = relationship('GitHubUser', secondary=lambda: issue_assignee, back_populates='issues', lazy='joined')


class Issue_Label(DbModel):
    __tablename__ = 'issue_label'

    id = Column(Integer, primary_key=True)
    label_id = Column(Integer, nullable=False)
    issue_id = Column(Integer, ForeignKey(Issue.id), nullable=False)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    issue = relationship('Issue', back_populates='labels')


issue_assignee = Table('issue_assignee', DbModel.metadata,
                       Column('issue_id', Integer, ForeignKey(Issue.id), primary_key=True),
                       Column('assignee_id', Integer, ForeignKey(GitHubUser.id), primary_key=True)
                       )
