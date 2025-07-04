Developing_On_AWS_12052025_Day3.md

[Join the Get AWS Certified: Foundational and Associate Challenge](https://pages.awscloud.com/GLOBAL-other-GC-Traincert-Foundational-and-Associate-Certification-Challenge-2025-reg.html)

Developing On AWS 2025 - Start Date: 12 May 2025

- [Building a Modern Application](#building-a-modern-application)
- [Granting Access to Your Application Users](#granting-access-to-your-application-users)
- [Deploying Your Application](#deploying-your-application)
- [Observing Your Application](#observing-your-application)
- [Course Wrap-Up](#course-wrap-up)

## Building a Modern Application

Advanced Developing on AWS [Official Course](https://aws.amazon.com/training/classroom/advanced-developing-on-aws/)

Serverless on AWS  [Official Page](https://aws.amazon.com/serverless/)

Iterating a Loop Using Lambda [Official Docs](https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-create-iterate-pattern-section.html)

Pattern: Strangler application [Official Page](https://microservices.io/patterns/refactoring/strangler-application.html)

Simple microservices architecture on AWS [Whitepaper](https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/simple-microservices-architecture-on-aws.html)

Building your Cloud Operating Model [Prescriptive Guide](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-cloud-operating-model/welcome.html)

Prime Video Switched from Serverless to EC2 and ECS to Save Costs [No-Official Blog](https://www.infoq.com/news/2023/05/prime-ec2-ecs-saves-costs/)

## Granting Access to Your Application Users

AWS Cognito user pool group precedence - working as expected and useless or broken? [Unofficial Blog](https://stackoverflow.com/questions/55180987/aws-cognito-user-pool-group-precedence-working-as-expected-and-useless-or-brok)

Controlling access to resources with Cognito groups and IAM roles - Authenticated users in Cognito Identity pools, Part 1 [Unofficial Blog](https://arpadt.com/articles/cognito-groups-iam-roles)

Implementing item-level access control to DynamoDB tables - Authenticated users in Cognito Identity pools, Part 2 [Unofficial Blog](https://arpadt.com/articles/item-level-control-ddb)

Integrating Amazon Cognito With Web and Mobile Apps [Developer Guide](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-integrate-apps.html)

Setting up Facebook as an identity pools IdP [Developer Guide](https://docs.aws.amazon.com/cognito/latest/developerguide/facebook.html)

## Deploying Your Application

![Mandatory](./mandatory.png) Whitepaper: Introduction to DevOps on AWS - Link: [Whitepaper](https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/introduction-devops-aws.pdf)

What is DevOps? [Product Page](https://aws.amazon.com/devops/what-is-devops/)

AWS SAM template anatomy [Developer Guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-template-anatomy.html)

Controlling access to an API with API Gateway resource policies [Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-resource-policies.html)

Create a deployment configuration with CodeDeploy [User Guide](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations-create.html)

Deployment configurations on an AWS Lambda compute platform [User Guide](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations.html#deployment-configuration-lambda)

Thinking Serverless: From Business Problem to Serverless Solution - Link: [AWS re:Invent 2020 Video](https://youtu.be/Z57KLdJZnGA)

Infrastructure as Code on AWS - Link: [AWS Online Tech Talks](https://youtu.be/cKQtPZwf97s)

![Mandatory](./mandatory.png) Getting Started with DevOps on AWS - Link: [Training](https://www.aws.training/Details/Curriculum?id=67465)

![Mandatory](./mandatory.png) How to migrate your AWS CodeCommit repository to another Git provider - Link: [Blog](https://aws.amazon.com/blogs/devops/how-to-migrate-your-aws-codecommit-repository-to-another-git-provider/)

AWS CodePipeline product integrations - Link: [Official Webpage](https://aws.amazon.com/codepipeline/product-integrations/)

![Mandatory](./mandatory.png) Developer Tools on AWS - Link: [Official Webpage](https://aws.amazon.com/products/developer-tools)

Section "Developer tools" on AWS Overview - Link: [AWS Whitepaper](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/developer-tools.html)

![Mandatory](./mandatory.png) AWS CodeDeploy Integrations - Link: [Official Webpage](https://docs.aws.amazon.com/codedeploy/latest/userguide/integrations.html)

Build specification reference for CodeBuild (buildspec.yaml) - Link: [Official Docs](https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html)

CodeDeploy AppSpec file reference (AppSpec .yaml) - Link: [Official Docs](https://docs.aws.amazon.com/codedeploy/latest/userguide/reference-appspec-file.html)

Blue/Green Deployment with CodeDeploy - Link: [Official Doc](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-bluegreen.html)

Fine-Tuning Blue/Green Deployments on Application Load Balancer- Link: [Official Doc](https://aws.amazon.com/blogs/devops/blue-green-deployments-with-application-load-balancer/)

Understanding How Deployments Affect Application Performance - Link: [AWS re:Invent 2020 Video](https://youtu.be/O9tDtJje-EA)

Conference for Serverless Framework - Leonardo Sarmiento - ex-EPAM[GitHub](https://github.com/lesarmiento37/serverless-ds)

![Mandatory](./mandatory.png) Tutorial: Deploy a Hello World application with AWS SAM [Official Docs](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started-hello-world.html)

**Question 09/06/2025**

1. Cloudformation tienen caracteristicas de multiples archivos de configuracion con la misma plantilla ? "Algo parecido a Workspaces de Terraform".

R:/ Cloudformation tiene solo un archivo de configuracion por entrada, por tanto no separa los ambientes basados en variables de ingreso, como puede ser lo mencionado por la otra alternativa. Una comparativa puede ser encontrada [aqui](https://www.geeksforgeeks.org/difference-between-cloudformation-vs-terraform/).

## Observing Your Application

![Mandatory](./mandatory.png) Cloudwatch Metrics concepts [Official Docs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html)

Using Amazon CloudWatch alarms [User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/AlarmThatSendsEmail.html)

AWS CloudWatch Logs Deep Dive [No-Official Blog](https://medium.com/@joudwawad/aws-cloudwatch-logs-deep-dive-d52b5bb7c40d)

Serverless Application Lens [Whitepaper](https://d1.awsstatic.com/whitepapers/architecture/AWS-Serverless-Applications-Lens.pdf)

![Mandatory](./mandatory.png) AWS Lambda Logging tools and best practices — Python [No-Official Blog](https://medium.com/codex/aws-lambda-logging-tools-and-best-practices-python-e156a76f52a7)

Complexities and Best Practices for AWS Lambda Logging [AWS Partner Blog](https://aws.amazon.com/blogs/apn/complexities-and-best-practices-for-aws-lambda-logging/)

Guidance for Observability on AWS [Solutions Library](https://aws.amazon.com/solutions/guidance/observability-on-aws/)

Anti-patterns for strategic instrumentation [Official Docs](https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/anti-patterns-for-strategic-instrumentation.html)

![Mandatory](./mandatory.png) AWS X-Ray concepts [Developer Guide](https://docs.aws.amazon.com/xray/latest/devguide/xray-concepts.html)

![Mandatory](./mandatory.png) Tracing [Prescriptive Guide](https://docs.aws.amazon.com/prescriptive-guidance/latest/performance-engineering-aws/tracing.html)

## Course Wrap-Up

![Mandatory](./mandatory.png) Serverless Architectures with AWS Lambda [Whitepaper](https://d1.awsstatic.com/whitepapers/serverless-architectures-with-aws-lambda.pdf)

How AWS Pricing Works [Whitepaper](https://docs.aws.amazon.com/whitepapers/latest/how-aws-pricing-works/welcome.html)

![Mandatory](./mandatory.png) Back to Basics [Whitepaper](https://aws.amazon.com/architecture/back-to-basics/?tma.sort-by=item.additionalFields.airDate&tma.sort-order=desc&awsf.categories=*all&awsm.page-tma=2)

Advanced Developing on AWS [Courses](https://www.aws.training/SessionSearch?pageNumber=1&courseId=36896&languageId=1 )

Developing Serverless Solutions on AWS [Courses](https://www.aws.training/SessionSearch?pageNumber=1&courseId=53785&languageId=1)

Getting Started with DevOps on AWS [Courses](https://www.aws.training/Details/eLearning?id=66768)

AWS Cloud Development Kit Primer [Courses](https://www.aws.training/Details/Curriculum?id=64511)

![Mandatory](./mandatory.png) Certification Preparation [Official Page](https://aws.amazon.com/certification/certification-prep)

![Mandatory](./mandatory.png) Prepare for Examen [Official Page](https://skillbuilder.aws/#prepare-for-exam)

Certification Preparation - Testing [Official Page](https://aws.amazon.com/certification/certification-prep/testing/)

Digital Training [Official Page](https://aws.amazon.com/training/digital)

Digital training [Official Page](https://explore.skillbuilder.aws/)

Classroom training [Official Page](https://aws.amazon.com/training)

AWS Certification [Official Page](https://aws.amazon.com/certification)

AWS Workshops [Official Page](https://workshops.aws/)

Tech Talks [Official Page](https://aws.amazon.com/events/online-tech-talks/on-demand/)

![Mandatory](./mandatory.png) AWS Ramp-Up Guides [Official Page](https://aws.amazon.com/training/ramp-up-guides/)
