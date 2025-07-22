import os
from typing import List
from interface.base_datastore import DataItem
from interface.base_indexer import BaseIndexer
from docling.document_converter import DocumentConverter
from docling.chunking import HybridChunker, DocChunk


class Indexer(BaseIndexer):
    def __init__(self):
        self.converter = DocumentConverter()
        self.chunker = HybridChunker()
        # Disable tokenizers parallelism to avoid OOM errors.
        os.environ["TOKENIZERS_PARALLELISM"] = "false"

    def index(self, document_paths: List[str]) -> List[DataItem]:
        items = []
        for document_path in document_paths:
            document = self.converter.convert(document_path).document
            chunks: List[DocChunk] = self.chunker.chunk(document)
            items.extend(self._items_from_chunks(chunks))
        return items

    def _items_from_chunks(self, chunks: List[DocChunk]) -> List[DataItem]:
        items = []
        for i, chunk in enumerate(chunks):
            content_headings = "## " + ", ".join(chunk.meta.headings)
            content_text = f"{content_headings}\n{chunk.text}"
            source = f"{chunk.meta.origin.filename}:{i}"
            item = DataItem(content=content_text, source=source)
            items.append(item)

        return items
