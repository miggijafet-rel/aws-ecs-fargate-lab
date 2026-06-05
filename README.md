# aws-ecs-fargate-lab
Dockerized Flask app deployed to AWS ECS Fargate with custom VPC, ALB, ECR, and CloudWatch logging


A lab environment deployment of a Dockerized Flask application on AWS ECS Fargate inside a custom VPC — featuring layered network security, an Application Load Balancer, ECR image registry, and CloudWatch observability.

Traffic flow:
Internet → IGW → ALB (public subnets) → ECS Fargate Tasks (private subnets)
ECS Tasks → NAT Gateway → IGW → Internet (for ECR pulls)

Security Design
The security group chain ensures each layer only accepts traffic from the layer directly above it:
alb-sg          → accepts 0.0.0.0/0 on ports 80/443
ecs-tasks-sg    → accepts traffic ONLY from alb-sg on port 5000
rds-sg          → accepts traffic ONLY from ecs-tasks-sg on port 5432
