Cloud_Practitioner_11112024.md

Cloud Practitioner 2024 - Start Date: 11 November 2024

![Mandatory](./mandatory.png) Cloud Practitioner - Link: [Exam Guide](https://d1.awsstatic.com/training-and-certification/docs-cloud-practitioner/AWS-Certified-Cloud-Practitioner_Exam-Guide.pdf)

![Mandatory](./mandatory.png) Cloud Practitioner - Link: [Official Page](https://aws.amazon.com/certification/certified-cloud-practitioner/)

Instructor' Badges - Link: [Official Page](https://www.credly.com/users/francisco-javier-moreno-diaz)

**Table Of Contents** 
- [1.1. Introduction to Amazon Web Services](#11-introduction-to-amazon-web-services)
- [1.2 Compute in the Cloud](#12-compute-in-the-cloud)
- [1.3 Global Infrastructure and Reliability](#13-global-infrastructure-and-reliability)
- [2.1 Networking](#21-networking)
- [2.2 Storage and Databases](#22-storage-and-databases)
  - [Storage](#storage)
  - [Databases](#databases)
- [2.3 Security](#23-security)
- [3.1 Monitoring and Analytics](#31-monitoring-and-analytics)
- [3.2 Pricing and Support](#32-pricing-and-support)
- [3.3 Migration and Innovation](#33-migration-and-innovation)
- [3.4 AWS Certified Cloud Practitioner Basics](#34-aws-certified-cloud-practitioner-basics)

## 1.1. Introduction to Amazon Web Services

Cloud Definition - National Institute of Standards and Technology - Link: [Official NIST Page](https://ccsp.alukos.com/standards/nist-sp-800-145/)

What is AWS - Link: [Official Page](https://aws.amazon.com/what-is-aws/)

![Mandatory](./mandatory.png) Overview of Amazon Web Services - Categories - Link: [Whitepaper](https://d1.awsstatic.com/whitepapers/aws-overview.pdf)

![Mandatory](./mandatory.png) AWS architecture icons - Link: [Official Page](https://aws.amazon.com/architecture/icons/)

How AWS Pricing Works - Archived - Link: [Whitepaper](http://d1.awsstatic.com/whitepapers/aws_pricing_overview.pdf)

![Mandatory](./mandatory.png) AWS Calculator, case on EC2 - Link: [Official Page](https://calculator.aws/#/addService/ec2-enhancement)

What is Cloud Computing - Link: [Official Page](https://aws.amazon.com/what-is-cloud-computing/)

![Mandatory](./mandatory.png) Types of Cloud Computing - Link: [Official Page](https://aws.amazon.com/types-of-cloud-computing/)

AWS Glossary - Link: [Official Glossary](https://docs.aws.amazon.com/general/latest/gr/glos-chap.html)

## 1.2 Compute in the Cloud

AWS Compute - Link: [Official Page](https://aws.amazon.com/products/compute)

![Mandatory](./mandatory.png) Amazon EC2 - Link: [Official Page](https://aws.amazon.com/ec2/)

![Mandatory](./mandatory.png) Amazon EC2 Instance Types, specs - Link: [Official Docs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/compute-optimized-instances.html)

Instance Explorer - Link: [Official Page](https://aws.amazon.com/ec2/instance-explorer/)

Instance Family on Console - Link: [AWS Console](https://us-east-1.console.aws.amazon.com/ec2/home?region=us-east-1#InstanceTypes:)

![Mandatory](./mandatory.png) EC2 Pricing - Link: [Official Page](https://aws.amazon.com/ec2/pricing/reserved-instances/)

![Mandatory](./mandatory.png) How to explain spot instances for Dummies - Link [No-Official Video](https://youtu.be/mgWZls55ATs?t=17)

![Mandatory](./mandatory.png) How are T3 Dedicated Hosts different from T3 Dedicated Instances? - Link: [Official Page](https://aws.amazon.com/ec2/dedicated-hosts/faqs/#:~:text=Both%20T3%20Dedicated%20Instances%20and,placed%20on%20a%20physical%20server.)

Elastic Load Balancing - Link: [Official Page](https://aws.amazon.com/elasticloadbalancing)

Elastic Load Balancing features - Link: [Official Page](https://aws.amazon.com/elasticloadbalancing/features/?nc=sn&loc=2)

![Mandatory](./mandatory.png) Elastic Load Balancer FAQs - Link: [Official Page](https://aws.amazon.com/elasticloadbalancing/faqs/?nc=sn&loc=5)

Amazon EC2 Auto Scaling - Link: [Official Page](https://aws.amazon.com/ec2/autoscaling)

AWS Application AutoScaling, no EC2 but MORE services - Link: [Official Docs](https://docs.aws.amazon.com/autoscaling/application/userguide/what-is-application-auto-scaling.html)

Types of scaling: manual, dynamic, scheduled, predictive - Link: [Official Docs](https://docs.aws.amazon.com/autoscaling/ec2/userguide/scale-your-group.html)

AWS Compute Blog - Link: [Blogs](https://aws.amazon.com/blogs/compute/)

![Mandatory](./mandatory.png) Overview of Amazon Web Services/AWS Services/Compute - Link: [Whitepaper](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/compute-services.html)

Hands-on Tutorials/Compute - Link: [Tutorials](https://aws.amazon.com/getting-started/hands-on/?awsf.getting-started-category=category%23compute&awsf.getting-started-content-type=content-type%23hands-on)

What is Virtualization and Benefits - Link: [Official Introduction](https://aws.amazon.com/iam/features/mfa)

How to choose Modern Strategy - Link: [Official Docs](https://docs.aws.amazon.com/decision-guides/latest/modern-apps-strategy-on-aws-how-to-choose/modern-apps-strategy-on-aws-how-to-choose.html)

AWS Lambda - Link: [Official Page](https://aws.amazon.com/lambda)

Amazon Elastic Container Service (Amazon ECS) - Link: [Official Page](https://aws.amazon.com/ecs/)

Docker - Link: [Official Docker Page](https://www.docker.com/)

Amazon Elastic Kubernetes Service (Amazon EKS) - Link: [Official Page](https://aws.amazon.com/eks/)

AWS Fargate - Link: [Official Page](https://aws.amazon.com/fargate/)

**QUESTIONS**:

**a) Se pueden vender instancias reservadas ?**

R:/ Si, de acuerdo a la [documentacion oficial](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ri-market-general.html) se puede realizar la venta de instancias reservadas en un marketplace, alli se encuentran las condiciones y el procedimiento para realizarlo.

**b) Donde se encuentran los iconos de servicios AWS para architectura?**

R:/ Se encuentra en [pagina oficial](https://aws.amazon.com/architecture/icons/), hacer click en el boton de "Get Started" y alli esta el Powerpoint PPTx Toolkits. Un enlace directo en este momento esta [aqui](https://d1.awsstatic.com/webteam/architecture-icons/q2-2024/AWS-Architecture-Icon-Decks.pptx.d6671530ea426cd7ff7fb00423bccb120bfc69df.zip).

**c) RDS (Servicios de bases de datos) aplica para EC2 Reserved Instances o Compute Savings?**

R:/ RDS tiene una manera de reservar instancias pero no es igual a EC2 Reserved Instancias, pero lo comparan debido a manera similar, se puede encontrar el [procedimiento](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithReservedDBInstances.html) y la [descripcion](https://docs.aws.amazon.com/whitepapers/latest/cost-optimization-reservation-models/amazon-rds-reserved-db-instances.html#:~:text=Similar%20to%20Amazon%20EC2%20Reserved,and%20SQL%20Server%20database%20engines.). El alcance de Compute Savings se encuentra [aqui](https://aws.amazon.com/savingsplans/compute-pricing/).

**d) Se tiene una tabla comparativa de Balanceadores de Carga en AWS, especialmente de Application Load Balancer y Network Load Balancer?**

R:/ Se tiene una descripcion oficial [aqui](https://aws.amazon.com/compare/the-difference-between-the-difference-between-application-network-and-gateway-load-balancing/)

## 1.3 Global Infrastructure and Reliability

AWS Global Infrastructure - Link: [Official Page](https://aws.amazon.com/about-aws/global-infrastructure/)

![Mandatory](./mandatory.png) Regions and Availability Zones - Link: [Official Page](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/)

![Mandatory](./mandatory.png) Hybrid Cloud with AWS - Link: [Official Page](https://aws.amazon.com/hybrid/)

AWS Infrastructure - Local Zones - Link: [Official Page](https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/?nc=sn&loc=3)

Networking & Content Delivery - Link: [Blogs](https://aws.amazon.com/blogs/networking-and-content-delivery/)

![Mandatory](./mandatory.png) Tools to Build on AWS - Link: [Official Page](https://aws.amazon.com/tools/)

## 2.1 Networking

![Mandatory](./mandatory.png) Networking Essentials - Link: [Official Docs](https://aws.amazon.com/getting-started/aws-networking-essentials/)

AWS Networking and Content Delivery - Link: [Official Page](https://aws.amazon.com/products/networking)

AWS Networking and Content Delivery - Link: [Blogs](https://aws.amazon.com/blogs/networking-and-content-delivery/)

Amazon Virtual Private Cloud - Link: [Service Page](https://aws.amazon.com/vpc)

![Mandatory](./mandatory.png) What is Amazon VPC - All VPC Components - Link: [Official Docs](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)

![Mandatory](./mandatory.png) How Amazon VPC works - Link: [Official Docs](https://docs.aws.amazon.com/vpc/latest/userguide/how-it-works.html)

ACL - Better Explanation - Link [Official Docs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)

Sec Groups - Example - Link [Official Docs](https://docs.aws.amazon.com/vpc/latest/userguide/security-group-rules.html)

Direct Connect - Dedicated Connection - Link: [Service Page](https://aws.amazon.com/directconnect/)

Route 53 - DNS Management - Link: [Service Page](https://aws.amazon.com/route53)

## 2.2 Storage and Databases

### Storage

![Mandatory](./mandatory.png) Cloud Storage on AWS - Link: [Official Page](https://aws.amazon.com/products/storage)

Amazon Elastic Block Store - Amazon EBS - - Link: [Service Page](https://aws.amazon.com/ebs)

Instance store temporary block storage for EC2 instances - Link: [Official Docs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html)

Amazon Simple Storage Service - Amazon S3 - - Link: [Service Page](https://aws.amazon.com/s3/)

![Mandatory](./mandatory.png) Simple Storage Service - S3 - Link: [Official Features Page](https://aws.amazon.com/s3/features/)

Looks Intelligent Tier - S3 Pricing - Link: [Official Pricing Page](https://aws.amazon.com/s3/pricing/)

Amazon S3 security - Link: [Official Docs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security.html)

Amazon Elastic File System - Amazon EFS- - Link: [Service Page](https://aws.amazon.com/efs/)

![Mandatory](./mandatory.png) Which Data Storage Option Should I Choose? - Link: [AWS Community](https://community.aws/content/2iClwJnscRUEUbna4TCRTVRK3Hu/which-data-storage-option-do-i-choose)

AWS Storage Blog - Link: [Blogs](https://aws.amazon.com/blogs/storage/)

Hands-On Tutorials: Storage - Link: [Tutorials](https://aws.amazon.com/getting-started/hands-on/?awsf.getting-started-category=category%23storage&awsf.getting-started-content-type=content-type%23hands-on)

### Databases

![Mandatory](./mandatory.png) Databases on AWS - Link: [Official Page](https://aws.amazon.com/products/databases)

![Mandatory](./mandatory.png) Amazon Relational Database Service - Amazon RDS - - Link: [Official Page](https://aws.amazon.com/rds/)

![Mandatory](./mandatory.png) Amazon Aurora - Link: [Service Page](https://aws.amazon.com/rds/aurora/)

![Mandatory](./mandatory.png) Amazon DynamoDB - Link: [Service Page](https://aws.amazon.com/dynamodb/)

Amazon Redshift - Link: [Service Page](https://aws.amazon.com/redshift)

AWS Database Migration Service - AWS DMS - - Link: [Service Page](https://aws.amazon.com/dms/)

Schema Conversion - Link: [Official Page](https://aws.amazon.com/dms/schema-conversion-tool/?nc=sn&loc=2)

Category Deep Dive: Databases - Link: [Official Page](https://aws.amazon.com/getting-started/deep-dive-databases/)

AWS Database Blog - Link: [Blogs](https://aws.amazon.com/blogs/database/)

## 2.3 Security

Security, Identity, and Compliance on AWS - Link: [Official Page](https://aws.amazon.com/security/)

![Mandatory](./mandatory.png) Introduction to AWS Security - Link: [Whitepaper](https://docs.aws.amazon.com/whitepapers/latest/introduction-aws-security/welcome.html)

![Mandatory](./mandatory.png) Amazon Web Services - Overview of Security Processes - Link: [Whitepaper](https://docs.aws.amazon.com/whitepapers/latest/aws-overview-security-processes/aws-overview-security-processes.pdf)

AWS Security Blog - Link: [Blogs](https://aws.amazon.com/blogs/security/)

AWS Compliance - Link: [Official Page](https://aws.amazon.com/compliance)

![Mandatory](./mandatory.png) Shared responsibility model - Link: [Official Page](https://aws.amazon.com/compliance/shared-responsibility-model/)

Data Privacy FAQ - Link: [Official Page](https://aws.amazon.com/compliance/data-privacy-faq/)

![Mandatory](./mandatory.png) AWS Identity and Access Management - IAM - - Link: [Service Page](https://aws.amazon.com/iam/)

Multi-factor Authentication - Link: [Official Page](https://aws.amazon.com/iam/features/mfa/)

![Mandatory](./mandatory.png) AWS Organizations - Link: [Service Page](https://aws.amazon.com/organizations)

Service control policies - SCPs - - Link: [Official Docs](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html)

AWS Artifact  - Link: [Service Page](https://aws.amazon.com/artifact)

Customer Compliance Center - Link: [Service Page](https://aws.amazon.com/compliance/customer-center/)

AWS Shield - Link: [Service Page](https://aws.amazon.com/shield)

![Mandatory](./mandatory.png) AWS WAF - Link: [Service Page](https://aws.amazon.com/waf)

![Mandatory](./mandatory.png) AWS Key Management Service - AWS KMS - - Link: [Service Page](https://aws.amazon.com/kms)

Amazon Inspector - Link: [Service Page](https://aws.amazon.com/inspector/)

Amazon GuardDuty - Link: [Service Page](https://aws.amazon.com/guardduty)

AWS Security Services - Link: [Official Page](https://aws.amazon.com/products/security/)

**QUESTIONS**:

**a) La diferencia entre Instance Store y Elastic Block Service ?**

R:/ Puede hacerse la [revision de Storage](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Storage.html), sin embargo me parece mas importante la definicion de ¨[Instance Store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html).

**b) Cual es la diferencia entre el modelo de responsabilidad compartida y los modelos de servicios (IaaS, PaaS y SaaS) ?**

R:/ Se puede mirar los modelos de servicio [aqui](https://aws.amazon.com/types-of-cloud-computing/) y el modelo de responsabilidad compartida [aqui](https://aws.amazon.com/compliance/shared-responsibility-model/). Sin embargo, creo que modelo es el framework mas entendible de los limites, mientras que los modelos ya son las instanciaciones (casos definidos) de la responsabilidad.

**c) Como es la manera de evaluacion de politicas? Si no tienen negacion y permisos simultaneamente**

R:/ Se puede mirar los casos de evaluacion de politica [aqui](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html#policies_evaluation_example) , pero la respuesta esta [aqui](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic_policy-eval-basics.html), donde dice que se tiene una precendencia para los casos de negacion.


## 3.1 Monitoring and Analytics

Monitoring and Observability - Link: [Official Page](https://aws.amazon.com/products/management-tools/use-cases/monitoring-and-observability/)

![Mandatory](./mandatory.png) Amazon CloudWatch - Link: [Service Page](https://aws.amazon.com/cloudwatch/)

![Mandatory](./mandatory.png) CloudWatch Metrics - Link: [Service Page](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html)

![Mandatory](./mandatory.png) CloudWatch Alarms - Link: [Service Page](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) 

![Mandatory](./mandatory.png) CloudWatch Dashboard - Link: [Service Page](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html)

Amazon CloudWatch Pricing - Link: [Service Page](https://aws.amazon.com/cloudwatch/pricing/)

Configuration, Compliance, and Auditing - Link: [Official Page](https://aws.amazon.com/products/management-tools/use-cases/configuration-compliance-and-auditing/)

![Mandatory](./mandatory.png) AWS CloudTrail - Link: [Service Page](https://aws.amazon.com/cloudtrail/)

CloudTrail Insight - Link: [Service Page](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-insights-events-with-cloudtrail.html)

![Mandatory](./mandatory.png) AWS Trusted Advisor - Link: [Service Page](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/)

Management and Governance on AWS - Link: [Official Page](https://aws.amazon.com/products/management-tools)

AWS Management & Governance Blog - Link: [Blogs](https://aws.amazon.com/blogs/mt/)

Management and Governance Cloud Environment Guide - Link: [Whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/management-and-governance-guide/management-and-governance-cloud-environment-guide.html?did=wp_card&trk=wp_card)

## 3.2 Pricing and Support

![Mandatory](./mandatory.png) How AWS Pricing Works - Link: [Whitepaper](https://d1.awsstatic.com/whitepapers/aws_pricing_overview.pdf)

![Mandatory](./mandatory.png) Introduction to AWS Economics - Link: [Whitepaper](https://d1.awsstatic.com/whitepapers/introduction-to-aws-cloud-economics-final.pdf)

![Mandatory](./mandatory.png) AWS Free Tier - Link: [Official Page](https://aws.amazon.com/free/)

AWS Cost Management - Link: [Official Page](https://aws.amazon.com/aws-cost-management/)

![Mandatory](./mandatory.png) AWS Billing & Cost Management dashboard - Link: [Official Page](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-what-is.html)

AWS Pricing - Link: [Official Page](https://aws.amazon.com/pricing)

![Mandatory](./mandatory.png) AWS Pricing Calculator - Link: [Official Page](https://calculator.aws/#/)

AWS Lambda pricing - Link: [Pricing Page](https://aws.amazon.com/lambda/pricing/)

![Mandatory](./mandatory.png) Amazon EC2 pricing - Link: [Pricing Page](https://aws.amazon.com/ec2/pricing/)

![Mandatory](./mandatory.png) Amazon S3 pricing  - Link: [Pricing Page](https://aws.amazon.com/s3/pricing/)

![Mandatory](./mandatory.png) AWS Cost and Usage Reports - Link: [Service Page](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html)

Consolidated billing - Link: [Service Page](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html)

![Mandatory](./mandatory.png) AWS Budgets - Link: [Service Page](https://aws.amazon.com/aws-cost-management/aws-budgets)

AWS Cost Explorer - Link: [Service Page](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)

AWS Support (Basic, Developer, Business, Enterprise) - Link: [Service Page](https://aws.amazon.com/premiumsupport/plans/)

AWS Support - Link: [Service Page](https://aws.amazon.com/premiumsupport)

![Mandatory](./mandatory.png) AWS Knowledge Center - Link: [Service Page](https://aws.amazon.com/premiumsupport/knowledge-center/)

AWS Marketplace - Link: [Service Page](https://aws.amazon.com/marketplace)

## 3.3 Migration and Innovation

AWS Cloud Adoption Framework - CAF - - Link: [Service Page](https://aws.amazon.com/professional-services/CAF/)

![Mandatory](./mandatory.png) Cloud Adoption Framework  - Link: [Whitepaper](https://d1.awsstatic.com/whitepapers/aws_cloud_adoption_framework.pdf)

AWS Fundamentals: Core Concepts - Link: [Service Page](https://aws.amazon.com/getting-started/fundamentals-core-concepts/)

![Mandatory](./mandatory.png) 6 Strategies for Migrating Applications to the Cloud - Link: [Blogs](https://aws.amazon.com/blogs/enterprise-strategy/6-strategies-for-migrating-applications-to-the-cloud/)

![Mandatory](./mandatory.png) Migrate and Modernize on AWS - Link: [Service Page](https://aws.amazon.com/products/migration-and-transfer)

A Process for Mass Migrations to the Cloud - Link: [Blogs](https://aws.amazon.com/blogs/enterprise-strategy/214-2/)

![Mandatory](./mandatory.png) AWS Snow Family  - Link: [Service Page](https://aws.amazon.com/snow)

AWS Snowcone - Link: [Service Page](https://aws.amazon.com/snowcone)

AWS Snowball - Link: [Service Page](https://aws.amazon.com/snowball/)

AWS Snowmobile - Link: [Service Page](https://aws.amazon.com/snowmobile)

The Facts on Facial Recognition with Artificial Intelligence - Link: [Service Page](https://aws.amazon.com/rekognition/the-facts-on-facial-recognition-with-artificial-intelligence/)

AWS Cloud Enterprise Strategy Blog - Link: [Blogs](https://aws.amazon.com/blogs/enterprise-strategy/)

Modernizing with AWS Blog - Link: [Blogs](https://aws.amazon.com/blogs/modernizing-with-aws/)

![Mandatory](./mandatory.png) AWS Well-Architected - Link: [Service Page](https://aws.amazon.com/architecture/well-architected/)

![Mandatory](./mandatory.png) AWS Well-Architected Framework - Link: [Whitepaper](https://d1.awsstatic.com/whitepapers/architecture/AWS_Well-Architected_Framework.pdf)

![Mandatory](./mandatory.png) AWS Well-Architected Tool - Link: [Service Page](https://aws.amazon.com/well-architected-tool/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc)

AWS Architecture Center - Link: [Service Page](https://aws.amazon.com/architecture)

AWS Architecture Blog - Link: [Service Page](https://aws.amazon.com/blogs/architecture)

## 3.4 AWS Certified Cloud Practitioner Basics

![Mandatory](./mandatory.png) Official exam guide - Link: [Service Page](https://d1.awsstatic.com/training-and-certification/docs-cloud-practitioner/AWS-Certified-Cloud-Practitioner_Exam-Guide.pdf)

![Mandatory](./mandatory.png) Cloud Practitioner - Link: [Lean About](https://aws.amazon.com/training/learn-about/cloud-practitioner/)

Demystifying Your AWS Certification Exam Score - Link: [Service Page](https://aws.amazon.com/blogs/training-and-certification/demystifying-your-aws-certification-exam-score/)

AWS Certified Cloud Practitioner website - Link: [Service Page](https://aws.amazon.com/certification/certified-cloud-practitioner/)

Overview of Amazon Web Services - Link: [Service Page](https://d1.awsstatic.com/whitepapers/aws-overview.pdf)

How AWS Pricing Works - Link: [Service Page](http://d1.awsstatic.com/whitepapers/aws_pricing_overview.pdf)

Cloud Essentials - Link: [RampUp Guide](https://d1.awsstatic.com/training-and-certification/ramp-up_guides/Ramp-Up_Guide_Cloud_Essentials.pdf)