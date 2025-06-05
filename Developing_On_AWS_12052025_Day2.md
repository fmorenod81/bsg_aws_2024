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

![Mandatory](./mandatory.png) Invoking a Lambda function asynchronously [Official Docs](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html)

AWS Lambda Destination to SQS for Asynchronous Invocations — DLQ Example [No-Official Article](https://medium.com/aws-lambda-serverless-developer-guide-with-hands/aws-lambda-destination-to-sqs-for-asynchronous-invocations-dlq-example-4c64f47b1024)

![Mandatory](./mandatory.png) Understanding the Lambda execution environment lifecycle [Official Documentation](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtime-environment.html)

AWS Lambda standardizes billing for INIT Phase [AWS Blog](https://aws.amazon.com/blogs/compute/aws-lambda-standardizes-billing-for-init-phase/)

Lambda Schedule [Official Docs](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-run-lambda-schedule.html)

![Mandatory](./mandatory.png) Configuring provisioned concurrency for a function [Official Docs](https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html)

Improving startup performance with Lambda SnapStart [Official Docs](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html)

AddPermission API Call [Developer Guide](http://docs.aws.amazon.com/lambda/latest/dg/API_AddPermission.html)

![Mandatory](./mandatory.png) AWS Lambda permissions [Developer Guide](http://docs.aws.amazon.com/lambda/latest/dg/intro-permission-model.html)

CreateEventSourceMapping [Developer Guide](http://docs.aws.amazon.com/lambda/latest/dg/API_CreateEventSourceMapping.html)

![Mandatory](./mandatory.png) How Lambda processes records from stream and queue-based event sources [Official Docs](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventsourcemapping.html)

What Is Event Source Mapping In Lambda? [No-Official Blog](https://towardsaws.com/what-is-event-source-mapping-in-lambda-e8e4ed92e1a4)

“Using Lambda with the Toolkit for Eclipse” in the AWS Toolkit for Eclipse User Guide [Official Docs](http://docs.aws.amazon.com/AWSToolkitEclipse/latest/GettingStartedGuide/lambda.html)

AWS Lambda Developer Guide: AWS Toolkit for Visual Studio [Official Docs](https://docs.aws.amazon.com/lambda/latest/dg/csharp-package-toolkit.html)

AWS Toolkit for PyCharm in the Jet Brains Marketplace [Official Docs](https://plugins.jetbrains.com/plugin/11349-aws-toolkit)

Manage Lambda function versions [Official Docs](https://docs.aws.amazon.com/lambda/latest/dg/configuration-versions.html)

Create an alias for a Lambda function [Official Docs](https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html)

Implement Lambda canary deployments using a weighted alias [Official Docs](https://docs.aws.amazon.com/lambda/latest/dg/configuring-alias-routing.html)

Optimizing static initialization [No-Official Blog](https://serverlessland.com/content/service/lambda/guides/aws-lambda-operator-guide/static-initialization)

AWS Lambda | Function URL | Environment Vars | Lambda Layers - Step by Step Tutorial (Part -17) [No-Official Video](https://youtu.be/XFGSuj83wdc?t=1790)

Lambda quotas [Official Docs](https://docs.aws.amazon.com/lambda/latest/dg/limits.html).

Getting Started Lambda quotas [Official Docs](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html)

Lambda runtimes [Official Docs](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html)

Quick Hands-on with Lambda Layer [Demo](https://aws-dojo.com/excercises/excercise17/)

![Mandatory](./mandatory.png) Best practices for working with AWS Lambda functions [Official Docs](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html)

![Mandatory](./mandatory.png) Configuring provisioned concurrency for a function [Official Docs](https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html)

**Question 03/06/2025**

1. Se puede llamar a Lambda de manera asincronica desde API Gateway ?

R:/ Si, se puede ver en la [documentacion](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-integration-async.html), como mencione no es un caso comun sin embargo, existe la posibilidad.

2. Que pasa cuando invoco mas lambda de los que estan en el limite ?

R:/ Existira un throtling y los mensajes de error que se encuentran detallado [aqui](https://repost.aws/knowledge-center/lambda-troubleshoot-throttling) asi como sugerencias para solucionarlo, sin embargo, creo que es bueno leer esta [respuesta](https://stackoverflow.com/questions/62294399/getting-throttlingexception-rate-exceeded-status-code-400-on-aws-api) para mirar la manera de implementacion de reintentos externos a AWS.

3. Cual es el costo de aplicar Warm Standby (Provisioned Concurrency) ?

R:/ Si existe una diferencia en esta seccion del [pricing](https://aws.amazon.com/lambda/pricing/#Provisioned_Concurrency_Pricing), no son iguales. Una gran explicacion esta en este [blog](https://aws.amazon.com/blogs/aws/new-provisioned-concurrency-for-lambda-functions/) acerca de como aplicarlo.

## Managing the APIs

![Mandatory](./mandatory.png) Choose between REST APIs and HTTP APIs [Official Docs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-vs-rest.html)

API Gateway REST vs. HTTP API: What Are The Differences? [No-Official Blog](https://dev.to/tinystacks/api-gateway-rest-vs-http-api-what-are-the-differences-2nj)

![Mandatory](./mandatory.png) Can SOAP API directly integrate with AWS API Gateway ? [AWS RePost](https://repost.aws/questions/QUoy5UHNJAQIKHK_i22mTaQw/can-soap-api-directly-integrate-with-aws-api-gateway)

Setting up a stage for a REST API [Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-stages.html)

![Mandatory](./mandatory.png) Creating and using usage plans with API keys [Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html)

Throttle API requests for better throughput [Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html)

Controlling and managing access to a REST API in API Gateway [Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-to-api.html)

Setting up data transformations for REST APIs [Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-data-transformations.html)

Generating an SDK for a REST API in API Gateway [Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-generate-sdk.html)

![Mandatory](./mandatory.png) Set up mock integrations in API Gateway [Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-mock-integration.html)

Enabling API caching to enhance responsiveness [Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-caching.html)

Troubleshooting Amazon API Gateway with enhanced observability variables [AWS Blog](https://aws.amazon.com/blogs/compute/troubleshooting-amazon-api-gateway-with-enhanced-observability-variables/)

Integration passthrough behavior [Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/integration-passthrough-behaviors.html)

Setting up stage variables for a REST API deployment [Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/stage-variables.html)

Performing canary deployments for service integrations with Amazon API Gateway [Developer Guide](https://aws.amazon.com/blogs/compute/performing-canary-deployments-for-service-integrations-with-amazon-api-gateway/)

![Mandatory](./mandatory.png) Amazon API Gateway tutorials and workshops [AWS Tutorials](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-tutorials.html)

![Mandatory](./mandatory.png) Choose an AWS Lambda integration tutorial [Official Docs](https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-with-lambda-integration.html)

Invoke REST APIs in API Gateway [Official Docs](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-call-api.html)

![Mandatory](./mandatory.png) Using Stages in AWS API Gateway [No-Official Blog](https://medium.com/tuanhdotnet/using-stages-in-aws-api-gateway-582ac414dcf2)

Deploy REST APIs in API Gateway [Official Docs](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-deploy-api.html)

Amazon API Gateway Developer Guide [Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html)

Architecting for scale with Amazon API Gateway private integrations [AWS Blogs](https://aws.amazon.com/blogs/compute/architecting-for-scale-with-amazon-api-gateway-private-integrations/)

Velocity Template Language (VTL) [Official Page](https://velocity.apache.org/engine/devel/vtl-reference.html)

Cross-Origin Resource Sharing (CORS) [Official Page](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)

**Question 04/06/2025**

1. Que relacion tienen el metodo OPTIONS y el CORS en API Gateway ?

R:/ El navegador usa OPTIONS como una metodo para hacer una llamada posterior a la falla solicitando la capacidades del servidor para el CORS, como se [muestra en esta pagina](https://auth0.com/blog/cors-tutorial-a-guide-to-cross-origin-resource-sharing/).
