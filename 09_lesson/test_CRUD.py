import pytest
from db import Session, Student

@pytest.fixture(scope="function")
def session():
    session = Session()
    yield session
    session.rollback()  
    session.close()

def test_add_student(session):
    student = Student(name="Иван Лысенко", age=20)
    session.add(student)
    session.commit()

    from_db = session.query(Student).filter_by(name="Иван Лысенко").first()
    assert from_db is not None
    assert from_db.name == "Иван Лысенко"

def test_update_student(session):
    student = Student(name="Анастасия Дуброва", age=21)
    session.add(student)
    session.commit()

    student.age = 22
    session.commit()

    updated = session.query(Student).filter_by(name="Анастасия Дуброва").first()
    assert updated.age == 22

def test_soft_delete_student(session):
    student = Student(name="Удаляемый Студент", age=19)
    session.add(student)
    session.commit()

    student.deleted = True 
    session.commit()

    deleted = session.query(Student).filter_by(name="Удаляемый Студент").first()
    assert deleted.deleted is True
