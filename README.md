# Python Network Automation Toolkit

A Python-based network automation tool designed to execute
commands across multiple Cisco IOS devices using SSH.

## Features
- YAML-based device inventory
- Multi-device command execution
- Graceful failure handling
- Centralized logging (console + file)
- CLI interface
- Clean, modular architecture

## Project Structure
```bash
python-network-automation-toolkit/
├── inventory/
│   └── devices.yaml
├── logs/
│   └── app.log
├── network/
│   ├── connector.py
│   ├── executor.py
│   └── inventory.py
├── utils/
│   └── logger.py
├── .gitignore
├── cli.py
├── README.md
└── requirements.txt
```

## Usage
```bash
python cli.py --command "show ip interface brief"
```

## Architecture Overview
The toolkit follows a layered design:

- CLI handles user input
- Inventory loader provides device data
- Executor coordinates multi-device execution
- Connector manages SSH lifecycle per device
- Logger provides centralized observability

This separation improves maintainability,
testability, and extensibility.
