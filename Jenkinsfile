node {
    stage('Git checkout') {
        checkout scm
    }
    stage('Run test') {
        cd C:\\"Program Files (x86)"\\Jenkins\\workspace\\pytest_pipeline_job
        sh 'pytest -v -s test_script.py'
    }

}
