# AWS Data Pipeline - NASA CMAPs Dataset

This project processes and analyzes the NASA Commercial Modular Aero-Propulsion System Simulation (CMAPs) dataset for predictive maintenance and remaining useful life (RUL) analysis.

## Project Overview

The NASA CMAPs dataset contains sensor data from aircraft engines that simulates degradation over time. This project focuses on:
- Data preprocessing and formatting
- Feature engineering for predictive maintenance
- Remaining Useful Life (RUL) prediction models
- AWS pipeline integration for scalable data processing

## Dataset Description

The dataset includes multiple flight datasets (FD001, FD002, FD003, FD004) with:
- **Training data**: Engine run-to-failure data
- **Test data**: Engine data with known RUL values
- **RUL data**: Actual remaining useful life values for validation

### File Structure
- `train_FD00X.csv`: Training data for each flight dataset
- `test_FD00X.csv`: Test data for each flight dataset  
- `RUL_FD00X.csv`: RUL values for test data validation
- `format_cmaps.py`: Data preprocessing script

## Getting Started

### Prerequisites
- Python 3.9+
- Required packages: pandas, numpy

### Installation
1. Clone the repository:
```bash
git clone <your-repo-url>
cd aws-data-pipeline
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Usage

Run the data formatting script:
```bash
python format_cmaps.py
```

## Project Structure

```
aws-data-pipeline/
├── format_cmaps.py      # Data preprocessing script
├── nasa_cmaps/         # Original NASA CMAPs data
├── kaggle/             # Kaggle API configuration
├── venv/               # Python virtual environment
├── *.csv               # Processed dataset files
└── README.md           # This file
```

## Data Processing

The `format_cmaps.py` script:
- Loads raw NASA CMAPs data
- Applies preprocessing transformations
- Exports formatted CSV files for analysis
- Prepares data for AWS pipeline integration

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- NASA for providing the CMAPs dataset
- Kaggle for hosting the competition data
- AWS for cloud infrastructure support

## Future Enhancements

- [ ] AWS Lambda functions for data processing
- [ ] S3 integration for data storage
- [ ] SageMaker integration for ML model training
- [ ] Real-time data streaming with Kinesis
- [ ] CloudWatch monitoring and alerting
