🧠 Clinical Trials Graph using Neo4j

This project loads clinical trial data into a Neo4j graph database and models the relationships between trials, conditions, interventions, sponsors, and collaborators. It enables graph-based exploration of clinical research data from ClinicalTrials.gov.
📊 Graph Schema

Each clinical trial is connected to related entities through clear relationships:

(Trial)-[:HAS_CONDITION]->(Condition)
(Trial)-[:HAS_INTERVENTION]->(Intervention)
(Trial)-[:SPONSORED_BY]->(Sponsor)
(Trial)-[:COLLABORATED_BY]->(Collaborator)
