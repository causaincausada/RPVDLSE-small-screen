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
            self.collection_ip_cam = self.db.ipcam
            self.collection_results = self.db.results
        except pymongo.errors.PyMongoError:
            pass

    def on_connect(self):
        try:
            self.collection_results.find_one()
            return True
        except pymongo.errors.PyMongoError:
            return False
        except AttributeError:
            return False

    def disconnect(self):
        try:
            self.client.close()
            return True
        except pymongo.errors.PyMongoError as mr:
            print(mr)
            return False
        except AttributeError:
            return True

    def get_results(self,
                    date_begin: datetime.datetime,
                    date_end: datetime.datetime,
                    hour_begin: datetime.datetime,
                    hour_end: datetime.datetime,
                    plate: str,
                    name: []):
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
                                "name": {"$regex": '^'+name}
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
                                "result": {"$regex": '^'+plate}
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
                            "name": {"$regex": '^'+name}
                            }, {
                            "result": {"$regex": '^'+plate}
                            }]}
        response = self.collection_results.find(query_filters)
        return response

    def get_size(self):
        try:
            cursor = self.collection_results.find()
            tam = 0
            for a in cursor:
                tam += 1
            return tam
        except pymongo.errors.PyMongoError:
            return -1

    def push_result(self, result=Result()):
        push = {
            "name": str(result.name),
            "date": result.date,
            "hour": result.hour,
            "result": str(result.result)
        }
        try:
            self.collection_results.insert_one(push)
            return True
        except pymongo.errors.WriteError as write_error:
            print(write_error)
            return False
        except AttributeError:
            return False

    def set_ip_cam(self, protection, protocol, user, passw, ip, port, ext):
        push = {
            "protection": protection,
            "protocol": protocol,
            "user": user,
            "pass": passw,
            "ip": ip,
            "port": port,
            "ext": ext
        }
        try:
            self.drop_ip_cam()
            self.collection_ip_cam.insert_one(push)
            return True
        except pymongo.errors.WriteError as write_error:
            print(write_error)
            return False
        except AttributeError:
            return False

    def get_ip_cam(self):
        try:
            cursor = self.collection_ip_cam.find()
            return cursor
        except pymongo.errors.PyMongoError:
            return -1

    def drop_ip_cam(self):
        self.collection_ip_cam.drop()

    def drop(self):
        self.collection_results.drop()

    def connection_close(self):
        self.client.close()
