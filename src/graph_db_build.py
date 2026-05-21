"""
load_pool_chemistry.py
======================
Carga el grafo de química de piscinas en Neo4j Aura
a partir de los archivos CSV de nodos y relaciones.

Requisitos:
    pip install neo4j pandas python-dotenv

Uso:
    python load_pool_chemistry.py
"""

import os
import pandas as pd
from neo4j import GraphDatabase
from dotenv import load_dotenv

# ─────────────────────────────────────────────
# 1. CONFIGURACIÓN
# ─────────────────────────────────────────────

load_dotenv()  # Carga variables desde .env si existe

NEO4J_URI      = os.getenv("NEO4J_URI")
NEO4J_USER     = os.getenv("NEO4J_USER")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")
NEO4J_DATABASE = os.getenv("NEO4J_DATABASE")

# Rutas a los CSV (ajustá si están en otra carpeta)
NODES_CSV = r"data\documentos\pool_chemistry_nodes.csv"
EDGES_CSV = r"data\documentos\pool_chemistry_edges.csv"


# ─────────────────────────────────────────────
# 2. CONEXIÓN
# ─────────────────────────────────────────────

def get_driver():
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    driver.verify_connectivity()
    print("✅ Conexión exitosa a Neo4j Aura")
    return driver


# ─────────────────────────────────────────────
# 3. CONSTRAINTS E ÍNDICES
# ─────────────────────────────────────────────

LABELS = ["Parameter", "Equipment", "Chemical", "Symptom"]

def create_constraints(session):
    print("\n📌 Creando constraints...")
    for label in LABELS:
        query = f"CREATE CONSTRAINT IF NOT EXISTS FOR (n:{label}) REQUIRE n.id IS UNIQUE"
        session.run(query)
        print(f"   ✔ Constraint en :{label}(id)")


# ─────────────────────────────────────────────
# 4. CARGA DE NODOS
# ─────────────────────────────────────────────

def load_nodes(session, df: pd.DataFrame):
    print(f"\n📦 Cargando {len(df)} nodos...")

    query = """
    CALL apoc.merge.node(
        [$label],
        {id: $id},
        {name: $name, description: $description}
    ) YIELD node
    RETURN node
    """

    # Versión sin APOC (compatible con cualquier Neo4j):
    query = """
    MERGE (n {id: $id})
    SET n += {name: $name, description: $description}
    WITH n
    CALL apoc.create.addLabels(n, [$label]) YIELD node
    RETURN node
    """

    # ← Usamos esta versión simple que no requiere APOC:
    for _, row in df.iterrows():
        label       = row["label"]
        node_id     = row["id"]
        name        = row["name"]
        description = row.get("description", "")

        q = f"""
        MERGE (n:{label} {{id: $id}})
        SET n.name        = $name,
            n.description = $description
        """
        session.run(q, id=node_id, name=name, description=description)
        print(f"   ✔ ({label}) {node_id} — {name}")


# ─────────────────────────────────────────────
# 5. CARGA DE RELACIONES
# ─────────────────────────────────────────────

def load_edges(session, df: pd.DataFrame):
    print(f"\n🔗 Cargando {len(df)} relaciones...")

    for _, row in df.iterrows():
        source     = row["source"]
        target     = row["target"]
        rel_type   = row["type"]
        properties = row.get("properties", "")

        # Neo4j no permite tipos de relación dinámicos con parámetros,
        # por eso se inyecta con f-string (los valores vienen de tu propio CSV).
        q = f"""
        MATCH (a {{id: $source}})
        MATCH (b {{id: $target}})
        MERGE (a)-[r:{rel_type}]->(b)
        SET r.description = $description
        """
        session.run(q, source=source, target=target, description=properties)
        print(f"   ✔ ({source})-[:{rel_type}]->({target})")


# ─────────────────────────────────────────────
# 6. VERIFICACIÓN
# ─────────────────────────────────────────────

def verify(session):
    print("\n📊 Verificación del grafo:")

    print("\n  Nodos por label:")
    result = session.run(
        "MATCH (n) RETURN labels(n)[0] AS Label, count(n) AS Total ORDER BY Total DESC"
    )
    for record in result:
        print(f"   {record['Label']:20s} → {record['Total']} nodos")

    print("\n  Relaciones por tipo:")
    result = session.run(
        "MATCH ()-[r]->() RETURN type(r) AS RelType, count(r) AS Total ORDER BY Total DESC"
    )
    for record in result:
        print(f"   {record['RelType']:30s} → {record['Total']} relaciones")


# ─────────────────────────────────────────────
# 7. LIMPIEZA OPCIONAL (descomentar si querés)
# ─────────────────────────────────────────────

def clear_database(session):
    """Elimina TODOS los nodos y relaciones. Usar con cuidado."""
    print("\n🗑  Limpiando base de datos...")
    session.run("MATCH (n) DETACH DELETE n")
    print("   ✔ Base de datos vacía")


# ─────────────────────────────────────────────
# 8. MAIN
# ─────────────────────────────────────────────

def main():
    print("=" * 55)
    print("  POOL CHEMISTRY GRAPH — Carga a Neo4j Aura")
    print("=" * 55)

    # Leer CSVs
    print(f"\n📂 Leyendo {NODES_CSV}...")
    nodes_df = pd.read_csv(NODES_CSV)
    print(f"   {len(nodes_df)} nodos encontrados")

    print(f"📂 Leyendo {EDGES_CSV}...")
    edges_df = pd.read_csv(EDGES_CSV)
    print(f"   {len(edges_df)} relaciones encontradas")

    # Conectar y cargar
    driver = get_driver()

    with driver.session(database=NEO4J_DATABASE) as session:

        # Descomentá la siguiente línea si querés empezar desde cero:
        # clear_database(session)

        create_constraints(session)
        load_nodes(session, nodes_df)
        load_edges(session, edges_df)
        verify(session)

    driver.close()
    print("\n✅ Carga completada. ¡Grafo listo en Neo4j Aura!\n")


if __name__ == "__main__":
    main()