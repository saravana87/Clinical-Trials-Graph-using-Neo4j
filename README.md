# 🧠 Clinical Trials Graph using Neo4j

This project transforms clinical trial data from [ClinicalTrials.gov](https://clinicaltrials.gov/) into a graph database using Neo4j. It allows you to explore relationships between trials, conditions, interventions, sponsors, and collaborators.

---
## 📊 Graph Schema

Each clinical trial becomes a node connected to related entities:

**
(Trial)-[:HAS_CONDITION]->(Condition)
(Trial)-[:HAS_INTERVENTION]->(Intervention)
(Trial)-[:SPONSORED_BY]->(Sponsor)
(Trial)-[:COLLABORATED_BY]->(Collaborator)
---

## 📦 Setup Instructions

### 1. Clone and Install

```bash
git clone https://github.com/your-username/clinical-neo4j.git
cd clinical-neo4j
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

**# Load Data**
python scripts/load_to_neo4j.py
