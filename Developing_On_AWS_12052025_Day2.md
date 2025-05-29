Developing_On_AWS_12052025_Day2.md

[Join the Get AWS Certified: Foundational and Associate Challenge](https://pages.awscloud.com/GLOBAL-other-GC-Traincert-Foundational-and-Associate-Certification-Challenge-2025-reg.html)

Developing On AWS 2025 - Start Date: 12 May 2025

- [Getting Started with Databases](#getting-started-with-databases)
- [Processing Your Database Operations](#processing-your-database-operations)
- [Processing Your Application Logic](#processing-your-application-logic)
- [Managing the APIs](#managing-the-apis)

## Getting Started with Databases

Core components of Amazon DynamoDB [Developer Guide](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html)

Partitions and Data Distribution [Official Docs](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.Partitions.html)

Working with Tables and Data in DynamoDB [Official Docs](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithTables.html)

![Mandatory](./mandatory.png) Pricing for On-Demand Capacity - Review Examples [Official Page](https://aws.amazon.com/dynamodb/pricing/on-demand/)

Service, Account, and Table Quotas in Amazon DynamoDB [Developer Guide](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html)

Improving Data Access with Secondary Indexes [Developer Guide](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SecondaryIndexes.html)

![Mandatory](./mandatory.png) Best practices for designing and using partition keys effectively in DynamoDB [Developer Guide](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-design.html)

![Mandatory](./mandatory.png) Using write sharding to distribute workloads evenly in your DynamoDB table [Developer Guide](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-sharding.html)

DynamoDB burst and adaptive capacity [Official Docs](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/burst-adaptive-capacity.html)

DynamoDB Indexes: Making the right choice between GSI and LSI - Amazon DynamoDB Nuggets [Official Video](https://youtu.be/BkEu7zBWge8)

Indices en DynamoDB: Escogiendo entre GSI y LSI - Amazon DynamoDB Nuggets | Amazon Web Services [Official Video](https://youtu.be/6A3HfcPuo0o)

NoSQL Workbench for DynamoDB [Developer Guide](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.html)

Setting Up DynamoDB Local (Downloadable Version) [Developer Guide](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.html)

PartiQL [Official Webpage](https://partiql.org/)

PartiQL - A SQL-Compatible Query Language for Amazon DynamoDB [Developer Guide](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ql-reference.html)



**Questions 28/05/2025**

1. Solo puede existir un Sort Key por Tabla?

R:/ En la documentacion, siempre se menciona un solo Sort Key por Base Table o por Secondary Index (ya sea LSI o GSI): [Core components of Amazon DynamoDB]( https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html) ,  [General guidelines for secondary indexes in DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-indexes-general.html) y [Best practices for using sort keys to organize data in DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-sort-keys.html)

2. Algo adicional que se vea en Dynamodb?

R:/ [DynamoDB Streams](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html) es una caracteristica muy usada para arquitecturas manejadas por eventos.

## Processing Your Database Operations

Service, Account, and Table Quotas in Amazon DynamoDB [Developer Guide](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ServiceQuotas.html)

DynamoDB read and write operations [Official Docs](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/read-write-operations.html)

Amazon DynamoDB Transactions: How it works [Official Docs](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/transaction-apis.html)

Best practices for querying and scanning data in DynamoDB [Developer Guide](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-query-scan.html)

What is the difference between scan and query in dynamodb? When use scan / query? [No-Official Blog](https://stackoverflow.com/questions/43452219/what-is-the-difference-between-scan-and-query-in-dynamodb-when-use-scan-query)

Understanding DynamoDB Write Capacity Units: PutItem vs UpdateItem [No-Official Blog](https://dev.to/aws-builders/understanding-dynamodb-write-capacity-units-putitem-vs-updateitem-1137#:~:text=Understanding%20DynamoDB%20Write%20Capacity%20Units:%20PutItem%20vs,the%20full%20item%20data%20in%20the%20request.)

PutItem API Reference [API Reference](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_PutItem.html)

UpdateItem API Reference [API Reference](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateItem.html#API_UpdateItem_Examples)

BatchWriteItem API Reference [API Reference](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BatchWriteItem.html)

Paginating Table Query Results [Developer Guide](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Query.Pagination.html)

![Mandatory](./mandatory.png) Overview of AWS SDK Support for DynamoDB [Developer Guide](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.SDKOverview.html)

Using expression attribute values in DynamoDB [Official Docs](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.ExpressionAttributeValues.html)

Condition and filter expressions, operators, and functions in DynamoDB [Official Docs](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.OperatorsAndFunctions.html)

Database Caching [Official Page](https://aws.amazon.com/caching/database-caching/)

Caching patterns [AWS Whitepaper](https://docs.aws.amazon.com/whitepapers/latest/database-caching-strategies-using-redis/caching-patterns.html)

## Processing Your Application Logic

Lambda Schedule [Official Docs](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-run-lambda-schedule.html)

Cold Start [Official Docs](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html)

AddPermission [Developer Guide](http://docs.aws.amazon.com/lambda/latest/dg/API_AddPermission.html)

AWS Lambda permissions [Developer Guide](http://docs.aws.amazon.com/lambda/latest/dg/intro-permission-model.html)

CreateEventSourceMapping [Developer Guide](http://docs.aws.amazon.com/lambda/latest/dg/API_CreateEventSourceMapping.html)

“Using Lambda with the Toolkit for Eclipse” in the AWS Toolkit for Eclipse User Guide [Official Docs](http://docs.aws.amazon.com/AWSToolkitEclipse/latest/GettingStartedGuide/lambda.html)

AWS Lambda Developer Guide: AWS Toolkit for Visual Studio [Official Docs](https://docs.aws.amazon.com/lambda/latest/dg/csharp-package-toolkit.html)

AWS Toolkit for PyCharm in the Jet Brains Marketplace [Official Docs](https://plugins.jetbrains.com/plugin/11349-aws-toolkit)

Lambda quotas [Official Docs](https://docs.aws.amazon.com/lambda/latest/dg/limits.html).

Lambda quotas x2 [Official Docs](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html)

Lambda runtimes [Official Docs](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html)


## Managing the APIs
