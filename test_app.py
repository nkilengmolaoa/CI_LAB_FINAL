# test_app.py
from app import greet, introduction, objective

def test_greet():
    assert greet() == "Welcome to my first CI Workflow!"

def test_introduction():
    assert introduction() == "it is time to prove that I have mastered the CI Workflow :)"

def test_objective():
    assert objective() == "let's see how many tries it will take to get it right"
