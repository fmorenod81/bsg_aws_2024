Architecting_On_AWS_07012025_Day2.md

Technical Essentials 2024 - Start Date: 7 January 2025 - [Unofficial Introduction to the course](./00-Personal_Taughts_07012025.pdf)

- [Storage](#storage)
- [Databases](#databases)

## Storage

[S3 Durability: Redudancy at 3 AZ](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DataDurability.html)

[S3 Features](https://aws.amazon.com/s3/features/)

[Proteccion/Permisos](https://aws.amazon.com/s3/faqs/?nc=sn&loc=7#Security)

[Tiene endpoint publico para acceso, no significa que sea publico. Publico: Bucket Policies (Para hacerlo publico), ACL y CORS - Cross-Origin Resource Sharing](https://aws.amazon.com/blogs/security/iam-policies-and-bucket-policies-and-acls-oh-my-controlling-access-to-s3-resources/)

[Ownership Grafico](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html)

[Access Point - Solo para objetos](https://aws.amazon.com/s3/features/access-points/)

[Dividir centralizacion en Bucket Policies](https://aws.amazon.com/blogs/storage/managing-amazon-s3-access-with-vpc-endpoints-and-s3-access-points/)

[Access Points: Por Network Control Origin (VPC), Usuario, Grupo, Cross-Account](https://aws.amazon.com/s3/faqs/?nc=sn&loc=7#S3_Access_Points)

[Access Points Policies: Alineado con SCP y con politicas de bucket - Ejemplos](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-policies.html)

[Encryption at Rest: Default encryption per Bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html)

[SSE-C Explanation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerSideEncryptionCustomerKeys.html)

[DSSE-KMS-$$-New13Jun2023](https://aws.amazon.com/about-aws/whats-new/2023/06/amazon-s3-dual-layer-encryption-compliance-workloads/)

[Object Lock - WORM (Retention Period- No Del, No Updates & Legal Hold) - Aplica al crearse](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-overview.html)

[Lifecycle - Basados en Creacion pero puede aplicar otros filtros, tamaño. Ejemplo 6.](https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-configuration-examples.html#lifecycle-config-conceptual-ex6)

[Replicacion](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-walkthrough1.html)

[Transfer Acceleration - PUT/GET](https://docs.aws.amazon.com/AmazonS3/latest/userguide/transfer-acceleration-speed-comparison.html)

[Another sh Tool](https://repost.aws/knowledge-center/upload-speed-s3-transfer-acceleration)

[Integracion con EventBridge - Cap. 7 ](https://aws.amazon.com/blogs/aws/new-use-amazon-s3-event-notifications-with-amazon-eventbridge/)

**QUESTIONS :**

**Q: Los S3 Access Point tienen costo ?**
R:/ No. Segun esta [informacion](https://aws.amazon.com/s3/features/access-points/#:~:text=S3%20Access%20Points%20are%20available%20in%20all%20regions%20at%20no%20additional%20cost.). Finalmente, puedes metodos de acceso para controlar costos de datos entre s3 y ec2 [aqui](https://repost.aws/articles/ARjzluyMS8RbeOOK4MGXRG6Q/cost-effective-methods-for-accessing-s3-buckets-cross-region)

**Q: Tienes un diagrama que explica la encripcion en S3 ?**
R:/ La mejor [Explicacion](https://faun.pub/aws-s3-encryption-2f6101573caa) que encontre fue esta.

**Q: Cuales son los limitantes para la replicacion en S3?**
R:/ Primero me autocorrigo, al decir que no existe replicacion bidireccional, si existe y aplica para casos de failover de region y de trafico. Mas informacion puede encontrarse [aqui](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html). Adicionalmente, la replicacion puede existir desde el momento de activacion en adelante (live replication) o hacia atras (OnDemand replication). Adicionalmente se pueden visualizar las condiciones/consideraciones para la replicacion [aqui](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-requirements.html).

## Databases

[Read Replica Lag](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html#USER_ReadRepl.Monitoring.Lag)

[Diferencias DB](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html#USER_ReadRepl.Overview.Differences)

[CQRS Pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-data-persistence/cqrs-pattern.html)

[MultiAZ Cluster](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html)

[Queries and Languages for DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SQLtoNoSQL.ReadData.Query.html)

[DynamoDB: Pricing](https://repost.aws/knowledge-center/dynamodb-optimize-costs)

[DynamoDB: OnDemand Pricing FAQ](https://aws.amazon.com/dynamodb/pricing/)

[DynamoDB: Provisioned Pricing](https://aws.amazon.com/dynamodb/pricing/provisioned/)

[DynamoDB: Free Tier](https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=tier%23always-free&awsf.Free%20Tier%20Categories=*all)

[DynamoDB: Autoscaling](https://aws.amazon.com/blogs/database/amazon-dynamodb-auto-scaling-performance-and-cost-optimization-at-any-scale/)

[DynamoDB: Global Tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/V2globaltables_HowItWorks.html)

[Cache: Lazy Load Redis](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Strategies.html)

[Cache: Lazy Load Memcached](https://docs.aws.amazon.com/AmazonElastiCache/latest/mem-ug/Strategies.html)

[ElastiCache](https://aws.amazon.com/elasticache/)

[Redis Vs MemCached](https://aws.amazon.com/elasticache/redis-vs-memcached/)

[ElastiCache FAQs](https://aws.amazon.com/elasticache/faqs/)

[ElastiCache: Global DataStore](https://aws.amazon.com/elasticache/faqs/#Global_Datastore)

[DMS: Como funciona: 3 fases del Migration Tasks: FullLoad, Changes in FullLoad, CDC](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.HighLevelView.html)