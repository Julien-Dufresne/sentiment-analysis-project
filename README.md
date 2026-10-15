# sentiment-analysis-project
sentiment-analysis-project
## Setup
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

### Option 2: Conda
conda create -n sentiment-env python=3.11 -y
conda activate sentiment-env
pip install -r requirements.txt

## Train
python src/train.py --data data/train.csv --out models/sentiment.joblib

Add by Shyma- 15:35
Add by Shyma -15:46
Add by Shyma -15:55