node {
    stage('Git checkout') {
        checkout scm
    }
    stage('Run test') {
        sh 'pytest -v -s -k test_script.py'
    }

}
