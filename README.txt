🧠 Clinical Trials Graph using Neo4j

This project loads clinical trial data into a Neo4j graph database and models the relationships between trials, conditions, interventions, sponsors, and collaborators. It enables graph-based exploration of clinical research data from ClinicalTrials.gov.
📊 Graph Schema

Each clinical trial is connected to related entities through clear relationships:

(Trial)-[:HAS_CONDITION]->(Condition)
(Trial)-[:HAS_INTERVENTION]->(Intervention)
(Trial)-[:SPONSORED_BY]->(Sponsor)
(Trial)-[:COLLABORATED_BY]->(Collaborator)

📥 Load Clinical Trial Data

Place your clinical_trials.csv file inside the data/ folder.

Then run the script to load the data into Neo4j:

python scripts/load_to_neo4j.py
🧪 Example Mapping

A sample CSV row like:

NCT Number: NCT001
Conditions: Diabetes; Obesity
Interventions: Metformin
Sponsor: NIH
Collaborators: Harvard; UCSF

Creates this graph:

(Trial {nct_number: "NCT001"})
→ HAS_CONDITION → (Condition {name: "Diabetes"})
→ HAS_CONDITION → (Condition {name: "Obesity"})
→ HAS_INTERVENTION → (Intervention {name: "Metformin"})
→ SPONSORED_BY → (Sponsor {name: "NIH"})
→ COLLABORATED_BY → (Collaborator {name: "Harvard"})
→ COLLABORATED_BY → (Collaborator {name: "UCSF"})
🔍 Visualize in Neo4j Browser

Open Neo4j browser at http://localhost:7474
Login using the credentials in your .env file.

To view a subgraph, run this Cypher query:

MATCH (t:Trial)-[r]->(n)
RETURN t, r, n
LIMIT 50

You’ll see an interactive graph view showing relationships between trials and related entities.
📜 License

MIT License
