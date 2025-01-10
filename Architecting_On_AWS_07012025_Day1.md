Technical_Essentials_01072024.md

Technical Essentials 2024 - Start Date: 7 January 2025 - [Unofficial Introduction to the course](./00-Personal_Taughts_07012025.pdf)

- [Introduction](#introduction)
- [Fundamentals](#fundamentals)
- [Account Security](#account-security)
- [Network 1](#network-1)
- [Compute](#compute)

## Introduction

[Deadlines - 4 certfs in 4 months](https://aws.amazon.com/blogs/training-and-certification/how-one-learner-earned-four-aws-certifications-in-four-months/)

[Official SAA C03](https://aws.amazon.com/certification/certified-solutions-architect-associate/)

[Architecting on AWS – Online Course Supplement on Skill Builder](https://explore.skillbuilder.aws/learn/course/external/view/elearning/8319/architecting-on-aws-online-course-supplement)

[Exam Guide](https://d1.awsstatic.com/training-and-certification/docs-sa-assoc/AWS-Certified-Solutions-Architect-Associate_Exam-Guide.pdf)

[RampUp Guides](https://aws.amazon.com/training/ramp-up-guides/)

[Docs](https://docs.aws.amazon.com/)

[Skill Builder](https://explore.skillbuilder.aws/learn/signin)

[SB Essentials](https://explore.skillbuilder.aws/learn/course/internal/view/elearning/10455/Fundamentos-de-la-nube-de-AWS-para-profesionales-Espa%2525C3%2525B1ol-de-Espa%2525C3%2525B1a-%25257C-AWS-Cloud-Practitioner-Essentials-Spanish-from-Spain-)

[Certfs Exam Readiness](https://explore.skillbuilder.aws/learn/course/internal/view/elearning/125/exam-readiness-aws-certified-solutions-architect-associate-digital)

[Workshops](https://workshops.aws/)

[Events](https://aws-experience.com/latam/smb/events)

[Learn Cloud Economics - Value of Cloud - Cloud ROI Framework - AWS](https://aws.amazon.com/economics/)

[Virtuous Circle](https://d1.awsstatic.com/whitepapers/introduction-to-aws-cloud-economics-final.pdf)

## Fundamentals

[The future of business is here](https://aws.amazon.com/campaigns/migrating-to-the-cloud/)

[Our Data Centers](https://aws.amazon.com/compliance/data-center/data-centers/)

[AZ - 100 km](https://docs.aws.amazon.com/sap/latest/general/arch-guide-architecture-guidelines-and-decisions.html)

[Costs-due to country taxes-Calculator for S3, east-1, Melbourne, Osaka, Zurich, Sao Paulo](https://calculator.aws/#/)

[Services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/)

[Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/)

[Local Zone](https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/?nc=sn&loc=3)

[Amazon CloudFront Key Features](https://aws.amazon.com/cloudfront/features/)

[Edge Location Vs Regional Edge Cache](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/HowCloudFrontWorks.html#CloudFrontRegionaledgecaches)

[Edge Location Vs Regional Edge Cache No Official](https://digitalcloud.training/amazon-cloudfront/#:~:text=Edge%20locations%20are%20not%20tied,cache%20longer%20at%20these%20locations.)

[Official Summary in a whitepaper](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/points-of-presence.html)

[Analyze solutions for biz needs & reqs - 5 Things](https://aws.amazon.com/blogs/training-and-certification/successful-solutions-architects-do-these-five-things/)

[Well Architected Framework](https://aws.amazon.com/architecture/well-architected/?wa-lens-whitepapers.sort-by=item.additionalFields.sortDate&wa-lens-whitepapers.sort-order=desc&wa-guidance-whitepapers.sort-by=item.additionalFields.sortDate&wa-guidance-whitepapers.sort-order=desc)

[Architecture Center](https://aws.amazon.com/architecture/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23pattern&awsf.methodology=*all&awsf.tech-category=*all&awsf.industries=*all&awsf.business-category=*all)

[Solutions Library](https://aws.amazon.com/solutions/)

[Shared-Responsability Model](https://aws.amazon.com/blogs/industries/applying-the-aws-shared-responsibility-model-to-your-gxp-solution/)

## Account Security

[Root Account](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html)

[PRACTICES: No daily tasks, MFA, no CLI/Programmatice Access](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege)

[IDp - SAML Federation Example](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml.html#CreatingSAML-configuring)

[Federation Page](https://aws.amazon.com/identity/federation/)

[Quickstart for CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html)

[Create admin user](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-set-up.html)

[TUTORIAL: IAM Assume Role CLI](https://repost.aws/knowledge-center/iam-assume-role-cli)

[Env Variables](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html)

[Cross-Account access using IAM](https://repost.aws/knowledge-center/cross-account-access-iam)

[MI CUENTA SOLAMENTE: Manejadas por AWS o Usuario-Con](https://us-east-1.console.aws.amazon.com/iamv2/home?region=us-east-1#/policies)

[MI CUENTA SOLAMENTE: No-Manejadas - No Explicitas-Con](https://us-east-1.console.aws.amazon.com/iamv2/home?region=us-east-1#/users/details/test2?section=permissions)

[MI CUENTA SOLAMENTE: Basadas en Recursos](https://s3.console.aws.amazon.com/s3/buckets/testfmorenodpublichtml?region=us-east-1&tab=permissions)

[SCP](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples_general.html#example-scp-deny-region)

[Re:Inforce Video for Permission Boundaries](https://www.youtube.com/watch?v=eVNvjQ0wr84)

[Official Doc for Permission Boundaries](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html)

[No-Official Video for Permission Boundaries](https://www.youtube.com/watch?v=D-1u0dBM-q8)

[MI CUENTA SOLAMENTE: Simple Policies for AWS Services - Review Link](https://us-east-1.console.aws.amazon.com/iamv2/home?region=us-east-1#/policies/details/arn%3Aaws%3Aiam%3A%3Aaws%3Apolicy%2FAmazonS3ReadOnlyAccess)

[MI CUENTA SOLAMENTE: Advanced Policies With Conditions - Review Link](https://us-east-1.console.aws.amazon.com/iamv2/home?region=us-east-1#/policies/details/arn%3Aaws%3Aiam%3A%3A768312754627%3Apolicy%2FFJMD_IAMRotateOwnAcessKeys?section=policy_permissions)

[Evaluation Logic - Pages](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html)

[Shared Responsability Model](https://aws.amazon.com/compliance/shared-responsibility-model/)


**QUESTIONS :**
Q: Se puede establecer la duracion del token ?
R: Dentro de la Doc del CLI de [Assume Role](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sts/assume-role.html), se especifica en la opcion duration-seconds.

Q: Como se puede limitar quien puede hacer las llamadas a AssumeRole?
R: Aunque no he encontrado documentacion oficial, ve las siguientes opciones: 

a) en el lab realizado en clase con [Bob]](https://repost.aws/knowledge-center/iam-assume-role-cli), se puede limitar en las APIs que puede llamar el usuario. 

b) En las condiciones del Trusted Policy al configurar la seccion de Conditions o Principal.

c) Limitar los servicios que lo llaman [Doc Official](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-calledvia)

## Network 1

[Subnetting](https://cidr.xyz/)

[VPC-Region-Con](https://us-east-1.console.aws.amazon.com/vpc/home?region=us-east-1#CreateVpc:createMode=vpcOnly)

[EIP - ENI - Use Cases](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/scenarios-enis.html)

[NACL](https://youtu.be/RBMcBBaM58E)

[Practicas mas implementada-Ejemplos](https://docs.aws.amazon.com/vpc/latest/userguide/security-group-rules.html)

## Compute

[MI CUENTA: Nombre:familia-gen-addicional.\*Tamano-Con](https://us-east-1.console.aws.amazon.com/ec2/home?region=us-east-1#InstanceTypes:)

[Tamano:large,xlarge,2xlarge-$$](https://calculator.aws/#/addService/ec2-enhancement)

[Tenancy](https://aws.amazon.com/ec2/dedicated-hosts/#:~:text=An%20important%20difference%20between%20a,same%20physical%20server%20over%20time.)

[Dedicated instance (mismo cuenta no mismo payer account, paga consumo instancia) vs Dedicated Hosts (mayor visibilidad cores, afinidad). Ambas mismo performance, seguridad y elemento fisico.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-instance.html)

[Placement Groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html)

[User-Data](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html)

[Tipos EBS - replicado en la misma AZ](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volumes.html)

[GP](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/general-purpose.html)

[GP2 Burst < 1TiB](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/general-purpose.html#gp2-performance)

[IO-Multiattached](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/provisioned-iops.html)

[Instace Store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html)

[Link Tabla](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-store-volumes.html)

[Compra Computo (Otros modelos) - No RESERVA](https://docs.aws.amazon.com/whitepapers/latest/cost-optimization-reservation-models/reservation-models-for-other-aws-services.html)

[Interensante diferencia entre RESERVA de Capacidades, instancias, Savings Plan - No se puede vender diferencia con Reserved Instance.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-reservations.html#capacity-reservations-differences)

[Link No Official](https://www.cloudzero.com/blog/savings-plans-vs-reserved-instances)

[Vender RI Mktplace](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ri-market-general.html)

[Spot](https://youtu.be/mgWZls55ATs)

[curl](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-instance-termination-notices.html)

[EventBridge](https://aws.amazon.com/blogs/compute/taking-advantage-of-amazon-ec2-spot-instance-interruption-notices/)

[URL](https://aws.amazon.com/blogs/aws/announcing-aws-lambda-function-urls-built-in-https-endpoints-for-single-function-microservices/)
