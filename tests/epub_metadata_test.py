import epub_metadata


class TestEpubMetadata():
    def setup_class(self):
        self.epub = epub_metadata.epub(
            'tests\Alices Adventures in Wonderland.epub')

    def test_title(self):
        title = self.epub.metadata.title
        assert title == "Alice's Adventures in Wonderland"

    def test_creator(self):
        creator = self.epub.metadata.creator
        assert creator == 'Lewis Carroll'

    def test_description(self):
        description = self.epub.metadata.description
        assert description == ''

    def test_publisher(self):
        publisher = self.epub.metadata.publisher
        assert publisher == 'D. Appleton and Co'

    def test_identifier(self):
        identifier = self.epub.metadata.identifier
        assert identifier == 'eb2934ae-bb1a-4652-bce7-9f78fc5ca496'

    def test_date(self):
        date = self.epub.metadata.date
        assert date == '1865-07-04'
