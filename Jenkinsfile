node {
    stage('Git checkout') {
        checkout scm
    }
    stage('Run test') {
        echo 'Running some test'
        bat 'python -m pytest -v -s test_script.py'
    }

}
