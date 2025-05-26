Developing_On_AWS_12052025_Day1.md 

[Join the Get AWS Certified: Foundational and Associate Challenge](https://pages.awscloud.com/GLOBAL-other-GC-Traincert-Foundational-and-Associate-Certification-Challenge-2025-reg.html)

Developing On AWS 2025 - Start Date: 12 May 2025

- [Course Overview](#course-overview)
- [Getting Started with Development on AWS](#getting-started-with-development-on-aws)
- [Getting Started with Permissions](#getting-started-with-permissions)
- [Demos](#demos)
- [Lab 1 Notes](#lab-1-notes)
- [Getting Started with Storage](#getting-started-with-storage)
- [Processing Your Storage Operations](#processing-your-storage-operations)

## Course Overview

Instructor' Certifications [Credly](https://credly.com/users/francisco-javier-moreno-diaz/)

AWS Instructor Led Training FAQs [FAQs](https://getready.aws.training/faq.html#labs-and-ebooks)

How one learner earned four AWS Certifications in four months [Amazon Blog](https://aws.amazon.com/blogs/training-and-certification/how-one-learner-earned-four-aws-certifications-in-four-months/)

AWS Certified Developer - Associate [Official Certification Page](https://aws.amazon.com/certification/certified-developer-associate/)

AWS Certified Developer - Associate [Exam Guide](https://d1.awsstatic.com/training-and-certification/docs-dev-associate/AWS-Certified-Developer-Associate_Exam-Guide.pdf)

Skill Builder as Official Digital Course [Skill Builder](https://explore.skillbuilder.aws/learn/signin)

AWS Cloud Practitioner Essentials (Español de España) [Skill Builder](https://explore.skillbuilder.aws/learn/course/internal/view/elearning/10455/Fundamentos-de-la-nube-de-AWS-para-profesionales-Espa%2525C3%2525B1ol-de-Espa%2525C3%2525B1a-%25257C-AWS-Cloud-Practitioner-Essentials-Spanish-from-Spain-)

Exam Prep Standard Course: AWS Certified Developer - Associate (DVA-C02) [Skill Builder](https://explore.skillbuilder.aws/learn/courses/14724/exam-prep-standard-course-aws-certified-developer-associate-dva-c02)

Standard Exam Prep Plan: AWS Certified Developer - Associate (DVA-C02) [Skill Builder](https://explore.skillbuilder.aws/learn/learning-plans/2177/plan)

Exam Prep Official Practice Question Set: AWS Certified Developer - Associate (DVA-C02 - English) [Skill Builder](https://explore.skillbuilder.aws/learn/courses/13757/exam-prep-official-practice-question-set-aws-certified-developer-associate-dva-c02-english)

AWS Ramp-Up Guides [Official Doc](https://aws.amazon.com/training/ramp-up-guides/)

AWS Workshops [Workshops](https://workshops.aws/)

AWS Connected Communities [LATAM Events](https://aws-experience.com/latam/smb/)

AWS Connected Communities [ES Events](https://aws-experience.com/emea/iberia)

AWS Well-Architected [Official Page](https://aws.amazon.com/architecture/well-architected)

## Getting Started with Development on AWS

AWS Signature Version 4 for API requests [Official Docs](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html)

Authenticating Requests (AWS Signature Version 4) [Official Docs](https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html)

Authenticating Requests: Using the Authorization Header (AWS Signature Version 4) [Official Docs](https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-auth-using-authorization-header.html)

Signature Version 4 signing process - [Official Docs](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html)

Signing AWS API requests - [Official Docs](http://docs.aws.amazon.com/general/latest/gr/signing_aws_api_requests.html)

CreateBucket API  [Official API Docs](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html)

Installing or updating to the latest version of the AWS CLI - [Official Doc](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

Setting up the AWS CLI [Official Doc](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-quickstart.html)

CLI Reference [Official Doc](http://docs.aws.amazon.com/cli/latest/reference/)

DynamoDB SDK Example - [Official Doc](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/getting-started-step-1.html)

Logging with the AWS SDK for .NET- [Amazon Blogs](https://aws.amazon.com/blogs/developer/logging-with-the-aws-sdk-for-net/)

.AWS SDK for .NET, Advanced configuration- [Official Doc](https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/net-dg-advanced-config.html )

Enabling Metrics for the AWS SDK for Java - [Official Doc](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/metrics.html)

Tools to Build on AWS - [Official Page](https://aws.amazon.com/developer/tools/)

Example of Tools to Build on AWS - [Official Q Plugin for VSCode](https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.amazon-q-vscode)

Amazon Q Developer Getting Started  [Amazon Q SkillBuilder](https://explore.skillbuilder.aws/learn/course/19491/play/122791)

Accelerate your Software Development Lifecycle with Amazon Q [AWS Blog](https://aws.amazon.com/blogs/devops/accelerate-your-software-development-lifecycle-with-amazon-q/)

Supported languages for Amazon Q Developer in the IDE [Official Docs](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-language-ide-support.html)

---
Python:

Boto3 documentation - [Official Docs](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

Boto3 quickstart - [Official Docs](https://boto3.readthedocs.org/en/latest/guide/quickstart.html)

AWS SDK for Python (Boto3)- [Official Docs](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

.NET:

Install AWSSDK packages with NuGet - [Official Docs](https://docs.aws.amazon.com/AWSSdkDocsNET/latest/V3/DeveloperGuide/net-dg-install-assemblies.html)

Starting a new AWS SDK for .NET project - [Official Docs](https://docs.aws.amazon.com/AWSSdkDocsNET/latest/V3/DeveloperGuide/net-dg-start-new-project.html)

AWS SDK for .NET - [Official Docs](https://docs.aws.amazon.com/sdkfornet/v3/apidocs)

Java:

Developer guide - AWS SDK for Java 2.x- [Official Docs](https://docs.aws.amazon.com/AWSSdkDocsJava/latest/DeveloperGuide/java-dg-install-sdk.html)

AWS SDK for Java - [Official Docs](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/overview-summary.html)

Other:

AWS Amplify: Amplify Documentation [Official Docs](https://docs.amplify.aws/)

AWS SDK for Ruby [Official Docs](https://aws.amazon.com/sdk-for-ruby/)

AWS SDK for JavaScript in Node.js [Official Docs](https://aws.amazon.com/sdk-for-javascript/)

AWS SDK for Go [Official Docs](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/welcome.html)

AWS SDK for JavaScript [Official Docs](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/)

AWS SDK for PHP [Official Docs](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/welcome.html)

AWS SDK for C++ [Official Docs](https://aws.amazon.com/sdk-for-cpp/)

## Getting Started with Permissions

IAM Identities - [Official Docs](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html)

Creating your first IAM admin user and user group [Official Docs](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html)

Identity-based policies and resource-based policies [Official Docs](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html)

Examples of Amazon S3 bucket policies [Official Docs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-bucket-policies.html#example-bucket-policies-encryption)

Delegate Access across AWS Accounts Using IAM Roles: Switch Roles (Console) [Official Docs](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html)

Apply AWS IAM Permissions Boundary | Hands-on [NO-Official Tutorial](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-api.html)

Permissions Boundaries Exercise [AWS Live re:Inforce Video](https://www.youtube.com/watch?v=eVNvjQ0wr84)

AWS managed policies for job functions [Official Docs](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html)

IAM roles [Official Docs](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)

Switching to an IAM role (AWS API) [Official Docs](https://youtu.be/D-1u0dBM-q8)

AWS service role [Official Docs](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-role)

How do I assume an IAM role using the AWS CLI? [AWS Re:Post](https://repost.aws/knowledge-center/iam-assume-role-cli)

Creating a role to delegate permissions to an AWS service [Official Docs](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html)

Providing access to an IAM user in another AWS account that you own [Official Docs](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.html)

Policy evaluation for requests within a single account [Official Docs](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic_policy-eval-basics.html)

Policy evaluation logic [Official Docs](http://docs.aws.amazon.com/IAM/latest/UserGuide/AccessPolicyLanguage_EvaluationLogic.html)

Output format [Official Docs](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html#cli-configure-quickstart-format)

Named profiles [Official Docs](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html)

(JetBrains) “Setting AWS credentials for the AWS Toolkit for JetBrains - [Official Docs](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/setup-credentials.html)

(Eclipse) “Set up AWS Credentials” in the AWS Toolkit for Eclipse User Guide  - [Official Docs](https://docs.aws.amazon.com/toolkit-for-eclipse/v1/user-guide/setup-credentials.html)

(Visual Studio) "Creating profiles for your AWS credentials” in the AWS Toolkit for Visual Studio User Guide  - [Official Docs](https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/keys-profiles-credentials.html)

(Visual Studio) “Setting up your AWS credentials” in the AWS Toolkit for Visual Studio Code User Guide  - [Official Docs](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/setup-credentials.html)

Global settings for config and credentials files [Official Docs](https://docs.aws.amazon.com/sdkref/latest/guide/settings-global.html)

Supported environment variables [Official Docs](https://docs.aws.amazon.com/sdkref/latest/guide/environment-variables.html)

(Java) Working with AWS Credentials [Official Docs](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/credentials.html)

(.NET) Configuring AWS Credentials [Official Docs](https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/net-dg-config-creds.html)

(Boto3) Credentials [Official Docs](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html)

Temporary security credentials in IAM - [Official Docs](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)

AWS Security Token Service API Reference - Actions [Official Docs](https://docs.aws.amazon.com/STS/latest/APIReference/API_Operations.html)

Using temporary security credentials with the AWS SDKs - [Official Docs](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html#using-temp-creds-sdk)

**Specific Java:**

Setting the JVM TTL for DNS Name Lookups [Official Docs](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/java-dg-jvm-ttl.html)

Environment variables to configure the AWS CLI [Official Docs](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html)

Error retries and exponential backoff in AWS [Official Docs](https://docs.aws.amazon.com/general/latest/gr/api-retries.html)

## Demos

AWS CLI is setup with multiple named profiles [Official Docs](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html)

## Lab 1 Notes

a) Review the ALL the notes on the Lab, i.e. TODO and the flags.

b) The "AWS Toolkit" isn't install automatically, so you have to do it.

## Getting Started with Storage

Cloud Storage on AWS [Official Page](https://aws.amazon.com/products/storage/)

Bucket restrictions and limitations [Official Docs](https://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html)

Organizing objects using prefixes [Official Docs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ListingKeysUsingAPIs.html)

S3 Security [AWS Blogs](https://aws.amazon.com/blogs/security/iam-policies-and-bucket-policies-and-acls-oh-my-controlling-access-to-s3-resources/)

S3 FAQs, specially on Security [Official FAQs](https://aws.amazon.com/s3/faqs/?nc=sn&loc=7#Security)

Tagging Best Practices [AWS Whitepaper](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf)

Managing access to shared datasets in general purpose buckets with access points [Official Docs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points.html)

S3 Access Points [Official Page](https://aws.amazon.com/s3/features/access-points/)

S3 access policy Vs S3 bucket policies ... how they interact [AWS RePost](https://repost.aws/questions/QU2lGn8dF5QmahMU_WS1vtJA/s3-access-policy-vs-s3-bucket-policies-how-they-interact)

S3 API Reference [Official Docs](https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html)

create_bucket [boto3 API](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/create_bucket.html)

** Questions 21/05/2025 **

1. Cual es la diferencia entre Terabyte y Tebibyte ?

R:/ La explicacion de diferencia entre las unidades binarias y las decimales las puede encontrar [aqui](https://www.ibm.com/docs/en/storage-insights?topic=overview-units-measurement-storage-data), sin embargo, la implicacion en almacenamiento de S3 dice asi "Amazon S3 storage usage is calculated in binary gigabytes (GB), where 1 GB is 2^30 bytes. This unit of measurement is also known as a gibibyte (GiB), defined by the International Electrotechnical Commission (IEC). Similarly, 1 TB is 2^40 bytes, i.e. 1024 GBs.", en la pagina de [S3 Pricing](https://aws.amazon.com/s3/pricing/), section "S3 Pricing Details".

2. Existe mauor informacion sobre las capas de S3?

R:/ Si puedes encontrar una tabla comparativa [aqui](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html), o en la [FAQ](https://aws.amazon.com/s3/storage-classes/).

3. Donde se puede obtener la informacion sobre el multipart upload ?

R: Puede verse [aqui](https://repost.aws/knowledge-center/s3-multipart-upload-cli) donde se especifica cuantos chunks simultaneos se pueden cargar, y en [esta pagina](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpu-upload-object.html) en la parte de High-level API de Python, se puede ver como se establece los tamanos del chunk. Otra opcion es configurando desde el CLI, como se especifica en [esta pagina](https://docs.aws.amazon.com/de_de/cli/latest/topic/s3-config.html).



## Processing Your Storage Operations

How do I use the AWS CLI to perform a multipart upload of a file to Amazon S3?”  [AWS RePost](https://aws.amazon.com/premiumsupport/knowledge-center/s3-multipart-upload-cli)

How do I use the AWS CLI to upload a large file in multiple parts to Amazon S3? [AWS RePost](https://repost.aws/knowledge-center/s3-multipart-upload-cli)

Uploading and copying objects using multipart upload in Amazon S3 [Official Docs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html)

Logging HOWTO [Python Docs](https://docs.python.org/3/howto/logging.html#logging-basic-tutorial)

Introducing Amazon S3 Object Lambda – Use Your Code to Process Data as It Is Being Retrieved from S3 [AWS Blog](https://aws.amazon.com/blogs/aws/introducing-amazon-s3-object-lambda-use-your-code-to-process-data-as-it-is-being-retrieved-from-s3/)

Amazon S3 Object Lambda [Official Page](https://aws.amazon.com/s3/features/object-lambda/)

Paginators [Boto3 Calls](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/paginators.html)

How do I use CloudFront to serve a static website hosted on Amazon S3 [AWS RePost](https://aws.amazon.com/premiumsupport/knowledge-center/cloudfront-serve-static-website/)

Requiring HTTPS for communication between viewers and CloudFront [Official Docs](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https-viewers-to-cloudfront.html)

Using cross-origin resource sharing (CORS) [Official Docs](https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html)

CORS configuration [Official Docs](https://docs.aws.amazon.com/AmazonS3/latest/dev/ManageCorsUsing.html)

Victor Okunev [GitHub from ex-AWS](https://github.com/realokun/aws/)