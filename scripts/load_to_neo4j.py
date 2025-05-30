import pandas as pd
from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

# Load Neo4j credentials
load_dotenv()
NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USER = os.getenv("NEO4J_USER")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

# Connect to Neo4j
driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

def create_graph(tx, trial):
    tx.run("""
        MERGE (t:Trial {nct_number: $nct_number})
        SET t.title = $title, t.status = $status, t.url = $url, t.age = $age, t.sex = $sex, t.study_type = $study_type

        FOREACH (cond IN $conditions |
            MERGE (c:Condition {name: cond})
            MERGE (t)-[:HAS_CONDITION]->(c)
        )

        FOREACH (intv IN $interventions |
            MERGE (i:Intervention {name: intv})
            MERGE (t)-[:HAS_INTERVENTION]->(i)
        )

        MERGE (s:Sponsor {name: $sponsor})
        MERGE (t)-[:SPONSORED_BY]->(s)

        FOREACH (collab IN $collaborators |
            MERGE (c:Collaborator {name: collab})
            MERGE (t)-[:COLLABORATED_BY]->(c)
        )
    """, **trial)

def parse_list_field(field):
    if pd.isna(field):
        return []
    return [item.strip() for item in field.split(";") if item.strip()]

def main():
    df = pd.read_csv("data/ctg-studies.csv", sep=",")  # adjust delimiter if needed

    with driver.session() as session:
        for _, row in df.iterrows():
            trial_data = {
                "nct_number": row["NCT Number"],
                "title": row["Study Title"],
                "status": row["Study Status"],
                "url": row["Study URL"],
                "age": row["Age"],
                "sex": row["Sex"],
                "study_type": row["Study Type"],
                "conditions": parse_list_field(row["Conditions"]),
                "interventions": parse_list_field(row["Interventions"]),
                "sponsor": row["Sponsor"],
                "collaborators": parse_list_field(row["Collaborators"])
            }
            session.execute_write(create_graph, trial_data)

    print("Data loaded to Neo4j.")

if __name__ == "__main__":
    main()
