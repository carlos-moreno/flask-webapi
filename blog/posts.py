from __future__ import annotations
from blog.database import mongo
from datetime import datetime
import pymongo

def get_all_posts(published: bool = True):
    """Return all posts
    """
    posts = mongo.db.posts.find({"published": published})
    return posts.sort("date", pymongo.DESCENDING)


def get_post_by_slug(slug: str) -> dict:
    """Return one post by slug
    """
    post = mongo.db.posts.find_one({"slug": slug})
    return post

def update_post_by_slug(slug: str, data: dict) -> dict:
    """Update the post by slug
    """
    # TODO: Se o título mudar, atualizar o slug (falhar se já existir)
    return mongo.db.posts.find_one_and_update({"slug": slug}, {"$set": data})

def new_post(title: str, content: str, published: bool = True) -> str:
    """Create a new post
    """
    slug = title.replace(" ", "-").replace("_", "-").lower()
    # TODO: Refatorar a criação do slug removendo acentos
    # TODO: Verificar se post com este slug já existe
    mongo.db.posts.insert_one(
        {
            "title": title,
            "content": content,
            "published": published,
            "slug": slug,
            "date": datetime.now(),
        }
    )
    return slug
