# Guía de Deploy de Microservicios — AFP UNO

## Entorno
- Cloud: AWS
- Orquestador: ECS Fargate
- CI/CD: GitHub Actions + AWS CodeDeploy
- Registro: Amazon ECR
- Monitoreo: CloudWatch + X-Ray

## Prerrequisitos para deploy
1. Código mergeado a la rama `main` (producción) o `staging` (pre-producción)
2. Pipeline de CI verde (tests unitarios + integración + linting)
3. Imagen Docker construida y publicada en ECR
4. Revisión de PR aprobada por al menos 2 reviewers

## Proceso de deploy

### Deploy a Staging
1. Merge a rama `staging` dispara el pipeline automáticamente.
2. GitHub Actions construye la imagen Docker.
3. Se publica en ECR con tag `staging-{commit_hash}`.
4. CodeDeploy actualiza el servicio ECS con rolling update.
5. Health checks validan la nueva versión (timeout: 5 min).
6. Si falla, rollback automático a la versión anterior.

### Deploy a Producción
1. Crear un Release en GitHub con tag semántico (v1.2.3).
2. El pipeline construye imagen con tag `prod-v1.2.3`.
3. Deploy blue/green en ECS Fargate.
4. Tráfico se migra gradualmente: 10% → 50% → 100% (canary).
5. Monitoreo activo durante 15 minutos post-deploy.
6. Rollback manual disponible vía botón en consola de CodeDeploy.

## Proceso de escalamiento
- Auto Scaling configurado por CPU > 70% y memoria > 80%.
- Mínimo: 2 tasks. Máximo: 10 tasks.
- Escalamiento horizontal (más containers, no más grandes).

## Rollback de emergencia
1. Ir a AWS Console → CodeDeploy → Deployments.
2. Seleccionar el deployment activo.
3. Click en "Stop and roll back deployment".
4. Verificar que el servicio vuelve a la versión anterior.
5. Notificar al equipo en el canal #incidents de Slack.

## Contactos
- DevOps Lead: infra@afpuno.cl
- Guardia producción: oncall@afpuno.cl
- Canal de incidentes: #incidents (Slack)
