# Project 2: Container Orchestration & Kubernetes

A production-ready containerized portfolio website demonstrating Docker containerization and Kubernetes orchestration with advanced features including autoscaling, load balancing, and resource management.

## 🎯 Project Overview

This project transforms a static HTML portfolio into a fully containerized, orchestrated application running on Kubernetes with production-grade features. The portfolio showcases DevOps skills through practical implementation of container orchestration technologies.

## ✨ Production Features

### High Availability & Scaling
- **2 Replica Pods** with automatic failover
- **Horizontal Pod Autoscaler** (2-10 pods based on CPU usage)
- **Load Balancing** across multiple pod instances
- **Zero-downtime deployments** with rolling updates

### Resource Management
- **CPU Limits**: 100m per pod (0.1 CPU cores)
- **Memory Limits**: 128Mi per pod
- **Resource Requests**: 50m CPU, 64Mi memory (guaranteed)
- **QoS Class**: Burstable for optimal resource utilization

### Monitoring & Observability
- **Real-time metrics** with metrics-server
- **Resource usage monitoring** (`kubectl top` commands)
- **Pod health checks** and automatic restart
- **Deployment status tracking**

### Multiple Access Methods
- **NodePort Service** for direct cluster access
- **Port Forwarding** for local development
- **Ingress Ready** for custom domain deployment
- **Service Discovery** within cluster

## 🛠 Technologies Used

### Core Technologies
- **Docker** - Container runtime and image building
- **Kubernetes** - Container orchestration platform
- **Minikube** - Local Kubernetes cluster
- **kubectl** - Kubernetes command-line tool

### Advanced Features
- **Helm** - Kubernetes package manager (explored)
- **Horizontal Pod Autoscaler** - Automatic scaling
- **Metrics Server** - Resource monitoring
- **Ingress Controller** - Traffic routing
- **Security Contexts** - Container security (explored)

### Supporting Tools
- **Nginx** - Web server (Alpine Linux base)
- **YAML** - Configuration management
- **Git** - Version control

## 🏗 Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Browser       │────│  Kubernetes      │────│   Docker        │
│                 │    │  Service         │    │   Containers    │
└─────────────────┘    │  (Load Balancer) │    │                 │
                       └──────────────────┘    │  ┌─────────────┐ │
                                ▼              │  │ Nginx +     │ │
                       ┌──────────────────┐    │  │ Portfolio   │ │
                       │  Pod 1           │    │  │ HTML        │ │
                       │  (Replica 1)     │────┤  └─────────────┘ │
                       └──────────────────┘    └─────────────────┘
                                ▼              
                       ┌──────────────────┐    ┌─────────────────┐
                       │  Pod 2           │────│   Docker        │
                       │  (Replica 2)     │    │   Containers    │
                       └──────────────────┘    │                 │
                                               │  ┌─────────────┐ │
                                               │  │ Nginx +     │ │
                                               │  │ Portfolio   │ │
                                               │  │ HTML        │ │
                                               │  └─────────────┘ │
                                               └─────────────────┘
```

## 📁 Project Structure

```
proj-2-containers/
├── README.md                     # This file
├── index.html                    # Portfolio website
├── Dockerfile                    # Container definition
├── portfolio-deployment.yaml     # Kubernetes deployment
├── portfolio-service.yaml        # Kubernetes service
├── portfolio-ingress.yaml        # Ingress configuration
└── portfolio-chart/              # Helm chart (optional)
    ├── Chart.yaml
    ├── values.yaml
    └── templates/
        ├── deployment.yaml
        ├── service.yaml
        └── ingress.yaml
```

## 🚀 Quick Start

### Prerequisites
- Docker installed and running
- Minikube cluster running
- kubectl configured
- Git for version control

### Deployment Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/venkat3085/proj-2-containers.git
   cd proj-2-containers
   ```

2. **Build Docker image**
   ```bash
   docker build -t venkat-portfolio .
   ```

3. **Load image to Minikube**
   ```bash
   minikube image load venkat-portfolio
   ```

4. **Deploy to Kubernetes**
   ```bash
   kubectl apply -f portfolio-deployment.yaml
   kubectl apply -f portfolio-service.yaml
   ```

5. **Enable autoscaling**
   ```bash
   kubectl autoscale deployment portfolio-deployment --cpu-percent=50 --min=2 --max=10
   ```

6. **Access the application**
   ```bash
   minikube service portfolio-service --url
   ```

## 📊 Monitoring & Management

### Check Deployment Status
```bash
# View pods
kubectl get pods

# Check service
kubectl get services

# Monitor autoscaler
kubectl get hpa

# View resource usage
kubectl top pods
kubectl top nodes
```

### Scaling Operations
```bash
# Manual scaling
kubectl scale deployment portfolio-deployment --replicas=3

# Check autoscaler status
kubectl describe hpa portfolio-deployment
```

### Troubleshooting
```bash
# View pod logs
kubectl logs <pod-name>

# Describe pod details
kubectl describe pod <pod-name>

# Check events
kubectl get events --sort-by=.metadata.creationTimestamp
```

## 🔧 Configuration Details

### Docker Configuration
- **Base Image**: `nginx:alpine` (lightweight)
- **Port**: 80 (standard HTTP)
- **Content**: Static HTML portfolio
- **Size**: Optimized for minimal footprint

### Kubernetes Resources
- **Deployment**: 2 replicas with rolling update strategy
- **Service**: NodePort type for external access
- **HPA**: CPU-based scaling (50% threshold)
- **Resource Limits**: Prevents resource exhaustion

### Security Considerations
- **Non-root execution** (explored, requires compatible base image)
- **Resource quotas** to prevent resource abuse
- **Network policies** ready for implementation
- **Security contexts** for container hardening

## 🎓 Learning Outcomes

### Docker Mastery
- Container lifecycle management
- Image building and optimization
- Multi-stage builds understanding
- Local vs production strategies

### Kubernetes Expertise
- Pod, Service, Deployment concepts
- YAML configuration management
- Resource management and quotas
- Horizontal Pod Autoscaling
- Service networking and discovery

### DevOps Practices
- Infrastructure as Code principles
- Container orchestration patterns
- Production deployment strategies
- Monitoring and observability
- Troubleshooting and debugging

## 🐛 Troubleshooting Guide

### Common Issues

**ImagePullBackOff Error**
```bash
# Solution: Ensure image is loaded in Minikube
minikube image load venkat-portfolio
kubectl rollout restart deployment portfolio-deployment
```

**Security Context Failures**
```bash
# Issue: Container runs as root, conflicts with runAsNonRoot
# Solution: Use compatible base image or remove security context
```

**Resource Limits Too Low**
```bash
# Issue: Pods crash due to insufficient resources
# Solution: Increase memory/CPU limits in deployment.yaml
```

**Service Not Accessible**
```bash
# Check service status
kubectl get services
minikube service portfolio-service --url
```

## 🔄 CI/CD Integration

### GitHub Actions (Future)
- Automated Docker builds
- Image security scanning
- Kubernetes deployment
- Integration testing

### GitOps Workflow (Future)
- ArgoCD for deployment automation
- Git-based configuration management
- Automated rollbacks
- Multi-environment support

## 📈 Performance Metrics

### Current Performance
- **Startup Time**: ~2 seconds per pod
- **Memory Usage**: 11-16Mi per pod
- **CPU Usage**: 0% (idle state)
- **Response Time**: <100ms

### Scaling Behavior
- **Scale Up**: When CPU > 50%
- **Scale Down**: When CPU < 50% (with stabilization)
- **Min Replicas**: 2 (high availability)
- **Max Replicas**: 10 (resource protection)

## 🚀 Next Steps

CI/CD integration with GitHub Actions and GitOps deployment with ArgoCD for automated testing, building, and deployment workflows.

## 👨‍💻 Author

**Venkat**
- DevOps Engineer specializing in container orchestration and cloud infrastructure
- Focus: Kubernetes, Docker, Terraform, Infrastructure as Code, Site Reliability Engineering
- GitHub: [github.com/venkat3085](https://github.com/venkat3085)
- Portfolio: Containerized and running on Kubernetes with production features
- Projects: Infrastructure as Code (Terraform) + Container Orchestration (Kubernetes)

## 📄 License

This project is part of a DevOps learning journey and is available for educational purposes.

## 🤝 Contributing

This is a learning project, but feedback and suggestions are welcome!
