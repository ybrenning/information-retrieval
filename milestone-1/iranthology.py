import ir_datasets
from ir_datasets.formats import JsonlDocs, TrecXmlQueries
from typing import NamedTuple
from ir_datasets.datasets.base import Dataset

class IRAnthologyDocument(NamedTuple):
    doc_id: str
    text: str

    def default_text(self):
        return self.text

ir_datasets.registry.register('iranthology-ir-lab-sose2023-information-retrievers', Dataset(
    JsonlDocs(ir_datasets.util.PackageDataFile(path="datasets_in_progress/milestone-1-documents.jsonl"), doc_cls=IRAnthologyDocument, lang='en'),
    TrecXmlQueries(ir_datasets.util.PackageDataFile(path="datasets_in_progress/milestone-1-topics.xml"), lang='en'),
))
