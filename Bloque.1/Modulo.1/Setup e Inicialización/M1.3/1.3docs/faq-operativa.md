# FAQ Operativa — AFP UNO

## Preguntas frecuentes del equipo de tecnología

### ¿Cómo accedo al ambiente de staging?
Necesitas VPN activa + credenciales de AWS del sandbox. Solicita acceso al equipo de infra vía ticket en Jira (proyecto INFRA). Tiempo de respuesta: 4 horas hábiles.

### ¿Dónde están los logs de producción?
En CloudWatch Log Groups. Cada microservicio tiene su grupo:
- `/ecs/afpuno-api-cotizaciones`
- `/ecs/afpuno-api-afiliados`
- `/ecs/afpuno-api-fondos`
- `/ecs/afpuno-worker-recaudacion`

Usa CloudWatch Insights para queries complejos.

### ¿Cuál es el proceso de escalamiento en producción?
Auto Scaling está configurado en ECS. Se escala automáticamente cuando:
- CPU > 70% por 3 minutos consecutivos
- Memoria > 80% por 3 minutos consecutivos
- Request count > 1000/min por target

Si necesitas escalamiento manual urgente, contacta al guardia de producción (oncall@afpuno.cl).

### ¿Cómo reporto un incidente?
1. Canal #incidents en Slack — describir síntoma y servicio afectado
2. Crear ticket en Jira (proyecto INCIDENT) con severidad:
   - P1: Servicio caído, afecta afiliados
   - P2: Degradación de servicio, funcionalidad parcial
   - P3: Error no crítico, sin impacto en usuario final
3. Para P1: llamar al guardia de producción inmediatamente

### ¿Cada cuánto se hacen releases?
- Staging: cada merge a rama staging (continuo)
- Producción: releases semanales los martes a las 10:00
- Hotfix: en cualquier momento previa aprobación del Tech Lead

### ¿Cómo solicito acceso a la base de datos de producción?
1. Ticket en Jira (proyecto DBA) justificando la necesidad
2. Aprobación del Tech Lead + DBA Lead
3. Acceso de solo lectura por 4 horas (sesión temporal)
4. Toda consulta queda logueada para auditoría

### ¿Qué hacer si un pipeline de CI falla?
1. Revisar los logs del step fallido en GitHub Actions
2. Si es un test flaky: re-run del job (máximo 2 intentos)
3. Si es un error real: corregir en la rama y pushear
4. Si es un problema de infra (timeout, networking): reportar en #devops

### ¿Cuál es la política de secrets y credenciales?
- Nunca en código ni en variables de entorno hardcodeadas
- Usar AWS Secrets Manager para producción
- Usar Parameter Store para staging
- Rotación automática cada 90 días
- Si se expone un secret: rotar inmediatamente + reportar incidente P2
