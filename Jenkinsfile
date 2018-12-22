node {
    stage('Git checkout') {
        checkout scm
    }
    stage('Run smoke test') {
        echo 'Running some test'
        //bat 'python -m pytest -v -s test_script.py'
    }
    stage('Run regression test') {
        echo 'Running regression test'
    }
    stage('Slack') {
        def COLOR_MAP = ['SUCCESS': 'good', 'FAILURE': 'danger', 'UNSTABLE': 'warning', 'ABORTED': 'warning']
        slackSend color: COLOR_MAP[currentBuild.result], message: "Build ${currentBuild.result} - ${env.JOB_NAME} #${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)"
    }
    
        
}
