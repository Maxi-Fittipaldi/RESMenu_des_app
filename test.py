from tkinter import Variable
import pytest
from flask import session
from RESMenu_des_app import app
from pathlib import Path
import click


@pytest.fixture()
def app():
    app = app()
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app

    # clean up / reset resources here


def test_request_example(bot):
    response = bot.get("/posts")
    assert b"<h2>jodete</h2>" in response.data

def test_access_session(bot):
    with bot:
        bot.post("/auth/login", data={"username": "flask"})
        # session is still accessible
        assert session["user_id"] == 1
def test_modify_session(bot):
    with bot.session_transaction() as session:
        # set a user id without going through the login route
        session["user_id"] = 1

    # session is saved now

    response = bot.get("/users/me")
    assert response.json["username"] == "flask"

def test_edit_user(bot):
    response = bot.post("/user/2/edit", data={
        "name": "Flask",
        "": "",
    })
    assert response.status_code == 200

def test_json_data(bot):
    response = bot.post("/graphql", json={
        "query": """
            query User($id: String!) {
                user(id: $id) {
                    name
                }
            }
        """,
        Variable = {"id": 2},
    })
    assert response.json["user"]["name"] == "Flask"
@app.cli.command("hello")
@click.option("--name", default="World")
def hello_command(name):
    click.echo(f"Hello, {name}!")

def test_hello_command(runner):
    result = runner.invoke(args="hello")
    assert "World" in result.output

    result = runner.invoke(args=["hello", "--name", "Flask"])
    assert "Flask" in result.output

def test_logout_redirect(bot):
    response = bot.get("/logout")
    # Check that there was one redirect response.
    assert len(response.history) == 1
    # Check that the second request was to the index page.
    assert response.request.path == "/"
