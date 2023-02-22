from typing import TYPE_CHECKING
from urllib.parse import quote_plus

import pymongo
from django.conf import settings

if TYPE_CHECKING:
    from pymongo.collection import Collection
    from pymongo.database import Database

__all__ = ["SceneGraph"]


client = pymongo.MongoClient(
    f"mongodb://{quote_plus(settings.MONGODB_USER)}:{quote_plus(settings.MONGODB_PASSWORD)}@{settings.MONGODB_HOST}"
)

db: "Database" = client.release
SceneGraph: "Collection" = db.scene_graph
