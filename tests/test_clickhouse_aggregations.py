from tests.util import ClickhouseTestCase

from farmsubsidy_store import aggregations


class ClickhouseAggregationsTestCase(ClickhouseTestCase):
    def test_clickhouse_aggregations(self):
        by_country = aggregations.AGGREGATIONS["by_country"]
        by_year = aggregations.AGGREGATIONS["by_year"]

        df = by_country(self.driver)
        self.assertEqual(len(df), 2)
        self.assertSetEqual(set(df["country"].unique()), set(["CZ", "LU"]))

        df = by_year(self.driver)
        self.assertEqual(len(df), 2)
        self.assertSetEqual(set(df["year"].unique()), set(["2015", "2019"]))

        # subset aggregations
        df = by_year(self.driver, country="LU")
        self.assertEqual(len(df), 1)
        self.assertSetEqual(set(df["year"].unique()), set(["2019"]))
