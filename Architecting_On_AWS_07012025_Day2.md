Architecting_On_AWS_07012025_Day2.md

Technical Essentials 2024 - Start Date: 7 January 2025 - [Unofficial Introduction to the course](./00-Personal_Taughts_07012025.pdf)

- [Storage](#storage)
- [Databases](#databases)
- [Monitoring and Scaling](#monitoring-and-scaling)
- [Automation](#automation)
- [Containers](#containers)

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

[NO Oficial: ElastiCache Redis vs InMemoryDB](https://cloudwellserved.com/amazon-elasticache-for-redis-vs-amazon-memorydb-for-redis/)

[Read Replica Lag](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html#USER_ReadRepl.Monitoring.Lag)

[Diferencias DB](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html#USER_ReadRepl.Overview.Differences)

[CQRS Pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-data-persistence/cqrs-pattern.html)

[MultiAZ Features](https://aws.amazon.com/rds/features/multi-az/)

[MultiAZ Cluster](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html)

[Aurora Pricing](https://aws.amazon.com/rds/aurora/pricing/)

[CAP Theorem](https://docs.aws.amazon.com/whitepapers/latest/availability-and-beyond-improving-resilience/cap-theorem.html)

[Queries and Languages for DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SQLtoNoSQL.ReadData.Query.html)

[DynamoDB: Pricing](https://repost.aws/knowledge-center/dynamodb-optimize-costs)

[DynamoDB: OnDemand Pricing FAQ](https://aws.amazon.com/dynamodb/pricing/)

[DynamoDB: Provisioned Pricing](https://aws.amazon.com/dynamodb/pricing/provisioned/)

[DynamoDB: Free Tier](https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=tier%23always-free&awsf.Free%20Tier%20Categories=*all)

[DynamoDB: Autoscaling](https://aws.amazon.com/blogs/database/amazon-dynamodb-auto-scaling-performance-and-cost-optimization-at-any-scale/)

[DynamoDB: Global Tables](https://aws.amazon.com/dynamodb/global-tables/)

[DynamoDB: Global Tables - How It Works!](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/V2globaltables_HowItWorks.html)

[Cache: Lazy Load Redis](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Strategies.html)

[Cache: Lazy Load Memcached](https://docs.aws.amazon.com/AmazonElastiCache/latest/mem-ug/Strategies.html)

[ElastiCache](https://aws.amazon.com/elasticache/)

[ElastiCache Redis and ValKey](https://aws.amazon.com/elasticache/redis/)

[Redis Vs MemCached](https://aws.amazon.com/elasticache/redis-vs-memcached/)

[ElastiCache FAQs](https://aws.amazon.com/elasticache/faqs/)

[ElastiCache: Global DataStore](https://aws.amazon.com/elasticache/faqs/#Global_Datastore)

[DMS: Como funciona: 3 fases del Migration Tasks: FullLoad, Changes in FullLoad, CDC](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.HighLevelView.html)

**QUESTIONS :**

**Q: Que incluye la replicacion en un DMS, por ejemplo, indices, stored procedures, etc ?**

R:/ Dentro de la documentacion de las [mejores practicas](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_BestPractices.html) y dentro de la resolucion de este [Re:Post](https://repost.aws/knowledge-center/dms-migrate-database-objects), se menciona que esa labora la realiza las herramientas nativas para el caso de la BD o Schema Conversion Tool (SCT). Sin embargo, en ambas fuentes de informacion se solicita que se revise el schema convertido o movido al nuevo destino en AWS. Incluso en el [DMS FAQ, section Schema Conversion](https://aws.amazon.com/dms/faqs/) se pueden usar herramienta de DMS para mirar conversiones en especifico.

**Q: Se puede limitar las tablas para ejecutar la replicacion en un DMS ?**

R:/ Si, se puede realizar configuraciones especiales para configurar el DMS, en esta [documentacion](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.Selections.html) se puede mirar el ejemplo "Example Migrate some tables in a schema" cuales son las tablas ser usadas en la migracion.

**Q: Donde se muestran las tecnologias de replicacion por motor de base de datos ?**
**Q: COmo el DMS orquesta el full backup en una replicacion ?**

R:/ Ambas preguntas estan relaciones desde el momento en que se realiza la marca de inicio de la replicacion, y el resto de los cambios en proceso (ongoing changes) que es el caso de Change Data Capture. En esta [pagina](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Task.CDC.html) se mira las tecnologias nativas del motor donde se realizan las llamadas eficientes para los ongoing changes. Adicionalmente, se mira como se realiza la marca de CDC Start point, es decir, desde el lugar donde se realizo el Full Backup  y donde despues de ello, la BD sabe cuales son los cambios realizados y tienen que ser enviados a AWS. El proceso de orquestacion para migracion de una gran cantidad datos de BD se puede mirar en este [blog](https://aws.amazon.com/blogs/storage/enable-large-scale-database-migrations-with-aws-dms-and-aws-snowball/).

## Monitoring and Scaling

[Cloudwatch conceptos metricas](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html)

[Cloudwatch conceptos logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogsConcepts.html)

[Log Groups, misma configuracion](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html)

[Cloudwatch Pricing](https://aws.amazon.com/cloudwatch/pricing/)

[Integracion de logs hacia metricas - Metric Filter Example Apache](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/ExtractBytesExample.html)

[MI PROPIA CUENTA: Quien hizo que y cuando](https://us-east-1.console.aws.amazon.com/cloudtrail/home?region=us-east-1#/events?ReadOnly=false)

[Verificar accesos no autorizados en near-RTime - VPC Flow](https://aws.amazon.com/blogs/mt/improve-security-by-analyzing-vpc-flow-logs-with-amazon-cloudwatch-contributor-insights/)

[Clouwatch FAQs](https://www.amazonaws.cn/en/cloudwatch/faqs/)

[ATM EventBridge](https://aws.amazon.com/blogs/compute/reducing-custom-code-by-using-advanced-rules-in-amazon-eventbridge/)

[S3 Event Notification vs EventBridge](https://aws.amazon.com/blogs/aws/new-use-amazon-s3-event-notifications-with-amazon-eventbridge/)

[Scheduler](https://aws.amazon.com/blogs/architecture/serverless-scheduling-with-amazon-eventbridge-aws-lambda-and-amazon-dynamodb/)

[ELB Comparison](https://aws.amazon.com/elasticloadbalancing/features/?nc=sn&loc=2)

[ELB FAQs](https://aws.amazon.com/elasticloadbalancing/faqs/?nc=sn&loc=5)

[Gateway LB](https://aws.amazon.com/elasticloadbalancing/gateway-load-balancer/)

[AWS autoscaling differente que EC2 Autoscaling](https://aws.amazon.com/autoscaling/features/)

[Importancia: Escenario DC: Explicacion de Costos: Oportunidad, Desperdiciado (Infra significa UX)](https://aws.amazon.com/blogs/aws-cloud-financial-management/five-things-you-should-do-to-create-an-accurate-on-premises-vs-cloud-comparison-model/)

[AS Policies: Type](https://docs.aws.amazon.com/autoscaling/ec2/userguide/scale-your-group.html)

[AS Policies: Dynamic](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html)

[Step vs Simple Policy](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-simple-step.html#SimpleScaling)

[Predictive Policy](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-predictive-scaling.html)

[Cost: Policies](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-mixed-instances-groups.html)

[Spot on ASG](https://aws.amazon.com/getting-started/hands-on/ec2-auto-scaling-spot-instances/)

## Automation

[Complete CI/CD with AWS CodeCommit, AWS CodeBuild, AWS CodeDeploy, and AWS CodePipeline](https://aws.amazon.com/blogs/devops/complete-ci-cd-with-aws-codecommit-aws-codebuild-aws-codedeploy-and-aws-codepipeline/. )

[GitHub connections](https://docs.aws.amazon.com/codepipeline/latest/userguide/connections-github.html. )

[Refer to resource outputs in another AWS CloudFormation stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/walkthrough-crossstackref.html)

[Update CloudFormation stacks using change sets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.html)

[AWS CloudFormation best practices](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/best-practices.html)

[Solutions Library](https://aws.amazon.com/solutions/)

[CDK v2-Cloud Dev Kit](https://docs.aws.amazon.com/cdk/v2/guide/home.html)

[Simple Sys Mngr-SSM - Agent](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html)

## Containers

[Simple microservices architecture on AWS](https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/simple-microservices-architecture-on-aws.html)

[Use service discovery to connect Amazon ECS services with DNS names](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html)

[Kubernetes on AWS](https://aws.amazon.com/kubernetes/.)

[Amazon EKS features](https://aws.amazon.com/eks/features/)

[Amazon ECS features](https://aws.amazon.com/ecs/features/)

[Automatically manage Amazon ECS capacity with cluster auto scaling](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-auto-scaling.html)

[AWS Fargate](https://aws.amazon.com/fargate/)

[Building your Cloud Operating Model](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-cloud-operating-model/welcome.html)

[Amazon EKS Distro ](https://aws.amazon.com/eks/eks-distro/)

[Amazon EKS Anywhere](https://aws.amazon.com/eks/eks-anywhere/)

[Amazon ECS Anywhere](https://aws.amazon.com/ecs/anywhere/)

[Amazon Elastic Container Service -Amazon ECS](https://aws.amazon.com/ecs/)

[Caso PrimeVideo de MicroSvr a Monolitos](https://www.primevideotech.com/video-streaming/scaling-up-the-prime-video-audio-video-monitoring-service-and-reducing-costs-by-90)

[Containers Overview](https://aws.amazon.com/containers/)

[Image Scanning](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html)

[Lifecycle](https://docs.aws.amazon.com/AmazonECR/latest/userguide/lifecycle_policy_examples.html)

[Private Image Replication](https://docs.aws.amazon.com/AmazonECR/latest/userguide/replication.html)

[Servicios (Opcionales) y Tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_run_task.html)

[Deteccion/Discovery: Namespaces en Cloud Map, VPC-DNS Private](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html)

[Running in your laptop or on the cloud](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html)

[Portable to any K8s, depends on version](https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions.html)

[Fargate Ejemplo](https://docs.aws.amazon.com/es_es/AmazonECS/latest/developerguide/ECS_AWSCLI_Fargate.html#ECS_AWSCLI_Fargate_list_task_definitions)

[ECS Task Specifications at CPU/Mem](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html)

**QUESTIONS :**

**Q: Existe Ingenieria Reversa para recursos en AWS ?**

R:/ Dentro de la documentacion de las [mejores practicas](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_BestPractices.html) y dentro de la resolucion de este [Re:Post](https://repost.aws/knowledge-center/dms-migrate-database-objects), se menciona que esa labora la realiza las herramientas nativas para el caso de la BD o Schema Conversion Tool (SCT). Sin embargo, en ambas fuentes de informacion se solicita que se revise el schema convertido o movido al nuevo destino en AWS. Incluso en el [DMS FAQ, section Schema Conversion](https://aws.amazon.com/dms/faqs/) se pueden usar herramienta de DMS para mirar conversiones en especifico.

**Q: Donde podria encontrar plantillas de CloudFormation para aprender ?**

R:/ [Dentro de](https://github.com/aws-cloudformation/aws-cloudformation-templates/tree/main/EC2)

**Q: Donde podria encontrar plantillas de CloudFormation para aprender ?**

R:/ https://aws.amazon.com/cdk/faqs/

**Q: Diferencias de lanzamiento de recursos entre ECS y EKS, especialmente con Balanceadores ?**

R:/ 