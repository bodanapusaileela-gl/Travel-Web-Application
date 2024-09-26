pipeline {
    agent any

    tools {
        // Ensure that 'JDK 17' matches exactly the name in Global Tool Configuration
        jdk 'JDK 17'
        
        // Ensure that 'Python 3.10.12' matches exactly the name in Global Tool Configuration
        'jenkins.plugins.shiningpanda.tools.PythonInstallation' 'Python3.10.12'
    }

    environment {
        SCANNER_HOME = tool 'sonar-scanner'
    }

    stages {
        stage('git-checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/bodanapusaileela-gl/Travel-Web-Application.git'
            }
        }

        stage('OWASP FS SCAN') {
            steps {
                // Run OWASP Dependency-Check
                dependencyCheck additionalArguments: '--scan ./', odcInstallation: 'DC'
                // Publish the Dependency-Check report
                dependencyCheckPublisher pattern: '**/dependency-check-report.xml'
            }
        }

        stage('TRIVY FS SCAN') {
            steps {
                // Run Trivy filesystem scan
                sh "trivy fs ."
            }
        }

        stage('SONARQUBE ANALYSIS') {
            steps {
                // Run SonarQube analysis
                withSonarQubeEnv('sonar') {
                    sh "$SCANNER_HOME/bin/sonar-scanner -Dsonar.projectName=travel-web -Dsonar.projectKey=travel-web"
                }
            }
        }
    }
}
