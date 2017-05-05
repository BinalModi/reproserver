import os
from sqlalchemy import Column, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.types import Boolean, DateTime, Integer, String


Base = declarative_base()


class Experiment(Base):
    """Experiments available on the server.

    Those match experiment files that were uploaded, whether or not an image
    has been built.

    Note that no filename is here, since the file might have been uploaded
    multiple times with different names.
    """
    __tablename__ = 'experiments'

    hash = Column(String, primary_key=True)
    status = Column(String)
    docker_image = Column(String)

    uploads = relationship('Upload', back_populates='experiment')
    runs = relationship('Run', back_populates='experiment')


class Upload(Base):
    """An upload of an experiment.

    There can be multiple uploads for the same experiment, each of them
    associated with a different uploader and filename.

    This is not used by the application, but might be important for accounting
    purposes.
    """
    __tablename__ = 'uploads'

    id = Column(Integer, primary_key=True)
    experiment_hash = Column(String, ForeignKey('experiment.id'))
    experiment = relationship('Experiment', uselist=False,
                              back_populates='uploads')
    submitted_ip = Column(String)
    timestamp = Column(DateTime)


class Parameter(Base):
    """An experiment parameter.
    
    Once the experiment has been built, the builder adds the list of its
    parameters to the database, that it extracted from the package metadata.
    Those are displayed to the user when running the experiment.
    """
    __tablename__ = 'parameters'

    id = Column(Integer, primary_key=True)
    experiment_hash = Column(String, ForeignKey('experiment.id'))
    experiment = relationship('Experiment', uselist=False,
                              back_populates='uploads')
    name = Column(String)
    optional = Column(Boolean)


class Run(Base):
    """A run.
    
    This is created when a user submits parameters and triggers the run of an
    experiment. It contains logs and the location of output files.
    """
    __tablename__ = 'runs'

    id = Column(Integer, primary_key=True)
    experiment_hash = Column(String, ForeignKey('experiment.id'))
    experiment = relationship('Experiment', uselist=False,
                              back_populates='uploads')
    submitted = Column(DateTime)
    started = Column(DateTime)
    done = Column(DateTime)

    logs = relationship('LogLine', back_populates='run')
    output_files = relationship('OutputFile', back_populates='run')


class LogLine(Base):
    """A line of log.
    
    TODO: Storing this in the database is not a great idea.
    """
    __tablename__ = 'logs'

    id = Column(Integer, primary_key=True)
    experiment_hash = Column(String, ForeignKey('experiment.id'))
    experiment = relationship('Experiment', uselist=False,
                              back_populates='uploads')
    timestamp = Column(DateTime)
    line = Column(String)


class OutputFile(Base):
    """An output file from a run.
    """
    __tablename__ = 'output_files'

    id = Column(Integer, primary_key=True)
    hash = Column(String)
    experiment_hash = Column(String, ForeignKey('experiment.id'))
    experiment = relationship('Experiment', uselist=False,
                              back_populates='uploads')
    name = Column(String)
    size = Column(Integer)


def connect():
    """Connect to the database using an environment variable.
    """
    engine = create_engine('postgresql://reproserver:hackmehackme@'
                           'reproserver_postgres',
                           echo=True)

    return sessionmaker(bind=engine)
