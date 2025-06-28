Technical_Essentials_20082024.md

TABLE OF CONTENTS
- [Questions](#questions)
- [Cloud](#cloud)
- [IAM](#iam)
- [Budget](#budget)
- [Compute Services](#compute-services)
- [Networking](#networking)
- [Storage](#storage)
- [Databases](#databases)
- [Monitoring](#monitoring)
- [Load Balancers](#load-balancers)
- [AutoScaling](#autoscaling)
- [Amazon Q Developer](#amazon-q-developer)

## Questions

a) Cuales son las 2 metricas mas comunes que se usan para Block Storage ?

b) Cuales son las familias de EBS y para que caso se usan ?

c) Cual es la capa mas reciente de S3 y que no aparece en la presentacion ?

d) Nombre 3 casos de uso para S3.

e) Que es un S3 Access Point y cual es su ventaja sobre un bucket policy -si aplica-.

f) Cuales son los limites en S3 de: Una operacion sencilla de carga (Simple PUT Operacion), tamaño maximo de un objeto, recomendacion de tamaño para carga en partes, operacion de carga usando la consola Web.

g) El servicio QLDB es blockchain ? SI no es asi cual seria el servicio?

h) Cual es el mas reciente motor para RDS ?

i) Donde estan localizadas los snapshots de EBS ?

R:/ Como se mencionó en la clase (26-Junio), los snapshots de EBS estan a nivel regional, y son almacenados en buckets S3 manejados por Amazon y el cliente no puede acceder a ellos directamente sino a traves de la consola de EBS. [Mayor información aqui](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-snapshots.html)

## Cloud

Course Overview - NOTE: Labs - Link: [Official Page](https://d1.awsstatic.com/training-and-certification/classroom-training/aws-technical-essentials.pdf)

Cloud Definition - NIST Definition - NOTE: Service Models and Deployment Models - Link: [Official NIST Page](https://ccsp.alukos.com/standards/nist-sp-800-145/)

AWS Infrastructure - Regions - NOTE: New region on Mexico and Edge Locations on Mx, Co, Pe - Link: [AWS Page](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/)

AWS Infrastructure - Local Zones - NOTE: LZ on Queretaro, Santiago, Lima and Bogota (Announced) - Link: [AWS Page](https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/?nc=sn&loc=3)

AWS Infrastructure - Local Zones - Features - Link: [AWS Page](https://aws.amazon.com/about-aws/global-infrastructure/localzones/features/?nc=sn&loc=2)

AWS Products - NOTE: Amazon RDS for DB2 - Link: [AWS Page](https://aws.amazon.com/products/?aws-products-all.sort-by=item.additionalFields.productNameLowercase&aws-products-all.sort-order=asc&awsf.re%3AInvent=event-year%23aws-reinvent-2023&awsf.Free%20Tier%20Type=*all&awsf.tech-category=*all)

AWS Learning Badges - Link: [Training Page](https://aws.amazon.com/training/badges/)

## IAM

Multifactor Authenticator - Link: [Official Introduction](https://aws.amazon.com/iam/features/mfa)

Example to use roles on IAM - Link: [AWS Repost](https://repost.aws/knowledge-center/iam-assume-role-cli)

## Budget

Budget Tutorial - Link: [AWS Tutorial](https://www.youtube.com/watch?v=O0sofGVT7uw)

## Compute Services

AMI Definition - Link: [Official Documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html)

Bootstrapping Options - Link: [Example](https://s3.amazonaws.com/cloudformation-examples/BoostrappingApplicationsWithAWSCloudFormation.pdf)

Instance Naming Convention - Link: [Official Doc](https://docs.aws.amazon.com/ec2/latest/instancetypes/instance-type-names.html)

What is Virtualization and Benefits - Link: [Official Introduction](https://aws.amazon.com/what-is/virtualization/)

How to learn Instance Families Names - Link: [No-Official Page](https://jaychapel.medium.com/ec2-instance-types-comparison-and-how-to-remember-them-bbb96b578aea)

Instance Explorer - Link: [Official Page](https://aws.amazon.com/ec2/instance-explorer/)

Instance Family on Console - Link: [AWS Console](https://us-east-1.console.aws.amazon.com/ec2/home?region=us-east-1#InstanceTypes:)

AWS Calculator, case on EC2 - Link: [Official Page](https://calculator.aws/#/addService/ec2-enhancement)

How Amazon EC2 instance hibernation works - Link: [Official Page](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-hibernate-overview.html)

Amazon EC2 Reserved Instances and Other AWS Reservation Models - Link: [Savings Plans](https://docs.aws.amazon.com/whitepapers/latest/cost-optimization-reservation-models/savings-plans.html) and [Reserved Instances](https://docs.aws.amazon.com/whitepapers/latest/cost-optimization-reservation-models/introduction.html)

How to explain spot instances for Dummies - Link [No-Official Video](https://youtu.be/mgWZls55ATs?t=17)

VM vs Containers - Technical Definition - Link [RedHat Definition](https://www.redhat.com/en/topics/containers/whats-a-linux-container#:~:text=Containers%20share%20the%20same%20operating,systems%20run%20x86%20Windows%20containers.)

How ECS works - Link [Official Page](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html)

Serverless Portfolio - Link: [AWS Page](https://aws.amazon.com/serverless/)

Lambda Service - Link: [AWS Page](https://aws.amazon.com/lambda/)

## Networking

VPC - All VPC Elements/Components - Link: [Official Documentation](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)

Networking Essentials - Link: [Official Documentation](https://aws.amazon.com/getting-started/aws-networking-essentials/)

EIP - Pricing Change - Link [Official Documentation](https://aws.amazon.com/blogs/aws/new-aws-public-ipv4-address-charge-public-ip-insights/)

ACL - Mejor grafica - Link [Official Documentation](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)

Sec Groups - Ejemplo - Link [Official Documentation](https://docs.aws.amazon.com/vpc/latest/userguide/security-group-rules.html)

## Storage

EBS Types - Use Cases- Link: [Official Service Page](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html)

Amazon FSx - Link: [Official Page](https://aws.amazon.com/fsx/)

Simple Storage Service - S3 - Link: [Official Features Page](https://aws.amazon.com/s3/features/)

How control access to S3: IAM Policies, S3 Policies and ACLs - Link: [Official Blog](https://aws.amazon.com/blogs/security/iam-policies-and-bucket-policies-and-acls-oh-my-controlling-access-to-s3-resources/)

Looks Intelligent Tier - S3 Pricing - Link: [Official Pricing Page](https://aws.amazon.com/s3/pricing/)

Versioning for Dummies - Link: [AWS Docs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html)

## Databases

AWS DB Products - Link: [Official Documentation](https://aws.amazon.com/products/databases/)

RDS Web Page - Link: [Official Page](https://aws.amazon.com/relational-database/)

NoSQL WebPage - Link: [Official Page](https://aws.amazon.com/nosql/)

DB differences on Writable RR, backup or parallel replication on Read Replication - Link: [Official Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html#USER_ReadRepl.Overview.Differences)

Multi-AZ DB instance deployments - Link: [Official Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZSingleStandby.html)

MultiAZ DB Cluster - !Readable! MultiAZ Deploy - Link: [Official Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html)

Core Components of Amazon DynamoDB - Link: [Official Page](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html)

Use Cases for DynamoDB - Link: [Official Page](https://aws.amazon.com/blogs/database/amazon-dynamodb-gaming-use-cases-and-design-patterns/)

General Guide for Pricing  - Link: [Official Page](https://aws.amazon.com/dynamodb/pricing/)

Check Always Free Tier for DynamoDB Provisioned - Link: [Official Page](https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=tier%23always-free&awsf.Free%20Tier%20Categories=categories%23databases)

## Monitoring

Amazon Cloudwatch Concepts - Link: [Official Doc](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html)

Amazon Cloudwatch Logs Concepts - Link: [Official Doc](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogsConcepts.html)

Extract metrics from a log  - Link: [Official Doc](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/ExtractBytesExample.html)

## Load Balancers

Elastic Load Balancer - Link: [Official Page](https://aws.amazon.com/elasticloadbalancing/features/?nc=sn&loc=2)

Elastic Load Balancer FAQs - Link: [Official Page](https://aws.amazon.com/elasticloadbalancing/faqs/?nc=sn&loc=5)

Gateway Load Balancer - Link: [Official Page](https://aws.amazon.com/elasticloadbalancing/gateway-load-balancer/)

## AutoScaling

AWS Application AutoScaling, no EC2 but MORE services - Link: [Official Doc](https://docs.aws.amazon.com/autoscaling/application/userguide/what-is-application-auto-scaling.html)

Types of scaling: manual, dynamic, scheduled, predictive - Link: [Official Doc](https://docs.aws.amazon.com/autoscaling/ec2/userguide/scale-your-group.html)

Dyn ASG: Target Tracking ASG - Link: [Official Doc](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html)

Dyn ASG: Step vs Simple Policy - Link: [Official Doc](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-simple-step.html#SimpleScaling)

Predictive ASG - Link: [Official Doc](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-predictive-scaling.html)

## Amazon Q Developer

Simple Example - Link: [Official Demo Video](https://youtu.be/j8BoVmHKFlI?t=49)