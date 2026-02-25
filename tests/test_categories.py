from abc import ABC
import unittest

from vkbottle_types.categories import (
    CATEGORIES,
    APICategories,
)


class FakeAPI(APICategories, ABC):
    def api_instance(self):
        """A real API client is not required for these tests."""
        return None


class TestAPICategories(unittest.TestCase):

    def setUp(self):
        self.api = FakeAPI()


    def test_all_categories_are_accessible(self):
        """
        All categories defined in CATEGORIES must be accessible via getattr
        without raising any exceptions.
        """
        for category in CATEGORIES:
            try:
                getattr(self.api, category)
            except Exception as e:
                self.fail(f"Category '{category}' raised {e!r}")


    def test_unknown_category_raises_attribute_error(self):
        """Accessing an unknown category must raise AttributeError."""
        with self.assertRaises(AttributeError):
            getattr(self.api, "other_category")


if __name__ == "__main__":
    unittest.main()