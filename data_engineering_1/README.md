# Centralized Medical Data Platform

**Petabyte-scale health-record repository** — streaming ingestion into a secure, centralized lake enabling advanced ML/DL at scale.

## Overview
A HIPAA-compliant data platform for centralized medical records ingestion, storage, and analytics. Designed for petabyte-scale streaming workloads with real-time processing capabilities.

## Challenge
- **HIPAA-grade security with streaming throughput**: Encrypting data in transit and at rest while maintaining sub-second ingestion latency

## Stack
- `Spark`
- `Kafka`
- `Flask`
- `Cloudera`
- `Presto`
- `Python`

## Architecture
```
[Data Sources] → [Kafka] → [Spark Streaming] → [HDFS/S3] → [Presto/Flask API]
                                    ↓
                              [ML/DL Pipeline]
```

## Components
- **Ingestion Layer**: Kafka clusters with exactly-once semantics
- **Processing Layer**: Spark Structured Streaming for ETL and feature engineering
- **Storage Layer**: Encrypted HDFS with columnar format (Parquet/ORC)
- **Query Layer**: Presto for interactive SQL, Flask REST APIs for model serving
- **Security**: End-to-end encryption, audit logging, role-based access control

## Results
See [Presentation](Presentation.pdf) for architecture diagrams, performance benchmarks, and compliance details.

## Artifacts
- `Presentation.pdf` — Architecture and benchmark slides
- `pics/pipeline.png` — Data flow diagram