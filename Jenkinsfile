pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                echo 'Setting up Python environment'
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Telnet Test') {
            steps {
                echo 'Running Telnet Test'
                sh '. venv/bin/activate && python3 boot-test-telnet.py'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up virtual environment'
            sh 'rm -rf venv'
        }

        success {
            echo 'Tests ran successfully'
        }

        failure {
            echo 'Tests failed, please check the results.'
        }

        unstable {
            junit 'telnet_test_results.xml'
        }
    }
}
