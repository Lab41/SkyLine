# Market Survey of Graph Databases/Analytics Platforms

The purpose of this survey is to assess the featuresets of existing open source graph databases and graph analytics platforms and to determine which (if any) of these platforms are suitable for processing streaming updates to a large collection of graphs and triggering notifications when those updates cause certain conditions to be met or cease to be met.

The points of comparison were chosen to determine both the general usefullness of each system under consideration for different use cases including the streaming and triggering scenario described above.

## Points of comparison

|Name|Query Languages|Language Bindings/APIs Available|ACID Compliance|Eventual Consistency Support|Single Machine Mode?|Cluster Mode?|Platform Dependencies|Graph Size Limited by Memory?|Supports Edge Labels?|Supports Vertex Labels?|Supports Dynamic Graphs/Streaming?|Supports Triggering|Supports Many Graphs|Type?|Access Control Features|Supports Auditing|Open Source?|Commercial Support Available?|Major Advocates|Large Users|Supported Import/Export Formats|Active Community?|Quality of Documentation|
|:------------------|:------------------------------------|:-------------------------------------------------------------------------------------------------|:--------------------------|:-----------------------------|:---------------------|:----------------------------------------------|:----------------------|:------------------------------|:----------------------------|:----------------------------|:-----------------------------------|:--------------------|:---------------------|:-----------------------|:------------------------------------------------------------------------|:-----------------------------------------|:------------------------------------------------------|:---------------------------------------|:------------------|:---------------------------------|:--------------------------------|:--------------------------------------------------------------------|:---------------------------------------|
|Titan (HBase)|Gremlin|Any via Rexter HTTP (for triggering stored procedures)|No|No (vertex consistency only)|Yes|Yes|None|No|Yes|Yes|Yes|Yes (via EventGraph)|Yes|Database|No. (Column level at best at the Hbase Level, no cell level security)|No|Yes (Apache 2)|Yes (from primary maintainers Aurelius)|Aurelius|CISCO, LANL, Digital Reasoning...|GML, GraphML, GraphSON|Yes, recent commits, open and resolved issues.|Comphrehensive, largely up to date|
|Titan (BerkeleyDB)|Gremlin|Any via Rexter HTTP (for triggering stored procedures)|Yes|No|Yes|Yes|None|No|Yes|Yes|Yes|Yes (via EventGraph)|Yes|Database|No|No|Yes (Apache 2/AGPL/Oracle OSI License)|Yes (from primary maintainers Aurelius)|Aurelius|CISCO, LANL, Digital Reasoning...|GML, GraphML, GraphSON|Yes, recent commits, open and resolved issues.|Comphrehensive, largely up to date|
|Titan (Cassandra)|Gremlin|Any via Rexter HTTP (for triggering stored procedures)|No|Yes|Yes|Yes|None|No|Yes|Yes|Yes|Yes (via EventGraph)|Yes|Database|No. (Table level at best at the Cassandra Level, no cell based security)|At Cassandra level only.|Yes (Apache 2)|Yes (from primary maintainers Aurelius)|Aurelius|CISCO, LANL, Digital Reasoning...|GML, GraphML, GraphSON|Yes, recent commits, open and resolved issues.|Comphrehensive, largely up to date|
|GraphLab|N/A|Python/Jython/Java?|N/A|N/A|Yes|Not yet|None|No|Yes|Yes|Yes||Yes?|Compute Engine|No|No|Yes (Apache 2)|Yes (from primary maintainers GraphLab)|GraphLab, Inc.|ExxonMobile, Adobe, Zillow||Yes, recent commits, open and resolved issues.|Somewhat sparse, but covers the basics.|
|GraphX|Scala|None at present|N/A|N/A|Yes|Yes|Spark|No|Yes|Yes|No|No||Compute Engine|No|Possibly, via Spark Event Logging|Yes (Apache 2)|Yes (from Cloudera, MapR)|AmpLab, Databricks|||Yes, recent commits, open and resolved issues (to Spark repository).|Somewhat sparse, but covers the basics.|
|Stinger|N/A|C, Java, Python|No|Yes|Yes|No|None|Yes|Yes|Yes|Yes|Yes||Compute Engine|No|No|Yes (MIT)|No|GA Tech||CSV, JSON|No|Minimal|
|Apache Jena|SPARQL 1.1|JVM-based (via JDBC) for submitting SPARQL queries, Any (via HTTP) for submitting SPARQL queries.|Yes|No|Yes|No|None|No|One string valued label only|One string valued label only|Yes|Yes (on add)||Database (Triple Store)|No|Possibly, via Executiong Logging|Yes (Apache 2)|No|||RDF|Yes, recent commits, open and resolved issues.|Somewhat sparse, but covers the basics.|
|Google Cayley|Freebase MQL/Gremlin-like Javascript|None at present|Yes (using BoltDB backend)||Yes|Yes|None|No|One string valued label only|One string valued label only|Yes|||Database (Triple Store)|Only at storage backend level, if at all.|Only at storage backend level, if at all.|Yes (Apache 2)|No|||RDF|Yes, recent commits, open and resolved issues.|Minimal|
|Neo4J|Cypher|Any (via HTTP); libraries exist for Java, .NET, Python, Javascript, Ruby, PHP|Yes (single node)|Yes (cluster)|Yes|Enterprise Only; Master-Slave Replication Only|None|No|Yes|Yes|Yes|No|No|Database|No|Possibly, via Query Logging|Community Edition - GPLv3; Enterprise Edition - AGPLv3|Yes (from primary maintainers Neo4J)|Neo4J|eBay, Walmart, HP,...|Cypher script|Yes, recent commits, open and resolved issues.|Comphrehensive, largely up to date|
|iGraph|N/A|R/Python/C(++)|N/A|N/A|Yes|No|None||Yes|Yes||||Compute Engine|No|No|Yes (GPL)|No||||Yes, recent commits, open and resolved issues.|Somewhat sparse, but covers the basics.|
|Weaver|N/A|Python/C++|||Yes|Yes|HyperDex|No|Yes|Yes|Yes|Yes||Database|No||Yes (Roughly MIT license)|No||||Yes, recent commits, open and resolved issues.|Minimal|

## References

Due to the number of systems under consideration varied nature of the points on which they were compared, this section is unfortunately long, as a significant amount of research was required to answer some of the questions posed in creating the above table.

1. http://ampcamp.berkeley.edu/big-data-mini-course/graph-analytics-with-graphx.html
1. http://apache-spark-user-list.1001560.n3.nabble.com/Incrementally-add-remove-vertices-in-GraphX-td2227.html
1. http://bigdata-guide.blogspot.com/2014/01/hbase-versus-cassandra-versus-accumulo.html
1. http://bugra.github.io/work/notes/2014-04-06/graphs-databases-and-graphlab/
1. http://code.google.com/p/leveldb/
1. http://en.wikipedia.org/wiki/Graph_database
1. http://forum.graphlab.com/discussion/276/using-vertex-properties-with-graphchi
1. http://forum.graphlab.com/discussion/723/graph-query-language
1. http://github.com/apache/jena
1. http://github.com/boltdb/bolt
1. http://graphlab.com/company/press/index.html
1. http://graphlab.com/learn/userguide/index.html
1. http://graphlab.com/products/create/docs/generated/graphlab.SFrame.html
1. http://graphlab.com/products/create/docs/generated/graphlab.SGraph.html
1. http://graphlab.com/products/create/docs/generated/graphlab.SGraph.show.html
1. http://graphlab.com/products/create/docs/generated/graphlab.pagerank.create.html
1. http://graphlab.com/products/create/docs/graphlab.toolkits.html
1. http://graphlab.com/products/create/features.html
1. http://graphlab.com/products/create/open_source.html
1. http://graphlab.com/products/create/performance.html
1. http://graphlab.com/products/create/purchase-plans.html
1. http://graphlab.com/products/create/quick-start-guide.html
1. http://graphlab.com/products/create/technology.html
1. http://grokbase.com/t/gg/neo4j/13bmt4wx3x/exporting-importing-neo4j-databases
1. http://hbase.apache.org/acid-semantics.html
1. http://hbase.apache.org/book/quickstart.html
1. http://hyperdex.org/
1. http://igraph.org/c/doc/igraph-Basic.html
1. http://igraph.org/c/doc/igraph-Error.html
1. http://igraph.org/c/doc/igraph-Licenses.html
1. http://igraph.org/c/doc/igraph-Memory.html
1. http://igraph.org/c/doc/igraph-installation.html
1. http://igraph.org/c/doc/igraph-introduction.html
1. http://igraph.org/c/doc/igraph-tutorial.html
1. http://igraph.org/python/
1. http://igraph.org/python/doc/tutorial/index.html
1. http://igraph.org/python/doc/tutorial/tutorial.html
1. http://igraph.org/r/doc/degree.html
1. http://igraph.org/redirect.html
1. http://jena.apache.org/documentation/javadoc/jena/com/hp/hpl/jena/reasoner/BaseInfGraph.html
1. http://jena.apache.org/documentation/serving_data/
1. http://mail-archives.apache.org/mod_mbox/spark-issues/201410.mbox/%3CJIRA.12745859.1412380185000.188318.1412380233755@Atlassian.JIRA%3E
1. http://maxdemarzi.com/2013/03/18/permission-resolution-with-neo4j-part-1/
1. http://neo4j.com/
1. http://neo4j.com/customers/
1. http://neo4j.com/developer/cypher-query-language/
1. http://neo4j.com/developer/guide-importing-data-and-etl/
1. http://neo4j.com/developer/language-guides/
1. http://neo4j.com/docs/milestone/languages.html
1. http://neo4j.com/docs/stable/configuration-logical-logs.html
1. http://neo4j.com/docs/stable/examples-acl-structures-in-graphs.html
1. http://neo4j.com/docs/stable/graphdb-neo4j-labels.html
1. http://neo4j.com/docs/stable/rest-api-relationship-properties.html
1. http://neo4j.com/docs/stable/server-configuration.html
1. http://neo4j.com/subscriptions/
1. http://s3.thinkaurelius.com/docs/titan/current/arch-overview.html
1. http://s3.thinkaurelius.com/docs/titan/current/benefits.html
1. http://s3.thinkaurelius.com/docs/titan/current/cassandra.html
1. http://s3.thinkaurelius.com/docs/titan/current/hbase.html
1. http://select.cs.cmu.edu/code/graphlab/download.html
1. http://select.cs.cmu.edu/code/graphlab/java_jython.html
1. http://stackoverflow.com/questions/11485470/how-should-i-get-open-graph-json-object-to-pass-in-facepy-class
1. http://stackoverflow.com/questions/13587800/audits-with-spring-data-neo4j
1. http://stackoverflow.com/questions/17411071/permissions-to-be-stored-as-a-node-or-a-property
1. http://stackoverflow.com/questions/18628658/architecture-for-a-globally-distributed-neo4j
1. http://stackoverflow.com/questions/22353866/titan-know-if-a-new-vertex-or-edge-was-created
1. http://stackoverflow.com/questions/25162342/can-graphx-be-used-to-store-process-query-and-update-large-distributed-graphs
1. http://stackoverflow.com/questions/25956361/titan-db-graph-to-json
1. http://stackoverflow.com/questions/8958583/is-there-a-way-to-log-queries-on-neo4j-like-hibernate
1. http://thinkaurelius.com/2012/08/06/titan-provides-real-time-big-graph-data/
1. http://thinkaurelius.com/affiliations/
1. http://thinkaurelius.github.io/faunus/
1. http://thinkaurelius.github.io/titan/
1. http://weaver.systems/
1. http://www.apache.org/dyn/closer.cgi/hbase/stable/
1. http://www.cloudera.com/content/cloudera/en/documentation/cdh4/v4-3-0/CDH4-Security-Guide/cdh4sg_topic_8_3.html
1. http://www.cloudera.com/content/cloudera/en/products-and-services/cdh/spark.html
1. http://www.datastax.com/docs/datastax_enterprise3.0/security/GRANT#grant-user
1. http://www.datastax.com/docs/datastax_enterprise3.0/security/data_auditing
1. http://www.datastax.com/docs/datastax_enterprise3.0/security/native_authorization
1. http://www.datastax.com/documentation/cassandra/1.2/cassandra/security/secureInternalAuthorizationTOC.html
1. http://www.datastax.com/documentation/cassandra/1.2/cassandra/security/secure_about_native_authorize_c.html
1. http://www.datastax.com/documentation/cassandra/1.2/cassandra/security/secure_intro.html
1. http://www.inside-r.org/packages/cran/igraph/docs/attributes
1. http://www.oracle.com/technetwork/database/berkeleydb/db-faq-095848.html
1. http://www.oracle.com/technetwork/database/berkeleydb/downloads/licensing-098979.html
1. http://www.oracle.com/technetwork/database/database-technologies/berkeleydb/downloads/jeoslicense-086837.html
1. http://www.oracle.com/technetwork/database/database-technologies/berkeleydb/downloads/oslicense-093458.html
1. http://www.quora.com/Do-graph-databases-like-Neo4j-support-triggers-and-constraints
1. http://www.quora.com/Who-is-using-Titan-in-production
1. http://www.slideshare.net/Linkurious/introduction-to-the-graph-technologies-landscape
1. http://www.slideshare.net/robertmccoll/introduction-to-stinger
1. http://www.stingergraph.com/
1. http://www.stingergraph.com/data/uploads/presentations/2014.ppaa.graphdbs.pdf
1. http://www.stingergraph.com/data/uploads/wssspe13-arxiv.pdf
1. http://www.stingergraph.com/files/HCW-Bader-120521.pdf
1. http://www.stingergraph.com/index.php?id=documentation
1. http://www.stingergraph.com/index.php?id=getting-started
1. http://www.stingergraph.com/index.php?id=introduction
1. http://www.stingergraph.com/index.php?id=news&post=the-next-generation-of-stinger
1. http://www.stingergraph.com/index.php?id=news&post=the-next-generation-of-stinger#
1. http://www.stingergraph.com/index.php?id=publications
1. https://amplab.cs.berkeley.edu/wp-content/uploads/2014/09/graphx.pdf
1. https://code.google.com/p/leveldb/
1. https://databricks.com/certified-on-spark
1. https://databricks.com/spark-support
1. https://developers.google.com/freebase/v1/mql-overview
1. https://github.com/GraphChi/graphchi-cpp/blob/master/toolkits/collaborative_filtering/als.cpp#L60-L72
1. https://github.com/amplab/graphx
1. https://github.com/amplab/graphx/blob/master/LICENSE
1. https://github.com/amplab/graphx/commits/master
1. https://github.com/amplab/graphx/issues
1. https://github.com/apache/jena
1. https://github.com/apache/jena/commits/master
1. https://github.com/apache/spark
1. https://github.com/apache/spark/commits/master
1. https://github.com/azinazadi/GraphLab/blob/master/src/graphlab/graph/io/GraphJSON.java
1. https://github.com/boltdb/bolt
1. https://github.com/dubey/weaver
1. https://github.com/dubey/weaver/blob/master/LICENSE
1. https://github.com/dubey/weaver/commits/master
1. https://github.com/google/cayley
1. https://github.com/google/cayley/blob/master/docs/Configuration.md
1. https://github.com/google/cayley/commits/master
1. https://github.com/google/cayley/tree/master/docs
1. https://github.com/google/leveldb
1. https://github.com/graphlab-code/graphlab
1. https://github.com/graphlab-code/graphlab/
1. https://github.com/graphlab-code/graphlab/commits/master
1. https://github.com/igraph/igraph
1. https://github.com/igraph/igraph/commits/master
1. https://github.com/igraph/igraph/issues
1. https://github.com/neo4j
1. https://github.com/neo4j/neo4j
1. https://github.com/robmccoll/stinger
1. https://github.com/robmccoll/stinger/commits/master
1. https://github.com/robmccoll/stinger/issues
1. https://github.com/robmccoll/stinger/tree/master/doc
1. https://github.com/thinkaurelius/faunus/wiki
1. https://github.com/thinkaurelius/faunus/wiki/Getting-Started
1. https://github.com/thinkaurelius/titan
1. https://github.com/thinkaurelius/titan/commits/titan05
1. https://github.com/thinkaurelius/titan/issues
1. https://github.com/thinkaurelius/titan/issues?q=is%3Aissue+is%3Aclosed
1. https://github.com/thinkaurelius/titan/wiki/Building-Titan
1. https://github.com/thinkaurelius/titan/wiki/Graph-Configuration
1. https://github.com/thinkaurelius/titan/wiki/Rexster-Graph-Server
1. https://github.com/thinkaurelius/titan/wiki/Storage-Backend-Overview
1. https://github.com/thinkaurelius/titan/wiki/Titan-Limitations
1. https://github.com/thinkaurelius/titan/wiki/Vertex-Centric-Indices
1. https://github.com/tinkerpop/blueprints/wiki
1. https://github.com/tinkerpop/blueprints/wiki/Event-Implementation
1. https://github.com/tinkerpop/blueprints/wiki/GraphML-Reader-and-Writer-Library
1. https://github.com/tinkerpop/blueprints/wiki/GraphSON-Reader-and-Writer-Library
1. https://github.com/zachlatta/stringer/blob/master/LICENSE
1. https://groups.google.com/forum/#!topic/aureliusgraphs/96ZJcKmyeXk
1. https://groups.google.com/forum/#!topic/aureliusgraphs/Mt3hvYSoSBE
1. https://groups.google.com/forum/#!topic/aureliusgraphs/_ZV_k80Q8ak
1. https://groups.google.com/forum/#!topic/aureliusgraphs/uNUA_NLQOpU
1. https://groups.google.com/forum/#!topic/aureliusgraphs/zRHR-KCgq1w
1. https://groups.google.com/forum/#!topic/graphlab-kdd/n-29A442sjs
1. https://issues.apache.org/jira/browse/JENA
1. https://issues.apache.org/jira/browse/JENA/?selectedTab=com.atlassian.jira.jira-projects-plugin:summary-panel
1. https://jena.apache.org/
1. https://jena.apache.org/documentation/query/logging.html
1. https://jena.apache.org/documentation/rdf/index.html
1. https://jena.apache.org/documentation/serving_data/index.html
1. https://jena.apache.org/documentation/tdb/index.html
1. https://jena.apache.org/documentation/tdb/tdb_transactions.html
1. https://jena.apache.org/getting_involved/index.html
1. https://jena.apache.org/index.html
1. https://jena.apache.org/tutorials/
1. https://jena.apache.org/tutorials/index.html
1. https://jena.apache.org/tutorials/rdf_api.html
1. https://jena.apache.org/tutorials/rdf_api.html#ch-Introduction
1. https://jena.apache.org/tutorials/sparql.html
1. https://jena.apache.org/tutorials/sparql_optionals.html
1. https://raw.githubusercontent.com/dubey/weaver/master/LICENSE
1. https://spark.apache.org/docs/1.1.0/graphx-programming-guide.html
1. https://spark.apache.org/docs/1.1.0/graphx-programming-guide.html#pagerank
1. https://spark.apache.org/docs/1.1.0/graphx-programming-guide.html#property-operators
1. https://spark.apache.org/docs/1.1.0/security.html
1. https://spark.apache.org/documentation.html
1. https://spark.apache.org/faq.html
1. https://spark.apache.org/graphx/
1. https://support.neo4j.com/hc/en-us
1. https://wiki.apache.org/cassandra/GettingStarted
1. https://www.mongodb.org/
