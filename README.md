# QuMARA

**Intent-Aware Multi-Agent Reinforcement Learning Framework for Adaptive Post-Quantum Authentication Orchestration in Cloud-Native Microservice Networks**

## Project Overview

QuMARA is a research-grade framework designed for dynamic runtime selection of post-quantum JWT authentication algorithms in cloud-native microservice architectures. Using Multi-Agent Reinforcement Learning (MARL), the system optimizes authentication policies based on system metrics, security requirements, and operational intent profiles.

### Key Features

- **Multi-Agent Reinforcement Learning**: Independent agents for each microservice learning optimal authentication policies
- **Post-Quantum Cryptography**: Support for ML-DSA and SLH-DSA algorithm families
- **Intent-Driven**: Runtime selection based on security, performance, and resource efficiency profiles
- **Cloud-Native**: Docker and Kubernetes deployment ready
- **Production-Grade**: Type-safe Python, comprehensive logging, monitoring, and metrics
- **Microservice Architecture**: Example services with decoupled authentication
- **RL Training**: Gymnasium-based environment with Stable-Baselines3 agents

## Architecture

```
qumara/
├── config/                 # YAML configuration files
├── data/                   # Raw, processed, benchmarks, and results
├── rl/                     # Reinforcement learning environment and agents
│   ├── environment/        # Gymnasium-based custom environments
│   ├── agents/             # MARL agent implementations
│   ├── models/             # Neural network models
│   ├── training/           # Training loops and strategies
│   └── evaluation/         # Evaluation and metrics
├── microservices/          # Example cloud-native services
├── k8s/                    # Kubernetes manifests
├── scripts/                # Utility and automation scripts
├── tests/                  # Unit and integration tests
├── utils/                  # Reusable utility modules
└── docs/                   # Documentation
```

## Installation

### Prerequisites

- Python 3.11+
- pip or conda
- Docker and Docker Compose (for containerized deployment)
- kubectl and k3d (for Kubernetes deployment)

### Setup

```bash
# Clone repository
git clone https://github.com/Karthi123k/Qumara1.git
cd Qumara1

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Load environment configuration
cp .env.example .env
```

### Docker Setup

```bash
# Build all services
docker-compose build

# Start services
docker-compose up -d
```

### Kubernetes Setup

```bash
# Create k3d cluster
k3d cluster create qumara

# Deploy QuMARA
kubectl create namespace qumara
kubectl apply -f k8s/ -n qumara
```

## Dependencies

### Core ML/RL
- **torch**: Deep learning framework
- **gymnasium**: RL environment API
- **stable-baselines3**: RL algorithms (PPO, DQN, A3C)
- **pettingzoo**: Multi-agent RL

### API & Services
- **fastapi**: Async web framework
- **uvicorn**: ASGI server
- **pydantic**: Data validation

### Monitoring & Observability
- **prometheus-client**: Metrics collection
- **psutil**: System resource monitoring

### Data & Visualization
- **pandas**: Data manipulation
- **numpy**: Numerical computing
- **scipy**: Scientific computing
- **matplotlib**: Data visualization

### Cloud & Container
- **docker**: Container runtime
- **kubernetes**: Container orchestration

## Project Structure

```
qumara/
├── __init__.py
├── README.md
├── LICENSE
├── requirements.txt
├── pyproject.toml
├── .gitignore
├── .env.example
├── docker-compose.yml
│
├── config/
│   ├── __init__.py
│   ├── config.yaml              # Main configuration
│   ├── algorithms.yaml          # Post-quantum algorithms
│   ├── training.yaml            # RL training parameters
│   ├── intent_profiles.yaml     # Intent definitions
│   └── logging.yaml             # Logging configuration
│
├── data/
│   ├── raw/                     # Raw experimental data
│   ├── processed/               # Preprocessed data
│   ├── benchmarks/              # Benchmark results
│   ├── results/                 # RL training results
│   ├── plots/                   # Generated plots
│   └── logs/                    # Application logs
│
├── rl/
│   ├── __init__.py
│   ├── environment/
│   │   ├── __init__.py
│   │   ├── base.py              # Base environment
│   │   └── auth_env.py          # Authentication environment
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── base.py              # Base agent
│   │   └── policy_agent.py      # Policy agents
│   ├── models/
│   │   ├── __init__.py
│   │   └── networks.py          # Neural network models
│   ├── training/
│   │   ├── __init__.py
│   │   ├── trainer.py           # Training loop
│   │   └── callbacks.py         # RL callbacks
│   └── evaluation/
│       ├── __init__.py
│       └── metrics.py           # Evaluation metrics
│
├── microservices/
│   ├── __init__.py
│   ├── auth_service/            # Authentication service
│   ├── user_service/            # User service
│   ├── customer_service/        # Customer service
│   ├── account_service/         # Account service
│   ├── payment_service/         # Payment service
│   ��── transaction_service/     # Transaction service
│   ├── fraud_service/           # Fraud detection
│   └── gateway/                 # API Gateway
│
├── k8s/
│   ├── namespace.yaml           # K8s namespace
│   ├── traefik/                 # Traefik ingress
│   ├── prometheus/              # Prometheus monitoring
│   ├── grafana/                 # Grafana dashboards
│   ├── services/                # Service definitions
│   ├── deployments/             # K8s deployments
│   ├── ingress/                 # Ingress rules
│   ├── configmaps/              # ConfigMaps
│   └── secrets/                 # Secrets
│
├── scripts/
│   ├── __init__.py
│   ├── train_agents.py          # Training script
│   ├── evaluate_agents.py       # Evaluation script
│   ├── benchmark.py             # Benchmarking
│   └── deploy.py                # Deployment script
│
├── tests/
│   ├── __init__.py
│   ├── test_config.py           # Configuration tests
│   ├── test_utils.py            # Utility tests
│   ├── test_environment.py      # Environment tests
│   └── test_agents.py           # Agent tests
│
├── utils/
���   ├── __init__.py
│   ├── config.py                # Configuration loader
│   ├── logger.py                # Logging utility
│   ├── exceptions.py            # Custom exceptions
│   ├── metrics.py               # Metrics utilities
│   ├── file_utils.py            # File operations
│   ├── csv_utils.py             # CSV operations
│   ├── timer.py                 # Timing utility
│   ├── network_utils.py         # Network utilities
│   └── visualization.py         # Plotting utilities
│
├── constants.py                 # Global constants
├── models.py                    # Data models & dataclasses
└── base.py                      # Abstract base classes
```

## Execution Workflow

### 1. Configuration

```python
from qumara.utils.config import ConfigLoader

config = ConfigLoader.load('config/config.yaml')
```

### 2. Environment Setup

```python
from qumara.rl.environment.auth_env import AuthenticationEnvironment

env = AuthenticationEnvironment(config=config)
```

### 3. Agent Training

```python
from qumara.rl.training.trainer import Trainer

trainer = Trainer(env=env, config=config)
trainer.train(episodes=10000)
```

### 4. Evaluation

```python
from qumara.rl.evaluation.metrics import EvaluationMetrics

metrics = EvaluationMetrics(config=config)
results = metrics.evaluate(agent=trained_agent)
```

### 5. Deployment

```bash
# Docker Deployment
docker-compose up -d

# Kubernetes Deployment
kubectl apply -f k8s/
```

## Post-Quantum Algorithms

QuMARA supports the following NIST-standardized post-quantum algorithms:

### ML-DSA (Module-Lattice-Based Digital Signature Algorithm)
- ML-DSA-44 (128-bit security)
- ML-DSA-65 (192-bit security)
- ML-DSA-87 (256-bit security)

### SLH-DSA (Stateless Hash-Based Digital Signature Algorithm)
- SLH-DSA-128 (128-bit security)
- SLH-DSA-192 (192-bit security)
- SLH-DSA-256 (256-bit security)

## Intent Profiles

Runtime authentication policies can be optimized for:

1. **Security First**: Maximize security level
2. **Performance First**: Minimize latency
3. **Balanced**: Optimize across all metrics
4. **Resource Efficient**: Minimize CPU/Memory
5. **Network Efficient**: Minimize bandwidth

## Monitoring & Observability

QuMARA integrates with:

- **Prometheus**: Metrics collection and storage
- **Grafana**: Dashboards and visualization
- **Structured Logging**: JSON and file-based logging

## Testing

```bash
# Run all tests
pytest

# With coverage
pytest --cov=qumara

# Specific test file
pytest tests/test_config.py -v
```

## Code Quality

```bash
# Format code
black qumara/
isort qumara/

# Lint
pylint qumara/
flake8 qumara/

# Type checking
mypy qumara/
```

## Performance Metrics

QuMARA tracks:

- **Authentication Latency**: Time to sign JWT
- **Verification Latency**: Time to verify JWT
- **Resource Utilization**: CPU and memory usage
- **Network Overhead**: JWT and signature sizes
- **Authentication Intent**: Policy selection rationale
- **System Availability**: Service uptime
- **Security Level**: Algorithm security category

## Citation

If you use QuMARA in your research, please cite:

```bibtex
@article{qumara2025,
  title={QuMARA: Intent-Aware Multi-Agent Reinforcement Learning Framework for Adaptive Post-Quantum Authentication Orchestration in Cloud-Native Microservice Networks},
  author={Contributors, QuMARA},
  journal={Computer Communications},
  year={2025},
  publisher={Elsevier}
}
```

## License

MIT License - See LICENSE file for details

## Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Commit changes with clear messages
4. Push to branch
5. Open a Pull Request

## Contact

For questions and support, open an issue on GitHub.
