from abc import ABCMeta, abstractmethod
from typing import List, TypeVar, Type, Dict, Union
from common.database import Database

T = TypeVar('T', bound='Model')


class Model(metaclass=ABCMeta):
    # need type hinting to get rid of warnings and reinforce attribute
    collection: str
    _id: str

    def __init__(self, *args, **kwargs):
        pass

    def save_to_mongo(self):
        """ upsert: update if _id exists, otherwise insert """
        Database.update(self.collection,
                        {"_id": self._id},
                        self.json())

    def remove_from_mongo(self):
        Database.remove(self.collection,
                        {"_id": self._id})

    @classmethod
    def get_by_id(cls: Type[T], _id: str) -> T:
        # Item.get_by_id() -> Item,
        # Alert.get_by_id() -> Alert
        return cls.find_one_by(attribute="_id",  value=_id)

    @abstractmethod
    def json(self) -> Dict:
        raise NotImplementedError

    @classmethod
    def all(cls: Type[T]) -> List[T]:
        elements_from_db = Database.find(collection=cls.collection,
                                         query={})
        return [cls(**element) for element in elements_from_db]

    @classmethod
    def find_one_by(cls: Type[T], attribute: str, value: Union[str, Dict]) -> T:
        # Item.find_one_by('url', 'https://aaa.com')
        return cls(**Database.find_one(collection=cls.collection,
                                       query={attribute: value}))

    @classmethod
    def find_many_by(cls: Type[T], attribute: str, value: str) -> List[T]:
        return [cls(**element) for element in Database.find(cls.collection, {attribute: value})]


