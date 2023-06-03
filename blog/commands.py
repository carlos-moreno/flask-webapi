import click

from blog.posts import (
    get_all_posts,
    get_post_by_slug,
    update_post_by_slug,
    new_post
)

@click.group()
def post():
    """Manage blog posts."""

@post.command()
@click.option("--title")
@click.option("--content")
def new(title, content):
    """Add new post to database."""
    new  = new_post(title=title, content=content)
    click.echo(f"New post created {new}")

@post.command("list")
def _list():
    """Lists all posts."""
    for post in get_all_posts():
        click.echo(post)
        click.echo("*" * 79)

@post.command()
@click.argument("slug")
def get(slug):
    """Get post by slug."""
    post = get_post_by_slug(slug)
    click.echo(post or "post not found!")

@post.command()
@click.argument("slug")
@click.option("--content", default=None, type=str)
@click.option("--publish", default=None, type=str)
def update(slug, content, publish):
    """Update post by slug."""
    data = {}
    if content:
        data["content"] = content
    if publish:
        data["publish"] = publish.lower() == "true"
    update_post_by_slug(slug, data)
    click.echo("Post updated.")

# TODO: Criar comando para despublicar o posts

def configure(app):
    app.cli.add_command(post)
