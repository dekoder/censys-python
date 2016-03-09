import json
import unittest

from censys import CensysAPIBase


class CensysIPv4(CensysAPIBase):

    def search(self, query, fields=None):
        if fields is None:
            fields = []
        page = 1
        pages = float('inf')
        data = {
            "query": query,
            "page": page,
            "fields": fields
        }

        while page <= pages:
            payload = self._post("search/ipv4", data=data)
            pages = payload['metadata']['pages']
            page += 1

            for result in payload["results"]:
                yield result

    def view(self, ip):
        return self._get("/".join(("view", "ipv4", ip)))

    def report(self, query, field, buckets=50):
        data = {
            "query": query,
            "field": field,
            "buckets": int(buckets)
        }
        return self._post("report/ipv4", data=data)


class CensysIPv4Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._api = CensysIPv4()

    def testGet(self):
        print json.dumps(self._api.view("84.206.102.184"))
        print "\n\n\n"

    def testEmptySearch(self):
        print json.dumps(self._api._post("search/ipv4", data={"query1":"query"}))
        print "\n\n\n"

    def testSearch(self):
        print json.dumps(self._api.search("*"))
        print "\n\n\n"

    def testReport(self):
        print json.dumps(self._api.report("*", "protocols", 5))
        print "\n\n\n"


if __name__ == "__main__":
    unittest.main()
