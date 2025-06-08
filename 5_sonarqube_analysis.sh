#!/bin/bash
# Script básico para rodar análise estática com SonarQube Scanner CLI
sonar-scanner -Dsonar.projectKey=meuprojeto -Dsonar.sources=. -Dsonar.host.url=http://localhost:9000 -Dsonar.login=seutoken
