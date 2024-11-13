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
