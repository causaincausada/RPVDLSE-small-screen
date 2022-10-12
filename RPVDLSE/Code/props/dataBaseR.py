import datetime
import pymongo
from pymongo import errors
from Code.props.result import Result


class DataBaseR:

    def __init__(self, mongo_host, mongo_port, mongo_timeout):
        self.mongo_uri = "mongodb://"+mongo_host+":"+mongo_port+"/"
        try:
            self.client = pymongo.MongoClient(self.mongo_uri, serverSelectionTimeoutMS=mongo_timeout)
            self.client.server_info()
            self.db = self.client.RPVDLSE
            self.collection_results = self.db.results
        except pymongo.errors.ServerSelectionTimeoutError as timeout_error:
            print(timeout_error)
        except pymongo.errors.InvalidURI as invalid_uri:
            print(invalid_uri)
        except pymongo.errors.ConnectionFailure as connection_error:
            print(connection_error)

    def on_connect(self):
        try:
            self.collection_results.find_one()
            return True
        except pymongo.errors.ServerSelectionTimeoutError as timeout_error:
            print(timeout_error)
            return False
        except pymongo.errors.InvalidURI as invalid_uri:
            print(invalid_uri)
            return False
        except pymongo.errors.ConnectionFailure as connection_error:
            print(connection_error)
            return False
        except AttributeError:
            return False

    def get_result(self):
        pass

    def get_results(self,
                    date_begin: datetime.datetime,
                    date_end: datetime.datetime,
                    hour_begin: datetime.datetime,
                    hour_end: datetime.datetime,
                    plate: str,
                    name: str):
        if plate == "" and name == "":
            query_filters = {"$and": [{
                                "$and": [{
                                    "date": {"$gte": date_begin}}, {
                                    "date": {"$lte": date_end}}
                                ]
                            }, {
                                "$and": [{
                                    "hour": {"$gte": hour_begin}}, {
                                    "hour": {"$lte": hour_end}}
                                ]
                            }]}
        elif plate == "":
            query_filters = {"$and": [{
                                "$and": [{
                                    "date": {"$gte": date_begin}}, {
                                    "date": {"$lte": date_end}}
                                ]
                            }, {
                                "$and": [{
                                    "hour": {"$gte": hour_begin}}, {
                                    "hour": {"$lte": hour_end}}
                                ]
                            }, {
                                "name": name
                            }]}
        elif name == "":
            query_filters = {"$and": [{
                                "$and": [{
                                    "date": {"$gte": date_begin}}, {
                                    "date": {"$lte": date_end}}
                                ]
                            }, {
                                "$and": [{
                                    "hour": {"$gte": hour_begin}}, {
                                    "hour": {"$lte": hour_end}}
                                ]
                            }, {
                                "result": plate
                            }]}
        else:
            query_filters = {"$and": [{
                                "$and": [{
                                    "date": {"$gte": date_begin}}, {
                                    "date": {"$lte": date_end}}
                                ]
                            }, {
                                "$and": [{
                                    "hour": {"$gte": hour_begin}}, {
                                    "hour": {"$lte": hour_end}}
                                ]
                            }, {
                            "name": name
                            }, {
                            "result": plate
                            }]}
        response = self.collection_results.find(query_filters)
        return response

    def push_result(self, result=Result()):
        push = {
            "name": result.name,
            "date": result.date,
            "hour": result.hour,
            "result": result.result
        }
        try:
            self.collection_results.insert_one(push)
            return True
        except pymongo.errors.WriteError as write_error:
            print(write_error)
            return False

    def connection_close(self):
        self.client.close()
