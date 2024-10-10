Technical_Essentials_01102024.md

Technical Essentials 2024 - [Unofficial Introduction to the course](./00-Personal_Taughts_26032024.pdf)

## Cloud

Course Overview - NOTE: Labs - Link: [Official Page](https://d1.awsstatic.com/training-and-certification/classroom-training/aws-technical-essentials.pdf)

Cloud Definition - National Institute of Standards and Technology - Link: [Official NIST Page](https://ccsp.alukos.com/standards/nist-sp-800-145/)

AWS Infrastructure - Regions - Link: [AWS Page](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/)

AWS Infrastructure - Local Zones - Link: [AWS Page](https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/?nc=sn&loc=3)

AWS Infrastructure - Local Zones - Features - Link: [AWS Page](https://aws.amazon.com/about-aws/global-infrastructure/localzones/features/?nc=sn&loc=2)

AWS Products - NOTE: Amazon RDS for DB2 - Link: [AWS Page](https://aws.amazon.com/products/?aws-products-all.sort-by=item.additionalFields.productNameLowercase&aws-products-all.sort-order=asc&awsf.re%3AInvent=event-year%23aws-reinvent-2023&awsf.Free%20Tier%20Type=*all&awsf.tech-category=*all)

AWS Learning Badges - Link: [Training Page](https://aws.amazon.com/training/badges/)

### QUESTIONS

*Q. Cuales son los lenguajes de SDK para AWS ?*
A. Puedes ver el listado actualizado [aqui](https://aws.amazon.com/developer/tools/), pero es mejor que escogas tu lenguaje y empieces a mirar codigo, por ejemplo para [Python](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/ec2-example-managing-instances.html) y empezar a hacer tus propios experimentos.

## IAM

What is Virtualization and Benefits - Link: [Official Introduction](https://aws.amazon.com/iam/features/mfa)

Example to use roles on IAM - Link: [AWS Respost](https://repost.aws/knowledge-center/iam-assume-role-cli)

## Budget

Budget Tutorial - Link: [AWS Tutorial](https://www.youtube.com/watch?v=O0sofGVT7uw)

## CodeWhisperer

Simple Example - Link: [Official Demo Video](https://youtu.be/j8BoVmHKFlI?t=40)

## Compute Services

AMI Definition - Link: [Official Documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html)

Bootstrapping Options - Link: [Example](https://s3.amazonaws.com/cloudformation-examples/BoostrappingApplicationsWithAWSCloudFormation.pdf)

Instance Naming Convention - Link: [Official Doc](https://docs.aws.amazon.com/ec2/latest/instancetypes/instance-type-names.html)

What is Virtualization and Benefits - Link: [Official Introduction](https://aws.amazon.com/what-is/virtualization/)

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

Comparison MultiAZ Instances and Read Replica - Link: [No-Official Documentation](https://jayendrapatil.com/aws-rds-replication-multi-az-read-replica/)

Key concepts and definitions for burstable performance instances - Link: [Official Documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-credits-baseline-concepts.html)

Core Components of Amazon DynamoDB - Link: [Official Page](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html)

Use Cases for DynamoDB - Link: [Official Page](https://aws.amazon.com/blogs/database/amazon-dynamodb-gaming-use-cases-and-design-patterns/)

General Guide for Pricing  - Link: [Official Page](https://aws.amazon.com/dynamodb/pricing/)

Check Always Free Tier for DynamoDB Provisioned - Link: [Official Page](https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=tier%23always-free&awsf.Free%20Tier%20Categories=categories%23databases)

Amazon Managed Blockchain - Link: [Official Page](https://aws.amazon.com/managed-blockchain/)

Amazon Quantum Ledger Database - Link: [Official Page](https://aws.amazon.com/qldb/)

Do I need a ledger database? An intro to Amazon QLDB - Link: [re:Invent 2018 Video](https://youtu.be/7G9epn3BfqE)
