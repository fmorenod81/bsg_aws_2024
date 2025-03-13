Technical_Essentials_11032025.md

TABLE OF CONTENTS

- [Introduction](#introduction)
- [IAM](#iam)
- [Budget](#budget)
- [Questions I](#questions-i)
- [Compute Services](#compute-services)
- [Networking](#networking)

## Introduction

Course Overview - NOTE: Labs - Link: [Official Page](https://d1.awsstatic.com/training-and-certification/classroom-training/aws-technical-essentials.pdf)

Cloud Definition - NIST Definition - NOTE: Service Models and Deployment Models - Link: [Official NIST Page](https://ccsp.alukos.com/standards/nist-sp-800-145/)

AWS Infrastructure - Regions - NOTE: New region on Mexico and Edge Locations on Mx, Co, Pe - Link: [AWS Page](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/)

AWS Infrastructure - Local Zones - NOTE: LZ on Queretaro, Santiago, Lima and Bogota (Announced) - Link: [AWS Page](https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/?nc=sn&loc=3)

Able a subnet with Local Zone - NOTE: My Own AWS Web Console - Link: [VPC Settings](https://us-east-1.console.aws.amazon.com/vpcconsole/home?region=us-east-1#Settings:) and [Subnet Settings](https://us-east-1.console.aws.amazon.com/vpcconsole/home?region=us-east-1#CreateSubnet:)

AWS Products - NOTE: Amazon RDS for DB2 - Link: [AWS Page](https://aws.amazon.com/products/?aws-products-all.sort-by=item.additionalFields.productNameLowercase&aws-products-all.sort-order=asc&awsf.re%3AInvent=event-year%23aws-reinvent-2023&awsf.Free%20Tier%20Type=*all&awsf.tech-category=*all)

Amazon Global Network Overview with James Hamilton - Link: [Re:Invent 2016 Video](https://youtu.be/uj7Ting6Ckk)

## IAM

Multifactor Authenticator - Link: [Official Introduction](https://aws.amazon.com/iam/features/mfa)

Example to use roles on IAM - Link: [AWS Repost](https://repost.aws/knowledge-center/iam-assume-role-cli)

## Budget

Budget Tutorial - Link: [AWS Tutorial](https://www.youtube.com/watch?v=O0sofGVT7uw)

## Questions I

1. Que otros tipos de cloud puede AWS ofrecerme y que servicios estarian asociados?

    R:/ Entender que tipos de nubes existen se pueden usar para despliegue se puede revisar en:

    Selecting the right cloud for workloads – differences between public, private, and hybrid - Link: [Whitepaper](https://docs.aws.amazon.com/whitepapers/latest/public-sector-cloud-transformation/selecting-the-right-cloud-for-workloads-differences-between-public-private-and-hybrid.html)

    Finalmente, los servicios asociados para la nube hibrida se encuentran en:

    Hybrid Cloud with AWS - Link: [Official Page]((https://aws.amazon.com/hybrid/)

2. Que estrategias tiene AWS para la migracion ?

    R:/ Existe una variedad de servicios, pero es mejor tener en cuenta los conceptos antes de empezar una implementacion:

Understanding Your Application Readiness when Migrating to AWS - Link: [Whitepaper](https://d1.awsstatic.com/whitepapers/understanding-application-readiness-when-migrating-to-aws.pdf?did=wp_card&trk=wp_card)

Migrating to AWS: Best Practices and Strategies - Link: [Whitepaper](https://d1.awsstatic.com/Migration/migrating-to-aws-ebook.pdf) 

Adicionalmente, si quiere entener los conceptos de Disaster Recovery y Business continuity, el adecuado whitepaper sera este:

Disaster Recovery of Workloads on AWS: Recovery in the Cloud - Link: [Whitepaper](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html)

Finalmente, el resumen del whitepaper lo pueden encontrar en este blog, de 4 partes:

Disaster Recovery (DR) Architecture on AWS, Part I: Strategies for Recovery in the Cloud - Link: [AWS Architecture Blog](https://aws.amazon.com/blogs/architecture/disaster-recovery-dr-architecture-on-aws-part-i-strategies-for-recovery-in-the-cloud/)

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
