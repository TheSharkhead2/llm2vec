from .dataset import DataSample, TrainSample, Dataset
from accelerate.logging import get_logger

logger = get_logger(__name__, log_level="INFO")


class ArXivAbstract(Dataset):
    def __init__(
        self,
        dataset_name: str = "ArXivAbstract",
        split: str = "validation",
        file_path: str = "cache/arxiv_abstracts.txt",
    ):
        self.dataset_name = dataset_name
        self.split = split
        self.data = []
        self.load_data(file_path)

    def __len__(self):
        return len(self.data)

    def load_data(self, file_path: str = None):
        logger.info(f"Loading arXiv abstracts data from {file_path}...")
        id_ = 0
        with open(file_path, "r") as f:
            for line in f:
                line = line.strip()
                self.data.append(
                    DataSample(
                        id_=id_,
                        query=line,
                        positive=line,
                    )
                )
                id_ += 1
        logger.info(f"Loaded {len(self.data)} samples.")

    def __getitem__(self, index):
        sample = self.data[index]
        if self.split == "train":
            return TrainSample(texts=[sample.query, sample.positive], label=1.0)
        elif self.split == "validation":
            assert False, "ArXivAbstract does not have a validation split."
