from neo4j import GraphDatabase
import pandas as pd

driver = GraphDatabase.driver("bolt://localhost:7687",
                              auth=("neo4j", "password123"))

with driver.session() as s:
    r = s.run("""
        CALL gds.pageRank.stream('socialGraph')
        YIELD nodeId, score
        RETURN gds.util.asNode(nodeId).id AS id,
               round(score*1000)/1000 AS pagerank
        ORDER BY pagerank DESC LIMIT 100
    """)
    pd.DataFrame([x.data() for x in r]).to_csv('centrality_results.csv', index=False)
    print("centrality_results.csv cree !")

    r2 = s.run("""
        MATCH (u:User)
        WHERE u.degree_out > 50 AND u.degree_in < 10
        RETURN u.id AS id, u.degree_out AS suit,
               u.degree_in AS suivi_par
    """)
    pd.DataFrame([x.data() for x in r2]).to_csv('bots_detected.csv', index=False)
    print("bots_detected.csv cree !")

driver.close()
